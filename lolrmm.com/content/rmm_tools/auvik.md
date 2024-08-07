+++
description = "Auvik is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Auvik"
weight = 10
displayTitle = "Auvik"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Auvik


### Description

Auvik is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `auvik.engine.exe`
- `auvik.agent.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.my.auvik.com`
    - `*.auvik.com`
    - `auvik.com`


### Detections
- Detects potential network activity of Auvik RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/auvik_network_sigma.yml)
- Detects potential processes activity of Auvik RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/auvik_processes_sigma.yml)

### References
- [https://support.auvik.com/hc/en-us/articles/204315700-What-protocols-and-ports-does-the-Auvik-collector-use](https://support.auvik.com/hc/en-us/articles/204315700-What-protocols-and-ports-does-the-Auvik-collector-use)



{{< /column >}}
{{< /block >}}
