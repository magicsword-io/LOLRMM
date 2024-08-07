+++
description = "ServerEye is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "ServerEye"
weight = 10
displayTitle = "ServerEye"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# ServerEye


### Description

ServerEye is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `servereye*.exe`
- `ServiceProxyLocalSys.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.server-eye.de`


### Detections
- Detects potential network activity of ServerEye RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/servereye_network_sigma.yml)
- Detects potential processes activity of ServerEye RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/servereye_processes_sigma.yml)

### References
- [https://www.servereye.de/wp-content/uploads/Anleitung-zur-Erstinstallation_aktuell.pdf](https://www.servereye.de/wp-content/uploads/Anleitung-zur-Erstinstallation_aktuell.pdf)



{{< /column >}}
{{< /block >}}
