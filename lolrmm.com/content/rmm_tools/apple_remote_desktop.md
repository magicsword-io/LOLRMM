+++
description = "Apple Remote Desktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Apple Remote Desktop"
weight = 10
displayTitle = "Apple Remote Desktop"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Apple Remote Desktop


### Description

Apple Remote Desktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/24/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ARDAgent.app`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`


### Detections
- Detects potential network activity of Apple Remote Desktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/apple_remote_desktop_network_sigma.yml)

### References
- [https://support.apple.com/guide/remote-desktop/install-and-set-up-remote-desktop-apdf49e03a4/mac](https://support.apple.com/guide/remote-desktop/install-and-set-up-remote-desktop-apdf49e03a4/mac)



{{< /column >}}
{{< /block >}}
