---
description: "Splashtop (Beta) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Splashtop (Beta)"
displayTitle: "Splashtop (Beta)"
---



# Splashtop (Beta)


### Description

Splashtop (Beta) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `SRServer.exe`
- `SplashtopSOS.exe`
- `Splashtop_Streamer_Windows*.exe`
- `SRManager.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `splashtop.com`


### Detections
- Detects potential network activity of Splashtop (Beta) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/splashtop__beta__network_sigma.yml)
- Detects potential processes activity of Splashtop (Beta) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/splashtop__beta__processes_sigma.yml)



