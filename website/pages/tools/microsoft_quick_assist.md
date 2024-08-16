---
description: "Microsoft Quick Assist is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Microsoft Quick Assist"
displayTitle: "Microsoft Quick Assist"
---



# Microsoft Quick Assist


### Description

Microsoft Quick Assist is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `quickassist.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`


### Detections
- Detects potential network activity of Microsoft Quick Assist RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/microsoft_quick_assist_network_sigma.yml)
- Detects potential processes activity of Microsoft Quick Assist RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/microsoft_quick_assist_processes_sigma.yml)

### References
- [https://support.microsoft.com/en-us/windows/install-quick-assist-c17479b7-a49d-4d12-938c-dbfb97c88bca](https://support.microsoft.com/en-us/windows/install-quick-assist-c17479b7-a49d-4d12-938c-dbfb97c88bca)


