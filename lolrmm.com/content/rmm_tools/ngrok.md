+++
description = "ngrok is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "ngrok"
weight = 10
displayTitle = "ngrok"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# ngrok


### Description

ngrok is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ngrok.exe`
- `C:\*\ngrok.zip`
- `*\ngrok*`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `user_managed`
    - `ngrok.com`


### Detections
- Detects potential network activity of ngrok RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ngrok_network_sigma.yml)
- Detects potential processes activity of ngrok RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ngrok_processes_sigma.yml)

### References
- [https://ngrok.com/docs/guides/running-behind-firewalls/](https://ngrok.com/docs/guides/running-behind-firewalls/)



{{< /column >}}
{{< /block >}}
