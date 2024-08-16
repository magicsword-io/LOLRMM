---
description: "FleetDeck.io is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "FleetDeck.io"
displayTitle: "FleetDeck.io"
---



# FleetDeck.io


### Description

FleetDeck.io is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `fleetdeck_agent_svc.exe`
- `fleetdeck_commander_svc.exe`
- `fleetdeck_installer.exe`
- `fleetdeck_commander_launcher.exe`
- `fleetdeck_agent.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `fleetdeck.io`


### Detections
- Detects potential network activity of FleetDeck.io RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fleetdeck.io_network_sigma.yml)
- Detects potential processes activity of FleetDeck.io RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fleetdeck.io_processes_sigma.yml)



