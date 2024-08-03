+++

description = ""
title = "a34d1cd4-ad9d-4dda-8e4e-ac86e42a6d92"
weight = 10
displayTitle = "bootmgfw.efi"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}


# bootmgfw.efi ![:inline](/images/twitter_verified.png) 


### Description

This was provided by Microsoft and revoked May-23
- **UUID**: a34d1cd4-ad9d-4dda-8e4e-ac86e42a6d92
- **Created**: 2023-05-22
- **Author**: Michael Haag
- **Acknowledgement**:  | [](https://twitter.com/)

{{< button "https://github.com/magicsword-io/bootloaders/raw/main/bootloaders/.bin" "Download" >}}
{{< tip "warning" >}}
This download link contains the Revoked Bootloader!

{{< /tip >}}

### Commands

```
bcdedit /copy &#34;{current}&#34; /d &#34;TheBoots&#34; | {% if ($_ -match &#39;{\S+}&#39;) { bcdedit /set $matches[0] path \windows\temp\bootmgfw.efi } }
```


| Use Case | Privileges | Operating System | 
|:---- | ---- | ---- |
| Persistence |  | 32-bit ARM |



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

<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=Black Lotus Microsoft Windows 10 version 1507">Black Lotus Microsoft Windows 10 version 1507</a></li>

### Known Vulnerable Samples

| Property           | Value |
|:-------------------|:------|
| Filename           | bootmgfw.efi |
| MD5                | [](https://www.virustotal.com/gui/file/) |
| SHA1               | [](https://www.virustotal.com/gui/file/) |
| SHA256             | [331A6D1D07B7A19AB36312AB8303C9FA5B5D2628B6EF5C593846B6F4B824059F](https://www.virustotal.com/gui/file/331A6D1D07B7A19AB36312AB8303C9FA5B5D2628B6EF5C593846B6F4B824059F) |
| Authentihash MD5   | [](https://www.virustotal.com/gui/search/authentihash%253A) |
| Authentihash SHA1  | [](https://www.virustotal.com/gui/search/authentihash%253A) |
| Authentihash SHA256| [DF6EC4F50BE2A4B7657F0397BED483BE143A18883615800A65A64B7E84D9B858](https://www.virustotal.com/gui/search/authentihash%253ADF6EC4F50BE2A4B7657F0397BED483BE143A18883615800A65A64B7E84D9B858) |


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



[*source*](https://github.com/magicsword-io/bootloaders/tree/main/yaml/a34d1cd4-ad9d-4dda-8e4e-ac86e42a6d92.yaml)

*last_updated:* 2023-08-31








{{< /column >}}
{{< /block >}}
