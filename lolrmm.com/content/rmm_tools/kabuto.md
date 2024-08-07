+++
description = "Kabuto is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Kabuto"
weight = 10
displayTitle = "Kabuto"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Kabuto


### Description

Kabuto is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `Kabuto.App.Runner.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.kabuto.io`
    - `repairtechsolutions.com/kabuto/`


### Detections
- Detects potential network activity of Kabuto RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/kabuto_network_sigma.yml)
- Detects potential processes activity of Kabuto RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/kabuto_processes_sigma.yml)

### References
- [https://www.repairtechsolutions.com/documentation/kabuto/](https://www.repairtechsolutions.com/documentation/kabuto/)



{{< /column >}}
{{< /block >}}
