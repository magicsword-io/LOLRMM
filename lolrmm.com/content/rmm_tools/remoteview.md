+++
description = "RemoteView is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "RemoteView"
weight = 10
displayTitle = "RemoteView"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# RemoteView


### Description

RemoteView is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `remoteview.exe`
- `rv.exe`
- `rvagent.exe`
- `rvagtray.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*content.rview.com`
    - `*.rview.com`
    - `content.rview.com`


### Detections
- Detects potential network activity of RemoteView RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remoteview_network_sigma.yml)
- Detects potential processes activity of RemoteView RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remoteview_processes_sigma.yml)

### References
- [https://help.rview.com/hc/en-us/articles/360005175994--RemoteView-Server-list-for-firewall](https://help.rview.com/hc/en-us/articles/360005175994--RemoteView-Server-list-for-firewall)



{{< /column >}}
{{< /block >}}
