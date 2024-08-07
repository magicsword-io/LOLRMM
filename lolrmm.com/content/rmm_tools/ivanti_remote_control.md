+++
description = "Ivanti Remote Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Ivanti Remote Control"
weight = 10
displayTitle = "Ivanti Remote Control"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Ivanti Remote Control


### Description

Ivanti Remote Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `IvantiRemoteControl.exe`
- `ArcUI.exe`
- `AgentlessRC.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.ivanticloud.com`


### Detections
- Detects potential network activity of Ivanti Remote Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ivanti_remote_control_network_sigma.yml)
- Detects potential processes activity of Ivanti Remote Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ivanti_remote_control_processes_sigma.yml)

### References
- [https://rc1.ivanticloud.com/](https://rc1.ivanticloud.com/)



{{< /column >}}
{{< /block >}}
