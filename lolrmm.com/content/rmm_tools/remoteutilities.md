+++
description = "RemoteUtilities is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "RemoteUtilities"
weight = 10
displayTitle = "RemoteUtilities"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# RemoteUtilities


### Description

RemoteUtilities is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rutview.exe`
- `*\Remote Manipulator System - Server\*`
- `C:\Program Files\Remote Utilities\*`
- `*\Remote Utilities\*`
- `rutserv.exe`
- `*\rutserv.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `remoteutilities.com`


### Detections
- Detects potential network activity of RemoteUtilities RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remoteutilities_network_sigma.yml)
- Detects potential processes activity of RemoteUtilities RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remoteutilities_processes_sigma.yml)




{{< /column >}}
{{< /block >}}
