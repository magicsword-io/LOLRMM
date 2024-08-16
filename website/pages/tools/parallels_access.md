---
description: "Parallels Access is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Parallels Access"
displayTitle: "Parallels Access"
---



# Parallels Access


### Description

Parallels Access is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `parallelsaccess-*.exe`
- `TSClient.exe`
- `prl_deskctl_agent.exe`
- `prl_deskctl_wizard.exe`
- `prl_pm_service.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.parallels.com`
    - `parallels.com/products/ras/try`


### Detections
- Detects potential network activity of Parallels Access RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/parallels_access_network_sigma.yml)
- Detects potential processes activity of Parallels Access RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/parallels_access_processes_sigma.yml)

### References
- [https://kb.parallels.com/en/129097](https://kb.parallels.com/en/129097)


