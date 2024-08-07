+++
description = "Pcnow is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Pcnow"
weight = 10
displayTitle = "Pcnow"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Pcnow


### Description

Pcnow is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `mwcliun.exe`
- `pcnmgr.exe`
- `webexpcnow.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `au.pcmag.com/utilities/21470/webex-pcnow`


### Detections
- Detects potential network activity of Pcnow RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pcnow_network_sigma.yml)
- Detects potential processes activity of Pcnow RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pcnow_processes_sigma.yml)

### References
- [http://pcnow.webex.com/ - DOA as of 2024](http://pcnow.webex.com/ - DOA as of 2024)



{{< /column >}}
{{< /block >}}
