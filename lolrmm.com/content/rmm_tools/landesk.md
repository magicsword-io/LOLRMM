+++
description = "LANDesk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "LANDesk"
weight = 10
displayTitle = "LANDesk"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# LANDesk


### Description

LANDesk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `issuser.exe`
- `landeskagentbootstrap.exe`
- `LANDeskPortalManager.exe`
- `ldinv32.exe`
- `ldsensors.exe`
- `C:\Program Files (x86)\LANDesk\*`
- `*\LANDesk\*`
- `*\issuser.exe`
- `*\softmon.exe`
- `*\tmcsvc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.ivanticloud.com`
    - `*.ivanti.com`
    - `ivanti.com`


### Detections
- Detects potential network activity of LANDesk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/landesk_network_sigma.yml)
- Detects potential processes activity of LANDesk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/landesk_processes_sigma.yml)

### References
- [https://forums.ivanti.com/s/article/URL-exception-list-for-Ivanti-Security-Controls?language=en_US](https://forums.ivanti.com/s/article/URL-exception-list-for-Ivanti-Security-Controls?language=en_US)



{{< /column >}}
{{< /block >}}
