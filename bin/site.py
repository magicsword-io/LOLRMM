import yaml
import argparse
import sys
import re
import os
import json
import datetime
import jinja2
import csv

def write_bootloaders_csv(bootloaders, output_dir, VERBOSE):
    output_file = os.path.join(output_dir, 'content', 'api', 'bootloaders.csv')
    
    header = ['Id', 'Author', 'Created', 'Command', 'Description', 'Usecase', 'Category', 'Privileges', 'MitreID',
              'OperatingSystem', 'Resources', 'bootloader Description', 'Person', 'Handle', 'Detection',
              'KnownVulnerableSamples_MD5', 'KnownVulnerableSamples_SHA1', 'KnownVulnerableSamples_SHA256',
              'KnownVulnerableSamples_Publisher', 'KnownVulnerableSamples_Date',
              'KnownVulnerableSamples_Company', 'KnownVulnerableSamples_Description', 
              'KnownVulnerableSamples_Authentihash_MD5', 'KnownVulnerableSamples_Authentihash_SHA1', 'KnownVulnerableSamples_Authentihash_SHA256', 'Verified', 'Tags']

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()

        for bootloader in bootloaders:
            if VERBOSE:
                print(f"Writing bootloader CSV: {bootloader['Id']}")

            md5s = [s['MD5'] for s in bootloader['KnownVulnerableSamples'] if 'MD5' in s]
            sha1s = [s['SHA1'] for s in bootloader['KnownVulnerableSamples'] if 'SHA1' in s]
            sha256s = [s['SHA256'] for s in bootloader['KnownVulnerableSamples'] if 'SHA256' in s]
            publishers = [s['Publisher'] for s in bootloader['KnownVulnerableSamples'] if 'Publisher' in s]
            dates = [s['Date'] for s in bootloader['KnownVulnerableSamples'] if 'Date' in s]
            companies = [s['Company'] for s in bootloader['KnownVulnerableSamples'] if 'Company' in s]
            descriptions = [s['Description'] for s in bootloader['KnownVulnerableSamples'] if 'Description' in s]
            authentihash_md5s = [s['Authentihash']['MD5'] for s in bootloader['KnownVulnerableSamples'] if 'Authentihash' in s]
            authentihash_sha1s = [s['Authentihash']['SHA1'] for s in bootloader['KnownVulnerableSamples'] if 'Authentihash' in s]
            authentihash_sha256s = [s['Authentihash']['SHA256'] for s in bootloader['KnownVulnerableSamples'] if 'Authentihash' in s]

        
            row = {
                'Id': bootloader.get('Id', ''),
                'Author': bootloader.get('Author', ''),
                'Created': bootloader.get('Created', ''),
                'Command': bootloader.get('Command', ''),
                'Description': bootloader.get('Description', ''),
                'Usecase': bootloader.get('Usecase', ''),
                'Category': bootloader.get('Category', ''),
                'Privileges': bootloader.get('Privileges', ''),
                'MitreID': bootloader.get('MitreID', ''),
                'OperatingSystem': bootloader.get('OperatingSystem', ''),
                'Resources': bootloader.get('Resources', ''),
                'bootloader Description': bootloader.get('bootloader Description', ''),
                'Person': bootloader.get('Person', ''),
                'Handle': bootloader.get('Handle', ''),
                'Detection': bootloader.get('Detection', ''),
                'KnownVulnerableSamples_MD5': ', '.join(str(md5) for md5 in md5s),
                'KnownVulnerableSamples_SHA1': ', '.join(str(sha1) for sha1 in sha1s),
                'KnownVulnerableSamples_SHA256': ', '.join(str(sha256) for sha256 in sha256s),
                'KnownVulnerableSamples_Publisher': ', '.join(str(publisher) for publisher in publishers),
                'KnownVulnerableSamples_Date': ', '.join(str(date) for date in dates),
                'KnownVulnerableSamples_Company': ', '.join(str(company) for company in companies),
                'KnownVulnerableSamples_Description': ', '.join(str(description) for description in descriptions),
                'KnownVulnerableSamples_Authentihash_MD5': ', '.join(str(md5) for md5 in authentihash_md5s),
                'KnownVulnerableSamples_Authentihash_SHA1': ', '.join(str(sha1) for sha1 in authentihash_sha1s),
                'KnownVulnerableSamples_Authentihash_SHA256': ', '.join(str(sha256) for sha256 in authentihash_sha256s),
                'Verified': bootloader.get('Verified', ''),
                'Tags': ', '.join(str(tag) for tag in bootloader['Tags'])                                  
            }

            writer.writerow(row)





def write_top_os(bootloaders, output_dir, top_n=5):
    os_count = {}
    for bootloader in bootloaders:
        command = bootloader.get('Commands')
        if not command:
            continue
        os_name = command.get('OperatingSystem')
        if not os_name or os_name.isspace() or os_name.lower() == 'n/a':
            continue
        os_name = os_name.strip().replace(',', '')
        if os_name not in os_count:
            os_count[os_name] = 0
        os_count[os_name] += 1
    sorted_os = sorted(os_count.items(), key=lambda x: x[1], reverse=True)[:top_n]
    with open(f"{output_dir}/content/bootloaders_top_{top_n}_os.csv", "w") as f:
        writer = csv.writer(f)
        for os, count in sorted_os:
            for _ in range(count):
                writer.writerow([count, os])

def write_top_publishers(bootloaders, output_dir, top_n=5):
    publishers_count = {}

    for bootloader in bootloaders:
        for hash_info in bootloader['KnownVulnerableSamples']:
            publisher_str = hash_info.get('Publisher')  # Use the `get()` method here

            if not publisher_str:
                continue

            publishers = re.findall(r'\"(.*?)\"|([^,]+)', publisher_str)
            for publisher_tuple in publishers:
                publisher = next(filter(None, publisher_tuple)).strip()

                if publisher.lower() == 'n/a' or publisher.isspace() or publisher.lower() == 'ltd.':
                    continue

                if publisher not in publishers_count:
                    publishers_count[publisher] = 0

                publishers_count[publisher] += 1

    sorted_publishers = sorted(publishers_count.items(), key=lambda x: x[1], reverse=True)[:top_n]

    with open(f"{output_dir}/content/bootloaders_top_{top_n}_os.csv", "w") as f:
        writer = csv.writer(f)

        for publisher, count in sorted_publishers:
            for _ in range(count):
                writer.writerow([count, publisher])



def generate_doc_bootloaders(REPO_PATH, OUTPUT_DIR, TEMPLATE_PATH, messages, VERBOSE):
    manifest_files = []
    for root, dirs, files in os.walk(REPO_PATH):
        for file in files:
                manifest_files.append((os.path.join(root, file)))

    bootloaders = []
    for manifest_file in manifest_files:
        bootloader = dict()
        if VERBOSE:
            print("processing bootloader {0}".format(manifest_file))

        with open(manifest_file, 'r') as stream:
            try:
                object = list(yaml.safe_load_all(stream))[0]
            except yaml.YAMLError as exc:
                print(exc)
                print("Error reading {0}".format(manifest_file))
                sys.exit(1)

        bootloaders.append(object)

    # write markdowns
    j2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH), trim_blocks=True, autoescape=True, lstrip_blocks=False)
    d = datetime.datetime.now()
    template = j2_env.get_template('bootloader.md.j2')
    for bootloader in bootloaders:
        file_name = bootloader["Id"] + '.md'
        output_path = os.path.join(OUTPUT_DIR + '/content/bootloaders/' + file_name)
        output = template.render(bootloader=bootloader, time=str(d.strftime("%Y-%m-%d")))
        with open(output_path, 'w', encoding="utf-8") as f:
            f.write(output)
    messages.append("site_gen.py wrote {0} bootloaders markdown to: {1}".format(len(bootloaders),OUTPUT_DIR + '/content/bootloaders/'))

    # write api csv
    write_bootloaders_csv(bootloaders, OUTPUT_DIR, VERBOSE)
    messages.append("site_gen.py wrote bootloaders CSV to: {0}".format(OUTPUT_DIR + '/content/api/bootloaders.csv'))

    # write api json
    with open(OUTPUT_DIR + '/content/api/' + 'bootloaders.json', 'w', encoding='utf-8') as f:
        json.dump(bootloaders, f, ensure_ascii=False, indent=4)
    messages.append("site_gen.py wrote bootloaders JSON to: {0}".format(OUTPUT_DIR + '/content/api/bootloaders.json'))

    # write listing csv
    with open(OUTPUT_DIR + '/content/' + 'bootloaders_table.csv', 'w') as f:
        writer = csv.writer(f)
        for bootloader in bootloaders:
            link = '[' + bootloader['Tags'][0] + '](bootloaders/' + bootloader["Id"] + '/)'
            if ('SHA256' not in bootloader['KnownVulnerableSamples'][0]) or (bootloader['KnownVulnerableSamples'][0]['SHA256'] is None ) or (bootloader['KnownVulnerableSamples'][0]['SHA256'] == ''):
                sha256='not available '
            else:
                sha256='[' + bootloader['KnownVulnerableSamples'][0]['SHA256'] + '](bootloaders/' + bootloader["Id"]+ '/)'
            writer.writerow([link, sha256, bootloader['Category'].capitalize(), bootloader['Created']])
    messages.append("site_gen.py wrote bootloaders table to: {0}".format(OUTPUT_DIR + '/content/bootloaders_table.csv'))

    # write top 5 os
    write_top_os(bootloaders, OUTPUT_DIR)
    messages.append("site_gen.py wrote bootloaders products to: {0}".format(OUTPUT_DIR + '/content/bootloaders_top_n_products.csv'))

    return bootloaders, messages


if __name__ == "__main__":

    # grab arguments
    parser = argparse.ArgumentParser(description="Generates bootloaders.io site", epilog="""
    This tool converts all bootloaders.io yamls and builds the site with all the supporting components.""")
    parser.add_argument("-p", "--path", required=False, default="yaml", help="path to lolbootloader yaml folder. Defaults to `yaml`")
    parser.add_argument("-o", "--output", required=False, default="bootloaders.io", help="path to the output directory for the site, defaults to `bootloaders.io`")
    parser.add_argument("-v", "--verbose", required=False, default=False, action='store_true', help="prints verbose output")

    # parse them
    args = parser.parse_args()
    REPO_PATH = args.path
    OUTPUT_DIR = args.output
    VERBOSE = args.verbose


    TEMPLATE_PATH = os.path.join(REPO_PATH, '../bin/jinja2_templates')

    if VERBOSE:
        print("wiping the {0}/content/bootloaders/ folder".format(OUTPUT_DIR))

    # first clean up old bootloaders
    try:
        for root, dirs, files in os.walk(OUTPUT_DIR + '/content/bootloaders/'):
            for file in files:
                if file.endswith(".md") and not file == '_index.md':
                    os.remove(root + '/' + file)
    except OSError as e:
        print("error: %s : %s" % (file, e.strerror))
        sys.exit(1)


    # also clean up API artifacts
    if os.path.exists(OUTPUT_DIR + '/content/api/bootloaders.json'):
        os.remove(OUTPUT_DIR + '/content/api/bootloaders.json')         
    if os.path.exists(OUTPUT_DIR + '/content/api/bootloaders.csv'):        
        os.remove(OUTPUT_DIR + '/content/api/bootloaders.csv')


    messages = []
    bootloaders, messages = generate_doc_bootloaders(REPO_PATH, OUTPUT_DIR, TEMPLATE_PATH, messages, VERBOSE)

    # print all the messages from generation
    for m in messages:
        print(m)
    print("finished successfully!")
