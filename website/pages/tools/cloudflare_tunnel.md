---
description: "CloudFlare Tunnel is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "CloudFlare Tunnel"
displayTitle: "CloudFlare Tunnel"
---



# CloudFlare Tunnel


### Description

CloudFlare Tunnel is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `cloudflared.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `cloudflare.com/products/tunnel/`


### Detections
- Detects potential network activity of CloudFlare Tunnel RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/cloudflare_tunnel_network_sigma.yml)
- Detects potential processes activity of CloudFlare Tunnel RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/cloudflare_tunnel_processes_sigma.yml)

### References
- [cloudflare.com/products/tunnel/](cloudflare.com/products/tunnel/)


