+++
description = "Tactical RMM is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Tactical RMM"
weight = 10
displayTitle = "Tactical RMM"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Tactical RMM


### Description

Tactical RMM is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `tacticalrmm.exe`
- `tacticalrmm.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `login.tailscale.com`
    - `login.tailscale.com`
    - `docs.tacticalrmm.com`


### Detections
- Detects potential network activity of Tactical RMM RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tactical_rmm_network_sigma.yml)
- Detects potential processes activity of Tactical RMM RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tactical_rmm_processes_sigma.yml)

### References
- [docs.tacticalrmm.com](docs.tacticalrmm.com)



{{< /column >}}
{{< /block >}}
