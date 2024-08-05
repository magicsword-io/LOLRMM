+++
description = "ScreenConnect is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "ScreenConnect"
weight = 10
displayTitle = "ScreenConnect"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# ScreenConnect


### Description

ScreenConnect is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.

**Author**: Ali Alwashali, Nasreddine Bencherchali

**Created**: 2023-10-01

**Last Modified**: 2024-08-03

### Details

- **Website**: [https://www.connectwise.com](https://www.connectwise.com)

#### PE Metadata


- **Free**: Yes

- **Verification**: No

#### Supported Operating Systems
- Android
- IOS
- Linux
- Mac
- Windows

#### Capabilities
- Command Line Support
- File Transfer
- Install Windows updates
- Receive notification when user performs a predefined event
- Remote Command Line
- Remote Control
- Sound Capture
- Start / Stop services
- View event logs


#### Installation Paths
- `C:\Program Files (x86)\ScreenConnect Client (Random)\ScreenConnect.ClientService.exe`
- `Remote Workforce Client.exe`
- `*\*\ScreenConnect.ClientService.exe`
- `C:\Program Files (x86)\ScreenConnect Client (<string ID>)\*`
- `*\ScreenConnect Client*\*`
- `*\*\ScreenConnect.WindowsClient.exe`
- `screenconnect*.exe`
- `screenconnect.windowsclient.exe`
- `Remote Workforce Client.exe`
- `screenconnect*.exe`
- `ConnectWiseControl*.exe`
- `connectwise*.exe`
- `screenconnect.windowsclient.exe`
- `screenconnect.clientservice.exe`

### Forensic Artifacts

#### Disk Artifacts
- **File**: `C:\Program Files*\ScreenConnect\App_Data\Session.db`
  **Description**: ScreenConnect session database
  **OS**: Windows
- **File**: `C:\Program Files*\ScreenConnect\App_Data\User.xml`
  **Description**: ScreenConnect user configuration
  **OS**: Windows
- **File**: `C:\ProgramData\ScreenConnect Client*\user.config`
  **Description**: ScreenConnect client user configuration
  **OS**: Windows



#### Network Artifacts

- **Description**: Known remote domains
  **Domain**:
    - `control.connectwise.com`
    - `*.connectwise.com`
    - `*.screenconnect.com`





### References
- [https://thedfirreport.com/2023/09/25/from-screenconnect-to-hive-ransomware-in-61-hours/](https://thedfirreport.com/2023/09/25/from-screenconnect-to-hive-ransomware-in-61-hours/)



{{< /column >}}
{{< /block >}}
