+++
title = "LOLRMM"
[dataset1]
  fileLink = "content/rmm_tools_table.csv"
  colors = ["#ef7f1a", "#627c62", "#11819b", "#4e1154"]
  columnTitles = ['Name', 'Category', 'Description', 'Author']
  baseChartOn = 4
  charts = ["table"]
  title = "RMM Tools List"
+++

{{< block "grid-2" >}}
{{< column >}}

# LOLRMM (Living Off the Land Remote Monitoring and Management)

LOLRMM is a curated list of Remote Monitoring and Management (RMM) tools that could potentially be abused by threat actors. This project aims to assist security professionals in staying informed about these tools and their potential for misuse.

{{< tip "warning" >}}
Feel free to open a [PR](https://github.com/magicsword-io/lolrmm/pulls), raise an [issue](https://github.com/magicsword-io/lolrmm/issues/new/choose "Open a Github Issue"), or suggest new RMM tools to be added.
{{< /tip >}}

{{< tip >}}
You can also access the RMM tools list via **API** using [CSV](api/rmm_tools.csv) or [JSON](api/rmm_tools.json). For users of security monitoring tools, check out the pre-built [configurations](https://github.com/magicsword-io/lolrmm/blob/main/detections/configs). We also provide [Sigma rules](https://github.com/magicsword-io/lolrmm/blob/main/detections/sigma) for SIEMs.  
{{< /tip >}}

{{< /column >}}
{{< /block >}}

{{< block "grid-1" >}}
{{< column >}}

## RMM Tools List

{{% chart "dataset1" "table" %}}

{{< /column >}}
{{< /block >}}