+++
description = "Action1 is a powerful Remote Monitoring and Management(RMM) tool that enables users to execute commands, scripts, and binaries.  Through the web interface of action1, the administrator must create a new policy or an app to establish remote execution and then points that the agent is installed."
title = "Action1"
weight = 10
displayTitle = "Action1"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Action1


### Description

Action1 is a powerful Remote Monitoring and Management(RMM) tool that enables users to execute commands, scripts, and binaries.  Through the web interface of action1, the administrator must create a new policy or an app to establish remote execution and then points that the agent is installed.


**Author**: @kostastsale

**Created**: 2024/03/08


### Details

- **Website**: [https://www.action1.com/](https://www.action1.com/)

#### PE Metadata
- **Filename**: action1_agent.exe
- **Original File Name**: action1_agent.exe
- **Description**: Endpoint Agent

- **Privileges**: SYSTEM

- **Free**: Yes

- **Verification**: Yes

#### Supported Operating Systems
- Windows

#### Capabilities
- Remote monitoring and management
- Patch management
- Network discovery
- Backup and disaster recovery
- Helpdesk and ticketing
- Reporting and analytics
- Billing and invoicing
- Customer portal
- Mobile app


#### Installation Paths
- `action1_connector.exe`
- `action1_agent.exe`
- `action1_remote.exe`
- `action1_update.exe`

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


#### Event Log Artifacts
- Event Details:
  - **Event ID**: 7045
  - **Provider Name**: Service Control Manager
  - **Log File**: System.evtx
  - **Service Name**: Action1 Agent
  - **Image Path**: "C:\\Windows\\Action1\\action1_agent.exe"
  - **Description**: Service installation event as result of Action1 installation.
- Event Details:
  - **Event ID**: 4688
  - **Provider Name**: Microsoft-Security-Auditing
  - **Log File**: Security.evtx
  - **Description**: Service installation event as result of Action1 installation.
  - **Command Line**: C:\Windows\Action1\action1_agent.exe service
- Event Details:
  - **Event ID**: 4688
  - **Provider Name**: Microsoft-Security-Auditing
  - **Log File**: Security.evtx
  - **Description**: Executing command to get logged on user.
  - **Command Line**: C:\Windows\Action1\action1_agent.exe loggedonuser

#### Registry Artifacts
- **Path**: `HKLM\System\CurrentControlSet\Services\A1Agent`
  **Description**: Service installation event as result of Action1 installation.

- **Path**: `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\Windows Error Reporting\LocalDumps\action1_agent.exe`
  **Description**: Ensures that detailed crash information is available for analysis, which aids in maintaining the stability and reliability of the software.

- **Path**: `HKLM\SOFTWARE\WOW6432Node\Action1`
  **Description**: Storing its configuration settings and other relevant information


#### Network Artifacts

- **Description**: Known remote domains
  **Domain**:
    - `action1.com`
    - `a1-backend-packages.s3.amazonaws.com`
    - `*.action1.com`
    - `server.action1.com`

  **Port**: `22543`



### Detections
-   **Arbitrary code execution and remote sessions via Action1 RMM**

  Threat hunting rule for detecting the execution of arbitrary code and remote sessions via Action1 RMM

  (Author: @kostastsale)

  [Link](https://github.com/tsale/Sigma_rules/blob/ea87e4fc851207ca0f002ec043624f2b3bf1b2da/Threat%20Hunting%20Queries/Action1_RMM.yml)


### References
- [https://www.action1.com/documentation/firewall-configuration/](https://www.action1.com/documentation/firewall-configuration/)
- [https://www.action1.com/documentation/](https://www.action1.com/documentation/)
- [https://twitter.com/Kostastsale/status/1646256901506605063?s=20](https://twitter.com/Kostastsale/status/1646256901506605063?s=20)

### Acknowledgements
- Kostas (@kostastsale)

{{< /column >}}
{{< /block >}}
