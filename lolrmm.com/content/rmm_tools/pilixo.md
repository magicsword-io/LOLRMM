+++
description = "Pilixo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Pilixo"
weight = 10
displayTitle = "Pilixo"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Pilixo


### Description

Pilixo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rdp.exe`
- `Pilixo_Installer*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `pilixo.com`
    - `download.pilixo.com`
    - `*.pilixo.com`


### Detections
- Detects potential network activity of Pilixo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pilixo_network_sigma.yml)
- Detects potential processes activity of Pilixo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pilixo_processes_sigma.yml)

### References
- [https://pilixo.freshdesk.com/support/solutions/articles/9000141879-device-connectivity-and-firewalls](https://pilixo.freshdesk.com/support/solutions/articles/9000141879-device-connectivity-and-firewalls)



{{< /column >}}
{{< /block >}}
