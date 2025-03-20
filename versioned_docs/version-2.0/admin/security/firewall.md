---
sidebar_position: 7
slug: /security-firewall
---

# 防火墙与安全组

## 关于防火墙

在 Linux 中，防火墙是以一个守护进程的方式存在，服务的名字是 firewalld ，它能够定义一组规则来控制外部传入系统中的网络访问。  

虽然与 Linux 防火墙流行的工具有：[firewalld](https://firewalld.org/)、iptables 和 nftables，但 firewalld 功能最为强大。  

## 安全组设置{#security}

但是为了简化安全使用，云平台通过一个可视化的管理界面--**安全组**，来实现与防火墙的同等功能。  

所以，一般使用云服务器的时候会关闭防火墙，用安全组替代它。

安全组配置最常见的操作就是开启某一个端口，比如：TCP:80，详细设置参考：    

* [Azure 安全组设置](./iaas-azure#security-group)
* [AWS 安全组设置](./iaas-aws#security-group)
* [阿里云 安全组设置](./iaas-alibabacloud#security-group)
* [腾讯云 安全组设置](./iaas-tencentcloud#security-group)
* [华为云 安全组设置](./iaas-huaweicloud#security-group)

## 问题解答

#### 如何判断已有服务的端口是否开放？

云控制台安全组可以查看所有端口的开放情况。  

但是，登录云控制台查看会有一定的不便。针对**已经存在服务**的端口，可以通过 **nc** 或 **telnet** 去测试端口：

* 使用 nc 命令测试

    ```
    # 成功
    $ nc -zvw10 8.142.3.195 22
    Connection to 8.142.3.195 22 port [tcp/*] succeeded!

    # 失败
    $ nc -zvw10 8.142.3.195 9091
    nc: connect to 8.142.3.195 port 9093 (tcp) failed: Connection refused

    ```


* 使用 telnet 命令测试

    ```
    # 成功
    $ telnet 8.142.3.195 22
    Trying 8.142.3.195...
    Connected to 8.142.3.195.
    Escape character is '^]'.

    # 失败
    $ telnet 8.142.3.195 9091
    Trying 8.142.3.195...
    telnet: Unable to connect to remote host: Connection refused
    ```
