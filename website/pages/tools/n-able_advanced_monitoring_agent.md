---
description: "N-Able Advanced Monitoring Agent is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "N-Able Advanced Monitoring Agent"
displayTitle: "N-Able Advanced Monitoring Agent"
---



# N-Able Advanced Monitoring Agent


### Description

N-Able Advanced Monitoring Agent is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `BASupSrvc.exe`
- `winagent.exe`
- `BASupApp.exe`
- `BASupTSHelper.exe`
- `Agent_*_RW.exe`
- `BASEClient.exe`
- `BASupSrvcCnfg.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.beanywhere.com `
    - `systemmonitor.co.uk`
    - `*system-monitor.com`
    - `cloudbackup.management`
    - `*systemmonitor.co.uk`
    - `n-able.com`
    - `systemmonitor.us`
    - `*systemmonitor.eu.com`
    - `*.logicnow.com`
    - `*.swi-tc.com`
    - `*remote.management`
    - `systemmonitor.us.cdn.cloudflare.net`
    - `*cloudbackup.management`
    - `remote.management`
    - `logicnow.com`
    - `system-monitor.com`
    - `*systemmonitor.us`
    - `systemmonitor.eu.com`
    - `*.n-able.com`


### Detections
- Detects potential network activity of N-Able Advanced Monitoring Agent RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/n-able_advanced_monitoring_agent_network_sigma.yml)
- Detects potential processes activity of N-Able Advanced Monitoring Agent RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/n-able_advanced_monitoring_agent_processes_sigma.yml)

### References
- [https://documentation.n-able.com/takecontrol/troubleshooting/Content/kb/Take-Control-Standalone-Ports-and-Domains-Firewall-and-AV-Exclusions.htm](https://documentation.n-able.com/takecontrol/troubleshooting/Content/kb/Take-Control-Standalone-Ports-and-Domains-Firewall-and-AV-Exclusions.htm)


