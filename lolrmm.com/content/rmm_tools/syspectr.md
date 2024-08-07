+++
description = "Syspectr is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Syspectr"
weight = 10
displayTitle = "Syspectr"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Syspectr


### Description

Syspectr is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `oo-syspectr*.exe`
- `OOSysAgent.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `atled.syspectr.com`
    - `app.syspectr.com`


### Detections
- Detects potential network activity of Syspectr RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/syspectr_network_sigma.yml)
- Detects potential processes activity of Syspectr RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/syspectr_processes_sigma.yml)

### References
- [https://www.syspectr.com/en/installation-in-a-network](https://www.syspectr.com/en/installation-in-a-network)



{{< /column >}}
{{< /block >}}
