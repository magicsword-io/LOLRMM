+++
description = "Site24x7 is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Site24x7"
weight = 10
displayTitle = "Site24x7"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Site24x7


### Description

Site24x7 is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/13/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `MEAgentHelper.exe`
- `MonitoringAgent.exe`
- `Site24x7WindowsAgentTrayIcon.exe`
- `Site24x7PluginAgent.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `plus*.site24x7.com`
    - `plus*.site24x7.eu`
    - `plus*.site24x7.in`
    - `plus*.site24x7.cn`
    - `plus*.site24x7.net.au`
    - `site24x7.com/msp`


### Detections
- Detects potential network activity of Site24x7 RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/site24x7_network_sigma.yml)
- Detects potential processes activity of Site24x7 RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/site24x7_processes_sigma.yml)

### References
- [https://support.site24x7.com/portal/en/kb/articles/which-ports-do-i-need-to-allow-access-in-my-firewall-to-use-site24x7-agent](https://support.site24x7.com/portal/en/kb/articles/which-ports-do-i-need-to-allow-access-in-my-firewall-to-use-site24x7-agent)



{{< /column >}}
{{< /block >}}
