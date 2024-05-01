---
title: RethinkDB
slug: /rethinkdb
tags:
  - RethinkDB
  - Cloud Native Database
---

import Meta from './_include/rethinkdb.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 RethinkDB 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

   - 页面上显示的用户名和密码是数据库的账号，不是控制台的账号
   - 控制台无需账号认证

2. 使用本地电脑的浏览器后，直接进入 RethinkDB 控制台
   ![](./assets/rethinkdb-gui-websoft9.png)

### Data Explorer 运行命令

大部分操作，豆可以通过控制台 Data Explorer 界面直接运行 ReQL 命令实现：

- 修改密码：
  ```
  r.db('rethinkdb').table('users').get('admin').update({password: 'newpassword'})
  ```
- 清空密码：
  ```
  r.db('rethinkdb').table('users').get('admin').update({password: 'newpassword'})
  ```
- 新增用户
  ```
   r.db('rethinkdb').table('users').insert({
      id: 'new_username',
      password: 'new_password'
   })
  ```

## 配置选项{#configs}

- 服务端命令行：`rethinkdb -h`

- 备份恢复：
  - `rethinkdb export abc.db`
  - `rethinkdb dump [options]`
  - `rethinkdb import -d [options]`

- 客户端命令行：官方未提供客户端 CLI，只提供开发包 [RethinkDB client drivers](https://rethinkdb.com/docs/install-drivers/)  
- 配置文件：
  - 通过 docker-compose.yml 文件的 command 传入个性化配置（推荐方案）
  - 容器 */etc/rethinkdb/instances.d/instance.conf* 增加配置文件 instance.conf

- 查询语言：[ReQL](https://rethinkdb.com/docs/introduction-to-reql/) 

## 管理维护{#administrator}

## 故障