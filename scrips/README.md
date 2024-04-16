这里是迁移脚本，脚本使用 https://github.com/axzml/CSDNExporter



```
html-parse.py: 解析 CSDN 中专栏 div 的代码，得到专栏名称和链接，并 dump 到link_map.json 文件中
dump-start.py: 负责从 link_map.json 中得到任务，去开始 dump
```