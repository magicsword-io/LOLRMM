---
description: "Seetrol is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Seetrol"
displayTitle: "Seetrol"
---



# Seetrol


### Description

Seetrol is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `seetrolcenter.exe`
- `seetrolclient.exe`
- `seetrolmyservice.exe`
- `seetrolremote.exe`
- `seetrolsetting.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `seetrol.co.kr`


### Detections
- Detects potential network activity of Seetrol RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/seetrol_network_sigma.yml)
- Detects potential processes activity of Seetrol RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/seetrol_processes_sigma.yml)

### References
- [http://www.seetrol.com/en/features/features3.php](http://www.seetrol.com/en/features/features3.php)


