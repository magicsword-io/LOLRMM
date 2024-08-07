+++
description = "Splashtop Remote is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Splashtop Remote"
weight = 10
displayTitle = "Splashtop Remote"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Splashtop Remote


### Description

Splashtop Remote is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `strwinclt.exe`
- `Splashtop_Streamer_Windows*.exe`
- `SplashtopSOS.exe`
- `sragent.exe`
- `srmanager.exe`
- `srserver.exe`
- `srservice.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `splashtop.com`
    - `*.api.splashtop.com`
    - `*.relay.splashtop.com`
    - `*.api.splashtop.eu`


### Detections
- Detects potential network activity of Splashtop Remote RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/splashtop_remote_network_sigma.yml)
- Detects potential processes activity of Splashtop Remote RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/splashtop_remote_processes_sigma.yml)

### References
- [https://support-splashtopbusiness.splashtop.com/hc/en-us/articles/115001811966-What-are-the-Firewall-Exceptions-and-IP-addresses-of-Splashtop-servers-Services](https://support-splashtopbusiness.splashtop.com/hc/en-us/articles/115001811966-What-are-the-Firewall-Exceptions-and-IP-addresses-of-Splashtop-servers-Services)



{{< /column >}}
{{< /block >}}
