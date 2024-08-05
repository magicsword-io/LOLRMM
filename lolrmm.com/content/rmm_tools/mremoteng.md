+++
description = "mRemoteNG is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "mRemoteNG"
weight = 10
displayTitle = "mRemoteNG"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# mRemoteNG


### Description

mRemoteNG is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata


- **Free**: No

- **Verification**: No




#### Installation Paths
- `mRemoteNG.exe`
- `C:\Program Files (x86)\mRemoteNG\*`
- `*\mRemoteNG\*`
- `*\mRemoteNG.exe`
- `c:\Program Files (x86)%\mRemoteNG`
- `*%\mRemoteNG`
- `mRemoteNG-Installer-*.msi`
- `*\mRemoteNG.exe`

### Forensic Artifacts

#### Disk Artifacts

- **File**: `C:\Users\*\AppData\Roaming\mRemoteNG\mRemoteNG.log`
  **Description**: mRemoteNG log file


  **OS**: Windows

- **File**: `C:\Users\*\AppData\Roaming\mRemoteNG\confCons.xml`
  **Description**: mRemoteNG configuration file


  **OS**: Windows

- **File**: `C:\Users\*\AppData\*\mRemoteNG\**10\user.config`
  **Description**: mRemoteNG user configuration file


  **OS**: Windows




#### Network Artifacts

- **Description**: Known remote domains
  **Domain**:
    - `user_managed`
    - `mremoteng.org`





### References
- [https://github.com/mRemoteNG/mRemoteNG](https://github.com/mRemoteNG/mRemoteNG)



{{< /column >}}
{{< /block >}}
