---
sidebar_position: 3
slug: /cockpit/admin
tags:
  - 故障
  - 路径
---


# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### Cockpit 配置子域访问

Cockpit 配置子目录域名有一定的特殊之处：

* [For Caddy](https://caddy.community/t/example-cockpit/8283)
* [For Nginx](https://cockpit-project.org/external/wiki/Proxying-Cockpit-over-NGINX#virtual-host-file)

1. 先修改/etc/cockpit/cockpit.conf
    ```
    [WebService]
    Origins = https://example.com wss://example.com
    AllowUnencrypted = true
    ForwardedForHeader = X-Forwarded-For
    UrlRoot=/panel
    ```

2. 然后配置 proxy 虚拟主机

    * For Caddy
    ```
    example.com {
        reverse_proxy /panel/* localhost:9090 {
            transport http {
                tls_insecure_skip_verify
            }
        }
    }
    ```
    
    * For Nginx
    
    ```
    server {
    listen         80;
    listen         443 ssl;
    server_name    example.com;

    location / {
        # Required to proxy the connection to Cockpit
        proxy_pass https://127.0.0.1:9090;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Required for web sockets to function
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        # Pass ETag header from Cockpit to clients.
        # See: https://github.com/cockpit-project/cockpit/issues/5239
        gzip off;
        };
    
        location /panel/ {
        # Required to proxy the connection to Cockpit
        proxy_pass https://127.0.0.1:9090;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Required for web sockets to function
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        # Pass ETag header from Cockpit to clients.
        # See: https://github.com/cockpit-project/cockpit/issues/5239
        gzip off;
        }
        }
    ```

## 故障排除

除以下列出的 Cockpit 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

## 问题解答

#### Cockpit 是否可以通过 http 访问？

可以，但需要在 Cockpit 配置文件中增加 `AllowUnencrypted = true`

#### 如何避免 http 访问 Cockpit 强制跳转 HTTPS？

建议采用 Nginx 转发

#### 采用 HTTPS 访问 Cockpit 后就无法用 HTTP 访问？

不是的，只需要清空浏览器缓存或重启浏览器