+++
description = "RES Automation Manager is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "RES Automation Manager"
weight = 10
displayTitle = "RES Automation Manager"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# RES Automation Manager


### Description

RES Automation Manager is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `wisshell*.exe`
- `wmc.exe`
- `wmc_deployer.exe`
- `wmcsvc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `ivanti.com/`


### Detections
- Detects potential network activity of RES Automation Manager RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/res_automation_manager_network_sigma.yml)
- Detects potential processes activity of RES Automation Manager RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/res_automation_manager_processes_sigma.yml)

### References
- [https://forums.ivanti.com/s/article/INFO-Which-ports-does-Ivanti-Automation-use?language=en_US&ui-force-components-controllers-recordGlobalValueProvider.RecordGvp.getRecord=1](https://forums.ivanti.com/s/article/INFO-Which-ports-does-Ivanti-Automation-use?language=en_US&ui-force-components-controllers-recordGlobalValueProvider.RecordGvp.getRecord=1)



{{< /column >}}
{{< /block >}}
