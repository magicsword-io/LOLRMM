+++
description = "Pandora RC (eHorus) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Pandora RC (eHorus)"
weight = 10
displayTitle = "Pandora RC (eHorus)"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Pandora RC (eHorus)


### Description

Pandora RC (eHorus) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ehorus standalone.exe`
- `ehorus_agent.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `portal.ehorus.com`


### Detections
- Detects potential network activity of Pandora RC (eHorus) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pandora_rc__ehorus__network_sigma.yml)
- Detects potential processes activity of Pandora RC (eHorus) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pandora_rc__ehorus__processes_sigma.yml)

### References
- [https://pandorafms.com/manual/!current/en/documentation/09_pandora_rc/01_pandora_rc_introduction](https://pandorafms.com/manual/!current/en/documentation/09_pandora_rc/01_pandora_rc_introduction)



{{< /column >}}
{{< /block >}}
