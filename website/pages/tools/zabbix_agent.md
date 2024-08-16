---
description: "Zabbix Agent is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Zabbix Agent"
displayTitle: "Zabbix Agent"
---



# Zabbix Agent


### Description

Zabbix Agent is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `zabbix_agent*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `zabbix.com`


### Detections
- Detects potential network activity of Zabbix Agent RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/zabbix_agent_network_sigma.yml)
- Detects potential processes activity of Zabbix Agent RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/zabbix_agent_processes_sigma.yml)

### References
- [https://www.zabbix.com/documentation/current/en/manual/appendix/install/windows_agent](https://www.zabbix.com/documentation/current/en/manual/appendix/install/windows_agent)


