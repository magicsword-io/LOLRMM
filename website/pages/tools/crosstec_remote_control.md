---
description: "CrossTec Remote Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "CrossTec Remote Control"
displayTitle: "CrossTec Remote Control"
---



# CrossTec Remote Control


### Description

CrossTec Remote Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `PCIVIDEO.EXE`
- `supporttool.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `crosstecsoftware.com/remotecontrol`


### Detections
- Detects potential network activity of CrossTec Remote Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/crosstec_remote_control_network_sigma.yml)
- Detects potential processes activity of CrossTec Remote Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/crosstec_remote_control_processes_sigma.yml)

### References
- [www.crosstecsoftware.com/supporthome.html - domain DOA 2/1/2024](www.crosstecsoftware.com/supporthome.html - domain DOA 2/1/2024)


