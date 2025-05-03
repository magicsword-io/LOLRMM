# LOLRMM - Living Off the Land Remote Monitoring and Management 🖥️🔍

![CI build](https://github.com/magicsword-io/LOLRMM/actions/workflows/validate.yml/badge.svg)
![RMM Tools](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/magicsword-io/LOLRMM/main/rmm-tools-count.json)

Welcome to LOLRMM (Living Off the Land Remote Monitoring and Management), a community-driven project that provides a curated list of Remote Monitoring and Management (RMM) tools that could potentially be abused by threat actors. Our mission is to assist security professionals in staying informed about these tools and their potential for misuse, providing the community a catalog of these tools which can be used for threat hunting, detection and prevention policy creations.

## 🌟 Key Features

- A comprehensive collection of RMM tools, that have historically been abused by threat actors
- Structured YAML files that describe key details of each RMM tool, including:
  - Tool name and description
  - Author and creation/modification dates
  - Technical details (website, PE metadata, privileges required, etc.)
  - Supported operating systems and capabilities
  - Known vulnerabilities
  - Installation paths
  - Artifacts left on disk, in event logs, registry, or network
  - Detection methods (including Sigma rules)
  - References and acknowledgements
- Integrates with Sigma to provide detection rules for RMM tools

## 🚀 Getting Started

To begin working with LOLRMM, you can:

1. Check out the [LOLRMM website](https://lolrmm.io/) for browsing the catalog.
2. Clone the repository to explore the YAML files directly.
3. Use our API to access the data programmatically in JSON or CSV format.

### API Usage Example

To fetch the complete list of RMM tools in JSON format, you can use the following curl command:

```bash
curl https://lolrmm.io/api/rmm_tools.json
```

This will return a JSON array containing detailed information about all cataloged RMM tools.

For CSV format, simply change the extension to `.csv`:

```bash
curl https://lolrmm.io/api/rmm_tools.csv
```

These APIs provide an easy way to integrate LOLRMM data into your threat hunting, detection, and prevention workflows.

## Support 📞

Please use the [GitHub issue tracker](https://github.com/magicsword-io/LOLRMM/issues) to submit bugs or request features.

## 🤝 Contributing & Making PRs

Stay engaged with the LOLRMM community by regularly checking for updates and contributing to the project. Your involvement will help ensure the project remains up-to-date and even more valuable to others.

If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them to your branch
4. Push your changes to your fork
5. Open a Pull Request (PR) against the upstream repository

For more detailed instructions, please refer to the CONTRIBUTING.md file (if available). To create a new YAML file for an RMM tool, use the provided YAML templates in the `yaml` directory.

## 🚨 Sigma Detection

LOLRMM provides Sigma detection rules to help you effectively detect potential threats related to RMM tools. To explore these rules in detail, navigate to the `detections/sigma/` directory.

Happy hunting! 🕵️‍♂️

## 🏗️ Building and Testing Locally

### Requirements

* [Python 3.10](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/docs/#installation)
* [Node.js](https://nodejs.org/)

### Steps to Build and Test Locally

1. Clone the repository:
```
git clone https://github.com/magicsword-io/LOLRMM.git
```

2. Change to the project directory:
```
cd LOLRMM
```

3. Install dependencies:
```
poetry install
```

4. Activate the virtual environment:
```
poetry shell
```

5. Build the site using the files under the /yaml folder:
```
python bin/site.py
```

6. Change to the website directory and install dependencies:
```
cd website && pnpm i
```

7. Run the website locally:
```
pnpm dev
```

8. Visit `http://localhost:3000` in your browser to view the site.

Join us in our quest to create a safer and more secure digital environment for organizations everywhere. With LOLRMM by your side, you'll be well-equipped to understand and address the potential risks associated with RMM tools in the ever-evolving cyber landscape.

## 🤖 GitHub Actions

### Purpose

The GitHub workflow files in the `.github/workflows` directory automate various tasks and processes for continuous integration, continuous delivery, and other project maintenance activities.
These workflow files leverage GitHub Actions to execute predefined steps based on specific triggers such as code pushes, pull requests, or scheduled intervals.

### Key Goals
- **Automate Testing**: Ensure that all code changes pass necessary tests before merging into the main branch.
- **Continuous Integration**: Automatically build and validate the project in different environments and configurations.
- **Code Quality Checks**: Run static analysis tools to maintain code quality and adherence to coding standards.
- **Deployment**: Manage the deployment process to various environments, ensuring seamless and reliable releases.
- **Badge Updates**: Automatically update project badges to reflect the current status, such as the number of Remote Monitoring and Management (RMM)

### Prerequisites
To create a `PUSH_TOKEN` for use in your GitHub Actions workflow, you'll need to generate a personal access token (PAT) on GitHub and then add it to your repository's secrets. Here's how to do it:

#### Steps to Create a Personal Access Token:
1. **Log in to GitHub**: Open your web browser and log in to your GitHub account.
2. **Generate a Token**:
   - Click on your profile picture in the top right corner and select "Settings".
   - In the left sidebar, click on "Developer settings".
   - Click on "Personal access tokens" and then "Tokens (classic)".
   - Click the "Generate new token" button.
   - Set a descriptive name for the token, like `PUSH_TOKEN`.
   - Select the appropriate scopes. At a minimum, you need `repo` scope for repository access.
   - Click "Generate token".
   - **Important**: Copy the token now and save it somewhere secure. You won't be able to see it again.

#### Steps to Add the Token to Your Repository's Secrets:
1. **Navigate to Your Repository**: Go to the main page of your repository on GitHub.
2. **Open Settings**:
   - Click on the "Settings" tab.
   - In the left sidebar, click on "Secrets and variables" and then "Actions".
3. **Add a New Secret**:
   - Click the "New repository secret" button.
   - Set the name of the secret to `PUSH_TOKEN`.
   - Paste the personal access token you generated earlier into the "Value" field.
   - Click "Add secret".

Now, your workflow file will use the `PUSH_TOKEN` from your repository secrets when it runs.

If you follow these steps, your `PUSH_TOKEN` should be correctly created and accessible for your GitHub Actions workflow.
