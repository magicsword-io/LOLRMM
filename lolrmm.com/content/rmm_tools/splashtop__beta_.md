+++
description = "Splashtop (Beta) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Splashtop (Beta)"
weight = 10
displayTitle = "Splashtop (Beta)"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

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
- **Description**: Known remote domains  **Domains**:
    - `splashtop.com`


### Detections
- Detects potential network activity of Splashtop (Beta) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/splashtop__beta__network_sigma.yml)
- Detects potential processes activity of Splashtop (Beta) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/splashtop__beta__processes_sigma.yml)




{{< /column >}}
{{< /block >}}
