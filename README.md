# 金渡镇镇域空间数据底座与"百千万工程"典型镇体检分析

> 基于 **GIS + Python + SQL** 的镇域空间数据分析项目。以肇庆市高要区金渡镇（广东省"百千万工程"典型镇、全国综合实力千强镇）为例，构建镇域空间数据底座，完成公共服务设施可达性评估与产业/用地变化分析。

## 为什么做这个项目

金渡镇位于肇庆市高要区中部，西江穿境而过，镇域面积 101.23 km²，下辖 16 个社区，常住人口约 10 万。2024/2025 年连续入选"全国综合实力千强镇"，2024 年入选广东省第二批"百千万工程"典型镇。

作者是该镇"百千万工程"大学生志愿服务项目志愿者。在日常服务中观察到：镇域底数（设施分布、服务覆盖、用地变化）缺乏一张**可计算、可更新、可查询**的空间数据底图。本项目用公开数据回答三个问题：

1. 公共服务设施（学校/卫生院/公园）对全镇常住人口的覆盖是否充分？盲区在哪？
2. 新增一个设施放在哪里，覆盖增量最大？
3. 1990 年以来，金渡镇的建成区与农业用地发生了怎样的变化？

## 项目结构

```
jindu-town-gis/
├── README.md            # 本文件
├── LICENSE              # MIT
├── requirements.txt     # Python 依赖
├── config.example.py    # 配置模板（复制为 config.py，填入高德key，不提交）
├── data/
│   ├── README.md        # 数据下载与存放说明
│   └── sample/          # 小体积样例数据（镇界、社区点）
├── scripts/             # 按编号运行的分析脚本
│   ├── 01_fetch_boundary_poi.py
│   ├── 02_load_postgis.py
│   ├── 03_accessibility.py
│   └── 04_landcover_change.py
├── sql/                 # SQL 问题集
├── outputs/             # 本地生成，不提交
└── docs/                # 报告与图集
```

## 数据来源

| 数据 | 来源 | 说明 |
|---|---|---|
| 镇界与社区 | 高德开放平台行政区划 API（GCJ02） | 个人开发者 key，免费 |
| POI | 高德搜索 API、OpenStreetMap | 仅限个人学习研究演示 |
| 路网与水系 | OpenStreetMap | 含西江、宋隆河 |
| 人口 | 高要区第七次人口普查公报、WorldPop | 公报数值为主 |
| 土地利用 1990-2022 | 武汉大学 CLCD（Zenodo） | 30m 逐年栅格 |
| DEM | 地理空间数据云 SRTM | 免费注册 |

> 坐标系：高德 GCJ02 / OSM·遥感 WGS84 / 国土业务 CGCS2000，转换脚本见 `scripts/utils/coord_transform.py`。

## 快速复现

```bash
# 1. 环境：Python 3.10+，PostgreSQL + PostGIS，QGIS
pip install -r requirements.txt

# 2. 复制配置模板，填入自己的高德 key
cp config.example.py config.py

# 3. 按 data/README.md 下载数据并放入 data/raw/

# 4. 依次运行
python scripts/01_fetch_boundary_poi.py
python scripts/02_load_postgis.py
python scripts/03_accessibility.py
python scripts/04_landcover_change.py
```

## 主要结论

- （待补充：15 分钟生活圈覆盖率、服务盲区社区、选址建议、用地变化数据）

## 技术栈

Python · GeoPandas · Shapely · pyproj · rasterio · OSMnx · PostgreSQL/PostGIS · QGIS · Folium

## 作者
赖安珂
- 人文地理与城乡规划专业，GIS 数据分析方向求职中
- 联系方式：Lak202610@163.com（邮箱）

## 许可证

- 代码：MIT（见 LICENSE）
- 数据：各自来源保留权利，见 `data/README.md`
- 报告与图件：CC BY-NC-SA 4.0
- 
