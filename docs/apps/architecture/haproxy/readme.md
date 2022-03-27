---
sidebar_position: 1
slug: /haproxy
tags:
  - HAProxy
  - IT 架构
  - 中间件
---

# 快速入门

[HAProxy](https://www.haproxy.org/) 是一个使用C语言编写的自由及开放源代码软件，其提供高可用性、负载均衡，以及基于 TCP 和 HTTP 的应用程序代理。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/haproxy/HAProxy-configuration.png)

部署 Websoft9 提供的 HAProxy 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:1080** 端口已经开启
3. 在服务器中查看 Jenkins 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  Jenkins，务必先完成 **[域名五步设置](./dns#domain)** 过程

## HAProxy 初始化向导

### 详细步骤

1. 本地电脑浏览器访问网址：*http://域名:1080/haproxy* 或 *http://服务器公网IP:1080/haproxy*, 提示需要登录

2. 输入账号密码（[不知道账号密码？](./setup/credentials#getpw)），成功登录到 Haproxy Statistics Report 后台  

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/haproxy/haproxy-statsgui-websoft9.png)


> 需要了解更多 HAProxy 的使用，请参考官方文档：

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## HAProxy 使用入门

参考 [HAProxy Documentation](http://cbonte.github.io/haproxy-dconv/) 或以 **xxx** 作为一个任务，帮助用户快速入门：

## HAProxy 常用操作

### 修改管理员密码

如需修改登录密码，请编辑 HAProxy 配置文件 */etc/haproxy/haproxy.cfg* 相关字段

   ```
   listen admin_stats 
    bind *:1080 
    mode http 
    maxconn 10 
    stats refresh 10s 
    stats uri /haproxy 
    stats realm Haproxy 
    stats auth admin:admin 
    stats hide-version 
    stats admin if TRUE
   ```


### 开启 HAProxy 监控

默认已经设置 HAProxy Statistics Report，访问：*http://服务器公网IP:1080/haproxy*

### 开启 HAProxy 日志

默认已经开启，查看 `/etc/rsyslog.conf` 配置文件了解详情

### 高可用性

通过部署 Keepalived 实现 HAProxy的高可用性

### 集群配置

只需在配置文件中添加需要管理的集群服务器信息即可启用HAProxy集群，范例如下：

```
# [HTTP Site Configuration]
listen  http_web 192.168.10.10:80
        mode http
        balance roundrobin  # Load Balancing algorithm
        option httpchk
        option forwardfor
        server server1 192.168.10.100:80 weight 1 maxconn 512 check
        server server2 192.168.10.101:80 weight 1 maxconn 512 check

# [HTTPS Site Configuration]
listen  https_web 192.168.10.10:443
        mode tcp
        balance source# Load Balancing algorithm
        reqadd X-Forwarded-Proto: http
        server server1 192.168.10.100:443 weight 1 maxconn 512 check
        server server2 192.168.10.101:443 weight 1 maxconn 512 check
```

## 参数

**[通用参数表](../setup/parameter)** 中可查看 Docker 等 HAProxy 应用中包含的基础架构组件路径、版本、端口等参数。 


下面仅列出 HAProxy 本身的参数：

### 路径{#path}

HAProxy 配置文件： */etc/haproxy/haproxy.cfg*    
HAProxy 日志目录： */var/log/haproxy.log*   

### 网址

HAProxy Statistics Report：*http://URL:端口/haproxy*  
HAProxy：*http://URL:端口/haproxy*  

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 1080   | 通过 HTTP 访问 HAProxy  Statistics Report | 可选   |
| 5000   | for  HAProx | 可选   |

### 版本

```shell
haproxy -v
```

### 服务

```shell
sudo systemctl start | stop | restart | status haproxy
```

### 命令行

HAProxy 提供了强大的的命令行工具 `haproxy`  

```
Usage : haproxy [-f <cfgfile>]* [ -vdVD ] [ -n <maxconn> ] [ -N <maxpconn> ]
        [ -p <pidfile> ] [ -m <max megs> ] [ -C <dir> ]
        -v displays version ; -vv shows known build options.
        -d enters debug mode ; -db only disables background mode.
        -dM[<byte>] poisons memory with <byte> (defaults to 0x50)
        -V enters verbose mode (disables quiet mode)
        -D goes daemon ; -C changes to <dir> before loading files.
        -q quiet mode : don't display messages
        -c check mode : only check config files and exit
        -n sets the maximum total # of connections (2000)
        -m limits the usable amount of memory (in MB)
        -N sets the default, per-proxy maximum # of connections (2000)
        -L set local peer name (default to hostname)
        -p writes pids of all children to this file
        -de disables epoll() usage even when available
        -dp disables poll() usage even when available
        -dS disables splice usage (broken on old kernels)
        -dG disables getaddrinfo() usage
        -dV disables SSL verify on servers side
        -sf/-st [pid ]* finishes/terminates old pids. Must be last arguments.
```


### API

[HAProxy APIS](https://www.haproxy.com/blog/haproxy-apis/)


