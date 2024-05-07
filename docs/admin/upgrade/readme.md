---
sidebar_position: 1
slug: /upgrade
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';

# 升级

技术日新月异，长时间不更新（升级）的程序，就如长时间不维护的建筑物一样，会加速老化、功能逐渐缺失直至无法使用。

使用 Websoft9 可能涉及到的升级包括：**Websoft9 升级、应用程序升级和操作系统更新**

## 升级目标

在做好备份后，方可开始升级：  

<DocCardList items={useCurrentSidebarCategory().items}/>

## 问题解答

#### 更新和升级有什么区别？

更新或升级这两个词有相近之处，虽然都是从低版本到高版本，但仔细体会它们也有明显的差异。

在实际升级工作中，主要存在两种形式的版本变化目标：

- **大版本变化**，例如：MySQL5.6->MySQL5.7，PHP5.6->PHP7.0  
- **小版本变化**，例如：MySQL5.6.25-->MySQL5.6.30，PHP5.6.33->PHP5.6.37

程序的大版本变化，是从功能上、架构上都有显著的改变（质变），升级过程复杂，存在升级失败的风险  
程序的小版本变化，是从补丁漏洞的角度上提供的更新内容（量变），升级过程相对简单

本文档约定：大版本变化为“**升级**”，小版本变化为“**更新**”


#### 应用升级需要额外升级环境吗？

不需要。Websoft9 提供的云原生应用，应用程序与环境封装在一个独立的容器中，升级容器即升级环境。  