import os
import yaml
from datetime import date
import uuid
from typing import Dict, List, Any

def extract_artifacts(yaml_data: Dict[str, Any]) -> Dict[str, List[str]]:
    artifacts = {
        'files': [],
        'registry': [],
        'network': [],
        'processes': []
    }
    
    for item in yaml_data.get('Artifacts', {}).get('Disk', []) or []:
        if isinstance(item, dict) and 'File' in item:
            artifacts['files'].append(item['File'])
    
    for item in yaml_data.get('Artifacts', {}).get('Registry', []) or []:
        if isinstance(item, dict) and 'Path' in item:
            artifacts['registry'].append(item['Path'])
    
    for item in yaml_data.get('Artifacts', {}).get('Network', []) or []:
        if isinstance(item, dict):
            if 'Domains' in item:
                if isinstance(item['Domains'], list):
                    artifacts['network'].extend(item['Domains'])
                elif isinstance(item['Domains'], str):
                    artifacts['network'].append(item['Domains'])
    
    details = yaml_data.get('Details', {})
    if isinstance(details, dict):
        artifacts['processes'] = [
            os.path.basename(item) for item in details.get('InstallationPaths', []) or []
            if isinstance(item, str) and item.lower().endswith('.exe')
        ]
    
    return artifacts

def generate_sigma_rules(yaml_file: str, output_dir: str) -> List[Dict[str, Any]]:
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    name = data.get('Name', 'Unknown')
    artifacts = extract_artifacts(data)
    
    rule_templates = {
        'registry': {
            "title": f"Potential {name} RMM Tool Registry Activity",
            "logsource": {"product": "windows", "category": "registry_event"},
            "detection": {"selection": {"TargetObject|contains": []}}
        },
        'network': {
            "title": f"Potential {name} RMM Tool Network Activity",
            "logsource": {"product": "windows", "category": "network_connection"},
            "detection": {"selection": {"DestinationHostname|endswith": []}}
        },
        'files': {
            "title": f"Potential {name} RMM Tool File Activity",
            "logsource": {"product": "windows", "category": "file_event"},
            "detection": {"selection": {"TargetFilename|endswith": []}}
        },
        'processes': {
            "title": f"Potential {name} RMM Tool Process Activity",
            "logsource": {"product": "windows", "category": "process_creation"},
            "detection": {"selection": {"ParentImage|endswith": []}}
        }
    }
    
    generated_rules = []
    for artifact_type, rule_template in rule_templates.items():
        if artifacts[artifact_type]:
            rule = {
                **rule_template,
                "id": str(uuid.uuid4()),
                "status": "experimental",
                "description": f"Detects potential {artifact_type} activity of {name} RMM tool",
                "author": "LOLRMM Project",
                "date": date.today().strftime('%Y-%m-%d'),
                "tags": ["attack.execution", "attack.t1219"],
                "falsepositives": [f"Legitimate use of {name}"],
                "level": "medium",
                "detection": {
                    "selection": {
                        list(rule_template["detection"]["selection"].keys())[0]: artifacts[artifact_type]
                    },
                    "condition": "selection"
                }
            }
            
            detection_key = list(rule_template["detection"]["selection"].keys())[0]
            rule["detection"]["selection"][detection_key] = artifacts[artifact_type]
            
            safe_name = name.lower().replace(' ', '_').replace('(', '_').replace(')', '_')
            output_file = f"{safe_name}_{artifact_type}_sigma.yml"
            full_output_path = os.path.join(output_dir, output_file)
            with open(full_output_path, 'w') as f:
                yaml.dump(rule, f, sort_keys=False)
            
            github_url = f"https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/{output_file}"
            generated_rules.append({
                "Sigma": github_url,
                "Description": f"Detects potential {artifact_type} activity of {name} RMM tool"
            })
    
    return generated_rules

def update_yaml_with_sigma_rules(yaml_file: str, sigma_rules: List[Dict[str, Any]]) -> None:
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    if 'Detections' not in data:
        data['Detections'] = []
    
    # Remove existing generated rules
    data['Detections'] = [rule for rule in data['Detections'] if not rule.get('Sigma', '').startswith('https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/')]
    
    # Add new generated rules
    data['Detections'].extend(sigma_rules)
    
    with open(yaml_file, 'w') as f:
        yaml.dump(data, f, sort_keys=False)

def main() -> None:
    yaml_dir = 'yaml/'
    output_dir = 'detections/sigma/'
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml'):
            yaml_file = os.path.join(yaml_dir, filename)
            sigma_rules = generate_sigma_rules(yaml_file, output_dir)
            update_yaml_with_sigma_rules(yaml_file, sigma_rules)
    
    print(f"[+] Sigma rule generation and YAML update complete. Files saved in {output_dir}")

if __name__ == "__main__":
    main()
