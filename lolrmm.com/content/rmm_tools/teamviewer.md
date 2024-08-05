+++
description = "TeamViewer is a remote monitoring and management (RMM) tool."
title = "TeamViewer"
weight = 10
displayTitle = "TeamViewer"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# TeamViewer


### Description

TeamViewer is a remote monitoring and management (RMM) tool.


**Author**: Nasreddine Bencherchali, Michael Haag

**Created**: 2024-08-02

**Last Modified**: 2024-08-02

### Details

- **Website**: [https://www.teamviewer.com/en](https://www.teamviewer.com/en)

#### PE Metadata
- **Filename**: TeamViewer.exe**Product**: TeamViewer
- **Privileges**: user

- **Free**: Yes

- **Verification**: No

#### Supported Operating Systems
- Android
- ChromeOS
- IOS
- Linux
- Mac
- Windows


#### Known Vulnerabilities
- [https://www.cvedetails.com/vulnerability-list/vendor_id-11100/product_id-19942/Teamviewer-Teamviewer.html](https://www.cvedetails.com/vulnerability-list/vendor_id-11100/product_id-19942/Teamviewer-Teamviewer.html)

#### Installation Paths
- `C:\Program Files\TeamViewer\`
- `teamviewer_desktop.exe`
- `teamviewer_service.exe`
- `teamviewerhost`

### Forensic Artifacts

#### Disk Artifacts
- **File**: `C:\Users\<username>\AppData\Local\Temp\TeamViewer\TV15Install.log`
  **Description**: N/A
  **OS**: Windows
- **File**: `TeamViewer\d\d_Logfile\.log`
  **Description**: N/A
  **OS**: Windows
- **File**: `C:\Program Files\TeamViewer\Connections_incoming.txt`
  **Description**: N/A
  **OS**: Windows
- **File**: `C:\Program Files\TeamViewer\TVNetwork.log`
  **Description**: N/A
  **OS**: Windows
- **File**: `%LOCALAPPDATA%\Temp\TeamViewer\TV15Install.log`
  **Description**: N/A
  **OS**: Windows
- **File**: `%APPDATA%\\TeamViewer\\TeamViewer\d\d_Logfile\.log`
  **Description**: N/A
  **OS**: Windows
- **File**: `teamviewerqs.exe`
  **Description**: N/A
  **OS**: Windows
- **File**: `tv_w32.exe`
  **Description**: N/A
  **OS**: Windows
- **File**: `tv_w64.exe`
  **Description**: N/A
  **OS**: Windows
- **File**: `tv_x64.exe`
  **Description**: N/A
  **OS**: Windows
- **File**: `teamviewer.exe`
  **Description**: N/A
  **OS**: Windows
- **File**: `teamviewer_service.exe`
  **Description**: N/A
  **OS**: Windows
- **File**: `%LOCALAPPDATA%\TeamViewer\Database\tvchatfilecache.db`
  **Description**: SQlite 3 database storing cache about TeamViewer chat
  **OS**: Windows
- **File**: `%LOCALAPPDATA%\TeamViewer\RemotePrinting\tvprint.db`
  **Description**: SQlite 3 database storing TeamViewer print jobs
  **OS**: Windows
- **File**: `%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\TeamViewer.lnk`
  **Description**: N/A
  **OS**: Windows
- **File**: `C:\Program Files*\TeamViewer\connections*.txt`
  **Description**: N/A
  **OS**: Windows
- **File**: `C:\Users\*\AppData\Roaming\TeamViewer\MRU\RemoteSupport\*tvc`
  **Description**: N/A
  **OS**: Windows

#### Event Log Artifacts
- Event Details:
  - **Event ID**: 7045
  - **Provider Name**: Service Control Manager
  - **Log File**: System.evtx
  - **Service Name**: TeamViewer
  - **Image Path**: "C:\\Program Files\\TeamViewer\\TeamViewer_Service.exe"
  - **Description**: Service installation event as result of TeamViewer installation.

#### Registry Artifacts
- **Path**: `HKLM\SOFTWARE\TeamViewer\*`
  **Description**: N/A
- **Path**: `HKU\<SID>\SOFTWARE\TeamViewer\*`
  **Description**: N/A
- **Path**: `HKLM\SYSTEM\CurrentControlSet\Services\TeamViewer\*`
  **Description**: N/A
- **Path**: `HKLM\SOFTWARE\TeamViewer\ConnectionHistory`
  **Description**: N/A
- **Path**: `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\TeamViewer\*`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\MainWindowHandle`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\DesktopWallpaperSingleImage`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\DesktopWallpaperSingleImagePath`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\DesktopWallpaperSingleImagePosition`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\MinimizeToTray`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\MultiMedia\AudioUserSelectedCapturingEndpoint`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\MultiMedia\AudioSendingVolumeV2`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\MultiMedia\AudioUserSelectedRenderingEndpoint`
  **Description**: N/A
- **Path**: `HKLM\SOFTWARE\TeamViewer\ConnectionHistory`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\ClientWindow_Mode`
  **Description**: N/A
- **Path**: `HKU\SID\SOFTWARE\TeamViewer\ClientWindowPositions`
  **Description**: N/A

#### Network Artifacts

- **Description**: N/A
  **Domain**: `*.teamviewer.com`

  **Port**: `443`

- **Description**: N/A
  **Domain**: `router15.teamviewer.com`

  **Port**: `443`

- **Description**: N/A
  **Domain**: `client.teamviewer.com`

  **Port**: `443`

- **Description**: N/A
  **Domain**: `taf.teamviewer.com`

  **Port**: `443`


#### Other Artifacts
- **Type**: Mutex  **Value**: TeamViewer_LogMutex
- **Type**: Mutex  **Value**: TeamViewerHooks_DynamicMemMutex
- **Type**: Mutex  **Value**: TeamViewer3_Win32_Instance_Mutex


### References
- [https://community.teamviewer.com/English/kb/articles/4139-ports-used-by-teamviewer](https://community.teamviewer.com/English/kb/articles/4139-ports-used-by-teamviewer)
- [https://arista.my.site.com/AristaCommunity/s/article/Security-Analysis-TeamViewer#](https://arista.my.site.com/AristaCommunity/s/article/Security-Analysis-TeamViewer#)
- [https://www.teamviewer.com/en/global/support/knowledge-base/teamviewer-classic/troubleshooting/log-file-reading-incoming-connection/](https://www.teamviewer.com/en/global/support/knowledge-base/teamviewer-classic/troubleshooting/log-file-reading-incoming-connection/)
- [https://www.synacktiv.com/publications/legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects.html](https://www.synacktiv.com/publications/legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects.html)
- [https://github.com/Purp1eW0lf/Blue-Team-Notes](https://github.com/Purp1eW0lf/Blue-Team-Notes)

### Acknowledgements
- Théo Letailleur (in/theosyn)

{{< /column >}}
{{< /block >}}
