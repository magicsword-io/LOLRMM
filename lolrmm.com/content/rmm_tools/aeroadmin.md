+++
description = "AeroAdmin is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "AeroAdmin"
weight = 10
displayTitle = "AeroAdmin"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# AeroAdmin


### Description

AeroAdmin is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `aeroadmin.exe`
- `AeroAdmin.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `auth*.aeroadmin.com`
    - `aeroadmin.com`


### Detections
- Detects potential network activity of AeroAdmin RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/aeroadmin_network_sigma.yml)
- Detects potential processes activity of AeroAdmin RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/aeroadmin_processes_sigma.yml)

### References
- [https://support.aeroadmin.com/kb/faq.php?id=58](https://support.aeroadmin.com/kb/faq.php?id=58)



{{< /column >}}
{{< /block >}}
