---
description: "OptiTune is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "OptiTune"
displayTitle: "OptiTune"
---



# OptiTune


### Description

OptiTune is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `OTService.exe`
- `OTPowerShell.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.optitune.us`
    - `*.opti-tune.com`


### Detections
- Detects potential network activity of OptiTune RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/optitune_network_sigma.yml)
- Detects potential processes activity of OptiTune RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/optitune_processes_sigma.yml)

### References
- [https://www.bravurasoftware.com/optitune/support/faq.aspx](https://www.bravurasoftware.com/optitune/support/faq.aspx)


