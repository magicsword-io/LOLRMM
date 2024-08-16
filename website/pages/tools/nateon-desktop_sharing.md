---
description: "NateOn-desktop sharing is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "NateOn-desktop sharing"
displayTitle: "NateOn-desktop sharing"
---



# NateOn-desktop sharing


### Description

NateOn-desktop sharing is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `nateon*.exe`
- `nateon.exe`
- `nateonmain.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.nate.com`


### Detections
- Detects potential network activity of NateOn-desktop sharing RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/nateon-desktop_sharing_network_sigma.yml)
- Detects potential processes activity of NateOn-desktop sharing RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/nateon-desktop_sharing_processes_sigma.yml)

### References
- [http://rsupport.nate.com/rview/r8/main/index.aspx](http://rsupport.nate.com/rview/r8/main/index.aspx)


