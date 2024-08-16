---
description: "RustDesk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "RustDesk"
displayTitle: "RustDesk"
---



# RustDesk


### Description

RustDesk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rustdesk*.exe`
- `rustdesk.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `rustdesk.com`
    - `user_managed`
    - `web.rustdesk.com`


### Detections
- Detects potential network activity of RustDesk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rustdesk_network_sigma.yml)
- Detects potential processes activity of RustDesk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rustdesk_processes_sigma.yml)

### References
- [https://rustdesk.com/docs/en/](https://rustdesk.com/docs/en/)


