---
description: "RDPView is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "RDPView"
displayTitle: "RDPView"
---



# RDPView


### Description

RDPView is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `dwrcs.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `systemmanager.ru/dntu.en/rdp_view.htm`


### Detections
- Detects potential network activity of RDPView RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rdpview_network_sigma.yml)
- Detects potential processes activity of RDPView RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rdpview_processes_sigma.yml)

### References
- [systemmanager.ru/dntu.en/rdp_view.htm - Same as Damware](systemmanager.ru/dntu.en/rdp_view.htm - Same as Damware)


