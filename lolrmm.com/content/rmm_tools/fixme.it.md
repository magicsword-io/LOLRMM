+++
description = "FixMe.it is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "FixMe.it"
weight = 10
displayTitle = "FixMe.it"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# FixMe.it


### Description

FixMe.it is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `FixMeit Unattended Access Setup.exe`
- `TiExpertStandalone.exe`
- `FixMeitClient*.exe`
- `FixMeit Client.exe`
- `FixMeit Expert Setup.exe`
- `TiExpertCore.exe`
- `fixmeitclient.exe`
- `TiClientCore.exe`
- `TiClientHelper*.exe`
- `no installation required | recommend blocking fixme[.]it SaaS portal`
- `no installation required | recommend blocking fixme[.]it SaaS portal`
- `9380CC75B872221A7425D7503565B67580407F60`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.fixme.it`
    - `*.techinline.net`
    - `fixme.it`
    - `*set.me`
    - `*setme.net`


### Detections
- Detects potential network activity of FixMe.it RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fixme.it_network_sigma.yml)
- Detects potential processes activity of FixMe.it RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fixme.it_processes_sigma.yml)

### References
- [https://docs.fixme.it/general-questions/which-ports-and-servers-does-fixme-it-use](https://docs.fixme.it/general-questions/which-ports-and-servers-does-fixme-it-use)



{{< /column >}}
{{< /block >}}
