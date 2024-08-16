---
description: "Dameware-mini remote control Protocol is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Dameware-mini remote control Protocol"
displayTitle: "Dameware-mini remote control Protocol"
---



# Dameware-mini remote control Protocol


### Description

Dameware-mini remote control Protocol is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `dntus*.exe`
- `dwrcs.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `dameware.com`


### Detections
- Detects potential network activity of Dameware-mini remote control Protocol RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/dameware-mini_remote_control_protocol_network_sigma.yml)
- Detects potential processes activity of Dameware-mini remote control Protocol RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/dameware-mini_remote_control_protocol_processes_sigma.yml)



