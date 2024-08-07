+++
description = "Any Support is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Any Support"
weight = 10
displayTitle = "Any Support"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Any Support


### Description

Any Support is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/27/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ManualLauncher.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.anysupport.net`


### Detections
- Detects potential network activity of Any Support RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/any_support_network_sigma.yml)
- Detects potential processes activity of Any Support RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/any_support_processes_sigma.yml)

### References
- [https://www.anysupport.net/introduce_howto.php](https://www.anysupport.net/introduce_howto.php)



{{< /column >}}
{{< /block >}}
