---
description: "Google Drive is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Google Drive"
displayTitle: "Google Drive"
---



# Google Drive


### Description

Google Drive is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `C:\Program Files\Google\Drive File Stream\*`
- `*\Google\Drive File Stream\*`
- `*Users\*\AppData\*\Google\DriveFS*`
- `G:\My Drive*`
- `*\GoogleDriveFS.exe`

### Forensic Artifacts






### Detections
- Detects potential processes activity of Google Drive RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/google_drive_processes_sigma.yml)



