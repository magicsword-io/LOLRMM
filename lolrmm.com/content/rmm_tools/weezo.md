+++
description = "Weezo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Weezo"
weight = 10
displayTitle = "Weezo"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Weezo


### Description

Weezo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `weezohttpd.exe`
- `weezo.exe`
- `weezo setup*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.weezo.me`
    - `weezo.net`
    - `*.weezo.net`
    - `weezo.en.softonic.com`


### Detections
- Detects potential network activity of Weezo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/weezo_network_sigma.yml)
- Detects potential processes activity of Weezo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/weezo_processes_sigma.yml)

### References
- [weezo.en.softonic.com](weezo.en.softonic.com)



{{< /column >}}
{{< /block >}}
