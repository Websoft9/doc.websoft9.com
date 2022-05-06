---
sidebar_position: 1
slug: /caddy
tags:
  - HTTP
  - Proxy
  - Web Server
---


# Guide

[Caddy](https://caddyserver.com/) is a powerful, enterprise-ready, open source web server with automatic HTTPS written in Go

## Tutorial

### Configure Caddy by API

Refer to: https://caddyserver.com/docs/quick-starts/api

### List directory files

```
file_server browse
```

### Reverse for Proxy

```
file_server
reverse_proxy /api/* 127.0.0.1:9005
```

## Troubleshoot{#troubleshoot}

## Parameters

### Path{#path}

Caddy configuration file：*/etc/caddy/Caddyfile*   

### CLI{#cmd}

```
$ caddy help

usage:
  caddy <command> [<args...>]

commands:
  adapt           Adapts a configuration to Caddy's native JSON
  add-package     Adds Caddy packages (EXPERIMENTAL)
  build-info      Prints information about this build
  environ         Prints the environment
  file-server     Spins up a production-ready file server
  fmt             Formats a Caddyfile
  hash-password   Hashes a password and writes base64
  help            Shows help for a Caddy subcommand
  list-modules    Lists the installed Caddy modules
  reload          Changes the config of the running Caddy instance
  remove-package  Removes Caddy packages (EXPERIMENTAL)
  reverse-proxy   A quick and production-ready reverse proxy
  run             Starts the Caddy process and blocks indefinitely
  start           Starts the Caddy process in the background and then returns
  stop            Gracefully stops a started Caddy process
  trust           Installs a CA certificate into local trust stores
  untrust         Untrusts a locally-trusted CA certificate
  upgrade         Upgrade Caddy (EXPERIMENTAL)
  validate        Tests whether a configuration file is valid
  version         Prints the version

```

### Service{#service}

```
sudo systemctl start | stop | restart | status caddy
```

### Templates{#template}

Caddy have provide [Example](https://caddy.community/c/wiki/13) for different open source software.  

Below is some template for you:  

#### Domain + php-fpm

```
domain.com {
	root * /var/www/domain.com
	encode zstd gzip
	file_server
	php_fastcgi unix//run/php/php7.4-fpm.sock
}
```

#### Domain + proxy

```
# Proxy for localhost
youdomain.example.com {
    reverse_proxy https://localhost:9090 {
        transport http {
            tls_insecure_skip_verify
        }
    }
}

# Proxy for Container
collabora.example.com {
  encode gzip

  reverse_proxy https://collabora:9980 {
    transport http {
      tls_insecure_skip_verify
    }
  }
}

```

#### IP + php-fpm Container

```
:80 {
	root * /srv/public
	encode gzip
	php_fastcgi php:9000
	file_server
}
```

#### IP + multiply port

```
:8080 {
	respond "I am 8080"
}

:8081 {
	respond "I am 8081"
}
```


