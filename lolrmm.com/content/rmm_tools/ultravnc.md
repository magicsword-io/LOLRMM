+++
description = "UltraVNC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "UltraVNC"
weight = 10
displayTitle = "UltraVNC"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# UltraVNC


### Description

UltraVNC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `UltraVNC*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `ultravnc.com`
    - `user_managed`


### Detections
- Detects potential network activity of UltraVNC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ultravnc_network_sigma.yml)
- Detects potential processes activity of UltraVNC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ultravnc_processes_sigma.yml)

### References
- [https://uvnc.com/docs/uvnc-server/49-UltraVNC-server-configuration.html](https://uvnc.com/docs/uvnc-server/49-UltraVNC-server-configuration.html)



{{< /column >}}
{{< /block >}}
