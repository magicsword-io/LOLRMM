---
description: "QQ IM-remote assistance is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "QQ IM-remote assistance"
displayTitle: "QQ IM-remote assistance"
---



# QQ IM-remote assistance


### Description

QQ IM-remote assistance is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `qq.exe`
- `QQProtect.exe`
- `qqpcmgr.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.mdt.qq.com`
    - `*.desktop.qq.com`
    - `upload_data.qq.com`
    - `qq-messenger.en.softonic.com`


### Detections
- Detects potential network activity of QQ IM-remote assistance RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/qq_im-remote_assistance_network_sigma.yml)
- Detects potential processes activity of QQ IM-remote assistance RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/qq_im-remote_assistance_processes_sigma.yml)

### References
- [https://en.wikipedia.org/wiki/Tencent_QQ](https://en.wikipedia.org/wiki/Tencent_QQ)


