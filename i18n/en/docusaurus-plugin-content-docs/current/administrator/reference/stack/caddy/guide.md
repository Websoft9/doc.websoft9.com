---
sidebar_position: 1
slug: /caddy
tags:
  - Caddy
  - Web 服务器
---


# 指南

Caddy是一款基于 Go 语言编写的强大且可扩展的平台，可以给你的站点、服务和应用程序提供服务。

## 场景

### 使用 API 配置 Caddy

参考官方文档：https://caddyserver.com/docs/quick-starts/api

### 列出目录文件

```
file_server browse
```

### 指定反代目录

在实践中，我们可能只想对 API 请求使用反向代理，即基本路径为/api/

```
file_server
reverse_proxy /api/* 127.0.0.1:9005
```


## 参数

### 路径{#path}

Caddy 配置文件：*/etc/caddy/Caddyfile*  

### 命令行{#cmd}

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

### 服务{#service}

```
sudo systemctl start | stop | restart | status caddy
```

### 模板{#template}

Caddy 官方提供了[丰富的模板](https://caddy.community/c/wiki/13)供用户参考、学习和讨论。  

这里列出几种典型的应用场景：

#### 域名 + 本地 php-fpm

```
domain.com {
	root * /var/www/domain.com
	encode zstd gzip
	file_server
	php_fastcgi unix//run/php/php7.4-fpm.sock
}
```

#### 域名 + 代理

```
# 代理到本机
youdomain.example.com {
    reverse_proxy https://localhost:9090 {
        transport http {
            tls_insecure_skip_verify
        }
    }
}

# 代理到容器
collabora.example.com {
  encode gzip

  reverse_proxy https://collabora:9980 {
    transport http {
      tls_insecure_skip_verify
    }
  }
}

```

#### IP + php-fpm 容器

```
:80 {
	root * /srv/public
	encode gzip
	php_fastcgi php:9000
	file_server
}
```

#### IP + 多端口访问

```
:8080 {
	respond "I am 8080"
}

:8081 {
	respond "I am 8081"
}
```


