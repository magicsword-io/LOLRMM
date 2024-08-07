+++
description = "Royal Apps is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Royal Apps"
weight = 10
displayTitle = "Royal Apps"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Royal Apps


### Description

Royal Apps is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `royalserver.exe`
- `royalts.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`


### Detections
- Detects potential network activity of Royal Apps RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/royal_apps_network_sigma.yml)
- Detects potential processes activity of Royal Apps RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/royal_apps_processes_sigma.yml)

### References
- [https://www.royalapps.com/ts/win/download](https://www.royalapps.com/ts/win/download)



{{< /column >}}
{{< /block >}}
