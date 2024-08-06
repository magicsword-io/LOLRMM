+++
description = "LogMeIn is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "LogMeIn"
weight = 10
displayTitle = "LogMeIn"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

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
- **Description**: LMIGuardianSvc
- **Product**: LMIGuardianSvc


- **Free**: No

- **Verification**: No





### Forensic Artifacts




#### Network Artifacts

- **Description**: N/A

  **Domains**:
    - `logmein-gateway.com`

  **Ports**:
    - `443`

- **Description**: N/A

  **Domains**:
    - `*.logmein.com`

  **Ports**:
    - `443`

- **Description**: N/A

  **Domains**:
    - `*.logmein.eu`

  **Ports**:
    - `443`

- **Description**: N/A

  **Domains**:
    - `logmeinrescue.com`

  **Ports**:
    - `443`

- **Description**: N/A

  **Domains**:
    - `*.logmeininc.com`

  **Ports**:
    - `443`



### Detections
-   [Sigma rule](https://github.com/SigmaHQ/sigma/blob/782f0f524e6f797ea114fe0d87b22cb4abaa6b7c/rules/windows/dns_query/dns_query_win_remote_access_software_domains_non_browsers.yml)

  DNS Query To Remote Access Software Domain From Non-Browser App



-   [Sigma rule](https://github.com/SigmaHQ/sigma/blob/782f0f524e6f797ea114fe0d87b22cb4abaa6b7c/rules/windows/process_creation/proc_creation_win_remote_access_tools_logmein.yml)

  Remote Access Tool - LogMeIn Execution




### References
- [https://support.logmeininc.com/central/help/allowlisting-and-firewall-configuration](https://support.logmeininc.com/central/help/allowlisting-and-firewall-configuration)

### Acknowledgements
- Nasreddine Bencherchali (@nas_bench)

{{< /column >}}
{{< /block >}}
