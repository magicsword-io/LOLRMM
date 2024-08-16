---
description: "Guacamole is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Guacamole"
displayTitle: "Guacamole"
---



# Guacamole


### Description

Guacamole is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `guacd.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `guacamole.apache.org`


### Detections
- Detects potential network activity of Guacamole RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/guacamole_network_sigma.yml)
- Detects potential processes activity of Guacamole RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/guacamole_processes_sigma.yml)

### References
- [guacamole.apache.org](guacamole.apache.org)


