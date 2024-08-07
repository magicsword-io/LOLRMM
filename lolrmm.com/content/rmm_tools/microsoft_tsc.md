+++
description = "Microsoft TSC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Microsoft TSC"
weight = 10
displayTitle = "Microsoft TSC"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Microsoft TSC


### Description

Microsoft TSC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `termsrv.exe`
- `mstsc.exe`

### Forensic Artifacts






### Detections
- Detects potential processes activity of Microsoft TSC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/microsoft_tsc_processes_sigma.yml)

### References
- [https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/terminal-server-startup-connection-application](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/terminal-server-startup-connection-application)



{{< /column >}}
{{< /block >}}
