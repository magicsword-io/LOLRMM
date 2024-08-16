---
description: "SuperOps is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "SuperOps"
displayTitle: "SuperOps"
---



# SuperOps


### Description

SuperOps is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `superopsticket.exe`
- `superops.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.superopsbeta.com`
    - `superops.ai`
    - `serv.superopsalpha.com`
    - `*.superops.ai`
    - `*.superopsalpha.com`


### Detections
- Detects potential network activity of SuperOps RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/superops_network_sigma.yml)
- Detects potential processes activity of SuperOps RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/superops_processes_sigma.yml)

### References
- [https://support.superops.com/en/articles/6632028-how-to-download-and-deploy-the-agent](https://support.superops.com/en/articles/6632028-how-to-download-and-deploy-the-agent)


