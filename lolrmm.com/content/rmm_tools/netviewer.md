+++
description = "Netviewer is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Netviewer"
weight = 10
displayTitle = "Netviewer"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Netviewer


### Description

Netviewer is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `netviewer*.exe`
- `netviewer.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `download.cnet.com/Net-Viewer/3000-2370_4-10034828.html`


### Detections
- Detects potential network activity of Netviewer RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/netviewer_network_sigma.yml)
- Detects potential processes activity of Netviewer RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/netviewer_processes_sigma.yml)




{{< /column >}}
{{< /block >}}
