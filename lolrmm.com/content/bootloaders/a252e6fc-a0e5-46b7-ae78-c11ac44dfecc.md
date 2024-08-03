+++

description = ""
title = "a252e6fc-a0e5-46b7-ae78-c11ac44dfecc"
weight = 10
displayTitle = "bootmgfw.efi"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}


# bootmgfw.efi ![:inline](/images/twitter_verified.png) 


### Description

This was provided by Microsoft and revoked May-23
- **UUID**: a252e6fc-a0e5-46b7-ae78-c11ac44dfecc
- **Created**: 2023-05-22
- **Author**: Michael Haag
- **Acknowledgement**:  | [](https://twitter.com/)

{{< button "https://github.com/magicsword-io/bootloaders/raw/main/bootloaders/3827b6fa1f4022001328be9d79e33b18.bin" "Download" >}}
{{< tip "warning" >}}
This download link contains the Revoked Bootloader!

{{< /tip >}}

### Commands

```
bcdedit /copy &#34;{current}&#34; /d &#34;TheBoots&#34; | {% if ($_ -match &#39;{\S+}&#39;) { bcdedit /set $matches[0] path \windows\temp\bootmgfw.efi } }
```


| Use Case | Privileges | Operating System | 
|:---- | ---- | ---- |
| Persistence |  | 64-bit |



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

<li><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=Black Lotus Microsoft Windows 8.1">Black Lotus Microsoft Windows 8.1</a></li>

### Known Vulnerable Samples

| Property           | Value |
|:-------------------|:------|
| Filename           | bootmgfw.efi |
| MD5                | [3827b6fa1f4022001328be9d79e33b18](https://www.virustotal.com/gui/file/3827b6fa1f4022001328be9d79e33b18) |
| SHA1               | [3b0ef33281ba05d9d9259b1fd44bf5d43e5187a4](https://www.virustotal.com/gui/file/3b0ef33281ba05d9d9259b1fd44bf5d43e5187a4) |
| SHA256             | [3927727eb2435b28d2cf0ce1757e72ce3e92a86362b87120040c744c1c08bce9](https://www.virustotal.com/gui/file/3927727eb2435b28d2cf0ce1757e72ce3e92a86362b87120040c744c1c08bce9) |
| Authentihash MD5   | [d9a85920d99763cc28d796c77094f958](https://www.virustotal.com/gui/search/authentihash%253Ad9a85920d99763cc28d796c77094f958) |
| Authentihash SHA1  | [932efcc1a062376a53c14b3fad8f6bf34b96524f](https://www.virustotal.com/gui/search/authentihash%253A932efcc1a062376a53c14b3fad8f6bf34b96524f) |
| Authentihash SHA256| [50871141459a21faba3dbbf63da5aac8863fa3d8a9891f182ed72e3a74b64fdc](https://www.virustotal.com/gui/search/authentihash%253A50871141459a21faba3dbbf63da5aac8863fa3d8a9891f182ed72e3a74b64fdc) |
| RichPEHeaderHash MD5   | [aaf18af925d829095e017c505f1a0039](https://www.virustotal.com/gui/search/rich_pe_header_hash%253Aaaf18af925d829095e017c505f1a0039) |
| RichPEHeaderHash SHA1  | [c3d13f7d96127a3b16c7a8c0a3dd98fd9f22c3cf](https://www.virustotal.com/gui/search/rich_pe_header_hash%253Ac3d13f7d96127a3b16c7a8c0a3dd98fd9f22c3cf) |
| RichPEHeaderHash SHA256| [05367ecae4cf78cc575048fb931468b1d210df8c38ff8ca05481124b1a1a6917](https://www.virustotal.com/gui/search/rich_pe_header_hash%253A05367ecae4cf78cc575048fb931468b1d210df8c38ff8ca05481124b1a1a6917) |
| Company           | Microsoft Corporation |
| Description       | Boot Manager |
| Product           | Microsoft® Windows® Operating System |
| OriginalFilename  | bootmgr.exe |

#### Certificates

{{< details "Expand" >}}
###### Certificate 330000038db0bfe1b0ca33b3d400000000038d
| Field                             | Value                      |
|-----------------------------------|----------------------------|
| ToBeSigned (TBS) MD5              | 74a1035aa6d38ec0a7a35a6d143cc612  |
| ToBeSigned (TBS) SHA1             | 62c5627f7d38759edce84eace5ae41fc7a54d6f8 |
| ToBeSigned (TBS) SHA256           | b6319137740477c564fb2beb1d50929a333f092aa362ce5129085a2c9d4bf489 |
| Subject                           | C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Windows |
| ValidFrom                         | 2022-05-05 19:23:15 |
| ValidTo                           | 2023-05-04 19:23:15 |
| Signature                         | 7aa4402e28e909a6f7ff198a87c8f546fd868da5adf65529e8ced9b8ff16f56d03704671b64454a21437cdc6b47d83ea130e55b30ed223fda526676f6034a0d649e924cdf96d3c26386378d2ab91da329e3ddecbfe21c7f32764df6409a7f82f67c90ab5d9d7c167376487b3579fc1d99201098d2124f91f6558fb03285a49159fcc6d6ff6f8bbbc51f5209689963bebbc504c08089fa7c13e3bbae4f3c77a3a083548f8c95a1504b66fd5cfa658f9353ca231fd085e94f9bdb9bf68e302cae1bb6d483f97b5d4a2d26486fcab72ebe5fd0b555066edd3d894531f836130e309ccf4e98d1b44950efb0812a2190d4b0df3c5bf7ee8123a1d57410cd797dc0ccf |
| SignatureAlgorithmOID             | 1.2.840.113549.1.1.11 |
| IsCertificateAuthority            | False |
| SerialNumber                      | 330000038db0bfe1b0ca33b3d400000000038d |
| Version                           | 3 |
###### Certificate 61077656000000000008
| Field                             | Value                      |
|-----------------------------------|----------------------------|
| ToBeSigned (TBS) MD5              | 30a3f0b64324ed7f465e7fc618cb69e7  |
| ToBeSigned (TBS) SHA1             | 002de3561519b662c5e3f5faba1b92c403fb7c41 |
| ToBeSigned (TBS) SHA256           | 4e80be107c860de896384b3eff50504dc2d76ac7151df3102a4450637a032146 |
| Subject                           | C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Windows Production PCA 2011 |
| ValidFrom                         | 2011-10-19 18:41:42 |
| ValidTo                           | 2026-10-19 18:51:42 |
| Signature                         | 14fc7c7151a579c26eb2ef393ebc3c520f6e2b3f101373fea868d048a6344d8a960526ee3146906179d6ff382e456bf4c0e528b8da1d8f8adb09d71ac74c0a36666a8cec1bd70490a81817a49bb9e240323676c4c15ac6bfe404c0ea16d3acc368ef62acdd546c503058a6eb7cfe94a74e8ef4ec7c867357c2522173345af3a38a56c804da0709edf88be3cef47e8eaef0f60b8a08fb3fc91d727f53b8ebbe63e0e33d3165b081e5f2accd16a49f3da8b19bc242d090845f541dff89eaba1d47906fb0734e419f409f5fe5a12ab21191738a2128f0cede73395f3eab5c60ecdf0310a8d309e9f4f69685b67f51886647198da2b0123d812a680577bb914c627bb6c107c7ba7a8734030e4b627a99e9cafcce4a37c92da4577c1cfe3ddcb80f5afad6c4b30285023aeab3d96ee4692137de81d1f675190567d393575e291b39c8ee2de1cde445735bd0d2ce7aab1619824658d05e9d81b367af6c35f2bce53f24e235a20a7506f6185699d4782cd1051bebd088019daa10f105dfba7e2c63b7069b2321c4f9786ce2581706362b911203cca4d9f22dbaf9949d40ed1845f1ce8a5c6b3eab03d370182a0a6ae05f47d1d5630a32f2afd7361f2a705ae5425908714b57ba7e8381f0213cf41cc1c5b990930e88459386e9b12099be98cbc595a45d62d6a0630820bd7510777d3df345b99f979fcb57806f33a904cf77a4621c597e |
| SignatureAlgorithmOID             | 1.2.840.113549.1.1.11 |
| IsCertificateAuthority            | True |
| SerialNumber                      | 61077656000000000008 |
| Version                           | 3 |

{{< /details >}}
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
```
{
  "Certificates": [
    {
      "IsCertificateAuthority": false,
      "SerialNumber": "330000038db0bfe1b0ca33b3d400000000038d",
      "Signature": "7aa4402e28e909a6f7ff198a87c8f546fd868da5adf65529e8ced9b8ff16f56d03704671b64454a21437cdc6b47d83ea130e55b30ed223fda526676f6034a0d649e924cdf96d3c26386378d2ab91da329e3ddecbfe21c7f32764df6409a7f82f67c90ab5d9d7c167376487b3579fc1d99201098d2124f91f6558fb03285a49159fcc6d6ff6f8bbbc51f5209689963bebbc504c08089fa7c13e3bbae4f3c77a3a083548f8c95a1504b66fd5cfa658f9353ca231fd085e94f9bdb9bf68e302cae1bb6d483f97b5d4a2d26486fcab72ebe5fd0b555066edd3d894531f836130e309ccf4e98d1b44950efb0812a2190d4b0df3c5bf7ee8123a1d57410cd797dc0ccf",
      "SignatureAlgorithmOID": "1.2.840.113549.1.1.11",
      "Subject": "C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Windows",
      "TBS": {
        "MD5": "74a1035aa6d38ec0a7a35a6d143cc612",
        "SHA1": "62c5627f7d38759edce84eace5ae41fc7a54d6f8",
        "SHA256": "b6319137740477c564fb2beb1d50929a333f092aa362ce5129085a2c9d4bf489"
      },
      "ValidFrom": "2022-05-05 19:23:15",
      "ValidTo": "2023-05-04 19:23:15",
      "Version": 3
    },
    {
      "IsCertificateAuthority": true,
      "SerialNumber": "61077656000000000008",
      "Signature": "14fc7c7151a579c26eb2ef393ebc3c520f6e2b3f101373fea868d048a6344d8a960526ee3146906179d6ff382e456bf4c0e528b8da1d8f8adb09d71ac74c0a36666a8cec1bd70490a81817a49bb9e240323676c4c15ac6bfe404c0ea16d3acc368ef62acdd546c503058a6eb7cfe94a74e8ef4ec7c867357c2522173345af3a38a56c804da0709edf88be3cef47e8eaef0f60b8a08fb3fc91d727f53b8ebbe63e0e33d3165b081e5f2accd16a49f3da8b19bc242d090845f541dff89eaba1d47906fb0734e419f409f5fe5a12ab21191738a2128f0cede73395f3eab5c60ecdf0310a8d309e9f4f69685b67f51886647198da2b0123d812a680577bb914c627bb6c107c7ba7a8734030e4b627a99e9cafcce4a37c92da4577c1cfe3ddcb80f5afad6c4b30285023aeab3d96ee4692137de81d1f675190567d393575e291b39c8ee2de1cde445735bd0d2ce7aab1619824658d05e9d81b367af6c35f2bce53f24e235a20a7506f6185699d4782cd1051bebd088019daa10f105dfba7e2c63b7069b2321c4f9786ce2581706362b911203cca4d9f22dbaf9949d40ed1845f1ce8a5c6b3eab03d370182a0a6ae05f47d1d5630a32f2afd7361f2a705ae5425908714b57ba7e8381f0213cf41cc1c5b990930e88459386e9b12099be98cbc595a45d62d6a0630820bd7510777d3df345b99f979fcb57806f33a904cf77a4621c597e",
      "SignatureAlgorithmOID": "1.2.840.113549.1.1.11",
      "Subject": "C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Windows Production PCA 2011",
      "TBS": {
        "MD5": "30a3f0b64324ed7f465e7fc618cb69e7",
        "SHA1": "002de3561519b662c5e3f5faba1b92c403fb7c41",
        "SHA256": "4e80be107c860de896384b3eff50504dc2d76ac7151df3102a4450637a032146"
      },
      "ValidFrom": "2011-10-19 18:41:42",
      "ValidTo": "2026-10-19 18:51:42",
      "Version": 3
    }
  ],
  "CertificatesInfo": "",
  "Signer": [
    {
      "Issuer": "C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Windows Production PCA 2011",
      "SerialNumber": "330000038db0bfe1b0ca33b3d400000000038d",
      "Version": 1
    }
  ],
  "SignerInfo": ""
}
```

{{< /details >}}
-----



[*source*](https://github.com/magicsword-io/bootloaders/tree/main/yaml/a252e6fc-a0e5-46b7-ae78-c11ac44dfecc.yaml)

*last_updated:* 2023-08-31








{{< /column >}}
{{< /block >}}
