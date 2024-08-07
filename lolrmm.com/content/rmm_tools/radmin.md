+++
description = "RAdmin is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "RAdmin"
weight = 10
displayTitle = "RAdmin"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# RAdmin


### Description

RAdmin is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.


**Author**: Nasreddine Bencherchali

**Created**: 2024-08-05

**Last Modified**: 2024-08-05

### Details

- **Website**: [https://www.radmin.com/](https://www.radmin.com/)

#### PE Metadata
- **Filename**: RServer3.exe
- **OriginalFileName**: RServer3.exe
- **InternalName**: RServer3
- **Description**: Radmin Server
- **Product**: Radmin Server
- **Comments**: Radmin - Remote Control Server
- **Filename**: Radmin.exe
- **OriginalFileName**: Radmin.exe
- **InternalName**: Radmin
- **Description**: Radmin Viewer
- **Product**: Radmin Viewer
- **Comments**: Radmin Viewer


- **Free**: No

- **Verification**: No

#### Supported Operating Systems
- Windows



#### Installation Paths
- `C:\Program Files (x86)\Radmin Viewer 3\Radmin.exe`
- `C:\Windows\SysWOW64\rserver30\rserver3.exe`
- `C:\Windows\SysWOW64\rserver30\FamItrfc`
- `C:\Windows\SysWOW64\rserver30\FamItrf2`

### Forensic Artifacts

#### Disk Artifacts
- **File**: `C:\Windows\SysWOW64\rserver30\Radm_log.htm`
  **Description**: RAdmin log file (32-bit)
  **OS**: Windows
- **File**: `C:\Windows\System32\rserver30\Radm_log.htm`
  **Description**: RAdmin log file (64-bit)
  **OS**: Windows
- **File**: `C:\Windows\System32\rserver30\CHATLOGS\*\*.htm`
  **Description**: RAdmin chat logs
  **OS**: Windows
- **File**: `C:\Users\*\Documents\ChatLogs\*\*.htm`
  **Description**: RAdmin user chat logs
  **OS**: Windows


#### Registry Artifacts
- **Path**: `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Radmin\v3.0\Server\Parameters\Radmin Security`
  **Description**: N/A

#### Network Artifacts
- **Description**: N/A  **Domains**:
    - `radmin.com`
  **Ports**:
    - `443`


### Detections
- PUA - Radmin Viewer Utility Execution
  - [Sigma Rule](https://github.com/SigmaHQ/sigma/blob/782f0f524e6f797ea114fe0d87b22cb4abaa6b7c/rules/windows/process_creation/proc_creation_win_pua_radmin.yml)
- Enumeration for 3rd Party Creds From CLI
  - [Sigma Rule](https://github.com/SigmaHQ/sigma/blob/782f0f524e6f797ea114fe0d87b22cb4abaa6b7c/rules/windows/process_creation/proc_creation_win_registry_enumeration_for_credentials_cli.yml)
- Detects potential registry activity of RAdmin RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/radmin_registry_sigma.yml)
- Detects potential network activity of RAdmin RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/radmin_network_sigma.yml)
- Detects potential files activity of RAdmin RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/radmin_files_sigma.yml)
- Detects potential processes activity of RAdmin RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/radmin_processes_sigma.yml)

### References
- [https://radmin-club.com/radmin/how-to-establish-a-connection-outside-of-lan/](https://radmin-club.com/radmin/how-to-establish-a-connection-outside-of-lan/)
- [https://helpdesk.radmin.com/radmin3help/](https://helpdesk.radmin.com/radmin3help/)
- [https://helpdesk.radmin.com/radmin3help/files/viewercmd.htm](https://helpdesk.radmin.com/radmin3help/files/viewercmd.htm)
- [https://helpdesk.radmin.com/radmin3help/files/cmd.htm](https://helpdesk.radmin.com/radmin3help/files/cmd.htm)

### Acknowledgements
- Nasreddine Bencherchali (@nas_bench)

{{< /column >}}
{{< /block >}}
