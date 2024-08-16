---
description: "Centurion is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Centurion"
displayTitle: "Centurion"
---



# Centurion


### Description

Centurion is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ctiserv.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `centuriontech.com`


### Detections
- Detects potential network activity of Centurion RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/centurion_network_sigma.yml)
- Detects potential processes activity of Centurion RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/centurion_processes_sigma.yml)

### References
- [https://data443.atlassian.net/servicedesk/customer/portal/20](https://data443.atlassian.net/servicedesk/customer/portal/20)


