+++
description = "Distant Desktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Distant Desktop"
weight = 10
displayTitle = "Distant Desktop"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Distant Desktop


### Description

Distant Desktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ddsystem.exe`
- `dd.exe`
- `distant-desktop.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.distantdesktop.com`
    - `*signalserver.xyz`


### Detections
- Detects potential network activity of Distant Desktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/distant_desktop_network_sigma.yml)
- Detects potential processes activity of Distant Desktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/distant_desktop_processes_sigma.yml)

### References
- [https://www.distantdesktop.com/manual/first-start.htm](https://www.distantdesktop.com/manual/first-start.htm)



{{< /column >}}
{{< /block >}}
