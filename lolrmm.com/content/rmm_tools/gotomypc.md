+++
description = "GoToMyPC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "GoToMyPC"
weight = 10
displayTitle = "GoToMyPC"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# GoToMyPC


### Description

GoToMyPC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.


**Author**: Nasreddine Bencherchali

**Created**: 2024-08-05

**Last Modified**: 2024-08-05

### Details


#### PE Metadata
- **Filename**: AppCore.exe
- **Filename**: g2comm.exe
- **Filename**: g2file*.exe
- **Filename**: g2fileh.exe
- **Filename**: g2host.exe
- **Filename**: g2m_download.exe
- **Filename**: g2mainh.exe
- **Filename**: G2MChat.exe
- **Filename**: G2MCodecInstExtractor.exe
- **Filename**: G2MComm.exe
- **Filename**: G2MCoreInstExtractor.exe
- **Filename**: G2MFeedback.exe
- **Filename**: G2MHost.exee
- **Filename**: G2MInstaller.exe
- **Filename**: G2MInstallerExtractor.exe
- **Filename**: G2MInstHigh.exe
- **Filename**: G2MLauncher.exe
- **Filename**: G2MMatchMaking.exe
- **Filename**: G2MMaterials.exe
- **Filename**: G2MPolling.exe
- **Filename**: G2MQandA.exe
- **Filename**: G2MRecorder.exe
- **Filename**: G2MScrUtil64.exe
- **Filename**: G2MSessionControl.exe
- **Filename**: G2MStart.exe
- **Filename**: G2MTesting.exe
- **Filename**: G2MTranscoder.exe
- **Filename**: G2MUI.exe
- **Filename**: G2MUninstall.exe
- **Filename**: g2mupload.exe
- **Filename**: g2mvideoconference.exe
- **Filename**: G2MView.exe
- **Filename**: g2printh.exe
- **Filename**: g2quick.exe
- **Filename**: g2svc.exe
- **Filename**: g2tray.exe
- **Filename**: gopcsrv.exe
- **Filename**: GoToScrUtils.exe
- **Filename**: GoTo.exe
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `C:\Program Files (x86)\GoToMyPC\*`

### Forensic Artifacts

#### Disk Artifacts
- **File**: `%AppData%\GoTo\Logs\goto.log`
  **Description**: N/A
  **OS**: Windows


#### Registry Artifacts
- **Path**: `HKEY_LOCAL_MACHINE\WOW6432Node\Citrix\GoToMyPc`
  **Description**: Configuration settings including registration email
- **Path**: `HKEY_LOCAL_MACHINE\WOW6432Node\Citrix\GoToMyPc\GuestInvite`
  **Description**: Guest invites send to connect
- **Path**: `HKEY_CURRENT_USER\SOFTWARE\Citrix\GoToMyPc\FileTransfer\history`
  **Description**: hostname of the computer making connections and location of transferred files
- **Path**: `HKEY_USERS\<SID>\SOFTWARE\Citrix\GoToMyPc\FileTransfer\history`
  **Description**: hostname of the computer making connections and location of transferred files

#### Network Artifacts
- **Description**: N/A  **Domains**:
    - `*.GoToMyPC.com`
  **Ports**:
    - `N/A`


### Detections
- Detects potential registry activity of GoToMyPC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/gotomypc_registry_sigma.yml)
- Detects potential network activity of GoToMyPC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/gotomypc_network_sigma.yml)
- Detects potential files activity of GoToMyPC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/gotomypc_files_sigma.yml)

### References
- [https://support.logmeininc.com/gotomypc/help/what-are-the-optimal-firewall-configurations#](https://support.logmeininc.com/gotomypc/help/what-are-the-optimal-firewall-configurations#)
- [https://support.goto.com/training/help/how-do-i-configure-gototraining-to-work-with-firewalls](https://support.goto.com/training/help/how-do-i-configure-gototraining-to-work-with-firewalls)
- [https://ruler-project.github.io/ruler-project/RULER/remote/Citrix%20GoToMyPC/](https://ruler-project.github.io/ruler-project/RULER/remote/Citrix%20GoToMyPC/)

### Acknowledgements
- Phill Moore (@phillmoore)

{{< /column >}}
{{< /block >}}
