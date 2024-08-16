---
description: "Quest KACE Agent (formerly Dell KACE) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Quest KACE Agent (formerly Dell KACE)"
displayTitle: "Quest KACE Agent (formerly Dell KACE)"
---



# Quest KACE Agent (formerly Dell KACE)


### Description

Quest KACE Agent (formerly Dell KACE) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `konea.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.kace.com`
    - `www.quest.com/kace/`


### Detections
- Detects potential network activity of Quest KACE Agent (formerly Dell KACE) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/quest_kace_agent__formerly_dell_kace__network_sigma.yml)
- Detects potential processes activity of Quest KACE Agent (formerly Dell KACE) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/quest_kace_agent__formerly_dell_kace__processes_sigma.yml)

### References
- [https://support.quest.com/kb/4211365/which-network-ports-and-urls-are-required-for-the-kace-sma-appliance-to-function](https://support.quest.com/kb/4211365/which-network-ports-and-urls-are-required-for-the-kace-sma-appliance-to-function)


