+++
description = "Acronic Cyber Protect (Remotix) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Acronic Cyber Protect (Remotix)"
weight = 10
displayTitle = "Acronic Cyber Protect (Remotix)"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Acronic Cyber Protect (Remotix)


### Description

Acronic Cyber Protect (Remotix) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `AcronisCyberProtectConnectQuickAssist*.exe`
- `AcronisCyberProtectConnectAgent.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `cloud.acronis.com`
    - `agents*-cloud.acronis.com`
    - `gw.remotix.com`
    - `connect.acronis.com`


### Detections
- Detects potential network activity of Acronic Cyber Protect (Remotix) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/acronic_cyber_protect__remotix__network_sigma.yml)
- Detects potential processes activity of Acronic Cyber Protect (Remotix) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/acronic_cyber_protect__remotix__processes_sigma.yml)

### References
- [https://kb.acronis.com/content/47189](https://kb.acronis.com/content/47189)



{{< /column >}}
{{< /block >}}
