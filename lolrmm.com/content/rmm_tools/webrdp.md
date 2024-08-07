+++
description = "WebRDP is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "WebRDP"
weight = 10
displayTitle = "WebRDP"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# WebRDP


### Description

WebRDP is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `webrdp.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `github.com/Mikej81/WebRDP`


### Detections
- Detects potential network activity of WebRDP RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/webrdp_network_sigma.yml)
- Detects potential processes activity of WebRDP RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/webrdp_processes_sigma.yml)

### References
- [github.com/Mikej81/WebRDP](github.com/Mikej81/WebRDP)



{{< /column >}}
{{< /block >}}
