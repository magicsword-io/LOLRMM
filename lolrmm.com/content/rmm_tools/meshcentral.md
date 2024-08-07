+++
description = "MeshCentral is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "MeshCentral"
weight = 10
displayTitle = "MeshCentral"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# MeshCentral


### Description

MeshCentral is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `meshcentral*.exe`
- `mesh*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `meshcentral.com`


### Detections
- Detects potential network activity of MeshCentral RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/meshcentral_network_sigma.yml)
- Detects potential processes activity of MeshCentral RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/meshcentral_processes_sigma.yml)

### References
- [https://ylianst.github.io/MeshCentral/meshcentral/](https://ylianst.github.io/MeshCentral/meshcentral/)



{{< /column >}}
{{< /block >}}
