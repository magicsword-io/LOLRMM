---
description: "UltraViewer is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "UltraViewer"
displayTitle: "UltraViewer"
---



# UltraViewer


### Description

UltraViewer is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `UltraViewer_Service.exe`
- `UltraViewer_setup*`
- `UltraViewer_Desktop.exe`
- `ultraviewer.exe`
- `C:\Program Files (x86)\UltraViewer\UltraViewer_Desktop.exe`
- `*\UltraViewer\`
- `*\UltraViewer_Desktop.exe`
- `ultraviewer_desktop.exe`
- `ultraviewer_service.exe`
- `UltraViewer_Desktop.exe`
- `UltraViewer_setup*`
- `UltraViewer_Service.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `* .ultraviewer.net`
    - `ultraviewer.net`


### Detections
- Detects potential network activity of UltraViewer RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ultraviewer_network_sigma.yml)
- Detects potential processes activity of UltraViewer RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ultraviewer_processes_sigma.yml)

### References
- [https://www.ultraviewer.net/en/200000026-summary-of-ultraviewer-s-security-information.html](https://www.ultraviewer.net/en/200000026-summary-of-ultraviewer-s-security-information.html)


