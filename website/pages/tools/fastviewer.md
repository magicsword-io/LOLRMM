---
description: "FastViewer is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "FastViewer"
displayTitle: "FastViewer"
---



# FastViewer


### Description

FastViewer is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `fastclient.exe`
- `fastmaster.exe`
- `FastViewer.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.fastviewer.com`
    - `fastviewer.com`


### Detections
- Detects potential network activity of FastViewer RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fastviewer_network_sigma.yml)
- Detects potential processes activity of FastViewer RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fastviewer_processes_sigma.yml)

### References
- [https://fastviewer.com/demo/EN_FastViewer_Server%20Installation%20Configuration.pdf](https://fastviewer.com/demo/EN_FastViewer_Server%20Installation%20Configuration.pdf)


