---
sidebar_position: 2
slug: /security/advanced
---

# 进阶

## 概念与原理

### 防火墙

与Linux防火墙有关的组件有三个，它们分别是：firewalld、iptables和nftables

```
#CentOS 安装 iptables
yum install iptables -y

#CentOS 安装 firewalld
yum install firewalld -y
```

据说，从CentOS7开始，建议使用firewalld作为主要的防火墙管理工具。firewalld功能更全面，甚至支持图形化设置，`firewall-config &`

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/firewalld-gui-websoft9.png)


> 如果使用云服务器，Linux系统的防火墙的端口管理被安全组替代，只要设置好合适的安全组规则，就能很好的控制端口的访问。

### 端口

```
# 显示 tcp，udp 的端口和进程等相关情况。
netstat -tunlp
netstat -tunlp | grep 端口号

# 查看服务器 22 端口的占用情况
lsof -i:22

# kill 端口对应的进程
kill -9 PID
```

### 安全组件

服务器的安全是一个看不见但非常重要的要点。

参考阅读：[Linux 服务器的基本安全](https://sollove.com/2013/03/03/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers/)

#### Fail2ban

Fail2ban 是一个对服务器日子进行监控并采取相应的措施的安全软件。比如：它从日志中发现某个多次尝试登陆但失败的IP，此时它会将其判别为尝试攻击的IP。

#### unattended-upgrades

unattended-upgrades 是一个自动升级补丁的软件。它的工作哲学是与长期未更新的安全漏洞相比，升级的危害相对更小一点。
```
apt-get install unattended-upgrades
vim /etc/apt/apt.conf.d/10periodic
```

#### clamav 基本使用
1.更新病毒库 命令 : freshclam 2\. 扫描: 2.1 扫描所有用户的主目录就使用 clamscan -r /home 2.2 扫描您计算机上的所有文件并且显示所有的文件的扫描结果，就使用 clamscan -r / 2.3 扫描您计算机上的所有文件并且显示有问题的文件的扫描结果， 就使用 clamscan -r –bell -i /

#### LMD 基本使用

扫描:maldet –scan-all /var #扫描 /var 目录

#### rkhunter基本使用

更新:rkhunter –update

扫描恶意软件和检查系统基本安全:rkhunter –check

#### Lynix 基本使用

检测: lynix audit system -Q #检测系统安全问题 并提出一定得建议


## 问题

#### 如何判断端口是否放通？

除了检查本机防火墙和云控制台安全组之外，可以通过 **telnet** 去连接
