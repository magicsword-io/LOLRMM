+++
description = "PDQ Connect is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "PDQ Connect"
weight = 10
displayTitle = "PDQ Connect"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# PDQ Connect


### Description

PDQ Connect is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `pdq-connect*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `app.pdq.com`
    - `cfcdn.pdq.com`


### Detections
- Detects potential network activity of PDQ Connect RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pdq_connect_network_sigma.yml)
- Detects potential processes activity of PDQ Connect RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pdq_connect_processes_sigma.yml)

### References
- [https://connect.pdq.com/hc/en-us/articles/9518992071707-Network-Requirements](https://connect.pdq.com/hc/en-us/articles/9518992071707-Network-Requirements)



{{< /column >}}
{{< /block >}}
