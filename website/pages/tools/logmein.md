---
description: "LogMeIn is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "LogMeIn"
displayTitle: "LogMeIn"
---



# LogMeIn


### Description

LogMeIn is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.


**Author**: Nasreddine Bencherchali

**Created**: 2024-08-05

**Last Modified**: 2024-08-05

### Details

- **Website**: [https://www.logmein.com/](https://www.logmein.com/)

#### PE Metadata
- **Filename**: lmiguardiansvc.exe
- **Filename**: lmiignition.exe
- **Filename**: logmeinsystray.exe
- **Filename**: logmein.exe
- **OriginalFileName**: 
- **Company**: LogMeIn, Inc.
- **Description**: LMIGuardianSvc
- **Product**: LMIGuardianSvc


- **Free**: No

- **Verification**: No





### Forensic Artifacts




#### Network Artifacts
- **Description**: N/A
<br/>**Domains**:
    - `logmein-gateway.com`
  **Ports**:
    - `443`
- **Description**: N/A
<br/>**Domains**:
    - `*.logmein.com`
  **Ports**:
    - `443`
- **Description**: N/A
<br/>**Domains**:
    - `*.logmein.eu`
  **Ports**:
    - `443`
- **Description**: N/A
<br/>**Domains**:
    - `logmeinrescue.com`
  **Ports**:
    - `443`
- **Description**: N/A
<br/>**Domains**:
    - `*.logmeininc.com`
  **Ports**:
    - `443`


### Detections
- DNS Query To Remote Access Software Domain From Non-Browser App
  - [Sigma Rule](https://github.com/SigmaHQ/sigma/blob/782f0f524e6f797ea114fe0d87b22cb4abaa6b7c/rules/windows/dns_query/dns_query_win_remote_access_software_domains_non_browsers.yml)
- Remote Access Tool - LogMeIn Execution
  - [Sigma Rule](https://github.com/SigmaHQ/sigma/blob/782f0f524e6f797ea114fe0d87b22cb4abaa6b7c/rules/windows/process_creation/proc_creation_win_remote_access_tools_logmein.yml)
- Detects potential network activity of LogMeIn RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/logmein_network_sigma.yml)

### References
- [https://support.logmeininc.com/central/help/allowlisting-and-firewall-configuration](https://support.logmeininc.com/central/help/allowlisting-and-firewall-configuration)

### Acknowledgements
- Nasreddine Bencherchali (@nas_bench)
