+++
description = "AweRay (AweSun) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "AweRay (AweSun)"
weight = 10
displayTitle = "AweRay (AweSun)"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# AweRay (AweSun)


### Description

AweRay (AweSun) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `aweray_remote*.exe`
- `AweSun.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `asapi-us.aweray.net`
    - `asapi.aweray.net`


### Detections
- Detects potential network activity of AweRay (AweSun) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/aweray__awesun__network_sigma.yml)
- Detects potential processes activity of AweRay (AweSun) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/aweray__awesun__processes_sigma.yml)




{{< /column >}}
{{< /block >}}
