---
slug: /cli
sidebar_position: 1.2
---

# CLI

Websoft9 的核心微服务 AppHub 提供了一个可以管理应用的 CLI。  

docker exec 到 apphub 容器，即可以使用：

```
$ docker exec -it websoft9-apphub bash
$ apphub --help

Usage: apphub [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  genkey     Generate a new API key
  getconfig  Get a config value
  getkey     Get the API key
  setconfig  Set a config value
```