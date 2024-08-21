---
sidebar_position: 4
slug: /troubleshoot/tree
---

# 故障树分析法

故障树分析法（Fault Tree Analysis, FTA）是一种系统化的方法，用于分析和识别导致系统故障的潜在原因。它通过图形化的方式展示各种可能的故障路径，帮助工程师和管理人员理解和解决复杂系统中的问题。  

以故障树分析法为模型，Websoft9 在实践中托管维护的问题的基本事件（Basic Events）主要为：**资源瓶颈、连接障碍和组件失效**  

同一个基本事件，解决方案具有高度一致性。  

#### 资源瓶颈

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

* [MySQL 日志太大，导致磁盘空间不足？](../mysql#binlogexceed)
* [Websoft9 默认端口被占用？](../faq#portconflict)
* [访问量很小，但网站访问很慢？](../faq#siteslow)

#### 连接障碍

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

* [无法访问 Websoft9 控制台？](../faq#blank)
* [应用网络超时？](../../faq#timeout)
* [连接 SFTP，出现 Disconnected...publickey](../servers#sftpnokey)
* [域名解析迟迟没有生效？](../domain-prepare#effect)

#### 组件失效

一个系统的子系统（或组件）失效，会导致周边依赖此系统的其他系统出现故障。  

系统（组件）的失效特征包括：不可操作、损坏、无法启动、非计划停止、锁定、商业因素（欠费）、安全事故等  

典型范例： 

* [访问应用 出现 502 错误？](../faq#nginx502)
