---
description: "Senso.cloud is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Senso.cloud"
displayTitle: "Senso.cloud"
---



# Senso.cloud


### Description

Senso.cloud is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `SensoClient.exe`
- `SensoService.exe`
- `aadg.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.senso.cloud`
    - `senso.cloud`


### Detections
- Detects potential network activity of Senso.cloud RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/senso.cloud_network_sigma.yml)
- Detects potential processes activity of Senso.cloud RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/senso.cloud_processes_sigma.yml)

### References
- [https://support.senso.cloud/support/solutions/articles/79000116305-firewall-and-content-filter-configuration](https://support.senso.cloud/support/solutions/articles/79000116305-firewall-and-content-filter-configuration)


