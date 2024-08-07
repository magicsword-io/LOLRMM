+++
description = "SpyAnywhere is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "SpyAnywhere"
weight = 10
displayTitle = "SpyAnywhere"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# SpyAnywhere


### Description

SpyAnywhere is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `sysdiag.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.spytech-web.com`
    - `spyanywhere.com`


### Detections
- Detects potential network activity of SpyAnywhere RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/spyanywhere_network_sigma.yml)
- Detects potential processes activity of SpyAnywhere RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/spyanywhere_processes_sigma.yml)

### References
- [https://www.spyanywhere.com/support.shtml](https://www.spyanywhere.com/support.shtml)



{{< /column >}}
{{< /block >}}
