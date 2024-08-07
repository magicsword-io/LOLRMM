+++
description = "Rapid7 is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Rapid7"
weight = 10
displayTitle = "Rapid7"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Rapid7


### Description

Rapid7 is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ir_agent.exe`
- `rapid7_agent_core.exe`
- `rapid7_endpoint_broker.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.analytics.insight.rapid7.com`
    - `*.endpoint.ingress.rapid7.com`


### Detections
- Detects potential network activity of Rapid7 RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rapid7_network_sigma.yml)
- Detects potential processes activity of Rapid7 RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rapid7_processes_sigma.yml)

### References
- [https://docs.rapid7.com/insightvm/configure-communications-with-the-insight-platform/](https://docs.rapid7.com/insightvm/configure-communications-with-the-insight-platform/)



{{< /column >}}
{{< /block >}}
