+++
description = "FleetDeck is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "FleetDeck"
weight = 10
displayTitle = "FleetDeck"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# FleetDeck


### Description

FleetDeck is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `fleetdeck_agent_svc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `fleetdeck.io`


### Detections
- Detects potential network activity of FleetDeck RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fleetdeck_network_sigma.yml)
- Detects potential processes activity of FleetDeck RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fleetdeck_processes_sigma.yml)




{{< /column >}}
{{< /block >}}
