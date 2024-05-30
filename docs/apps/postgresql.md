---
title: PostgreSQL
slug: /postgresql
tags:
  - 数据库
  - 关系型
  - SQL
---

import Meta from './_include/postgresql.md';

<Meta name="meta" />

## 入门指南{#guide}

### 连接数据库

1. Websoft9 控制台安装 PostgreSQL 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取用户名和密码

2. 进入 PostgreSQL 容器的命令模式，使用 psql 连接数据库

    ```
    # 测试基于 host 访问（需密码）
    $ psql -h postgres -U postgres
    Password for user postgres: 
    psql (15.6 (Debian 15.6-1.pgdg120+2))
    Type "help" for help.

    postgres=# 

    # 测试本地 local 访问（无需密码）
    psql -d postgres -U postgres
    ```

### 常用 SQL 语句

```
# 修改密码
ALTER USER postgres WITH PASSWORD 'postgres'
```

### 图形化工具{#pgadmin}

参考：[pgAdmin](./pgadmin)

### 远程访问

#### 端口映射访问

PostgreSQL 应用默认已经映射到宿主机外网端口，只需要确保安全组放通对应的端口即可。  

#### 转发桥接访问

如果 PostgreSQL 容器端口没有映射到宿主机，可以通过 Websoft9 网关的 **Streams** 转发模式桥接访问，但需确保：

1. postgresql.conf 配置项 `listen_addresses = '*'`
2. pg_hba.conf 配置项 `host    all             all             0.0.0.0/0            md5`

## 配置选项{#configs}

- 默认用户：PostgreSQL 本身并没有固定的管理员账号，但 Websoft9 设置 `postgres` 作为默认账号名称
- 客户端：psql, clusterdb, pgAdmin 等
- 服务端：initdb, pg_ctl, postgres, postmaster, pg_upgrade 等
- [四种连接方式](https://www.cnblogs.com/flying-tiger/p/5983588.html?tdsourcetag=s_pcqq_aiomsg)：local, host, hostssl, hostnossl
- [认证方式](https://www.postgresql.org/docs/current/auth-methods.html)：reject, md5, password, trust, peer, scram-sha-256
- 配置文件（已挂载）：
  - /var/lib/postgresql/data/postgresql.conf
  - /var/lib/postgresql/data/pg_hba.conf
- 命令行：`psql`
- [API](https://www.postgresql.org/about/news/postgresql-restful-api-1616/)

## 管理维护{#administrator}

- **重置密码**：在容器命令模式下，使用 `psql -d postgres -U postgres` 无需验证下登录，再运行 SQL 修改密码的语句

## 故障