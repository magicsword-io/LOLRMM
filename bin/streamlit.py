import streamlit as st
import yaml
from datetime import datetime, date
import os

def list_yaml_files():
    yaml_files = [f for f in os.listdir('yaml') if f.endswith('.yaml')]
    return ['New RMM Tool'] + yaml_files

def load_yaml_template(filename):
    if filename == 'New RMM Tool':
        return default_template()
    try:
        with open(f'yaml/{filename}', 'r') as file:
            data = yaml.safe_load(file)
            # Convert PEMetadata to dict if it's a list
            if 'Details' in data and 'PEMetadata' in data['Details'] and isinstance(data['Details']['PEMetadata'], list):
                data['Details']['PEMetadata'] = data['Details']['PEMetadata'][0] if data['Details']['PEMetadata'] else {}
            return data
    except yaml.YAMLError as e:
        st.error(f"Error loading YAML file: {e}")
        return default_template()
    except FileNotFoundError:
        st.warning(f"{filename} not found. Using default template.")
        return default_template()

def default_template():
    return {
        'Name': '',
        'Category': '',
        'Description': '',
        'Author': '',
        'Created': datetime.now().strftime("%Y-%m-%d"),
        'LastModified': datetime.now().strftime("%Y-%m-%d"),
        'Details': {
            'Website': '',
            'PEMetadata': {
                'Filename': '',
                'OriginalFileName': '',
                'Description': '',
                'Product': ''
            },
            'Privileges': '',
            'Free': False,
            'Verification': False,
            'SupportedOS': [],
            'Capabilities': [],
            'Vulnerabilities': [],
            'InstallationPaths': []
        },
        'Artifacts': {
            'Disk': [],
            'EventLog': [],
            'Registry': [],
            'Network': []
        },
        'Detections': [],
        'References': [],
        'Acknowledgement': []
    }

def save_yaml(data, filename):
    with open(f'yaml/{filename}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

def main():
    st.set_page_config(layout="wide", page_title="LOLRMM")
    st.title("LOLRMM")

    yaml_files = list_yaml_files()
    selected_file = st.selectbox("Select RMM Tool or create new", yaml_files, key="file_select")

    template = load_yaml_template(selected_file)

    # Create tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Basic Info", "Details", "Artifacts", "Detections", "References & Acknowledgements"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("RMM Tool Name", value=template.get('Name', ''), key="name")
            category = st.text_input("Category", value=template.get('Category', ''), key="category")
            author = st.text_input("Author", value=template.get('Author', ''), key="author")
        with col2:
            created_date = handle_date(template.get('Created', ''), "Created")
            created = st.date_input("Created Date", value=created_date, key="created")
            last_modified_date = handle_date(template.get('LastModified', ''), "LastModified")
            last_modified = st.date_input("Last Modified Date", value=last_modified_date, key="last_modified")
        description = st.text_area("Description", value=template.get('Description', ''), key="description", height=150)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            website = st.text_input("Website", value=template.get('Details', {}).get('Website', ''), key="website")
            privileges = st.text_input("Privileges", value=template.get('Details', {}).get('Privileges', ''), key="privileges")
            free = st.checkbox("Free", value=template.get('Details', {}).get('Free', False), key="free")
            verification = st.checkbox("Verification", value=template.get('Details', {}).get('Verification', False), key="verification")
        
        with col2:
            with st.expander("PE Metadata"):
                filename = st.text_input("Filename", value=template.get('Details', {}).get('PEMetadata', {}).get('Filename', ''), key="filename")
                original_filename = st.text_input("Original Filename", value=template.get('Details', {}).get('PEMetadata', {}).get('OriginalFileName', ''), key="original_filename")
                pe_description = st.text_input("PE Description", value=template.get('Details', {}).get('PEMetadata', {}).get('Description', ''), key="pe_description")
                product = st.text_input("Product", value=template.get('Details', {}).get('PEMetadata', {}).get('Product', ''), key="product")

        all_os_options = ['Windows', 'Mac', 'Linux', 'Android', 'iOS', 'ChromeOS']
        template_supported_os = template.get('Details', {}).get('SupportedOS', [])
        template_supported_os = [os.title() if os != 'iOS' else os for os in template_supported_os]
        valid_supported_os = [os for os in template_supported_os if os in all_os_options]

        supported_os = st.multiselect("Supported OS", 
                                      options=all_os_options,
                                      default=valid_supported_os,
                                      key="supported_os")

        # Get the capabilities from the template
        template_capabilities = template.get('Details', {}).get('Capabilities', [])
        
        # Create a set of all unique capabilities (from template and some common ones)
        all_capabilities = set(template_capabilities + [
            'File Transfer', 'File System Access', 'Remote Control', 
            'GUI Support', 'Command line Support', 'Remote monitoring and management',
            'Remote desktop', 'Remote shell open'
        ])

        capabilities = st.multiselect("Capabilities", 
                                      options=sorted(list(all_capabilities)),
                                      default=template_capabilities,
                                      key="capabilities")

        vulnerabilities = st.text_area("Vulnerabilities (one per line)", value='\n'.join(template.get('Details', {}).get('Vulnerabilities', [])), key="vulnerabilities")
        installation_paths = st.text_area("Installation Paths (one per line)", value='\n'.join(template.get('Details', {}).get('InstallationPaths', [])), key="installation_paths")

    with tab3:
        artifact_types = ['Disk', 'EventLog', 'Registry', 'Network']
        artifacts = {}

        for artifact_type in artifact_types:
            with st.expander(f"{artifact_type} Artifacts"):
                artifacts[artifact_type] = []
                for i, artifact in enumerate(template.get('Artifacts', {}).get(artifact_type, [])):
                    st.markdown(f"**{artifact_type} Artifact {i+1}**")
                    artifact_data = {}
                    for key, value in artifact.items():
                        if isinstance(value, list):
                            artifact_data[key] = st.text_area(f"{key} {i+1}", value='\n'.join(value), key=f"{artifact_type}_{i}_{key}")
                        else:
                            artifact_data[key] = st.text_input(f"{key} {i+1}", value=value, key=f"{artifact_type}_{i}_{key}")
                    artifacts[artifact_type].append(artifact_data)
                    st.markdown("---")

    with tab4:
        detections = []
        for i, detection in enumerate(template.get('Detections', [])):
            with st.expander(f"Detection {i+1}"):
                sigma = st.text_input(f"Sigma Rule", value=detection.get('Sigma', ''), key=f"detection_{i}_sigma")
                description = st.text_area(f"Description", value=detection.get('Description', ''), key=f"detection_{i}_description")
                detections.append({
                    'Sigma': sigma,
                    'Description': description
                })

    with tab5:
        col1, col2 = st.columns(2)
        with col1:
            references = st.text_area("References (one per line)", value='\n'.join(template.get('References', [])), key="references", height=200)
        
        with col2:
            acknowledgements = []
            for i, ack in enumerate(template.get('Acknowledgement', [])):
                st.markdown(f"**Acknowledgement {i+1}**")
                person = st.text_input(f"Person", value=ack.get('Person', ''), key=f"ack_{i}_person")
                handle = st.text_input(f"Handle", value=ack.get('Handle', ''), key=f"ack_{i}_handle")
                acknowledgements.append({
                    'Person': person,
                    'Handle': handle
                })

    if st.button("Generate YAML", key="generate_yaml"):
        yaml_data = {
            'Name': name,
            'Category': category,
            'Description': description,
            'Author': author,
            'Created': created.strftime("%Y-%m-%d"),
            'LastModified': last_modified.strftime("%Y-%m-%d"),
            'Details': {
                'Website': website,
                'PEMetadata': {
                    'Filename': filename,
                    'OriginalFileName': original_filename,
                    'Description': pe_description,
                    'Product': product
                },
                'Privileges': privileges,
                'Free': free,
                'Verification': verification,
                'SupportedOS': supported_os,
                'Capabilities': capabilities,
                'Vulnerabilities': vulnerabilities.split('\n'),
                'InstallationPaths': installation_paths.split('\n')
            },
            'Artifacts': artifacts,
            'Detections': detections,
            'References': references.split('\n'),
            'Acknowledgement': acknowledgements
        }

        save_yaml(yaml_data, name.lower().replace(' ', '_'))
        st.success(f"YAML file for {name} has been generated and saved!")

def handle_date(date_value, field_name):
    try:
        if isinstance(date_value, str):
            return datetime.strptime(date_value, "%Y-%m-%d").date()
        elif isinstance(date_value, datetime):
            return date_value.date()
        elif isinstance(date_value, date):
            return date_value
        else:
            raise ValueError("Invalid date format")
    except ValueError:
        st.warning(f"Invalid '{field_name}' date format in YAML: {date_value}. Using current date.")
        return datetime.now().date()

if __name__ == "__main__":
    main()