+++
description = "MyGreenPC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "MyGreenPC"
weight = 10
displayTitle = "MyGreenPC"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# MyGreenPC


### Description

MyGreenPC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `mygreenpc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*mygreenpc.com`


### Detections
- Detects potential network activity of MyGreenPC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/mygreenpc_network_sigma.yml)
- Detects potential processes activity of MyGreenPC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/mygreenpc_processes_sigma.yml)

### References
- [http://www.mygreenpc.com/](http://www.mygreenpc.com/)



{{< /column >}}
{{< /block >}}
