---
sidebar_position: 2
slug: /desktop/admin
tags:
  - Linux
  - 虚拟桌面
  - Linux 操作系统
  - GNOME
  - KDE
  - Xfce
  - Mate
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 故障处理{#troubleshoot}

#### 远程桌面时，报错：“由于安全设置错误，客户端无法连接到远程计算机...”  

原因：本地远程桌面客户端与服务端协议不匹配    
方案：[修改本地客户端协议](https://blog.csdn.net/sherlockmj/article/details/123650902)  

#### useradd 创建的用户无法远程连接？

现象：`useradd` 创建用户，然后 `passwd username` 设置密码。这样的账户无法连接服务器  
原因： useradd 主要是用于创建应用账号，不是 Linux 系统账号  
方案： 使用 `adduser` 创建

#### 不知道 VNC 的连接密码？

使用 SSH 连接到服务器后，输入如下的命令设置密码即可
```
vncpasswd
systemctl restart vnc
```

#### 登录后，不小心锁屏了怎么办？

登录密码无法解锁，只能重启服务器后再登录。建议登录桌面后，关闭锁屏功能。

以 Gnome 为例，关闭步骤：【Privacy】>【Screen Lock】，将【Automatic Screen Lock】设置为 off


## 常见问题

#### 使用秘钥对是否可以连接桌面？

不可以，请先使用 **SSH** 登录服务器后，运行 `passwd` 命令为用户设置登录密码

#### RDP 为什么比 VNC 更快？

VNC 原理：服务器端渲染图像后，再把图像传输到客户端直接显示  
RDP 原理：服务器端传送**渲染图像的指令**，再传输到客户端经过**显卡计算**后显示  

标准的服务器没有显卡（GPU），故服务器渲染图像只能使用CPU，效率非常低。同时，传输图像比传输指令耗费的带宽更大。

#### 桌面锁定状态下是否支持秘钥解锁？

不支持

#### Gnome 的开机 Logo 是否可以修改？

可以，具体参考[此处](https://www.dazhuanlan.com/2020/03/01/5e5ab2a1bd7d8/)

#### 预装的是哪个 VNC Server？

主要是 [TigerVNC](https://github.com/TigerVNC/tigervnc)

#### 是否能安装web浏览器？

可以，以安装 Google Chrome 为例：

```
# For CentOS7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum localinstall google-chrome-stable_current_x86_64.rpm
/usr/bin/google-chrome --no-sandbox

# For Ubuntu
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
vim /usr/bin/google-chrome/google-chrome
exec -a "$0" "$HERE/chrome" "$@"  修改为 exec -a "$0" "$HERE/chrome" "$@" --no-sandbox
rm -r ~/.config/google-chrome
```

## 参数

### 端口

* XRDP 连接端口： 3389
* VNC 连接端口：5901

### 服务
```
# For RDP
sudo systemctl start | stop | restart | status xrdp

# For Gnome
sudo systemctl start | stop | restart | status gdm

# For VNC
sudo systemctl start | stop | restart | status vncserver
```
