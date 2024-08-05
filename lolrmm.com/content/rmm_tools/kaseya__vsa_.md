+++
description = "Kaseya (VSA) aka Unigma is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Kaseya (VSA)"
weight = 10
displayTitle = "Kaseya (VSA)"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Kaseya (VSA)


### Description

Kaseya (VSA) aka Unigma is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata


- **Free**: No

- **Verification**: No




#### Installation Paths
- `agentmon.exe`
- `KaUpdHlp.exe`
- `KaUsrTsk.exe`

### Forensic Artifacts

#### Disk Artifacts

- **File**: `C:\Users\*\AppData\Local\Kaseya\Log\KaseyaLiveConnect\*`

  **Description**: Kaseya Live Connect logs


  **OS**: Windows

- **File**: `C:\ProgramData\Kaseya\Log\Endpoint\*`

  **Description**: Kaseya Endpoint logs


  **OS**: Windows

- **File**: `C:\Program Files*\Kaseya\*\agentmon.log`

  **Description**: Kaseya Agent Monitor log


  **OS**: Windows

- **File**: `C:\Users\*\AppData\Local\Temp\KASetup.log`

  **Description**: Kaseya Setup log in user temp directory


  **OS**: Windows

- **File**: `C:\Windows\Temp\KASetup.log`

  **Description**: Kaseya Setup log in Windows temp directory


  **OS**: Windows

- **File**: `C:\ProgramData\Kaseya\Log\KaseyaEdgeServices\*`

  **Description**: Kaseya Edge Services logs


  **OS**: Windows




#### Network Artifacts

- **Description**: Known remote domains
  **Domain**:
    - `deploy01.kaseya.com`
    - `*managedsupport.kaseya.net`
    - `*.kaseya.net`
    - `kaseya.com`





### References
- [https://helpdesk.kaseya.com/hc/en-gb/articles/229012608-Software-Deployment-URL-Port-Requirements](https://helpdesk.kaseya.com/hc/en-gb/articles/229012608-Software-Deployment-URL-Port-Requirements)



{{< /column >}}
{{< /block >}}
