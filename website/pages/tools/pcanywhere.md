---
description: "pcAnywhere is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "pcAnywhere"
displayTitle: "pcAnywhere"
---



# pcAnywhere


### Description

pcAnywhere is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `awhost32.exe`
- `awrem32.exe`
- `pcaquickconnect.exe`
- `winaw32.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`


### Detections
- Detects potential network activity of pcAnywhere RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pcanywhere_network_sigma.yml)
- Detects potential processes activity of pcAnywhere RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pcanywhere_processes_sigma.yml)

### References
- [https://en.wikipedia.org/wiki/PcAnywhere](https://en.wikipedia.org/wiki/PcAnywhere)


