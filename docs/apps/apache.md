---
title: Apache
slug: /apache
tags:
  - HTTP 服务器
  - https
  - 微服务
  - 云原生
---

import Meta from './_include/apache.md';

<Meta name="meta" />

## 入门指南{#guide}

Websoft9 提供的 Apache 应用两个用途：

- 直接运行静态网站
- 作为反向代理服务（不推荐使用 Apache 反向代理）

Apache 容器中不包含 PHP，如果想部署 PHP 网站，通过 Websoft9 控制台运行 [PHP](./php) 容器。  

### 部署静态网站

1. Websoft9 控制台安装 Apache 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取访问信息

2. 点击访问地址，可看到一个用于演示的静态页面

3. 参考 [基于程序环境部署应用](./runtime) 部署静态网站


### 挂载 httpd.conf 配置文件

虽然 Apache 配置文件可以通过 `sed` 命令修改，但建议挂载到容器外进行设置：

1. 进入 Apache 容器，拷贝 */usr/local/apache2/conf/httpd.conf* 文件的内容

2. 通过 **我的应用 > Apache 应用 > 编排 > 马上修改**，进入应用的 Git 仓库

3. 将拷贝的 httpd.conf 内容粘贴到 *./src/httpd.conf* 中，再修改 **docker-compose.yml** 挂载设置

4. 重建容器后生效

### 设置伪静态

使用和设置 Apache 伪静态有三个步骤：

- 确保已经安装并启用 Rewirte 模块
- Apache 配置文件中增加 AllowOverride All
- 网站根目录 .htaccess文件中配置伪静态规则

### 并发连接设置

配置文件中如下内容可作为并发连接相关设置：

```
<IfModule prefork.c>
   StartServers        5
   MinSpareServers     5
   MaxSpareServers     10
   MaxClients          256
   MaxRequestsPerChild 3000
</IfModule>
```

## 配置选项{#configs}

- Apache 容器端口：80
- CLI：`httpd -h`
- Apache [官方文档](https://httpd.apache.org/docs/2.4/)
- Apache [容器使用指南](https://hub.docker.com/_/httpd)
- Apache 配置文件：*/usr/local/apache2/conf/httpd.conf*

## 管理维护{#administrator}

## 故障

#### You don't have permission...?

错误详情：You don't have permission to access/on this server  
解决办法：

1.  检查网站目录的权限
2.  检查 Apache 配置文件是否有 **AllowOverride All   Require all granted** 相关内容

#### Apache 频繁 403 错误？

403错误是一种在网站访问过程中的错误提示，表示禁止访问或拒绝服务。出现403错误，情况有两种：

- 服务器被动的受到人为饱和的DoS或DDoS恶意攻击，导致服务器无法提供正常的服务
- 服务器的主动防御措施（Apache 的 mod_evasive 模块），当某个 IP 短时间连续向服务器发送请求，服务器启动DoS防御策略，利用预设的规则主动拒绝向某个IP提服务
