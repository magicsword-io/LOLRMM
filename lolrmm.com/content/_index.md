+++
title = "lolrmm.com"
[dataset1]
  fileLink = "content/bootloaders_table.csv"
  colors = ["#ef7f1a", "#627c62", "#11819b", "#4e1154"] # chart colors
  columnTitles = ['Tag','SHA256','Category', 'Created'] # optional if not table will be displayed from dataset
  baseChartOn = 4 # number of column the chart(s) and graph should be drawn from # can be overridden directly via shortcode parameter # it's therefore optional
  charts = ["table"]
  title = "Bootkit List"

[dataset2]
  fileLink = "content/bootloaders_top_5_os.csv"
  colors = ["#ef7f1a", "#627c62", "#11819b", "#4e1154", "#a1c9a2", "#38a9d9", "#f9b34c", "#824da4", "#e0c7c2", "#c2c2a3", "#d6a994", "#f2c057"] # chart colors
  columnTitles = ["Count", "Name"] # optional if not table will be displayed from dataset
  baseChartOn = 2 # number of column the chart(s) and graph should be drawn from # can be overridden directly via shortcode parameter # it's therefore optional
  piechart = true
  barchart = true
  title = "Top OS"

+++

{{< block "grid-3" >}}

{{< column "mt-4">}}

# lolrmm.com
lolrmm.com is a curated list of known malicious bootloaders for various operating systems. The project aims to assist security professionals in staying informed and mitigating potential threats associated with bootloaders.

{{< tip "warning" >}}
Feel free to open a [PR](https://github.com/magicsword-io/bootloaders/pulls), raise an [issue](https://github.com/magicsword-io/bootloaders/issues/new/choose "Open a Github Issue"), or suggest new bootkit(s) to be added.
{{< /tip >}}

{{< tip >}}
You can also access the malicious bootkit list via **API** using [CSV](api/bootloaders.csv) or [JSON](api/bootloaders.json). For users of security monitoring tools, check out the pre-built [configurations](https://github.com/magicsword-io/bootloaders/blob/main/detections/configs). We also provide [Sigma rules](https://github.com/magicsword-io/bootloaders/blob/main/detections/sigma) for SIEMs.  
{{< /tip >}}

{{< /column >}}

{{< column "mt-4">}}

# Top Architecture

{{% chart "dataset2" "pie" %}}

{{< /column >}}

{{< /block >}}

{{< block "grid-1" >}}
{{< column >}}
{{% chart "dataset1" "table" %}}
{{< /column >}}
{{< /block >}}
