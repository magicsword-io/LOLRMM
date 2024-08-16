---
description: "Netop Remote Control (Impero Connect) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Netop Remote Control (Impero Connect)"
displayTitle: "Netop Remote Control (Impero Connect)"
---



# Netop Remote Control (Impero Connect)


### Description

Netop Remote Control (Impero Connect) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

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
- `ngstw32.exe`
- `Netop Ondemand.exe`
- `nldrw32.exe`
- `rmserverconsolemediator.exe`
- `ImperoInit.exe`
- `Connect.Backdrop.cloud*.exe`
- `ImperoClientSVC.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.connect.backdrop.cloud`
    - `*.netop.com`


### Detections
- Detects potential network activity of Netop Remote Control (Impero Connect) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/netop_remote_control__impero_connect__network_sigma.yml)
- Detects potential processes activity of Netop Remote Control (Impero Connect) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/netop_remote_control__impero_connect__processes_sigma.yml)

### References
- [https://kb.netop.com/article/firewall-and-proxy-server-considerations-when-using-netop-portal-communication-373.html](https://kb.netop.com/article/firewall-and-proxy-server-considerations-when-using-netop-portal-communication-373.html)


