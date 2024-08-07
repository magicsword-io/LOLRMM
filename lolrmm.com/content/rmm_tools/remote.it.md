+++
description = "Remote.it is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Remote.it"
weight = 10
displayTitle = "Remote.it"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Remote.it


### Description

Remote.it is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `remote-it-installer.exe`
- `remote.it.exe`
- `remoteit.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `auth.api.remote.it`
    - `api.remote.it`
    - `remote.it`


### Detections
- Detects potential network activity of Remote.it RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remote.it_network_sigma.yml)
- Detects potential processes activity of Remote.it RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remote.it_processes_sigma.yml)

### References
- [https://docs.remote.it/introduction/get-started](https://docs.remote.it/introduction/get-started)



{{< /column >}}
{{< /block >}}
