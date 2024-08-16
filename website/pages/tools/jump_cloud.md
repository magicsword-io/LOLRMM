---
description: "Jump Cloud is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Jump Cloud"
displayTitle: "Jump Cloud"
---



# Jump Cloud


### Description

Jump Cloud is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `JumpCloud*.exe `

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.api.jumpcloud.com`
    - `*.assist.jumpcloud.com`


### Detections
- Detects potential network activity of Jump Cloud RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/jump_cloud_network_sigma.yml)

### References
- [https://jumpcloud.com/support/understand-remote-assist-agent](https://jumpcloud.com/support/understand-remote-assist-agent)


