---
sidebar_position: 3
slug: /desktop/study
tags:
  - Linux
  - 虚拟桌面
  - Linux 操作系统
  - GNOME
  - KDE
  - Xfce
  - Mate
---

# 原理学习

## 安装配置桌面{#desktop}

一般来说 Linux 默认情况下并自带安装桌面，需要用户自主安装配置才可以使用。

> 如果你使用了 Websoft9 提供的 Linux 原生桌面镜像，便可以直接使用

```
#  CentOS
yum groupinstall -y "GNOME Desktop" 
systemctl set-default graphical.target
systemctl set-default graphical.target

# OracleLinux
yum groupinstall -y 'Server with GUI'  # 如果这一步骤有错误,先执行 yum update 更新系统
yum install -y tigervnc-server tigervnc-server-module
systemctl set-default graphical.target
systemctl isolate graphical.target
systemctl get-default
```

## 安装配置 VNC Server{#vnc}

以 CentOS 为例（同样适用于 OracleLinux）介绍 VNC Server 安装详细流程：  

1. 安装 VNC Server

   ```bash
   yum install -y tigervnc-server tigervnc-server-module
   ```

2. 设置 VNC 密码

   ```
   # vnc 设置密码
   vncserver 
   ```

3. 增加 VNC Server 服务
   ```
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
   ```

4. 启动服务
   ```
   systemctl enable vncserver@:1.service
   systemctl start vncserver@:1.service
   ```


