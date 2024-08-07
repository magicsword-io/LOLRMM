+++
description = "KickIdler is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "KickIdler"
weight = 10
displayTitle = "KickIdler"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# KickIdler


### Description

KickIdler is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `grabberEM.*msi`
- `grabberTT*.msi`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `kickidler.com`
    - `my.kickidler.com`


### Detections
- Detects potential network activity of KickIdler RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/kickidler_network_sigma.yml)

### References
- [https://www.kickidler.com/for-it/faq/](https://www.kickidler.com/for-it/faq/)



{{< /column >}}
{{< /block >}}
