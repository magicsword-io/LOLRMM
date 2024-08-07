+++
description = "Pocket Controller is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Pocket Controller"
weight = 10
displayTitle = "Pocket Controller"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Pocket Controller


### Description

Pocket Controller is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `pocketcontroller.exe`
- `pocketcloudservice.exe`
- `wysebrowser.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `soti.net/products/soti-pocket-controller`


### Detections
- Detects potential network activity of Pocket Controller RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pocket_controller_network_sigma.yml)
- Detects potential processes activity of Pocket Controller RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pocket_controller_processes_sigma.yml)




{{< /column >}}
{{< /block >}}
