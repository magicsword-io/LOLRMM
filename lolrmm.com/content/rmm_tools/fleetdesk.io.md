+++
description = "FleetDesk.io is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "FleetDesk.io"
weight = 10
displayTitle = "FleetDesk.io"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# FleetDesk.io


### Description

FleetDesk.io is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

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
- `fleetdeck_agent.exe`
- `fleetdeck_commander_launcher.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.fleetdeck.io`
    - `cognito-idp.us-west-2.amazonaws.com`
    - `fleetdeck.io`


### Detections
- Detects potential network activity of FleetDesk.io RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fleetdesk.io_network_sigma.yml)
- Detects potential processes activity of FleetDesk.io RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/fleetdesk.io_processes_sigma.yml)

### References
- [https://fleetdeck.io/faq/](https://fleetdeck.io/faq/)



{{< /column >}}
{{< /block >}}
