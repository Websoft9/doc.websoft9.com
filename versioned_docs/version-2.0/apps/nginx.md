---
title: Nginx
slug: /nginx
tags:
  - 方向代理
  - HTTP服务器
  - 负载均衡
  - 静态网站
---

import Meta from './_include/nginx.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 提供的 Nginx 应用两个用途：

- 直接运行静态网站
- 作为反向代理服务

下面我们分别对它的使用方法做出详细的说明

### 部署静态网站

1. Websoft9 控制台安装 NGINX 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取访问信息。    

2. 参考 [基于程序环境部署应用](runtime) 部署静态网站


### 反向代理其他应用

参考下面的步骤，体验 NGINX 方向代理的能力：

1. Websoft9 控制台 "应用商店" 分别运行一个 **Netdata** 和 **Caddy**

2. 通过 "我的应用" > "NGINX" 的**编排** 标签页中修改 src/default.conf，将 **location /** 用以下的内容替换
   ```
    location / {
        proxy_pass http://netdata_h31py:19999;
        # 可选的代理设置
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
   ```

3. 重启 NGINX 应用，访问 NGINX 的 URL，就会发现应用已指向了 Netdata 的页面

在 Websoft9 托管平台中，上面的 Netdata 访问的路由： 用户 > Websoft9 网关 > NGINX > Netdata


## 配置选项{#configs}

- NGINX 应用根目录（已挂载）：*/usr/share/nginx/html*
- NGINX 配置文件（已挂载）：*/etc/nginx/conf.d/default.conf*
- NGINX 最大打开文件数：通过 */etc/security/limits.conf* 设置
- NGINX 容器端口：80
- CLI：`nginx -h`
- NGINX 配置文件[生成工具](https://www.digitalocean.com/community/tools/nginx)工具
- 伪静态规则[模板](https://github.com/Websoft9Archive/role_nginx/tree/main/files/rewrite)

## 管理维护{#administrator}

## 问题与故障

#### 为 HTML, CSS, JS 开启 Gzip？

默认情况下 Nginx 并没有开启 Gzip，需将如下代码添加到配置文件中：

```
gzip on;
gzip_types application/xml application/json text/css text/javascript application/javascript;
gzip_vary on;
gzip_comp_level 6;
gzip_min_length 500;
```