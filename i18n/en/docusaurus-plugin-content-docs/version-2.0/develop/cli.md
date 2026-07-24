---
slug: /cli
sidebar_position: 1.2
---

# CLI

Websoft9 provides a command-line tool for configuration management and operations.

Enter the Websoft9 container to use it:

```
$ docker exec -it websoft9 bash
$ websoft9 --help

Usage: websoft9 [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  getconfig     Get config values
  setconfig     Set a config value
  setsysconfig  Set a system config value
  upgrade       Upgrade App Store resources
```

### Common Examples

```bash
# View all configuration
docker exec -it websoft9 websoft9 getconfig

# Sync latest App Store resources
docker exec -it websoft9 websoft9 upgrade apps

# Reset admin password (interactive prompt)
docker exec -it websoft9 websoft9 resetpwd
```