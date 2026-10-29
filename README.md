# 数据存放与下载说明

## 目录约定

```
data/
├── raw/       # 原始数据（已加入 .gitignore，本地保存）
├── interim/   # 中间处理结果（已忽略）
└── sample/    # 小体积样例（提交进仓库，供复现演示）
```

## 各类数据的下载方式

| 数据 | 下载/获取方式 | 存放位置 |
|---|---|---|
| 金渡镇边界与社区 | 运行 `scripts/01_fetch_boundary_poi.py`（需高德 key），或手动保存 GeoJSON | `data/raw/boundary/` |
| POI | 同上脚本；OSM 经 Overpass API 导出 | `data/raw/poi/` |
| OSM 路网/水系 | Geofabrik 下载广东压缩包后裁剪，或 Overpass 查询 | `data/raw/osm/` |
| 人口 | 高要区七普公报（数值整理为 CSV）；WorldPop 栅格 | `data/raw/population/` |
| CLCD 土地利用 | Zenodo 检索 "CLCD"（武汉大学，1990-2022，30m），按镇范围裁剪 | `data/raw/clcd/` |
| DEM | 地理空间数据云（gscloud.cn）SRTM 30m，注册后下载 | `data/raw/dem/` |

## 许可与合规

- **高德数据**：仅限个人学习、研究、演示使用，不得用于商业用途；成果公开时注明"数据来源：高德开放平台"。
- **OSM 数据**：© OpenStreetMap contributors，ODbL 许可，衍生成果需同样开放（本项目仅作分析底图，公开图件注明版权）。
- **CLCD**：引用论文 Yang Jie, Huang Xin. The 30 m annual land cover dataset and its dynamics in China from 1990 to 2019. *Earth System Science Data*, 2021.
- **政府内部台账数据**：**不进本仓库**。自动化脚本只公开数据结构和处理逻辑，数值用模拟数据替换（见 `scripts/toolbox/`）。
- 边界数据仅用于学习研究；涉及公开发布的地图请注意审图号要求，建议使用天地图标准底图。
