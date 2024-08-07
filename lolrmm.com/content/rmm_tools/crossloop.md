+++
description = "CrossLoop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "CrossLoop"
weight = 10
displayTitle = "CrossLoop"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# CrossLoop


### Description

CrossLoop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `crossloopservice.exe`
- `CrossLoopConnect.exe`
- `WinVNCStub.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.crossloop.com`
    - `crossloop.en.softonic.com`


### Detections
- Detects potential network activity of CrossLoop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/crossloop_network_sigma.yml)
- Detects potential processes activity of CrossLoop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/crossloop_processes_sigma.yml)

### References
- [www.CrossLoop.com -> redirects to avast.com](www.CrossLoop.com -> redirects to avast.com)



{{< /column >}}
{{< /block >}}
