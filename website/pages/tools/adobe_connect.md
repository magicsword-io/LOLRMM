---
description: "Adobe Connect is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Adobe Connect"
displayTitle: "Adobe Connect"
---



# Adobe Connect


### Description

Adobe Connect is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/27/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ConnectAppSetup*.exe`
- `ConnectShellSetup*.exe`
- `Connect.exe`
- `ConnectDetector.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.adobeconnect.com`


### Detections
- Detects potential network activity of Adobe Connect RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/adobe_connect_network_sigma.yml)
- Detects potential processes activity of Adobe Connect RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/adobe_connect_processes_sigma.yml)

### References
- [https://helpx.adobe.com/adobe-connect/firewall-proxy-server-configuration-adobe-connect.html](https://helpx.adobe.com/adobe-connect/firewall-proxy-server-configuration-adobe-connect.html)


