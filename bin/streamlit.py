import streamlit as st
import yaml
from datetime import datetime, date
import os
import jsonschema
import json
from pathlib import Path


def load_schema(schema_file="bin/spec/lolrmm.spec.json"):
    try:
        with open(schema_file, "r") as f:
            return json.load(f)
    except IOError:
        st.error(f"ERROR: reading schema file {schema_file}")
        return None


def list_yaml_files():
    yaml_files = [
        f for f in os.listdir("yaml") if f.endswith(".yaml") or f.endswith(".yml")
    ]
    return ["New RMM Tool"] + yaml_files


def load_yaml_template(filename):
    if filename == "New RMM Tool":
        return default_template()
    try:
        with open(f"yaml/{filename}", "r") as file:
            data = yaml.safe_load(file)

            # Provide default values for empty fields
            default = default_template()

            # Handle PEMetadata as a list
            pe_metadata = data.get("Details", {}).get("PEMetadata", [])
            pe_metadata_dict = (
                pe_metadata[0] if isinstance(pe_metadata, list) and pe_metadata else {}
            )

            # Merge the loaded data with default values
            merged_data = {
                "Name": data.get("Name", ""),
                "Category": data.get("Category") or default["Category"],
                "Description": data.get("Description", ""),
                "Author": data.get("Author") or default["Author"],
                "Created": data.get("Created") or default["Created"],
                "LastModified": data.get("LastModified") or default["LastModified"],
                "Details": {
                    "Website": data.get("Details", {}).get("Website")
                    or default["Details"]["Website"],
                    "PEMetadata": {
                        "Filename": pe_metadata_dict.get("Filename")
                        or default["Details"]["PEMetadata"]["Filename"],
                        "OriginalFileName": pe_metadata_dict.get("OriginalFileName")
                        or default["Details"]["PEMetadata"]["OriginalFileName"],
                        "Description": pe_metadata_dict.get("Description")
                        or default["Details"]["PEMetadata"]["Description"],
                        "Product": pe_metadata_dict.get("Product")
                        or default["Details"]["PEMetadata"]["Product"],
                    },
                    "Privileges": data.get("Details", {}).get("Privileges")
                    or default["Details"]["Privileges"],
                    "Free": data.get("Details", {}).get("Free", False),
                    "Verification": data.get("Details", {}).get("Verification", False),
                    "SupportedOS": data.get("Details", {}).get("SupportedOS")
                    or default["Details"]["SupportedOS"],
                    "Capabilities": data.get("Details", {}).get("Capabilities")
                    or default["Details"]["Capabilities"],
                    "Vulnerabilities": data.get("Details", {}).get("Vulnerabilities")
                    or default["Details"]["Vulnerabilities"],
                    "InstallationPaths": data.get("Details", {}).get(
                        "InstallationPaths"
                    )
                    or default["Details"]["InstallationPaths"],
                },
                "Artifacts": data.get("Artifacts") or default["Artifacts"],
                "Detections": data.get("Detections") or default["Detections"],
                "References": data.get("References") or default["References"],
                "Acknowledgement": data.get("Acknowledgement")
                or default["Acknowledgement"],
            }

            # Update session state with the loaded name
            st.session_state.name = merged_data["Name"]

            return merged_data
    except yaml.YAMLError as e:
        st.error(f"Error loading YAML file: {e}")
        return default_template()
    except FileNotFoundError:
        st.warning(f"{filename} not found. Using default template.")
        return default_template()


def default_template():
    return {
        "Name": "",
        "Category": "",
        "Description": "",
        "Author": "",
        "Created": datetime.now().strftime("%Y-%m-%d"),
        "LastModified": datetime.now().strftime("%Y-%m-%d"),
        "Details": {
            "Website": "",
            "PEMetadata": {
                "Filename": "",
                "OriginalFileName": "",
                "Description": "",
                "Product": "",
            },
            "Privileges": "",
            "Free": False,
            "Verification": False,
            "SupportedOS": [],
            "Capabilities": [],
            "Vulnerabilities": [],
            "InstallationPaths": [],
        },
        "Artifacts": {"Disk": [], "EventLog": [], "Registry": [], "Network": []},
        "Detections": [],
        "References": [],
        "Acknowledgement": [],
    }


def save_yaml(data, filename):
    with open(f"yaml/{filename}.yaml", "w") as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)


def validate_yaml_data(yaml_data, schema):
    validator = jsonschema.Draft7Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    errors = list(validator.iter_errors(yaml_data))
    return errors


def check_hash_lengths(yaml_data):
    errors = []
    known_vulnerable_samples = yaml_data.get("KnownVulnerableSamples", [])
    for sample in known_vulnerable_samples:
        md5 = sample.get("MD5", "")
        if md5 and len(md5) != 32:
            errors.append(f"ERROR: MD5 length is not 32 characters")
        sha1 = sample.get("SHA1", "")
        if sha1 and len(sha1) != 40:
            errors.append(f"ERROR: SHA1 length is not 40 characters")
        sha256 = sample.get("SHA256", "")
        if sha256 and len(sha256) != 64:
            errors.append(f"ERROR: SHA256 length is not 64 characters")
    return errors


def main():
    st.set_page_config(layout="wide", page_title="LOLRMM")
    st.title("LOLRMM")

    if "name" not in st.session_state:
        st.session_state.name = ""

    yaml_files = list_yaml_files()
    selected_file = st.selectbox(
        "Select RMM Tool or create new", yaml_files, key="file_select"
    )

    template = load_yaml_template(selected_file)

    # Create tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Basic Info",
            "Details",
            "Artifacts",
            "Detections",
            "References & Acknowledgements",
        ]
    )

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            # Use a callback to update session state
            def update_name():
                st.session_state.name = st.session_state.name_input

            name = st.text_input(
                "RMM Tool Name",
                value=st.session_state.name,
                key="name_input",
                on_change=update_name,
            )
            st.write(f"Debug: Current name value: {st.session_state.name}")
            category = st.text_input(
                "Category", value=template.get("Category", ""), key="category"
            )
            author = st.text_input(
                "Author", value=template.get("Author", ""), key="author"
            )
        with col2:
            created_date = handle_date(template.get("Created", ""), "Created")
            created = st.date_input("Created Date", value=created_date, key="created")
            last_modified_date = handle_date(
                template.get("LastModified", ""), "LastModified"
            )
            last_modified = st.date_input(
                "Last Modified Date", value=last_modified_date, key="last_modified"
            )

        st.write(f"Debug: Template description: {template.get('Description', '')}")
        description = st.text_area(
            "Description",
            value=template.get("Description", ""),
            key="description",
            height=150,
        )
        st.write(f"Debug: Input description value: {description}")

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            website = st.text_input(
                "Website",
                value=template.get("Details", {}).get("Website", ""),
                key="website",
            )
            privileges = st.text_input(
                "Privileges",
                value=template.get("Details", {}).get("Privileges", ""),
                key="privileges",
            )
            free = st.checkbox(
                "Free", value=template.get("Details", {}).get("Free", False), key="free"
            )
            verification = st.checkbox(
                "Verification",
                value=template.get("Details", {}).get("Verification", False),
                key="verification",
            )

        with col2:
            with st.expander("PE Metadata"):
                filename = st.text_input(
                    "Filename",
                    value=template.get("Details", {})
                    .get("PEMetadata", {})
                    .get("Filename", ""),
                    key="filename",
                )
                original_filename = st.text_input(
                    "Original Filename",
                    value=template.get("Details", {})
                    .get("PEMetadata", {})
                    .get("OriginalFileName", ""),
                    key="original_filename",
                )
                pe_description = st.text_input(
                    "PE Description",
                    value=template.get("Details", {})
                    .get("PEMetadata", {})
                    .get("Description", ""),
                    key="pe_description",
                )
                product = st.text_input(
                    "Product",
                    value=template.get("Details", {})
                    .get("PEMetadata", {})
                    .get("Product", ""),
                    key="product",
                )

        all_os_options = ["Windows", "Mac", "Linux", "Android", "iOS", "ChromeOS"]
        template_supported_os = template.get("Details", {}).get("SupportedOS", [])
        template_supported_os = [
            os.title() if os != "iOS" else os for os in template_supported_os
        ]
        valid_supported_os = [
            os for os in template_supported_os if os in all_os_options
        ]

        supported_os = st.multiselect(
            "Supported OS",
            options=all_os_options,
            default=valid_supported_os,
            key="supported_os",
        )

        # Get the capabilities from the template
        template_capabilities = template.get("Details", {}).get("Capabilities", [])

        # Create a set of all unique capabilities (from template and some common ones)
        all_capabilities = set(
            template_capabilities
            + [
                "File Transfer",
                "File System Access",
                "Remote Control",
                "GUI Support",
                "Command line Support",
                "Remote monitoring and management",
                "Remote desktop",
                "Remote shell open",
            ]
        )

        capabilities = st.multiselect(
            "Capabilities",
            options=sorted(list(all_capabilities)),
            default=template_capabilities,
            key="capabilities",
        )

        vulnerabilities = st.text_area(
            "Vulnerabilities (one per line)",
            value="\n".join(template.get("Details", {}).get("Vulnerabilities", [])),
            key="vulnerabilities",
        )
        installation_paths = st.text_area(
            "Installation Paths (one per line)",
            value="\n".join(template.get("Details", {}).get("InstallationPaths", [])),
            key="installation_paths",
        )

    with tab3:
        artifact_types = ["Disk", "EventLog", "Registry", "Network", "Other"]
        artifacts = {}

        for artifact_type in artifact_types:
            with st.expander(f"{artifact_type} Artifacts"):
                artifacts[artifact_type] = []
                num_artifacts = st.number_input(
                    f"Number of {artifact_type} Artifacts",
                    min_value=0,
                    value=1,
                    key=f"num_{artifact_type}",
                )

                for i in range(num_artifacts):
                    st.markdown(f"**{artifact_type} Artifact {i+1}**")
                    artifact_data = {}

                    if artifact_type == "Disk":
                        artifact_data["File"] = st.text_input(
                            f"File {i+1}", key=f"{artifact_type}_{i}_file"
                        )
                        artifact_data["Description"] = st.text_input(
                            f"Description {i+1}", key=f"{artifact_type}_{i}_description"
                        )
                        artifact_data["OS"] = st.text_input(
                            f"OS {i+1}", key=f"{artifact_type}_{i}_os"
                        )
                        artifact_data["Example"] = st.text_area(
                            f"Example {i+1} (one per line)",
                            key=f"{artifact_type}_{i}_example",
                        ).split("\n")
                    elif artifact_type == "EventLog":
                        artifact_data["EventID"] = st.number_input(
                            f"EventID {i+1}", key=f"{artifact_type}_{i}_eventid"
                        )
                        artifact_data["ProviderName"] = st.text_input(
                            f"ProviderName {i+1}",
                            key=f"{artifact_type}_{i}_providername",
                        )
                        artifact_data["LogFile"] = st.text_input(
                            f"LogFile {i+1}", key=f"{artifact_type}_{i}_logfile"
                        )
                        artifact_data["ServiceName"] = st.text_input(
                            f"ServiceName {i+1}", key=f"{artifact_type}_{i}_servicename"
                        )
                        artifact_data["ImagePath"] = st.text_input(
                            f"ImagePath {i+1}", key=f"{artifact_type}_{i}_imagepath"
                        )
                        artifact_data["Description"] = st.text_input(
                            f"Description {i+1}", key=f"{artifact_type}_{i}_description"
                        )
                        artifact_data["CommandLine"] = st.text_input(
                            f"CommandLine {i+1}", key=f"{artifact_type}_{i}_commandline"
                        )
                    elif artifact_type == "Registry":
                        artifact_data["Path"] = st.text_input(
                            f"Path {i+1}", key=f"{artifact_type}_{i}_path"
                        )
                        artifact_data["Description"] = st.text_input(
                            f"Description {i+1}", key=f"{artifact_type}_{i}_description"
                        )
                    elif artifact_type == "Network":
                        artifact_data["Description"] = st.text_input(
                            f"Description {i+1}", key=f"{artifact_type}_{i}_description"
                        )
                        artifact_data["Domains"] = st.text_area(
                            f"Domains {i+1} (one per line)",
                            key=f"{artifact_type}_{i}_domains",
                        ).split("\n")
                        artifact_data["Ports"] = st.text_area(
                            f"Ports {i+1} (one per line)",
                            key=f"{artifact_type}_{i}_ports",
                        ).split("\n")
                    elif artifact_type == "Other":
                        artifact_data["Type"] = st.text_input(
                            f"Type {i+1}", key=f"{artifact_type}_{i}_type"
                        )
                        artifact_data["Value"] = st.text_input(
                            f"Value {i+1}", key=f"{artifact_type}_{i}_value"
                        )

                    artifacts[artifact_type].append(artifact_data)
                    st.markdown("---")

    with tab4:
        num_detections = st.number_input(
            "Number of Detections", min_value=0, value=1, key="num_detections"
        )
        detections = []
        for i in range(num_detections):
            with st.expander(f"Detection {i+1}"):
                name = st.text_input(f"Name", key=f"detection_{i}_name")
                description = st.text_area(
                    f"Description", key=f"detection_{i}_description"
                )
                author = st.text_input(f"Author", key=f"detection_{i}_author")
                link = st.text_input(f"Link", key=f"detection_{i}_link")
                detections.append(
                    {
                        "Name": name,
                        "Description": description,
                        "author": author,
                        "Link": link,
                    }
                )

    with tab5:
        col1, col2 = st.columns(2)
        with col1:
            references = st.text_area(
                "References (one per line)",
                value="\n".join(template.get("References", [])),
                key="references",
                height=200,
            )

        with col2:
            num_acknowledgements = st.number_input(
                "Number of Acknowledgements",
                min_value=0,
                value=1,
                key="num_acknowledgements",
            )
            acknowledgements = []
            for i in range(num_acknowledgements):
                st.markdown(f"**Acknowledgement {i+1}**")
                person = st.text_input(f"Person", key=f"ack_{i}_person")
                handle = st.text_input(f"Handle", key=f"ack_{i}_handle")
                acknowledgements.append({"Person": person, "Handle": handle})

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate YAML", key="generate_yaml"):
            st.write(f"Debug: Name at button press: {st.session_state.name}")
            if not st.session_state.name or st.session_state.name.strip() == "":
                st.error(
                    "A name for the RMM Tool is required. Please enter a name in the 'Basic Info' tab."
                )
            else:
                # Get the description from the form
                description_value = (
                    st.session_state.description
                )  # Get description from session state
                st.write(f"Debug: Description from session: {description_value}")

                if not description_value or description_value.strip() == "":
                    st.error(
                        "A description is required. Please enter a description in the 'Basic Info' tab."
                    )
                    return

                yaml_data = {
                    "Name": st.session_state.name,
                    "Category": category,
                    "Description": description_value,  # Use the description from session state
                    "Author": author,
                    "Created": created.strftime("%Y-%m-%d"),
                    "LastModified": last_modified.strftime("%Y-%m-%d"),
                    "Details": {
                        "Website": website,
                        "PEMetadata": {
                            "Filename": filename,
                            "OriginalFileName": original_filename,
                            "Description": pe_description,
                            "Product": product,
                        },
                        "Privileges": privileges,
                        "Free": free,
                        "Verification": verification,
                        "SupportedOS": supported_os,
                        "Capabilities": capabilities,
                        "Vulnerabilities": (
                            vulnerabilities.split("\n") if vulnerabilities else []
                        ),
                        "InstallationPaths": (
                            installation_paths.split("\n") if installation_paths else []
                        ),
                    },
                    "Artifacts": {
                        "Disk": artifacts.get("Disk", []),
                        "EventLog": artifacts.get("EventLog", []),
                        "Registry": artifacts.get("Registry", []),
                        "Network": artifacts.get("Network", []),
                    },
                    "Detections": detections,
                    "References": references.split("\n") if references else [],
                    "Acknowledgement": acknowledgements,
                }

                # Debug output
                st.write(
                    f"Debug: Final description in yaml_data: {yaml_data.get('Description', '')}"
                )

                # Don't filter out Description even if empty
                yaml_data = {
                    k: v for k, v in yaml_data.items()
                }  # Remove the filtering entirely

                schema = load_schema()
                if schema:
                    validation_errors = validate_yaml_data(yaml_data, schema)
                    hash_errors = check_hash_lengths(yaml_data)
                    all_errors = validation_errors + hash_errors

                    if all_errors:
                        st.error("Validation errors found:")
                        for error in all_errors:
                            st.error(str(error))
                    else:
                        filename = st.session_state.name.lower().replace(" ", "_")
                        save_yaml(yaml_data, filename)
                        st.success(
                            f"YAML file for {st.session_state.name} has been generated and saved as {filename}.yaml!"
                        )

                        st.session_state.yaml_content = yaml.dump(
                            yaml_data, default_flow_style=False, sort_keys=False
                        )
                else:
                    st.error("Could not load schema file. YAML generation aborted.")

    with col2:
        if st.button("View YAML", key="view_yaml"):
            if "yaml_content" in st.session_state and st.session_state.yaml_content:
                with st.expander("YAML Content", expanded=True):
                    st.code(st.session_state.yaml_content, language="yaml")
            else:
                st.warning(
                    "No YAML has been generated yet. Please generate YAML first."
                )


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
        st.warning(
            f"Invalid '{field_name}' date format in YAML: {date_value}. Using current date."
        )
        return datetime.now().date()


if __name__ == "__main__":
    main()
