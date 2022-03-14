---
sidebar_position: 5
slug: /linux
---

# 指南

## 如何连接Linux？

最常见的方式是使用SSH工具连接Linux，SSH工具包括：Putty,Xshell,WinSCP等  

如果使用云服务器，云厂商一般都会提供在线的SSH工具

## 如何安装FTP？

安装FTP是比较繁琐的工作，具体参考：[FTP相关章节](/zh/admin-file.md#ftp)

## 如何初始化数据磁盘？

初始化数据磁盘主要分为三个步骤：

* 磁盘分区
* 磁盘初始化
* 磁盘挂载

## 如何写一个系统服务？

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

## 如何设置计划任务？

Cron是一个Linux下的定时执行工具，可以在无需人工干预的情况下定时地运行任务task。

1. 安装Crontab
   ```
   yum install vixie-cron
   yum install crontabs
   ```
2. 编写计划任务脚本：我们推荐一个在线的[Crontab生成器](https://crontab-generator.org/)，帮助不熟悉语法的用户简化脚本的编写
   ```
   4 * * * * echo "hello" >/dev/null 2>&1
   ```
3. 将脚本插入Cron配置文件：*/etc/crontab*

## 如何安装图形化桌面

下面针对不同Linux家族，提供安装桌面的命令

### CentOS/Oracle
```
yum groupinstall -y "GNOME Desktop" 
systemctl set-default graphical.target
systemctl set-default graphical.target
```

### OracleLinux

1. 安装,使用root用户执行

   ```bash
   yum groupinstall -y 'Server with GUI'  # 如果这一步骤有错误,先执行 yum update 更新系统
   yum install -y tigervnc-server tigervnc-server-module
   ```

2. 配置桌面

   ```
   systemctl set-default graphical.target
   systemctl isolate graphical.target
   systemctl get-default
   ```

### Ubuntu
```
待完善
```

## 如何安装VNC Server

### Centos/Oracle Linux

1. 安装VNC

   ```bash
   yum install -y tigervnc-server tigervnc-server-module
   ```

2. 配置桌面

   ```
   # vnc 设置密码
   vncserver 
   
   # 配置文件
   cat > /etc/systemd/system/vncserver@:1.service << EOF
   [Unit]
   Description=Remote desktop service (VNC)
   After=syslog.target network.target
   
   [Service]
   Type=forking
   
   ExecStartPre=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
   ExecStart=/usr/sbin/runuser -l root -c "/usr/bin/vncserver %i"
   PIDFile=/root/.vnc/%H%i.pid
   ExecStop=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
   
   [Install]
   WantedBy=multi-user.target
   EOF
   
   # 启动VNC
   systemctl enable vncserver@:1.service
   systemctl start vncserver@:1.service
   ```

## 如何实现自动交互应答？

Linux 系统中，通过安装 expect 扩展，来实现自动交互应答
```
yum install expect -y
```

下面是一个 expect 使用范例：

```
#! /usr/bin/expect
set timeout 2  # 演示2秒
spawn /mnt/ask.sh  #开始 ask.sh 文件的交互式问答
expect "name?" #应对包含 name? 的问题
send "tom\r" #回答问题
expect "old?" #应对包含 old? 的问题
send "18\r"#回答问题
expect eof #结束
```

### 弹出可视化界面如何实现自动交互应答？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-installinteract-websoft9.png)

expect 自动交互应答方案在字符交互中非常有效，但在弹出可视化界面交互中不能很好的发挥作用。这种情况下，可以通过追加`DEBIAN_FRONTEND=noninteractive`实现，下面是一个在ubuntu系统安装 kde-plasma-desktop 使用范例：

```
  - name: Install KDE Desktop
    shell: |
      sudo DEBIAN_FRONTEND=noninteractive apt install kde-plasma-desktop -y
      sduo apt remove gdm3 -y
      sudo apt remove lightdm -y
      sudo dpkg-reconfigure sddm
    when: os_desktop=="kde"
```

## 推荐可视化面板工具？


Linux命令行操作功能强大的同时，也让一些用户望而生畏。Linux面板工具可以通过Web页面，对服务器进行可视化操作，降低Linux使用门槛。

### Cockpit

Cockpit 是一个基于 Web 的服务器管理工具，可用于 CentOS 和 RHEL 系统。最近发布的 CentOS 8 和 RHEL 8，其中 cockpit 是默认的服务器管理工具。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cockpit/cockpit-gui-websoft9.png)

### Webmin

Webmin是一款开源免费的Web面板，可以对Linux进行深度操作。
登录方式：*http://公网IP地址:10000* ，登录账号为服务器账号（root/服务器密码）

出现如下错误，解决办法:

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-is-running-in-SSL-mode-websoft9.png)

安装Webmin后，在浏览器中访问Webmin控制面板时看到上述错误。错误显示您已经访问了Webmin控制面板URL，而前面没有https。
- Web服务器以SSL模式运行，因此您必须尝试使用https而不是http。尝试使用URL“ https：// IP：10000”或“ https：// serverIP：10000”，并检查是否遇到相同的错误。
- 如果问题还在，进行如下操作：
1.使用vi编辑器编辑文件/etc/webmin/miniserv.conf
2.将“ ssl = 1”行更改为“ ssl = 0”（禁用）
3.重启webmin服务 systemctl restart webmin 


更多参考[详细文档](https://libs.websoft9.com/Websoft9/documents/zh/webmin/index.html)

## 本地电脑访问服务器上的Firefox

1. 本地电脑下载[MobaXterm](https://mobaxterm.mobatek.net/)
2. 使用SSH登录到服务器后，分别安装如下组件
   ```
   yum groupinstall "X Window System" -y
   yum install dbus-x11 -y
   yum install firefox -y
   ```
3. 开启一个与 SSH客户端配套的 X11 Windows 客户端
4. 在SSH中输入命令 `firefox`
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-xwindows-websoft9.JPG)
5. 此时Firefox的图形化界面就被传输到本地
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-xwindowsfirefox-websoft9.JPG)

## 如何分析日志？

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

## 常见问题

#### 字符编码问题
Ubuntu参考：https://help.ubuntu.com/community/Locale

#### Systemd 是可以用于处理开机一次性运行脚本？

可以，将 Tpye=oneshot 即可

```
[Unit]
Description=Switch-off Touchpad

[Service]
Type=oneshot
ExecStart=/usr/bin/touchpad-off

[Install]
WantedBy=multi-user.target
```

#### 如何查询当前服务器的连接数？
```
ps aux | grep httpd | wc -l
```

#### 如何设置 /tmp, /var/tmp 目录的清理策略？

以CentOS为例，修改 */usr/lib/tmpfiles.d/tmp.conf* 即可

#### Linux 系统有哪些时间？

```
$ timedatectl status
Local time: Tue 2021-11-23 10:08:06 CST
Universal time: Tue 2021-11-23 02:08:06 UTC
RTC time: Tue 2021-11-23 10:08:04
    Time zone: Asia/Shanghai (CST, +0800)
    NTP enabled: yes
    NTP synchronized: yes
    RTC in local TZ: yes
    DST active: n/a
```

* Local time: 你自己手表上的时间
* Universal time：世界统一时间
* Real Time Clock：RTC, CMOS or BIOS clock
* System clock：系统时间，开机的时候读取 RTC 时间

NTP 是指网络时间服务，用于校对时间。 

#### Linux 系统有哪些特殊字符？

```
#   ;   ;;      .      ,       /       \       'string'|       
!   $   ${}   $?      $$   $*  "string"*     **   ?   :   
^   $#   $@    `command`{}  []   [[]]   ()    (())  ||   
&&       {xx,yy,zz,...}~   ~+   ~-    &   \<...\>   +   
-        %=   ==   != 
```