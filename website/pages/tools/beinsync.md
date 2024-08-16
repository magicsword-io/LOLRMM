---
description: "BeInSync is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "BeInSync"
displayTitle: "BeInSync"
---



# BeInSync


### Description

BeInSync is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `Beinsync*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.beinsync.net`
    - `*.beinsync.com`


### Detections
- Detects potential network activity of BeInSync RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/beinsync_network_sigma.yml)
- Detects potential processes activity of BeInSync RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/beinsync_processes_sigma.yml)

### References
- [https://en.wikipedia.org/wiki/Phoenix_Technologies](https://en.wikipedia.org/wiki/Phoenix_Technologies)


