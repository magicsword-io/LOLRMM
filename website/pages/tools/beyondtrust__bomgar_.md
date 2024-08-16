---
description: "BeyondTrust (Bomgar) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "BeyondTrust (Bomgar)"
displayTitle: "BeyondTrust (Bomgar)"
---



# BeyondTrust (Bomgar)


### Description

BeyondTrust (Bomgar) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `bomgar-scc-*.exe`
- `bomgar-scc.exe`
- `bomgar-pac-*.exe`
- `bomgar-pac.exe`
- `bomgar-rdp.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.beyondtrustcloud.com`
    - `*.bomgarcloud.com`
    - `bomgarcloud.com`


### Detections
- Detects potential network activity of BeyondTrust (Bomgar) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/beyondtrust__bomgar__network_sigma.yml)
- Detects potential processes activity of BeyondTrust (Bomgar) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/beyondtrust__bomgar__processes_sigma.yml)

### References
- [https://www.beyondtrust.com/docs/remote-support/getting-started/deployment/cloud/network.htm](https://www.beyondtrust.com/docs/remote-support/getting-started/deployment/cloud/network.htm)


