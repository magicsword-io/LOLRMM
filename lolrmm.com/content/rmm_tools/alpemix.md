+++
description = "Alpemix is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Alpemix"
weight = 10
displayTitle = "Alpemix"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Alpemix


### Description

Alpemix is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.


**Author**: Nasreddine Bencherchali

**Created**: 2024-08-05

**Last Modified**: 2024-08-05

### Details

- **Website**: [https://www.alpemix.com/en/Home](https://www.alpemix.com/en/Home)

#### PE Metadata
- **Filename**: Alpemix.exe
- **Original File Name**: Alpemix
- **Description**: Alpemix
- **Product**: Alpemix


- **Free**: No

- **Verification**: No

#### Supported Operating Systems
- Windows
- Linux
- Android
- Mac
- IOS

#### Capabilities
- 5 Different Solutions for Remote Support
- Access to Unattended Computers
- Access to User Account Control (UAC) Screens
- Add Your Own Logo
- Auto Sizing
- Automatic Update
- Clipboard Transfer
- Computer Independent Licensing
- Contact List and Groups
- Encrypted Communication
- External Communication Barrier
- File Transfer
- Instant Messaging
- Multi-Platform Support
- Multiple Chat
- Multiple Connections
- No Port Forwarding Required
- Peer to Peer Connection (p2p)
- Receiving Offline Message
- Remote Restart
- ReportingRestricting The Authority
- Screen Sharing
- Sending Announcement Message
- Sharing a certain part of the screen
- Video Recording
- Voice Communication
- Who is currently supporting?
- Working in Black Screen Mode


#### Installation Paths
- `C:\AlpemixService.exe`
- `C:\AlpemixSrvc\`

### Forensic Artifacts

#### Disk Artifacts

- **File**: `%localappdata%\Alpemix\Alpemix.ini`

  **Description**: N/A


  **OS**: Windows


#### Event Log Artifacts
- Event Details:
  - **Event ID**: 7045
  - **Provider Name**: Service Control Manager
  - **Log File**: System.evtx
  - **Service Name**: AlpemixSrvc
  - **Image Path**: *\Alpemix.exe servicestartxxx
  - **Description**: Service installation event as result of Alpemix installation.

#### Registry Artifacts
- **Path**: `HKLM\SYSTEM\CurrentControlSet\Services\AlpemixSrvcx`
  **Description**: N/A


#### Network Artifacts

- **Description**: N/A

  **Domains**:
    - `*.alpemix.com`

  **Ports**:
    - `443`

- **Description**: N/A

  **Domains**:
    - `*.teknopars.com`

  **Ports**:
    - `80`




### References
- [https://www.alpemix.com/en/remote-access](https://www.alpemix.com/en/remote-access)

### Acknowledgements
- Nasreddine Bencherchali (@nas_bench)

{{< /column >}}
{{< /block >}}
