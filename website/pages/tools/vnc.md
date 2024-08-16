---
description: "VNC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "VNC"
displayTitle: "VNC"
---



# VNC


### Description

VNC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `winvnc*.exe`
- `vncserver.exe`
- `winwvc.exe`
- `winvncsc.exe`
- `vncserverui.exe`
- `vncviewer.exe`
- `winvnc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `realvnc.com/en/connect/download/vnc`


### Detections
- Detects potential network activity of VNC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/vnc_network_sigma.yml)
- Detects potential processes activity of VNC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/vnc_processes_sigma.yml)

### References
- [https://realvnc.com/en/connect/download/vnc](https://realvnc.com/en/connect/download/vnc)


