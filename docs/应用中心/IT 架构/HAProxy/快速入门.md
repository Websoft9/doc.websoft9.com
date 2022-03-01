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

在云服务器上部署 HAProxy 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:1080** 端口是否开启
3. 若想用域名访问 HAProxy，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `cat /credentials/password.txt` 命令，可以查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### HAProxy

* 管理员账号：*`admin`*
* 管理员密码：存储在您的服务器指定文件中（ */credentials/password.txt* ）

## HAProxy 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名:1080/haproxy* 或 *http://Internet IP:1080/haproxy*, 提示需要登录

2. 输入账号密码（[不知道账号密码？](#账号密码)），成功登录到 Haproxy Statistics Report 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/haproxy/haproxy-statsgui-websoft9.png)

3. 如需修改登录密码，请编辑HAProxy配置文件 */etc/haproxy/haproxy.cfg* 相关字段
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

> 需要了解更多 HAProxy 的使用，请参考官方文档：[HAProxy Documentation](http://cbonte.github.io/haproxy-dconv/)


## HAProxy 入门向导

Coming soon...


## 常用操作

### 开启监控

使用[Websoft9](https://www.websoft9.com)提供的HAProxy部署方案，默认已经设置HAProxy Statistics Report，只需直接访问即可：*http://服务器公网IP:1080/haproxy*

### 开启HAProxy日志

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

## 异常处理

#### 浏览器打开IP地址，无法访问 HAProxy（白屏没有结果）？

您的服务器对应的安全组1080端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### HAProxy 服务启动失败？

暂无

