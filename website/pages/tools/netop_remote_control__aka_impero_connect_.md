---
description: "Netop Remote Control (aka Impero Connect) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Netop Remote Control (aka Impero Connect)"
displayTitle: "Netop Remote Control (aka Impero Connect)"
---



# Netop Remote Control (aka Impero Connect)


### Description

Netop Remote Control (aka Impero Connect) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `nhostsvc.exe`
- `nhstw32.exe`
- `nldrw32.exe`
- `rmserverconsolemediator.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `imperosoftware.com/impero-connect/`


### Detections
- Detects potential network activity of Netop Remote Control (aka Impero Connect) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/netop_remote_control__aka_impero_connect__network_sigma.yml)
- Detects potential processes activity of Netop Remote Control (aka Impero Connect) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/netop_remote_control__aka_impero_connect__processes_sigma.yml)



