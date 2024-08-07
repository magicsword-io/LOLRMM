+++
description = "Ericom AccessNow is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Ericom AccessNow"
weight = 10
displayTitle = "Ericom AccessNow"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Ericom AccessNow


### Description

Ericom AccessNow is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `accessserver*.exe`
- `accessserver.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `ericom.com`


### Detections
- Detects potential network activity of Ericom AccessNow RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ericom_accessnow_network_sigma.yml)
- Detects potential processes activity of Ericom AccessNow RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ericom_accessnow_processes_sigma.yml)

### References
- [https://www.ericom.com/connect-accessnow/](https://www.ericom.com/connect-accessnow/)



{{< /column >}}
{{< /block >}}
