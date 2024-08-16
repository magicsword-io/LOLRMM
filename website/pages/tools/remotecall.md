---
description: "RemoteCall is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "RemoteCall"
displayTitle: "RemoteCall"
---



# RemoteCall


### Description

RemoteCall is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rcengmgru.exe`
- `rcmgrsvc.exe`
- `rxstartsupport.exe`
- `rcstartsupport.exe`
- `raautoup.exe`
- `agentu.exe`
- `remotesupportplayeru.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.remotecall.com`
    - `*.startsupport.com`
    - `remotecall.com`


### Detections
- Detects potential network activity of RemoteCall RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remotecall_network_sigma.yml)
- Detects potential processes activity of RemoteCall RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remotecall_processes_sigma.yml)

### References
- [https://help.remotecall.com/hc/en-us/articles/360005128814--RemoteCall-Server-List-For-Firewall](https://help.remotecall.com/hc/en-us/articles/360005128814--RemoteCall-Server-List-For-Firewall)


