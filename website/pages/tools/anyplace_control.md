---
description: "Anyplace Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Anyplace Control"
displayTitle: "Anyplace Control"
---



# Anyplace Control


### Description

Anyplace Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `apc_host.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `anyplace-control.com`


### Detections
- Detects potential network activity of Anyplace Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/anyplace_control_network_sigma.yml)
- Detects potential processes activity of Anyplace Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/anyplace_control_processes_sigma.yml)

### References
- [http://www.anyplace-control.com/anyplace-control/help/faq.htm](http://www.anyplace-control.com/anyplace-control/help/faq.htm)


