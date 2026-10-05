# data-analysis-learning

数据分析技能补强 · 每日练习记录（12 天计划：2026-09-30 ~ 2026-10-11）

技术栈：Python · pandas · matplotlib · pyecharts · MySQL

## 学习路线

**第 1 周：pandas + 可视化**

- Day 01-02：pandas 基础（DataFrame、筛选、排序）
- Day 03-04：groupby 聚合、merge 合并、数据清洗
- Day 05-06：matplotlib 常用图表（折线/柱状/饼图/直方图）
- Day 07：pyecharts 交互式图表

**第 2 周：统计思维 + Excel + 综合演练**

- Day 08-09：描述统计、业务指标（PV/UV、转化率、复购率）
- Day 10：假设检验、AB 测试入门
- Day 11：Excel 透视表与常用函数
- Day 12：淘宝用户行为数据集综合演练（项目一热身）

## 目录结构

```
data-analysis-learning/
├── day01-pandas基础/      # 每天一个文件夹：代码 + 笔记
├── day03-groupby聚合/
├── ...
├── data/                  # 数据集（不入库，见下方下载说明）
├── output/                # 练习产出的图表
├── requirements.txt       # 依赖清单
└── README.md
```

## 环境准备

```powershell
pip install -r requirements.txt
```

## 每日提交（留痕）

```powershell
git add .
git commit -m "dayXX: 今天完成的内容"
git push
```

## 数据集说明

- Day 01-07：练习代码内置迷你数据，或用 seaborn 自带数据集（tips、titanic）
- Day 12：淘宝用户行为数据集（天池 / 和鲸社区搜索"淘宝用户行为数据集"下载，放入 `data/` 目录）
