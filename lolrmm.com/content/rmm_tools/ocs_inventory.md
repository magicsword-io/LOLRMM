+++
description = "OCS inventory is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "OCS inventory"
weight = 10
displayTitle = "OCS inventory"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# OCS inventory


### Description

OCS inventory is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ocsinventory.exe`
- `ocsservice.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `ocsinventory-ng.org`


### Detections
- Detects potential network activity of OCS inventory RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ocs_inventory_network_sigma.yml)
- Detects potential processes activity of OCS inventory RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ocs_inventory_processes_sigma.yml)

### References
- [https://ocsinventory-ng.org/?page_id=878&lang=en](https://ocsinventory-ng.org/?page_id=878&lang=en)



{{< /column >}}
{{< /block >}}
