---
title: Redis
slug: /redis
tags:
  - 缓存
  - 数据库
---

import Meta from './_include/redis.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 控制台安装 Redis 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取账号信息。  

### 连接使用

有两种验证 Redis 可用性的方案：

- 进入 Redis 容器的命令行模式，运行 `redis-cli` 即进入交互式使用方式
- Websoft9 控制台安装 [Redis Insight](./redisinsight)，然后再 Redis


## 配置选项{#configs}

- 数据持久化：默认开启
- 外网访问：已经通过容器 command 中 `--bind 0.0.0.0` 开启
- [ACL](https://redis.io/topics/acl) 验证：默认开启
- [Redis API](https://docs.redis.com/latest/rs/references/rest-api/)
- [redis-cli](https://redis.io/topics/rediscli): `redis-cli help`
- 配置文件：本应用默认没有设置配置文件，而是通过应用编排文件 docker-compose.yml 中的 **command** 指令设置

## 管理维护{#administrator}

#### 重置密码

进入 Redis 容器的命令行模式，运行 `redis-cli` 即进入交互式，再运行 `CONFIG SET requirepass "newpassword"`

## 故障
