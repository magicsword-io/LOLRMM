+++
description = "Laplink Gold is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Laplink Gold"
weight = 10
displayTitle = "Laplink Gold"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Laplink Gold


### Description

Laplink Gold is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `tsircusr.exe`
- `laplink.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `wen.laplink.com/product/laplink-gold`


### Detections
- Detects potential network activity of Laplink Gold RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/laplink_gold_network_sigma.yml)
- Detects potential processes activity of Laplink Gold RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/laplink_gold_processes_sigma.yml)

### References
- [wen.laplink.com/product/laplink-gold](wen.laplink.com/product/laplink-gold)



{{< /column >}}
{{< /block >}}
