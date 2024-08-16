---
description: "Jump Desktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Jump Desktop"
displayTitle: "Jump Desktop"
---



# Jump Desktop


### Description

Jump Desktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `jumpclient.exe`
- `jumpdesktop.exe`
- `jumpservice.exe`
- `jumpconnect.exe`
- `jumpupdater.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.jumpdesktop.com`
    - `jumpdesktop.com`
    - `jumpto.me`
    - `*.jumpto.me`


### Detections
- Detects potential network activity of Jump Desktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/jump_desktop_network_sigma.yml)
- Detects potential processes activity of Jump Desktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/jump_desktop_processes_sigma.yml)

### References
- [https://support.jumpdesktop.com/hc/en-us/articles/360042490351-Administrators-Guide-For-Jump-Desktop-Connect](https://support.jumpdesktop.com/hc/en-us/articles/360042490351-Administrators-Guide-For-Jump-Desktop-Connect)


