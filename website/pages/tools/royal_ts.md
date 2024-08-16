---
description: "Royal TS is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Royal TS"
displayTitle: "Royal TS"
---



# Royal TS


### Description

Royal TS is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `royalts.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `royalapps.com`


### Detections
- Detects potential network activity of Royal TS RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/royal_ts_network_sigma.yml)
- Detects potential processes activity of Royal TS RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/royal_ts_processes_sigma.yml)



