---
description: "TurboMeeting is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "TurboMeeting"
displayTitle: "TurboMeeting"
---



# TurboMeeting


### Description

TurboMeeting is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `pcstarter.exe`
- `turbomeeting.exe`
- `turbomeetingstarter.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `acceo.com/turbomeeting/`


### Detections
- Detects potential network activity of TurboMeeting RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/turbomeeting_network_sigma.yml)
- Detects potential processes activity of TurboMeeting RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/turbomeeting_processes_sigma.yml)

### References
- [http://sourcing.rhubcom.com/v5/faqs.html#collapsetwentysix2-topdiv](http://sourcing.rhubcom.com/v5/faqs.html#collapsetwentysix2-topdiv)


