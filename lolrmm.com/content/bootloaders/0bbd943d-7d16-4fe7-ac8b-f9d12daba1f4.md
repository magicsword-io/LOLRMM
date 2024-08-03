+++

description = ""
title = "0bbd943d-7d16-4fe7-ac8b-f9d12daba1f4"
weight = 10
displayTitle = "0bbd943d-7d16-4fe7-ac8b-f9d12daba1f4"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}


# 0bbd943d-7d16-4fe7-ac8b-f9d12daba1f4 ![:inline](/images/twitter_verified.png) 


### Description

This was provided by Unknown and revoked Jul-20
- **UUID**: 0bbd943d-7d16-4fe7-ac8b-f9d12daba1f4
- **Created**: 2023-05-22
- **Author**: Michael Haag
- **Acknowledgement**:  | [](https://twitter.com/)

{{< button "https://github.com/magicsword-io/bootloaders/raw/main/bootloaders/.bin" "Download" >}}
{{< tip "warning" >}}
This download link contains the Revoked Bootloader!

{{< /tip >}}

### Commands

```
bcdedit /copy &#34;{current}&#34; /d &#34;TheBoots&#34; | {% if ($_ -match &#39;{\S+}&#39;) { bcdedit /set $matches[0] path \windows\temp\ } }
```


| Use Case | Privileges | Operating System | 
|:---- | ---- | ---- |
| Persistence |  | 32-bit |



### Detections


{{< block "grid-3" >}}
{{< column >}}
#### YARA 🏹
{{< details "Expand" >}}

{{< button "https://github.com/magicsword-io/bootloaders/tree/main/detections/yara/yara-rules_bootloaders_strict.yar" "Exact Match" >}}{{< tip >}}with header and size limitation{{< /tip >}} 

{{< button "https://github.com/magicsword-io/bootloaders/tree/main/detections/yara/yara-rules_bootloaders.yar" "Threat Hunting" >}}{{< tip >}}without header and size limitation{{< /tip >}} 

{{< button "https://github.com/magicsword-io/bootloaders/tree/main/detections/yara/yara-rules_bootloaders_strict_renamed.yar" "Renamed" >}}{{< tip >}}for renamed bootloader files{{< /tip >}} 


{{< /details >}}
{{< /column >}}



{{< column >}}

#### Sigma 🛡️
{{< details "Expand" >}}
{{< button "https://github.com/magicsword-io/bootloaders/tree/main/detections/sigma/bootloader_load_win_vuln_bootloaders_names.yml" "Names" >}}{{< tip >}}detects loading using name only{{< /tip >}} 


{{< button "https://github.com/magicsword-io/bootloaders/tree/main/detections/sigma/bootloader_load_win_vuln_bootloaders.yml" "Hashes" >}}{{< tip >}}detects loading using hashes only{{< /tip >}} 

{{< /details >}}

{{< /column >}}


{{< column "mb-2" >}}

#### Sysmon 🔎
{{< details "Expand" >}}
{{< button "https://github.com/magicsword-io/bootloaders/tree/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml" "Block" >}}{{< tip >}}on hashes{{< /tip >}} 

{{< button "https://github.com/magicsword-io/bootloaders/tree/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml" "Alert" >}}{{< tip >}}on hashes{{< /tip >}} 

{{< /details >}}

{{< /column >}}
{{< /block >}}


### Resources
<br>
<li><a href="https://uefi.org/revocationlistfile">https://uefi.org/revocationlistfile</a></li>
<li><a href="https://support.microsoft.com/en-gb/topic/microsoft-guidance-for-applying-secure-boot-dbx-update-kb4575994-e3b9e4cb-a330-b3ba-a602-15083965d9ca">https://support.microsoft.com/en-gb/topic/microsoft-guidance-for-applying-secure-boot-dbx-update-kb4575994-e3b9e4cb-a330-b3ba-a602-15083965d9ca</a></li>
<br>

### CVE

<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10713">CVE-2020-10713</a></li>
<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14308">CVE-2020-14308</a></li>
<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14309">CVE-2020-14309</a></li>
<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14310">CVE-2020-14310</a></li>
<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14311">CVE-2020-14311</a></li>
<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15705">CVE-2020-15705</a></li>
<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15706">CVE-2020-15706</a></li>
<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15707">CVE-2020-15707</a></li>

### Known Vulnerable Samples

| Property           | Value |
|:-------------------|:------|
| Filename           |  |
| MD5                | [](https://www.virustotal.com/gui/file/) |
| SHA1               | [](https://www.virustotal.com/gui/file/) |
| SHA256             | [26A8EBB3EF412AA70D4AB4486EBEE8DB42656AE7F2EC868FA95FA656090F01BE](https://www.virustotal.com/gui/file/26A8EBB3EF412AA70D4AB4486EBEE8DB42656AE7F2EC868FA95FA656090F01BE) |
| Authentihash MD5   | [](https://www.virustotal.com/gui/search/authentihash%253A) |
| Authentihash SHA1  | [](https://www.virustotal.com/gui/search/authentihash%253A) |
| Authentihash SHA256| [B52531C84351EB695A8AFF0B7A5BDF93972CDEDFAF4067745425D75E21CD0CBB](https://www.virustotal.com/gui/search/authentihash%253AB52531C84351EB695A8AFF0B7A5BDF93972CDEDFAF4067745425D75E21CD0CBB) |


#### Imports
{{< details "Expand" >}}
* 

{{< /details >}}
#### Imports
{{< details "Expand" >}}
* 

{{< /details >}}
#### ImportedFunctions
{{< details "Expand" >}}

{{< /details >}}
#### ExportedFunctions
{{< details "Expand" >}}

{{< /details >}}

#### Signature
{{< details "Expand" >}}

{{< /details >}}
-----



[*source*](https://github.com/magicsword-io/bootloaders/tree/main/yaml/0bbd943d-7d16-4fe7-ac8b-f9d12daba1f4.yaml)

*last_updated:* 2023-08-31








{{< /column >}}
{{< /block >}}
