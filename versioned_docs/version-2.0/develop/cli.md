---
slug: /cli
sidebar_position: 1.2
---

# CLI

Websoft9 提供了命令行工具，用于配置管理和运维操作。  

进入 Websoft9 容器即可使用：

```
$ docker exec -it websoft9 bash
$ websoft9 --help

Usage: websoft9 [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  getconfig     获取配置项
  setconfig     设置配置项
  setsysconfig  设置系统配置项
  upgrade       升级应用商店资源
```

### 常用示例

```bash
# 查看所有配置
docker exec -it websoft9 websoft9 getconfig

# 同步应用商店最新资源
docker exec -it websoft9 websoft9 upgrade apps

# 重置管理员密码（交互式输入新密码）
docker exec -it websoft9 websoft9 resetpwd
```