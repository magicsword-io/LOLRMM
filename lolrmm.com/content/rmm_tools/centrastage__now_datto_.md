+++
description = "CentraStage (Now Datto) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "CentraStage (Now Datto)"
weight = 10
displayTitle = "CentraStage (Now Datto)"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# CentraStage (Now Datto)


### Description

CentraStage (Now Datto) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `CagService.exe`
- `AEMAgent.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.rmm.datto.com`
    - `*cc.centrastage.net`
    - `datto.com/au/products/rmm/`


### Detections
- Detects potential network activity of CentraStage (Now Datto) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/centrastage__now_datto__network_sigma.yml)
- Detects potential processes activity of CentraStage (Now Datto) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/centrastage__now_datto__processes_sigma.yml)

### References
- [https://rmm.datto.com/help/de/Content/1INTRODUCTION/Requirements/AllowListRequirements.htm](https://rmm.datto.com/help/de/Content/1INTRODUCTION/Requirements/AllowListRequirements.htm)



{{< /column >}}
{{< /block >}}
