import yaml
import argparse
import sys
import os
import json
import datetime
import jinja2
import csv
import re
import shutil

def write_rmm_tools_csv(rmm_tools, output_dir, VERBOSE):
    output_file = os.path.join(output_dir, 'public', 'api', 'rmm_tools.csv')
    
    header = ['Name', 'Category', 'Description', 'Author', 'Created', 'LastModified',
              'Website', 'Filename', 'OriginalFileName', 'PEDescription', 'Product',
              'Privileges', 'Free', 'Verification', 'SupportedOS', 'Capabilities',
              'Vulnerabilities', 'InstallationPaths', 'Artifacts', 'Detections',
              'References', 'Acknowledgement']

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()

        for rmm_tool in rmm_tools:
            if VERBOSE:
                print(f"Writing RMM tool CSV: {rmm_tool['Name']}")

            pe_metadata = rmm_tool.get('Details', {}).get('PEMetadata', {})
            if isinstance(pe_metadata, list) and pe_metadata:
                pe_metadata = pe_metadata[0]  # Take the first item if it's a list

            row = {
                'Name': rmm_tool.get('Name', ''),
                'Category': rmm_tool.get('Category', ''),
                'Description': rmm_tool.get('Description', ''),
                'Author': rmm_tool.get('Author', ''),
                'Created': rmm_tool.get('Created', ''),
                'LastModified': rmm_tool.get('LastModified', ''),
                'Website': rmm_tool.get('Details', {}).get('Website', ''),
                'Filename': pe_metadata.get('Filename', ''),
                'OriginalFileName': pe_metadata.get('OriginalFileName', ''),
                'PEDescription': pe_metadata.get('Description', ''),
                'Product': pe_metadata.get('Product', ''),
                'Privileges': rmm_tool.get('Details', {}).get('Privileges', ''),
                'Free': str(rmm_tool.get('Details', {}).get('Free', '')),
                'Verification': str(rmm_tool.get('Details', {}).get('Verification', '')),
                'SupportedOS': ', '.join(rmm_tool.get('Details', {}).get('SupportedOS', [])),
                'Capabilities': ', '.join(rmm_tool.get('Details', {}).get('Capabilities', [])),
                'Vulnerabilities': ', '.join(rmm_tool.get('Details', {}).get('Vulnerabilities', [])),
                'InstallationPaths': ', '.join(rmm_tool.get('Details', {}).get('InstallationPaths', [])) if isinstance(rmm_tool.get('Details', {}).get('InstallationPaths', []), list) else str(rmm_tool.get('Details', {}).get('InstallationPaths', '')),
                'Artifacts': json.dumps({k: v if k != 'Network' else [{'Description': item.get('Description', ''), 'Domains': item.get('Domains', []), 'Ports': item.get('Ports', [])} for item in v] for k, v in rmm_tool.get('Artifacts', {}).items()}),
                'Detections': json.dumps(rmm_tool.get('Detections', [])),
                'References': ', '.join(rmm_tool.get('References', [])),
                'Acknowledgement': json.dumps(rmm_tool.get('Acknowledgement', []))
            }

            writer.writerow(row)

def write_rmm_tools_table_csv(rmm_tools, output_dir, VERBOSE):
    output_file = os.path.join(output_dir, 'public', 'rmm_tools_table.csv')
    
    header = ['Name', 'Category', 'Description', 'Author']

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()

        for rmm_tool in rmm_tools:
            if VERBOSE:
                print(f"Writing RMM tool table CSV: {rmm_tool['Name']}")

            # Replace parentheses with underscores in the link
            name_link = f"[{rmm_tool['Name']}](/rmm_tools/{rmm_tool['Name'].lower().replace(' ', '_').replace('(', '_').replace(')', '_')})"

            row = {
                'Name': name_link,
                'Category': rmm_tool.get('Category', ''),
                'Description': rmm_tool.get('Description', '')[:100] + '...' if rmm_tool.get('Description', '') else '',
                'Author': rmm_tool.get('Author', '')
            }

            writer.writerow(row)

def generate_doc_rmm_tools(REPO_PATH, OUTPUT_DIR, TEMPLATE_PATH, messages, VERBOSE):
    manifest_files = []
    for root, dirs, files in os.walk(REPO_PATH):
        for file in files:
            if file.endswith('.yaml'):
                manifest_files.append(os.path.join(root, file))

    rmm_tools = []
    for manifest_file in manifest_files:
        if VERBOSE:
            print(f"Processing RMM tool: {manifest_file}")

        with open(manifest_file, 'r') as stream:
            try:
                rmm_tool = yaml.safe_load(stream)
                rmm_tools.append(rmm_tool)
            except yaml.YAMLError as exc:
                print(f"Error reading {manifest_file}: {exc}")
                sys.exit(1)

    # Write markdowns
    j2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH), 
                                trim_blocks=True, 
                                lstrip_blocks=True, 
                                autoescape=False)
    
    def clean_multiline(text):
        if isinstance(text, str):
            return text.replace('\n', ' ').strip()
        return text

    j2_env.filters['clean_multiline'] = clean_multiline
    j2_env.globals.update(dump=json.dumps)
    j2_env.globals.update(escape=re.escape)

    tools_dir = os.path.join(OUTPUT_DIR, 'pages', 'tools')
    shutil.rmtree(tools_dir)
    os.mkdir(tools_dir)
    d = datetime.datetime.now()
    template = j2_env.get_template('rmm.md.j2')
    for rmm_tool in rmm_tools:
        # Replace parentheses with underscores in the file name
        file_name = f"{rmm_tool['Name'].lower().replace(' ', '_').replace('(', '_').replace(')', '_')}.mdx"
        output_path = os.path.join(tools_dir, file_name)
        output = template.render(rmm=rmm_tool, time=str(d.strftime("%Y-%m-%d")))
        with open(output_path, 'w', encoding="utf-8") as f:
            f.write(output)
    messages.append(f"site_gen.py wrote {len(rmm_tools)} RMM tools markdown to: {tools_dir}")

    # Write API CSV
    write_rmm_tools_csv(rmm_tools, OUTPUT_DIR, VERBOSE)
    messages.append(f"site_gen.py wrote RMM tools CSV to: {os.path.join(OUTPUT_DIR, 'public', 'api', 'rmm_tools.csv')}")

    # Write API JSON
    with open(os.path.join(OUTPUT_DIR, 'public', 'api', 'rmm_tools.json'), 'w', encoding='utf-8') as f:
        json.dump(rmm_tools, f, ensure_ascii=False, indent=4)
    messages.append(f"site_gen.py wrote RMM tools JSON to: {os.path.join(OUTPUT_DIR, 'public', 'api', 'rmm_tools.json')}")

    # Write RMM tools table CSV
    write_rmm_tools_table_csv(rmm_tools, OUTPUT_DIR, VERBOSE)
    messages.append(f"site_gen.py wrote RMM tools table CSV to: {os.path.join(OUTPUT_DIR, 'public' , 'rmm_tools_table.csv')}")

    return rmm_tools, messages

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates LOLRMM site", epilog="This tool converts all LOLRMM YAMLs and builds the site with all the supporting components.")
    parser.add_argument("-p", "--path", required=False, default="yaml", help="path to LOLRMM yaml folder. Defaults to `yaml`")
    parser.add_argument("-o", "--output", required=False, default="website", help="path to the output directory for the site, defaults to `website`")
    parser.add_argument("-v", "--verbose", required=False, default=False, action='store_true', help="prints verbose output")

    args = parser.parse_args()
    REPO_PATH = args.path
    OUTPUT_DIR = args.output
    VERBOSE = args.verbose

    TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'jinja2_templates')

    if VERBOSE:
        print(f"Wiping the {os.path.join(OUTPUT_DIR, 'pages', 'tools')} folder")

    # Clean up old RMM tool files
    try:
        rmm_tools_dir = os.path.join(OUTPUT_DIR, 'pages', 'tools')
        for file in os.listdir(rmm_tools_dir):
            if file.endswith(".md") and file != '_index.md':
                os.remove(os.path.join(rmm_tools_dir, file))
    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Clean up API artifacts
    api_json = os.path.join(OUTPUT_DIR, 'public', 'api', 'rmm_tools.json')
    api_csv = os.path.join(OUTPUT_DIR, 'public', 'api',  'rmm_tools.csv')
    if os.path.exists(api_json):
        os.remove(api_json)
    if os.path.exists(api_csv):
        os.remove(api_csv)

    messages = []
    rmm_tools, messages = generate_doc_rmm_tools(REPO_PATH, OUTPUT_DIR, TEMPLATE_PATH, messages, VERBOSE)

    for m in messages:
        print(m)
    print("Finished successfully!")