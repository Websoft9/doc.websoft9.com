---
sidebar_position: 1
slug: /database
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';

# 创建、连接和管理数据库

Websoft9 托管平台在设计上专注于为用户提供数据库的灵活使用和管理。不论是与应用捆绑启动的数据库，独立运行的数据库服务，还是第三方数据库实例，平台都能够提供一个集中的、[可视化的管理接口](./dbtools)。   

这样的设计使得数据库的维护和操作变得简洁而直观，无论数据库的部署形式如何，用户都能从同一平台上获得一致的管理体验。

## 指南

<DocCardList items={useCurrentSidebarCategory().items}/>

## 问题

#### 应用默认的数据库形式？

Websoft9 默认为每个应用捆绑一个包含独立配置的数据库实例，不同应用的数据库是独立运行的，应用间数据互不干扰。  
