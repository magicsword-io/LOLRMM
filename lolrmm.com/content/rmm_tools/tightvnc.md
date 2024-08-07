+++
description = "TightVNC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "TightVNC"
weight = 10
displayTitle = "TightVNC"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# TightVNC


### Description

TightVNC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `tvnviewer.exe`
- `TightVNCViewerPortable*.exe`
- `tvnserver.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `tightvnc.com`


### Detections
- Detects potential network activity of TightVNC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tightvnc_network_sigma.yml)
- Detects potential processes activity of TightVNC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tightvnc_processes_sigma.yml)

### References
- [https://www.tightvnc.com/doc/win/TightVNC_for_Windows-Installation_and_Getting_Started.pdf](https://www.tightvnc.com/doc/win/TightVNC_for_Windows-Installation_and_Getting_Started.pdf)



{{< /column >}}
{{< /block >}}
