---
description: "LabTech RMM (Now ConnectWise Automate) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "LabTech RMM (Now ConnectWise Automate)"
displayTitle: "LabTech RMM (Now ConnectWise Automate)"
---



# LabTech RMM (Now ConnectWise Automate)


### Description

LabTech RMM (Now ConnectWise Automate) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ltsvc.exe`
- `ltsvcmon.exe`
- `lttray.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `connectwise.com`


### Detections
- Detects potential network activity of LabTech RMM (Now ConnectWise Automate) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/labtech_rmm__now_connectwise_automate__network_sigma.yml)
- Detects potential processes activity of LabTech RMM (Now ConnectWise Automate) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/labtech_rmm__now_connectwise_automate__processes_sigma.yml)



