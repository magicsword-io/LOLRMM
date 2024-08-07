+++
description = "Level.io is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Level.io"
weight = 10
displayTitle = "Level.io"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Level.io


### Description

Level.io is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `level-windows-amd64.exe`
- `level.exe`
- `level-remote-control-ffmpeg.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `level.io`
    - `*.level.io`


### Detections
- Detects potential network activity of Level.io RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/level.io_network_sigma.yml)
- Detects potential processes activity of Level.io RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/level.io_processes_sigma.yml)

### References
- [https://docs.level.io/1.0/admin-guides/troubleshooting-agent-issues](https://docs.level.io/1.0/admin-guides/troubleshooting-agent-issues)



{{< /column >}}
{{< /block >}}
