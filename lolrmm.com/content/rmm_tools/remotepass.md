+++
description = "RemotePass is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "RemotePass"
weight = 10
displayTitle = "RemotePass"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# RemotePass


### Description

RemotePass is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `remotepass-access.exe`
- `rpaccess.exe`
- `rpwhostscr.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `remotepass.com`


### Detections
- Detects potential network activity of RemotePass RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remotepass_network_sigma.yml)
- Detects potential processes activity of RemotePass RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remotepass_processes_sigma.yml)

### References
- [https://www.remotepass.com/rpaccess.html - DOA as of 2024](https://www.remotepass.com/rpaccess.html - DOA as of 2024)



{{< /column >}}
{{< /block >}}
