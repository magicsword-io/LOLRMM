+++
description = "ScreenMeet is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "ScreenMeet"
weight = 10
displayTitle = "ScreenMeet"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# ScreenMeet


### Description

ScreenMeet is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ScreenMeetSupport.exe`
- `ScreenMeet.Support.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.screenmeet.com`
    - `*.scrn.mt`


### Detections
- Detects potential network activity of ScreenMeet RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/screenmeet_network_sigma.yml)
- Detects potential processes activity of ScreenMeet RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/screenmeet_processes_sigma.yml)

### References
- [https://docs.screenmeet.com/docs/firewall-white-list](https://docs.screenmeet.com/docs/firewall-white-list)



{{< /column >}}
{{< /block >}}
