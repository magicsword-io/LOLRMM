---
description: "Chrome Remote Desktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Chrome Remote Desktop"
displayTitle: "Chrome Remote Desktop"
---



# Chrome Remote Desktop


### Description

Chrome Remote Desktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `remote_host.exe`
- `remoting_host.exe`
- `C:\Program Files (x86)\Google\Chrome Remote Desktop\*`
- `*\Google\Chrome Remote Desktop\*`
- `*\remoting_host.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*remotedesktop-pa.googleapis.com`
    - `*remotedesktop.google.com`
    - `remotedesktop.google.com`


### Detections
- Detects potential network activity of Chrome Remote Desktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/chrome_remote_desktop_network_sigma.yml)
- Detects potential processes activity of Chrome Remote Desktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/chrome_remote_desktop_processes_sigma.yml)

### References
- [https://support.google.com/chrome/a/answer/2799701?hl=en](https://support.google.com/chrome/a/answer/2799701?hl=en)


