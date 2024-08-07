+++
description = "Jump Cloud is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Jump Cloud"
weight = 10
displayTitle = "Jump Cloud"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

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
- **Description**: Known remote domains  **Domains**:
    - `*.api.jumpcloud.com`
    - `*.assist.jumpcloud.com`


### Detections
- Detects potential network activity of Jump Cloud RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/jump_cloud_network_sigma.yml)

### References
- [https://jumpcloud.com/support/understand-remote-assist-agent](https://jumpcloud.com/support/understand-remote-assist-agent)



{{< /column >}}
{{< /block >}}
