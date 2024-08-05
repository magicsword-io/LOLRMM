+++
description = "RAdmin is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "RAdmin"
weight = 10
displayTitle = "RAdmin"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# RAdmin


### Description

RAdmin is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata


- **Free**: No

- **Verification**: No




#### Installation Paths
- `C:\Program Files\Radmin Viewer 3\*`
- `radmin3.exe`
- `*\Radmin.exe`
- `radmin.exe`
- `rserver3.exe`
- `famitrfc.exe`
- `*\Radmin Viewer 3\*`

### Forensic Artifacts

#### Disk Artifacts

- **File**: `C:\Windows\SysWOW64\rserver30\Radm_log.htm`

  **Description**: RAdmin log file (32-bit)


  **OS**: Windows

- **File**: `C:\Windows\System32\rserver30\Radm_log.htm`

  **Description**: RAdmin log file (64-bit)


  **OS**: Windows

- **File**: `C:\Windows\System32\rserver30\CHATLOGS\*\*.htm`

  **Description**: RAdmin chat logs


  **OS**: Windows

- **File**: `C:\Users\*\Documents\ChatLogs\*\*.htm`

  **Description**: RAdmin user chat logs


  **OS**: Windows




#### Network Artifacts

- **Description**: Known remote domains
  **Domain**:
    - `user_managed`
    - `radmin.com`





### References
- [https://radmin-club.com/radmin/how-to-establish-a-connection-outside-of-lan/](https://radmin-club.com/radmin/how-to-establish-a-connection-outside-of-lan/)



{{< /column >}}
{{< /block >}}
