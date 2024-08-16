---
description: "Naverisk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Naverisk"
displayTitle: "Naverisk"
---



# Naverisk


### Description

Naverisk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `AgentSetup-*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `naverisk.com`


### Detections
- Detects potential network activity of Naverisk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/naverisk_network_sigma.yml)
- Detects potential processes activity of Naverisk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/naverisk_processes_sigma.yml)

### References
- [http://kb.naverisk.com/en/articles/2811223-deploying-naverisk-agents](http://kb.naverisk.com/en/articles/2811223-deploying-naverisk-agents)


