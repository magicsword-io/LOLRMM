+++
description = "Pocket Controller (Soti Xsight) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Pocket Controller (Soti Xsight)"
weight = 10
displayTitle = "Pocket Controller (Soti Xsight)"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Pocket Controller (Soti Xsight)


### Description

Pocket Controller (Soti Xsight) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `pocketcontroller.exe`
- `wysebrowser.exe`
- `XSightService.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*soti.net`


### Detections
- Detects potential network activity of Pocket Controller (Soti Xsight) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pocket_controller__soti_xsight__network_sigma.yml)
- Detects potential processes activity of Pocket Controller (Soti Xsight) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pocket_controller__soti_xsight__processes_sigma.yml)

### References
- [https://pulse.soti.net/support/soti-xsight/help/](https://pulse.soti.net/support/soti-xsight/help/)



{{< /column >}}
{{< /block >}}
