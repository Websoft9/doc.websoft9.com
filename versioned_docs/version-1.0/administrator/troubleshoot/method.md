---
sidebar_position: 3
slug: /troubleshoot/method
---

# 故障诊断三分法

三分法：任何软件的故障只能在**资源瓶颈、连接障碍和组件失效** 三个方面之一或组合，除此之外便没有其他。  

它对软件故障的一种归类描述，它是 Websoft9 结合运维实践与 Triz 理论后的创新认知和哲学思考。   

> 笛卡尔说：最有价值的知识是关于方法的知识。 

### 资源瓶颈

资源瓶颈主要指计算资源不足：CUP 超负荷、内存不足、硬盘空间已满、带宽太小、进程互斥、端口被占用等。

```
# 查看内存使用
free

# 查看硬盘使用
df -hl 

# 查看进程以及 CPU 使用
top

# 查看端口
netstat -tunlp
```

典型范例：  

* [MySQL 日志太大，导致磁盘空间不足？](../mysql/admin#binlogexceed)
* [端口被占用导致应用无法启动或报错？](../faq#portconflict)
* [访问量很小，但网站访问很慢？](../faq#siteslow)
* [root 账户修改文件权限，报错 "Operation not permitted"？](../faq#rootnoauth)

### 连接障碍

网络不通、访问权限不足、账号错误、黑名单问题、错误的连接对象等特征下，都是技术组件的连接问题。  

连接的双方包括：  

* 应用 连接 数据库
* 客户端 连接 服务端
* 浏览器 访问 网站

连接障碍有分为静态和动态两种：

* 静态：严格安全机制，不符合条件的连接被禁止
* 动态：连接开始可用，但外界条件发生变化，导致某种安全机制启动，连接变得不可用

诊断连接命令：  
```
# 查看端口是否开放
nmap -p 22 47.92.175.174
nmap -p 80 47.92.175.174

# 分别查看本机开放的 TCP 端口、UDP 端口
nmap -sT 127.0.0.1
nmap -sU 127.0.0.1

# DNS 诊断
dig websoft9.com

# 端到端连通诊断
ping websoft9.com

# 路由跟踪
traceroute websoft9.com

# Telnet
telnet websoft9.com 9090

# Ping 与 traceroute 组合
mtr websoft9.com
```

典型范例：  

* [无法连接 Windows 远程桌面？](../faq#notconnectwin)
* [http://服务器公网IP 无法打开初始化界面？](../faq#blank)
* [网站重定向错误导致打不开？](../faq#redirect)
* [升级或安装扩展时网络超时？](../faq#timeout)
* [Windows 容器无法访问外网？](../faq#winnonetwork)
* [连接 SFTP，出现 Disconnected...publickey](../faq#sftpnokey)
* [域名解析迟迟没有生效？](../administrator/domain_step#effect)
* [容器应用无法远程访问？](../docker/advanced#常见问题)
* [Apache mod_evasive for DDoS](https://www.howtogeek.com/devops/how-to-configure-mod_evasive-for-apache-ddos-protection/)：mod_evasive 不合理的设置会频繁导致 403 错误

### 组件失效

一个系统的子系统（或组件）失效，会导致周边依赖此系统的其他系统出现故障。  

系统（组件）的失效特征包括：不可操作、损坏、无法启动、非计划停止、锁定、商业因素（欠费）、安全事故等  

典型范例：  

* [Nginx 出现 502 错误？](../faq#nginx502)
* [Docker 容器无法启动？](../faq#containernotstart)
* [Docker service 无法启动？](../faq#dockernotstart)
