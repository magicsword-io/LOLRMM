---
description: "ToDesk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "ToDesk"
displayTitle: "ToDesk"
---



# ToDesk


### Description

ToDesk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `todesk.exe`
- `ToDesk_Service.exe`
- `ToDesk_Setup.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `todesk.com`
    - `*.todesk.com`
    - `*.todesk.com`
    - `todesktop.com`


### Detections
- Detects potential network activity of ToDesk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/todesk_network_sigma.yml)
- Detects potential processes activity of ToDesk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/todesk_processes_sigma.yml)

### References
- [https://www.todesk.com/](https://www.todesk.com/)


