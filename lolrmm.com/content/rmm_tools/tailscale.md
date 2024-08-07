+++
description = "Tailscale is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Tailscale"
weight = 10
displayTitle = "Tailscale"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Tailscale


### Description

Tailscale is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `tailscale-*.exe`
- `tailscaled.exe`
- `tailscale-ipn.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.tailscale.com`
    - `*.tailscale.io`
    - `tailscale.com`


### Detections
- Detects potential network activity of Tailscale RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tailscale_network_sigma.yml)
- Detects potential processes activity of Tailscale RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tailscale_processes_sigma.yml)

### References
- [https://tailscale.com/kb/1023/troubleshooting](https://tailscale.com/kb/1023/troubleshooting)



{{< /column >}}
{{< /block >}}
