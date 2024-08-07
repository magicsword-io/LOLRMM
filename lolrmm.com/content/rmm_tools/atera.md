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
- **OriginalFileName**: AteraAgent.exe
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
  - **EventID**: 7045
  - **ProviderName**: Service Control Manager
  - **LogFile**: System.evtx
  - **ServiceName**: AteraAgent
  - **ImagePath**: "C:\\Program Files (x86)\\ATERA Networks\\AteraAgent\\AteraAgent.exe"
  - **Description**: Service installation event as result of AteraAgent installation.
- Event Details:
  - **EventID**: 7045
  - **ProviderName**: Service Control Manager
  - **LogFile**: System.evtx
  - **ServiceName**: WinRing0_1_2_0
  - **ImagePath**: "C:\\Program Files (x86)\\ATERA Networks\\AteraAgent\\Packages\\AgentPackageMonitoring\\OpenHardwareMonitorLib.sys"
  - **Description**: Service installation event as result of Atera pakcage manager installation.
- Event Details:
  - **EventID**: 11707
  - **ProviderName**: MsiInstaller
  - **LogFile**: Application.evtx
  - **Data**: Product: AteraAgent -- Installation completed successfully.
  - **Description**: Service installation event as result of AteraAgent installation.
- Event Details:
  - **EventID**: 4688
  - **ProviderName**: Microsoft-Security-Auditing
  - **LogFile**: Security.evtx
  - **CommandLine**: C:\\Program Files\\ATERA Networks\\AteraAgent\\Packages\\AgentPackageFileExplorer\\AgentPackageFileExplorer.exe XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXX XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXX agent-api.atera.com/Production 443 [BASE64BLOB]
  - **Description**: Service installation event as result of AteraAgent installation.

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
- **Description**: N/A  **Domains**:
    - `pubsub.atera.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `pubsub.pubnub.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `agentreporting.atera.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `getalphacontrol.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `app.atera.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `agenthb.atera.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `packagesstore.blob.core.windows.net`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `ps.pndsn.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `agent-api.atera.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `cacerts.thawte.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `agentreportingstore.blob.core.windows.net`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `atera-agent-heartbeat.servicebus.windows.net`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `ps.atera.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `atera.pubnubapi.com`
  **Ports**:
    - `N/A`
- **Description**: N/A  **Domains**:
    - `appcdn.atera.com`
  **Ports**:
    - `N/A`


### Detections
- Detects AteraAgent installations with suspicious command line arguments.
  - [Sigma Rule](https://github.com/The-DFIR-Report/Sigma-Rules/blob/d67407d357ad32b247e2a303abc5a38bb30fd576/rules/windows/process_creation/proc_creation_win_ateraagent_malicious_installations.yml)
  - **AteraAgent malicious installations**
- Detects Atera Agent installation.
  - [Sigma Rule](https://github.com/SigmaHQ/sigma/blob/782f0f524e6f797ea114fe0d87b22cb4abaa6b7c/rules/windows/builtin/application/msiinstaller/win_software_atera_rmm_agent_install.yml)
  - **Atera Agent Installation**
- Detects potential registry activity of Atera RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/atera_registry_sigma.yml)
- Detects potential network activity of Atera RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/atera_network_sigma.yml)
- Detects potential files activity of Atera RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/atera_files_sigma.yml)
- Detects potential processes activity of Atera RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/atera_processes_sigma.yml)

### References
- [https://support.atera.com/hc/en-us/articles/360015461139-Firewall-Settings-for-Atera-s-Integrations](https://support.atera.com/hc/en-us/articles/360015461139-Firewall-Settings-for-Atera-s-Integrations)
- [https://support.atera.com/hc/en-us/articles/215955967-Troubleshoot-Atera-s-Windows-agent](https://support.atera.com/hc/en-us/articles/215955967-Troubleshoot-Atera-s-Windows-agent)
- [https://support.atera.com/hc/en-us/articles/115015619747-Release-Notes-February-2018](https://support.atera.com/hc/en-us/articles/115015619747-Release-Notes-February-2018)
- [https://thedfirreport.com/?s=ateraagent](https://thedfirreport.com/?s=ateraagent)

### Acknowledgements
- Théo Letailleur (in/theosyn)- Nasreddine Bencherchali (@nas_bench)- Kostas (@kostastsale)

{{< /column >}}
{{< /block >}}
