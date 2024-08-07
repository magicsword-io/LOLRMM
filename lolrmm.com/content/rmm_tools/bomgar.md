+++
description = "Bomgar is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Bomgar"
weight = 10
displayTitle = "Bomgar"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Bomgar


### Description

Bomgar is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `bomgar-scc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `beyondtrust.com/brand/bomgar`


### Detections
- Detects potential network activity of Bomgar RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/bomgar_network_sigma.yml)
- Detects potential processes activity of Bomgar RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/bomgar_processes_sigma.yml)




{{< /column >}}
{{< /block >}}
