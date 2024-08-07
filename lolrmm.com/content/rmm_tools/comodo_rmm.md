+++
description = "Comodo RMM is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Comodo RMM"
weight = 10
displayTitle = "Comodo RMM"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Comodo RMM


### Description

Comodo RMM is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `itsmagent.exe`
- `rviewer.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.itsm-us1.comodo.com`
    - `*mdmsupport.comodo.com`
    - `one.comodo.com`


### Detections
- Detects potential network activity of Comodo RMM RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/comodo_rmm_network_sigma.yml)
- Detects potential processes activity of Comodo RMM RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/comodo_rmm_processes_sigma.yml)

### References
- [https://help.itarian.com/topic-459-1-1005-14776-Appendix-1b---Endpoint-Manager-Services---IP-Nos,-Host-Names-and-Port-Details---US-Customers.html](https://help.itarian.com/topic-459-1-1005-14776-Appendix-1b---Endpoint-Manager-Services---IP-Nos,-Host-Names-and-Port-Details---US-Customers.html)



{{< /column >}}
{{< /block >}}
