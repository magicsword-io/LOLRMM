+++
description = "Atera is a remote monitoring and management (RMM) tool. It is used by threat actors to deploy ransomware or facilitate command execution and lateral movement."
title = "Atera"
weight = 10
displayTitle = "Atera"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Atera


### Description

Atera is a remote monitoring and management (RMM) tool. It is used by threat actors to deploy ransomware or facilitate command execution and lateral movement.



**Created**: 2024/08/03


### Details

- **Website**: [https://www.atera.com/](https://www.atera.com/)

#### PE Metadata
- **Filename**: AteraAgent.exe
- **Original File Name**: AteraAgent.exe
- **Description**: AteraAgent

- **Privileges**: SYSTEM

- **Free**: Yes

- **Verification**: Yes

#### Supported Operating Systems
- Windows
- MacOS
- Linux

#### Capabilities
- Integrated remote access with Splashtop and AnyDesk
- Remote monitoring and management
- Patch management
- Network discovery
- Backup and disaster recovery
- Helpdesk and ticketing
- Reporting and analytics
- Billing and invoicing
- Customer portal
- Mobile app

#### Known Vulnerabilities
- [CVE-2023-26078](CVE-2023-26078)
- [CVE-2023-26077](CVE-2023-26077)

#### Installation Paths
- `*\AgentPackageNetworkDiscovery.exe`
- `*\AgentPackageTaskScheduler.exe`
- `*\ATERA Networks\AteraAgent\*`
- `*\AteraAgent.exe`
- `atera_agent.exe`
- `atera_agent.exe`
- `ateraagent.exe`
- `C:\Program Files\ATERA Networks\AteraAgent\*`
- `C:\Program Files\Atera Networks`
- `C:\Program Files (x86)\Atera Networks`
- `syncrosetup.exe`

### Forensic Artifacts

#### Disk Artifacts

- **File**: `C:\Program Files\ATERA Networks\AteraAgent\Packages\AgentPackageRunCommandInteractive\log.txt`
  **Description**: N/A


  **OS**: Windows

- **File**: `C:\Program Files\ATERA Networks\AteraAgent\Packages\*`
  **Description**: N/A


  **OS**: Windows

- **File**: `C:\Program Files\ATERA Networks\AteraAgent\AteraAgent.exe`
  **Description**: Atera service binary


  **OS**: Windows

- **File**: `C:\Program Files\Atera Networks\AlphaAgent.exe`
  **Description**: Atera service binary


  **OS**: Windows

- **File**: `C:\Program Files\ATERA Networks\AteraAgent\Packages\AgentPackageSTRemote\AgentPackageSTRemote.exe`
  **Description**: N/A


  **OS**: Windows

- **File**: `C:\Program Files\ATERA Networks\AteraAgent\Packages\AgentPackageMonitoring\AgentPackageMonitoring.exe`
  **Description**: N/A


  **OS**: Windows

- **File**: `C:\Program Files\ATERA Networks\AteraAgent\Packages\AgentPackageHeartbeat\AgentPackageHeartbeat.exe`
  **Description**: N/A


  **OS**: Windows

- **File**: `C:\Program Files\ATERA Networks\AteraAgent\Packages\AgentPackageFileExplorer\AgentPackageFileExplorer.exe`
  **Description**: N/A


  **OS**: Windows

- **File**: `C:\Program Files\ATERA Networks\AteraAgent\Packages\AgentPackageRunCommandInteractive\AgentPackageRunCommandInteractive.exe`
  **Description**: N/A


  **OS**: Windows


#### Event Log Artifacts
- Event Details:
  - **Event ID**: 7045
  - **Provider Name**: Service Control Manager
  - **Log File**: System.evtx
  - **Service Name**: AteraAgent
  - **Image Path**: "C:\\Program Files (x86)\\ATERA Networks\\AteraAgent\\AteraAgent.exe"
  - **Description**: Service installation event as result of AteraAgent installation.
- Event Details:
  - **Event ID**: 7045
  - **Provider Name**: Service Control Manager
  - **Log File**: System.evtx
  - **Service Name**: WinRing0_1_2_0
  - **Image Path**: "C:\\Program Files (x86)\\ATERA Networks\\AteraAgent\\Packages\\AgentPackageMonitoring\\OpenHardwareMonitorLib.sys"
  - **Description**: Service installation event as result of Atera pakcage manager installation.
- Event Details:
  - **Event ID**: 11707
  - **Provider Name**: MsiInstaller
  - **Log File**: Application.evtx
  - **Description**: Service installation event as result of AteraAgent installation.
- Event Details:
  - **Event ID**: 4688
  - **Provider Name**: Microsoft-Security-Auditing
  - **Log File**: Security.evtx
  - **Description**: Service installation event as result of AteraAgent installation.
  - **Command Line**: C:\\Program Files\\ATERA Networks\\AteraAgent\\Packages\\AgentPackageFileExplorer\\AgentPackageFileExplorer.exe XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXX XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXX agent-api.atera.com/Production 443 [BASE64BLOB]

#### Registry Artifacts
- **Path**: `HKLM\SOFTWARE\ATERA Networks\AlphaAgent`

- **Path**: `HKLM\SYSTEM\CurrentControlSet\Services\AteraAgent`

- **Path**: `KLM\SOFTWARE\WOW6432Node\Splashtop Inc.`

- **Path**: `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Splashtop Software Updater`

- **Path**: `HKLM\SYSTEM\ControlSet\Services\EventLog\Application\AlphaAgent`

- **Path**: `HKLM\SYSTEM\ControlSet\Services\EventLog\Application\AteraAgent`

- **Path**: `HKLM\SOFTWARE\Microsoft\Tracing\AteraAgent_RASAPI32`

- **Path**: `HKLM\SOFTWARE\Microsoft\Tracing\AteraAgent_RASMANCS`

- **Path**: `HKLM\SOFTWARE\ATERA Networks\*`


#### Network Artifacts

- **Description**: N/A
  **Domain**:
    `pubsub.atera.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `pubsub.pubnub.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `agentreporting.atera.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `getalphacontrol.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `app.atera.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `agenthb.atera.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `packagesstore.blob.core.windows.net`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `ps.pndsn.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `agent-api.atera.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `cacerts.thawte.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `agentreportingstore.blob.core.windows.net`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `atera-agent-heartbeat.servicebus.windows.net`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `ps.atera.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `atera.pubnubapi.com`

  **Port**: `N/A`

- **Description**: N/A
  **Domain**:
    `appcdn.atera.com`

  **Port**: `N/A`



### Detections
-   **AteraAgent malicious installations**

  Detects AteraAgent installations with suspicious command line arguments.


  [Link](https://github.com/The-DFIR-Report/Sigma-Rules/blob/d67407d357ad32b247e2a303abc5a38bb30fd576/rules/windows/process_creation/proc_creation_win_ateraagent_malicious_installations.yml)
  
-   **Atera Agent Installation**

  Detects Atera Agent installation.


  [Link](https://github.com/SigmaHQ/sigma/blob/782f0f524e6f797ea114fe0d87b22cb4abaa6b7c/rules/windows/builtin/application/msiinstaller/win_software_atera_rmm_agent_install.yml)
  

### References
- [https://support.atera.com/hc/en-us/articles/360015461139-Firewall-Settings-for-Atera-s-Integrations](https://support.atera.com/hc/en-us/articles/360015461139-Firewall-Settings-for-Atera-s-Integrations)
- [https://support.atera.com/hc/en-us/articles/215955967-Troubleshoot-Atera-s-Windows-agent](https://support.atera.com/hc/en-us/articles/215955967-Troubleshoot-Atera-s-Windows-agent)
- [https://support.atera.com/hc/en-us/articles/115015619747-Release-Notes-February-2018](https://support.atera.com/hc/en-us/articles/115015619747-Release-Notes-February-2018)
- [https://thedfirreport.com/?s=ateraagent](https://thedfirreport.com/?s=ateraagent)

### Acknowledgements
- Théo Letailleur (in/theosyn)- Nasreddine Bencherchali (@nas_bench)- Kostas (@kostastsale)

{{< /column >}}
{{< /block >}}
