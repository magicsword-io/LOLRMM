---
description: "Panorama9 is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Panorama9"
displayTitle: "Panorama9"
---



# Panorama9


### Description

Panorama9 is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `p9agent*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `trusted.panorama9.com`
    - `changes.panorama9.com`
    - `panorama9.com`


### Detections
- Detects potential network activity of Panorama9 RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/panorama9_network_sigma.yml)
- Detects potential processes activity of Panorama9 RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/panorama9_processes_sigma.yml)

### References
- [https://support.panorama9.com/en/articles/1859605-what-ports-and-hosts-does-the-p9-agent-communicate-with](https://support.panorama9.com/en/articles/1859605-what-ports-and-hosts-does-the-p9-agent-communicate-with)


