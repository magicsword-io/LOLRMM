+++
description = "eHorus is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "eHorus"
weight = 10
displayTitle = "eHorus"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# eHorus


### Description

eHorus is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ehorus standalone.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `ehorus.com`


### Detections
- Detects potential network activity of eHorus RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ehorus_network_sigma.yml)
- Detects potential processes activity of eHorus RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ehorus_processes_sigma.yml)




{{< /column >}}
{{< /block >}}
