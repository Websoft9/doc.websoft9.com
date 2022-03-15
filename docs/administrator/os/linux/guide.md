---
sidebar_position: 5
slug: /linux
---

# 指南

## 场景

### 连接 Linux

最常见的方式是使用SSH工具连接Linux，SSH工具包括：Putty,Xshell,WinSCP等  

如果使用云服务器，云厂商一般都会提供在线的SSH工具

### 安装 FTP

安装FTP是比较繁琐的工作，具体参考：[FTP相关章节](/zh/admin-file.md#ftp)

### 初始化数据磁盘

初始化数据磁盘主要分为三个步骤：

* 磁盘分区
* 磁盘初始化
* 磁盘挂载

### 自动关机设置

需求：每天晚上20:00服务器自动关机

```
[Unit]
Description=shutdown linux service

[Service]
Type=oneshot
ExecStart=/usr/sbin/shutdown -h 20:00

[Install]
WantedBy=multi-user.target
```


### 编写 Systemd 系统服务 

服务(service) 本质就是进程，运行在后台，通常都会监听某个端口，等待其它程序的请求，比如(mysql , sshd 防火墙等)，因此我们又称为守护进程，是 Linux 中非常重要的知识点。

一般通过下面的格式来管理服务：
```
systemctl    服务名 [start | stop | restart | reload | status]
```

那服务是如何创建的呢？在Linux技术里面编写这种服务也被称之为编写Systemd 的 Unit 文件  

以 Websoft9 提供的 Redmine 自动化项目为例，下面描述完整的服务创建过程：

1. 编辑好[redmine.service](https://github.com/Websoft9/ansible-redmine/blob/master/roles/redmine/files/redmine.service)文件
   ```
   [Unit]
   Description=Redmine
   After=nginx.service
   [Service]
   Environment=RAILS_ENV=production
   Type=simple
   WorkingDirectory=/data/wwwroot/redmine
   ExecStart=/usr/local/bin/puma -b tcp://127.0.0.1:9292 -e production 
   User=redmine
   [Install]
   WantedBy=multi-user.target
   ```
   
2. 将服务文件放入路径：*/etc/systemd/system* 下

3. 启动并设置开机启动

4. 测试服务的可用性
   ···
   systemctl restart redmine
   systemctl stop redmine
   ···

附：通配符含义

| 替换符 | 含义                                                         |
| ------ | ------------------------------------------------------------ |
| "`%b`" | 系统的"Boot ID"字符串。参见 [random(4)](http://man7.org/linux/man-pages/man4/random.4.html) 手册。 |
| "`%H`" | 系统的主机名(hostname)                                       |
| "`%m`" | 系统的"Machine ID"字符串。参见 [machine-id(5)](http://www.jinbuguo.com/systemd/machine-id.html#) 手册。 |
| "`%T`" | 临时文件目录。也就是 `/tmp` 或 "`$TMPDIR`", "`$TEMP`", "`$TMP`" 之一(若已设置) |
| "`%v`" | 内核版本(**uname -r** 的输出)                                |
| "`%V`" | 存放大体积临时文件以及持久临时文件的目录。也就是 `/var/tmp` 或 "`$TMPDIR`", "`$TEMP`", "`$TMP`" 之一(若已设置) |
| "`%%`" | 百分号自身(%)。使用"%%"表示一个真正的"%"字符。               |

### 设置一次性任务

Systemd 可以用于处理开机一次性运行脚本。只需将 Tpye=oneshot 即可

```
[Unit]
Description=Switch-off Touchpad

[Service]
Type=oneshot
ExecStart=/usr/bin/touchpad-off

[Install]
WantedBy=multi-user.target
```


### 设置计划任务

Cron是一个Linux下的定时执行工具，可以在无需人工干预的情况下定时地运行任务task。

1. 安装Crontab
   ```
   yum install vixie-cron
   yum install crontabs
   ```
2. 编写计划任务脚本：可通过[在线 Crontab 生成器](https://crontab-generator.org/)，简化脚本的编写
   ```
   4 * * * * echo "hello" >/dev/null 2>&1
   ```
3. 将脚本插入Cron配置文件：*/etc/crontab*

### 临时目录清理策略

以 CentOS 为例，为  /tmp, /var/tmp 临时目录清理策略，只需修改 */usr/lib/tmpfiles.d/tmp.conf* 


### 安装配置 Desktop

阅读：[详情](./desktop/study#desktop)


### 安装配置 VNC Server

阅读：[详情](./desktop/study#vnc)

### 原生可视化 Web 面板

[Cockpit](././cockpit) 是一个基于 Web 的服务器管理工具，可用于 CentOS 和 RHEL 系统。最近发布的 CentOS 8 和 RHEL 8，其中 cockpit 是默认的服务器管理工具。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cockpit/cockpit-gui-websoft9.png)

### 分析日志

日志是诊断故障的关键，大部分的问题都会在日志中留下“蛛丝马迹”。所以，学会分析日志是运维中最重要的技能之一。  

先来一个热身，运行如下几个命令，感受日志系统的强大：  

```
# 查看 systemd 的错误日志，-p 支持 emerg alert err crit warning notice info debug 等值
journalctl -p err

# 查看指定服务的日志
journalctl -u httpd

# 查看内核日志
journalctl -k

# 查看脚本的日志
journalctl /usr/bin/bash

# 查看指定用户的日志
journalctl UID=33 --since today
```

## 参数

### 路径{#path}
### 端口{#port}
### 服务{#service}

