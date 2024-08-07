+++
description = "BeamYourScreen is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "BeamYourScreen"
weight = 10
displayTitle = "BeamYourScreen"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# BeamYourScreen


### Description

BeamYourScreen is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `beamyourscreen.exe`
- `beamyourscreen-host.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `beamyourscreen.com`
    - `*.beamyourscreen.com`


### Detections
- Detects potential network activity of BeamYourScreen RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/beamyourscreen_network_sigma.yml)
- Detects potential processes activity of BeamYourScreen RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/beamyourscreen_processes_sigma.yml)

### References
- [beamyourscreen redirects to https://www.mikogo.com/](beamyourscreen redirects to https://www.mikogo.com/)



{{< /column >}}
{{< /block >}}
