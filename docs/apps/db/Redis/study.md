---
sidebar_position: 3
slug: /redis/study
tags:
  - Redis
  - Cloud Native Database
---

# 原理学习

## Redis CLI

### 关于

[redis-cli](https://redis.io/topics/rediscli) 是 Redis 命令行界面，这是一个简单的程序，可以将命令直接发送到 Redis，并直接从终端读取服务器发送的回复。

Redis CLI 支持交互式模式和标准命令行两种使用方式：

```
# 交互式模式（无密码验证），即进入 CLI 的随时待命状态
redis-cli
127.0.0.1:6379>

# 交互式模式（密码验证），即进入 CLI 的随时待命状态
redis-cli -h 127.0.0.1 -p 6379 -a 123456
127.0.0.1:6379>

# 标准命令行模式，即运行一条有明确目标的命令，执行完成后自动退出
redis-cli help
redis-cli incr mycounter
redis-cli --stat
redis-cli --bigkeys
```

### 使用

常用命令包括：

| **Command** | **Description** |
| --- | --- |
| redis-benchmark | Performance test |
| SAVE | Backup Data |
| CONFIG GET dir | Restore Data |
| INFO | Manage Redis services |