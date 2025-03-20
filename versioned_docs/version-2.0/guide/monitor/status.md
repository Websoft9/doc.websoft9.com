---
sidebar_position: 1
slug: /monitor-status
---

# 应用状态监测与告警

Websoft9 从两个层面提供对应用状态的监测：

- 容器运行状态：做为应用的组成部分，容器的运行状态可很好的体现应用的健康情况
- 应用访问状态：从应用可访问、可通达的角度，监测应用的可用性，并给出实施告警

## 容器运行状态

1. 登录到 Websoft9 控制台后，通过 **我的应用** 菜单找到所需监控的应用

2. 进入 **容器** 标签页，查看所有容器的运行状态
   ![](./assets/websoft9-container-status-websoft9.png)

## 应用访问状态

Websoft9 没有单独提供应用访问的监测和告警工具，不是因为这些工具不重要，而是已经存高质量的开源软件可以完成这些任务。  

我们推荐用户通过 Websoft9 应用商店，安装 [Uptime Kuma](./uptimekuma)，然后将需监测的应用接入到此工具中，并**设置告警**策略。  

![](./assets/uptimekuma-gui-websoft9.jpg)
