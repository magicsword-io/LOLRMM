+++
description = "ConnectWise Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "ConnectWise Control"
weight = 10
displayTitle = "ConnectWise Control"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# ConnectWise Control


### Description

ConnectWise Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `screenconnect.clientservice.exe`
- `connectwisecontrol.client.exe`
- `screenconnect.windowsclient.exe`
- `connectwisechat-customer.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `live.screenconnect.com`
    - `control.connectwise.com`


### Detections
- Detects potential network activity of ConnectWise Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/connectwise_control_network_sigma.yml)
- Detects potential processes activity of ConnectWise Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/connectwise_control_processes_sigma.yml)




{{< /column >}}
{{< /block >}}
