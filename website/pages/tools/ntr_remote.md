---
description: "NTR Remote is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "NTR Remote"
displayTitle: "NTR Remote"
---



# NTR Remote


### Description

NTR Remote is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `NTRsupportPro_EN.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.ntrsupport.com`


### Detections
- Detects potential network activity of NTR Remote RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ntr_remote_network_sigma.yml)
- Detects potential processes activity of NTR Remote RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ntr_remote_processes_sigma.yml)

### References
- [DOA as of 2024](DOA as of 2024)


