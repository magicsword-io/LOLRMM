---
description: "Action1 is a powerful Remote Monitoring and Management(RMM) tool that enables users to execute commands, scripts, and binaries.  Through the web interface of action1, the administrator must create a new policy or an app to establish remote execution and then points that the agent is installed."
title: "Action1"
displayTitle: "Action1"
---



# Action1


### Description

Action1 is a powerful Remote Monitoring and Management(RMM) tool that enables users to execute commands, scripts, and binaries. 
Through the web interface of action1, the administrator must create a new policy or an app to establish remote execution and then points that the agent is installed.


**Author**: @kostastsale

**Created**: 2024-08-03

**Last Modified**: 2024-08-03

### Details

- **Website**: [https://www.action1.com/](https://www.action1.com/)

#### PE Metadata
- **Filename**: action1_connector.exe
- **Filename**: action1_remote.exe
- **Filename**: action1_update.exe
- **Filename**: action1_agent.exe
- **OriginalFileName**: action1_agent.exe
- **Description**: Endpoint Agent

- **Privileges**: SYSTEM

- **Free**: Yes

- **Verification**: Yes

#### Supported Operating Systems
- Windows

#### Capabilities
- Backup and disaster recovery
- Billing and invoicing
- Customer portal
- HelpDesk and ticketing
- Mobile app
- Network discovery
- Patch management
- Remote monitoring and management
- Reporting and analytics


#### Installation Paths
- `C:\Windows\Action1\*`

### Forensic Artifacts

#### Disk Artifacts
- **File**: `C:\Windows\Action1\action1_agent.exe`
  **Description**: Action1 service binary
  **OS**: Windows
- **File**: `C:\Windows\Action1\*`
  **Description**: Multiple files and binaries related to Action1 installation
  **OS**: Windows
- **File**: `C:\Windows\Action1\scripts\*`
  **Description**: Multiple scripts related to Action1 installation
  **OS**: Windows
- **File**: `C:\Windows\Action1\rule_data\*`
  **Description**: Files related to Action1 rules
  **OS**: Windows
- **File**: `C:\Windows\Action1\action1_log_*.log`
  **Description**: Contains history, errors, system notifications. Incoming and outgoing connections.
  **OS**: Windows

#### Event Log Artifacts
- Event Details:
  - **EventID**: 7045
  - **ProviderName**: Service Control Manager
  - **LogFile**: System.evtx
  - **ServiceName**: Action1 Agent
  - **ImagePath**: "C:\\Windows\\Action1\\action1_agent.exe"
  - **Description**: Service installation event as result of Action1 installation.
- Event Details:
  - **EventID**: 4688
  - **ProviderName**: Microsoft-Security-Auditing
  - **LogFile**: Security.evtx
  - **CommandLine**: C:\Windows\Action1\action1_agent.exe service
  - **Description**: Service installation event as result of Action1 installation.
- Event Details:
  - **EventID**: 4688
  - **ProviderName**: Microsoft-Security-Auditing
  - **LogFile**: Security.evtx
  - **CommandLine**: C:\Windows\Action1\action1_agent.exe loggedonuser
  - **Description**: Executing command to get logged on user.

#### Registry Artifacts
- **Path**: `HKLM\System\CurrentControlSet\Services\A1Agent`
  **Description**: Service installation event as result of Action1 installation.
- **Path**: `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\Windows Error Reporting\LocalDumps\action1_agent.exe`
  **Description**: Ensures that detailed crash information is available for analysis, which aids in maintaining the stability and reliability of the software.
- **Path**: `HKLM\SOFTWARE\WOW6432Node\Action1`
  **Description**: Storing its configuration settings and other relevant information

#### Network Artifacts
- **Description**: N/A
<br/>**Domains**:
    - `*.action1.com`
  **Ports**:
    - `443`
- **Description**: N/A
<br/>**Domains**:
    - `a1-backend-packages.s3.amazonaws.com`
  **Ports**:
    - `443`


### Detections
- Threat hunting rule for detecting the execution of arbitrary code and remote sessions via Action1 RMM
  - **Arbitrary code execution and remote sessions via Action1 RMM**
  - Author: @kostastsale
  - [Additional Information](https://github.com/tsale/Sigma_rules/blob/ea87e4fc851207ca0f002ec043624f2b3bf1b2da/Threat%20Hunting%20Queries/Action1_RMM.yml)
- Detects potential registry activity of Action1 RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/action1_registry_sigma.yml)
- Detects potential network activity of Action1 RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/action1_network_sigma.yml)
- Detects potential files activity of Action1 RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/action1_files_sigma.yml)

### References
- [https://www.action1.com/documentation/firewall-configuration/](https://www.action1.com/documentation/firewall-configuration/)
- [https://www.action1.com/documentation/](https://www.action1.com/documentation/)
- [https://twitter.com/Kostastsale/status/1646256901506605063?s=20](https://twitter.com/Kostastsale/status/1646256901506605063?s=20)
- [https://ruler-project.github.io/ruler-project/RULER/remote/Action1/](https://ruler-project.github.io/ruler-project/RULER/remote/Action1/)

### Acknowledgements
- Kostas (@kostastsale)
