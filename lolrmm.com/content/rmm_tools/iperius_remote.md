+++
description = "Iperius Remote is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Iperius Remote"
weight = 10
displayTitle = "Iperius Remote"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Iperius Remote


### Description

Iperius Remote is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `iperius.exe`
- `iperiusremote.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.iperiusremote.com`
    - `*.iperius.com`
    - `*.iperius-rs.com`
    - `iperiusremote.com`


### Detections
- Detects potential network activity of Iperius Remote RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/iperius_remote_network_sigma.yml)
- Detects potential processes activity of Iperius Remote RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/iperius_remote_processes_sigma.yml)

### References
- [https://www.iperiusremote.com/download-iperius-remote-desktop-windows.aspx](https://www.iperiusremote.com/download-iperius-remote-desktop-windows.aspx)



{{< /column >}}
{{< /block >}}
