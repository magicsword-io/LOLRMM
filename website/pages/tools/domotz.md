---
description: "Domotz is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Domotz"
displayTitle: "Domotz"
---



# Domotz


### Description

Domotz is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `domotz.exe`
- `Domotz Pro Desktop App.exe`
- `domotz_bash.exe`
- `domotz*.exe`
- `Domotz Pro Desktop App Setup*.exe`
- `domotz-windows*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.domotz.co`
    - `domotz.com`
    - `*cell-1.domotz.com`


### Detections
- Detects potential network activity of Domotz RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/domotz_network_sigma.yml)
- Detects potential processes activity of Domotz RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/domotz_processes_sigma.yml)

### References
- [https://help.domotz.com/tips-tricks/unblock-outgoing-connections-on-firewall/](https://help.domotz.com/tips-tricks/unblock-outgoing-connections-on-firewall/)


