---
description: "I'm InTouch is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "I'm InTouch"
displayTitle: "I'm InTouch"
---



# I'm InTouch


### Description

I'm InTouch is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `iit.exe`
- `intouch.exe`
- `I'm InTouch Go Installer.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.01com.com`
    - `01com.com/imintouch-remote-pc-desktop`


### Detections
- Detects potential network activity of I'm InTouch RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/i'm_intouch_network_sigma.yml)
- Detects potential processes activity of I'm InTouch RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/i'm_intouch_processes_sigma.yml)

### References
- [https://www.01com.com/mobile/imintouch-remote-pc-desktop/faqs/remote-access/](https://www.01com.com/mobile/imintouch-remote-pc-desktop/faqs/remote-access/)


