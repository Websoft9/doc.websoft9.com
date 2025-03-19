---
slug: /cli
sidebar_position: 1.2
---

# CLI

AppHub, the core microservice of Microsoft9, provides a CLI for managing applications.  

To use it, enter the Apphub container in command mode:

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