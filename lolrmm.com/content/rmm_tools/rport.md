+++
description = "RPort is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "RPort"
weight = 10
displayTitle = "RPort"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# RPort


### Description

RPort is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rport.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `rport.io`


### Detections
- Detects potential network activity of RPort RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rport_network_sigma.yml)
- Detects potential processes activity of RPort RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rport_processes_sigma.yml)

### References
- [https://kb.rport.io/using-the-remote-access](https://kb.rport.io/using-the-remote-access)



{{< /column >}}
{{< /block >}}
