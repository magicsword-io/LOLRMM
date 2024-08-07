+++
description = "rdpwrap is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "rdpwrap"
weight = 10
displayTitle = "rdpwrap"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# rdpwrap


### Description

rdpwrap is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `RDPWInst.exe`
- `RDPCheck.exe`
- `RDPConf.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `github.com/stascorp/rdpwrap`


### Detections
- Detects potential network activity of rdpwrap RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rdpwrap_network_sigma.yml)
- Detects potential processes activity of rdpwrap RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rdpwrap_processes_sigma.yml)

### References
- [github.com/stascorp/rdpwrap](github.com/stascorp/rdpwrap)



{{< /column >}}
{{< /block >}}
