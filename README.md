# Voter-Model-Long-Range-Interactions

This repository contains simulation codes for studying the Voter model on a 2D lattice with long-range interactions. It includes tools to visualize opinion dynamics over time and observe the effects of varying the network size (N) and the proportion of long-range edges (p) on the duration of metastable states (plateaus).

## 题目描述


1. 阅读本周资料
 
2. 根据既有研究，尝试在$d=2$的格子网络上随机增加（或随机重连）比例为$p$的长程边，观察Voter模型的$n_a(t)$随时间的变化是否会出现一段相对平坦的区间（称为plateau)，此时系统处于亚稳态。请通过变化$N$和$p$来观察plateau长度的变化规律（亦即，亚稳态的持续时长）。另外，考虑到$d=2$的格子非常容易可视化(每个节点可以分配平面坐标)，请对随机的一次仿真（$N$建议大一些，$p$可以变化），观察不同$p$时，处于plateau时期的观点分布成什么形态（不同观点的节点有不同的颜色标记，可以不绘制边）
 
3. （附加）保存某次仿真的每一步可视化图片，进而合成为视频，可以观察voter模型下观点的连续演化过程
