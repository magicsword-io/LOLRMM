+++
description = "BeAnyWhere is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "BeAnyWhere"
weight = 10
displayTitle = "BeAnyWhere"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# BeAnyWhere


### Description

BeAnyWhere is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `basuptshelper.exe`
- `basupsrvcupdate.exe`
- `BASupApp.exe`
- `BASupSysInf.exe`
- `BASupAppSrvc.exe`
- `TakeControl.exe`
- `BASupAppElev.exe`
- `basupsrvc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `beanywhere.en.uptodown.com/windows`
    - `beanywhere.com`


### Detections
- Detects potential network activity of BeAnyWhere RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/beanywhere_network_sigma.yml)
- Detects potential processes activity of BeAnyWhere RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/beanywhere_processes_sigma.yml)

### References
- [https://www.shouldiremoveit.com/beanywhere-support-service-40908-program.aspx](https://www.shouldiremoveit.com/beanywhere-support-service-40908-program.aspx)



{{< /column >}}
{{< /block >}}
