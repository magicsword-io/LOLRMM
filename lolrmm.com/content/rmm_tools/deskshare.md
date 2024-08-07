+++
description = "DeskShare is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "DeskShare"
weight = 10
displayTitle = "DeskShare"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# DeskShare


### Description

DeskShare is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `TeamTaskManager.exe`
- `DSGuest.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`


### Detections
- Detects potential network activity of DeskShare RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/deskshare_network_sigma.yml)
- Detects potential processes activity of DeskShare RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/deskshare_processes_sigma.yml)

### References
- [https://www.deskshare.com/help/fml/Active-and-Passive-connection-mode.aspx](https://www.deskshare.com/help/fml/Active-and-Passive-connection-mode.aspx)



{{< /column >}}
{{< /block >}}
