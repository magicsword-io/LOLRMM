+++
description = "FixMe is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "FixMe"
weight = 10
displayTitle = "FixMe"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# FixMe


### Description

FixMe is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `FixMeit Client.exe`
- `TiExpertStandalone.exe`
- `FixMeitClient*.exe`
- `TiExpertCore.exe`
- `FixMeit Unattended Access Setup.exe`
- `FixMeit Expert Setup.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `fixme.it`


### Detections
- Detects potential network activity of FixMe RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fixme_network_sigma.yml)
- Detects potential processes activity of FixMe RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fixme_processes_sigma.yml)




{{< /column >}}
{{< /block >}}
