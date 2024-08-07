+++
description = "ITSupport247 (ConnectWise) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "ITSupport247 (ConnectWise)"
weight = 10
displayTitle = "ITSupport247 (ConnectWise)"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# ITSupport247 (ConnectWise)


### Description

ITSupport247 (ConnectWise) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `saazapsc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.itsupport247.net`
    - `itsupport247.net`


### Detections
- Detects potential network activity of ITSupport247 (ConnectWise) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/itsupport247__connectwise__network_sigma.yml)
- Detects potential processes activity of ITSupport247 (ConnectWise) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/itsupport247__connectwise__processes_sigma.yml)

### References
- [https://control.itsupport247.net/](https://control.itsupport247.net/)



{{< /column >}}
{{< /block >}}
