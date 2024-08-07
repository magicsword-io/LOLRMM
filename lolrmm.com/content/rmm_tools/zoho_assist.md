+++
description = "Zoho Assist is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Zoho Assist"
weight = 10
displayTitle = "Zoho Assist"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Zoho Assist


### Description

Zoho Assist is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `zaservice.exe`
- `ZMAgent.exe`
- `C:\*\ZA_Access.exe`
- `ZohoMeeting.exe`
- `Zohours.exe`
- `zohotray.exe`
- `ZohoURSService.exe`
- `*\ZA_Access.exe`
- `Zaservice.exe`
- `za_connect.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.zoho.com.au`
    - `*.zohoassist.jp`
    - `assist.zoho.com`
    - `zoho.com/assist/`
    - `*.zoho.in`
    - `downloads.zohodl.com.cn`
    - `*.zohoassist.com`
    - `downloads.zohocdn.com`
    - `gateway.zohoassist.com`
    - `*.zohoassist.com.cn`
    - `*.zoho.com.cn`
    - `*.zoho.com`
    - `*.zoho.eu`


### Detections
- Detects potential network activity of Zoho Assist RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/zoho_assist_network_sigma.yml)
- Detects potential processes activity of Zoho Assist RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/zoho_assist_processes_sigma.yml)

### References
- [https://www.zoho.com/assist/kb/firewall-configuration.html](https://www.zoho.com/assist/kb/firewall-configuration.html)



{{< /column >}}
{{< /block >}}
