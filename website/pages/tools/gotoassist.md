---
description: "GoToAssist is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "GoToAssist"
displayTitle: "GoToAssist"
---



# GoToAssist


### Description

GoToAssist is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `gotoassist.exe`
- `g2a*.exe`
- `GoTo Assist Opener.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `goto.com`
    - `*.getgo.com`
    - `*.fastsupport.com`
    - `*.gotoassist.com`
    - `helpme.net`
    - `*.gotoassist.me`
    - `*.gotoassist.at`
    - `*.desktopstreaming.com`


### Detections
- Detects potential network activity of GoToAssist RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/gotoassist_network_sigma.yml)
- Detects potential processes activity of GoToAssist RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/gotoassist_processes_sigma.yml)

### References
- [https://help.gotoassist.com/remote-support/help/what-should-i-allow-on-my-firewall-for-gotoassist-remote-support-v5](https://help.gotoassist.com/remote-support/help/what-should-i-allow-on-my-firewall-for-gotoassist-remote-support-v5)


