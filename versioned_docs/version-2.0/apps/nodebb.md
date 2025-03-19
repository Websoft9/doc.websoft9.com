---
title: NodeBB
slug: /nodebb
tags:
  - 论坛软件
  - 社区管理
  - NodeBB
---

import Meta from './_include/nodebb.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 NodeBB 后，通过 **我的应用** 查看应用详情:

    - 在 **访问** 标签页中获取访问 URL
    - 在 **容器** 标签页中获取主容器名
    - 在 **数据库** 标签页中获取内网主机和密码

2. 本地浏览器访问 URL，根据提示填写初始化内容，其中数据库的配置如下：
   
    - **Database Type**：Postgresql
    - **Host IP or address of your PostgreSQL instance**：1中获取的内网主机
    - **Host port of your PostgreSQL instance**：5432
    - **PostgreSQL username**：nodebb
    - **Password of your PostgreSQL database**：1中获取的密码
    - **PostgreSQL database name**：nodebb
    - **Enable SSL for PostgreSQL database access**：false

3. 点击 **Install NodeBB**，等待几分钟安装完成即可使用



## 配置选项{#configs}

## 管理维护{#administrator}

## 故障