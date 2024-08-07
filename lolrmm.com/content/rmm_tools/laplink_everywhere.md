+++
description = "Laplink Everywhere is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Laplink Everywhere"
weight = 10
displayTitle = "Laplink Everywhere"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Laplink Everywhere


### Description

Laplink Everywhere is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `laplink.exe`
- `laplink-everywhere-setup*.exe`
- `laplinkeverywhere.exe`
- `llrcservice.exe`
- `serverproxyservice.exe`
- `OOSysAgent.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `everywhere.laplink.com`
    - `le.laplink.com`
    - `atled.syspectr.com`


### Detections
- Detects potential network activity of Laplink Everywhere RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/laplink_everywhere_network_sigma.yml)
- Detects potential processes activity of Laplink Everywhere RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/laplink_everywhere_processes_sigma.yml)

### References
- [https://everywhere.laplink.com/docs](https://everywhere.laplink.com/docs)



{{< /column >}}
{{< /block >}}
