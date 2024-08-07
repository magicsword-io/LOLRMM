+++
description = "PSEXEC (Clone) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "PSEXEC (Clone)"
weight = 10
displayTitle = "PSEXEC (Clone)"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# PSEXEC (Clone)


### Description

PSEXEC (Clone) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `paexec.exe`
- `PAExec-*.exe`
- `csexec.exe `
- `remcom.exe`
- `remcomsvc.exe`
- `xcmd.exe`
- `xcmdsvc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`


### Detections
- Detects potential network activity of PSEXEC (Clone) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/psexec__clone__network_sigma.yml)
- Detects potential processes activity of PSEXEC (Clone) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/psexec__clone__processes_sigma.yml)

### References
- [https://www.poweradmin.com/paexec/](https://www.poweradmin.com/paexec/)



{{< /column >}}
{{< /block >}}
