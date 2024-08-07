+++
description = "Itarian is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Itarian"
weight = 10
displayTitle = "Itarian"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Itarian


### Description

Itarian is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ITSMAgent.exe`
- `RViewer.exe`
- `ItsmRsp.exe`
- `RAccess.exe`
- `RmmService.exe`
- `ITarianRemoteAccessSetup.exe`
- `RDesktop.exe`
- `ComodoRemoteControl.exe`
- `ITSMService.exe`
- `RHost.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `mdmsupport.comodo.com`
    - `*.itsm-us1.comodo.com`
    - `*.cmdm.comodo.com`
    - `remoteaccess.itarian.com`
    - `servicedesk.itarian.com`


### Detections
- Detects potential network activity of Itarian RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/itarian_network_sigma.yml)
- Detects potential processes activity of Itarian RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/itarian_processes_sigma.yml)

### References
- [https://help.itarian.com/topic-459-1-1005-14776-Appendix-1b---Endpoint-Manager-Services---IP-Nos,-Host-Names-and-Port-Details---US-Customers.html](https://help.itarian.com/topic-459-1-1005-14776-Appendix-1b---Endpoint-Manager-Services---IP-Nos,-Host-Names-and-Port-Details---US-Customers.html)



{{< /column >}}
{{< /block >}}
