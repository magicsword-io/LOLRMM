---
description: "Connectwise Automate (LabTech) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Connectwise Automate (LabTech)"
displayTitle: "Connectwise Automate (LabTech)"
---



# Connectwise Automate (LabTech)


### Description

Connectwise Automate (LabTech) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ltsvc.exe`
- `ltsvcmon.exe`
- `lttray.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.hostedrmm.com`


### Detections
- Detects potential network activity of Connectwise Automate (LabTech) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/connectwise_automate__labtech__network_sigma.yml)
- Detects potential processes activity of Connectwise Automate (LabTech) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/connectwise_automate__labtech__processes_sigma.yml)

### References
- [https://www.connectwise.com/company/announcements/labtech-now-connectwise-automate](https://www.connectwise.com/company/announcements/labtech-now-connectwise-automate)


