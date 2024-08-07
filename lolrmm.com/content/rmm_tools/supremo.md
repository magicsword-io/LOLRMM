+++
description = "Supremo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Supremo"
weight = 10
displayTitle = "Supremo"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Supremo


### Description

Supremo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/13/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `supremo.exe`
- `supremoservice.exe`
- `supremosystem.exe`
- `supremohelper.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `supremocontrol.com`
    - `*.supremocontrol.com`
    - `* .nanosystems.it`


### Detections
- Detects potential network activity of Supremo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/supremo_network_sigma.yml)
- Detects potential processes activity of Supremo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/supremo_processes_sigma.yml)

### References
- [https://www.supremocontrol.com/frequently-asked-questions/](https://www.supremocontrol.com/frequently-asked-questions/)



{{< /column >}}
{{< /block >}}
