+++
description = "MyIVO is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "MyIVO"
weight = 10
displayTitle = "MyIVO"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# MyIVO


### Description

MyIVO is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `myivomgr.exe`
- `myivomanager.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `myivo-server.software.informer.com`


### Detections
- Detects potential network activity of MyIVO RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/myivo_network_sigma.yml)
- Detects potential processes activity of MyIVO RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/myivo_processes_sigma.yml)

### References
- [myivo.com - DOA as of 2024](myivo.com - DOA as of 2024)



{{< /column >}}
{{< /block >}}
