+++
description = "NinjaRMM is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "NinjaRMM"
weight = 10
displayTitle = "NinjaRMM"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# NinjaRMM


### Description

NinjaRMM is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ninjarmmagent.exe`
- `NinjaRMMAgent.exe`
- `NinjaRMMAgenPatcher.exe`
- `ninjarmm-cli.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.ninjarmm.com`
    - `*.ninjaone.com`
    - `resources.ninjarmm.com`
    - `ninjaone.com`


### Detections
- Detects potential network activity of NinjaRMM RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ninjarmm_network_sigma.yml)
- Detects potential processes activity of NinjaRMM RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ninjarmm_processes_sigma.yml)

### References
- [https://www.ninjaone.com/faq/](https://www.ninjaone.com/faq/)



{{< /column >}}
{{< /block >}}
