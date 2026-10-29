# -*- coding: utf-8 -*-
# 使用说明：
# 1. 把本文件复制一份，改名为 config.py
# 2. 在 config.py 里填入你的真实高德 key
# 3. config.py 已在 .gitignore 中，永远不会被提交到公开仓库
# 本文件（config.example.py）只放模板，可提交。

# 高德开放平台 Web服务 Key（个人开发者免费申请）
# 申请入口：https://lbs.amap.com/api/webservice/guide/create-project/get-key
AMAP_KEY = "在这里粘贴你的高德Key"

# 行政区划 API 参数示例
DISTRICT_KEYWORDS = "金渡镇"
DISTRICT_SUBDISTRICT = 2  # 0=不返回下级 1=返回下一级 2=返回下两级（尝试社区级）

# 数据目录
DATA_DIR = "data/raw"
