+++
description = "LogMeIn rescue is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "LogMeIn rescue"
weight = 10
displayTitle = "LogMeIn rescue"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# LogMeIn rescue


### Description

LogMeIn rescue is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `support-logmeinrescue*.exe`
- `support-logmeinrescue.exe`
- `lmi_rescue.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.logmeinrescue.com`
    - `*.logmeinrescue.eu`
    - `logmeinrescue.com`


### Detections
- Detects potential network activity of LogMeIn rescue RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/logmein_rescue_network_sigma.yml)
- Detects potential processes activity of LogMeIn rescue RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/logmein_rescue_processes_sigma.yml)

### References
- [https://support.logmeinrescue.com/rescue/help/allowlisting-and-rescue](https://support.logmeinrescue.com/rescue/help/allowlisting-and-rescue)



{{< /column >}}
{{< /block >}}
