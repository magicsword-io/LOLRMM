---
description: "Sorillus is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Sorillus"
displayTitle: "Sorillus"
---



# Sorillus


### Description

Sorillus is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `Sorillus-Launcher*.exe`
- `Sorillus Launcher.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.sorillus.com`
    - `sorillus.com`


### Detections
- Detects potential network activity of Sorillus RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/sorillus_network_sigma.yml)
- Detects potential processes activity of Sorillus RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/sorillus_processes_sigma.yml)

### References
- [https://sorillus.com/](https://sorillus.com/)


