---
description: "Visual Studio Dev Tunnel is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Visual Studio Dev Tunnel"
displayTitle: "Visual Studio Dev Tunnel"
---



# Visual Studio Dev Tunnel


### Description

Visual Studio Dev Tunnel is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No





### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `global.rel.tunnels.api.visualstudio.com`
    - `*.rel.tunnels.api.visualstudio.com`
    - `*.devtunnels.ms`


### Detections
- Detects potential network activity of Visual Studio Dev Tunnel RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/visual_studio_dev_tunnel_network_sigma.yml)

### References
- [https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/security](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/security)


