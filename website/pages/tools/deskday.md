---
description: "DeskDay is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "DeskDay"
displayTitle: "DeskDay"
---



# DeskDay


### Description

DeskDay is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ultimate_*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `deskday.ai`
    - `app.deskday.ai`


### Detections
- Detects potential network activity of DeskDay RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/deskday_network_sigma.yml)
- Detects potential processes activity of DeskDay RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/deskday_processes_sigma.yml)

### References
- [https://support.deskday.ai/en/articles/8235973-installing-the-end-user-application-ultimate](https://support.deskday.ai/en/articles/8235973-installing-the-end-user-application-ultimate)


