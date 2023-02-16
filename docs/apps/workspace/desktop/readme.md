---
sidebar_position: 1
slug: /desktop
tags:
  - Linux
  - 虚拟桌面
  - Linux 操作系统
  - GNOME
  - KDE
  - Xfce
  - Mate
---

# 快速入门

原生桌面指的除预装桌面之外，没有安装其他软件的原生操作系统。  

Windows 桌面风格统一，而 [Linux 桌面](./desktop/study#desktoplist)会根据不同的发行版而产生差异。

## 场景

### 连接 Windows 桌面

Windows 10, Windows 11 等桌面连接参考相关章节：[连接 Windows](./user/cloud#connectwindows)

### 连接 Linux 桌面

连接 Linux 桌面主要有两种方式：XRDP 和 VNC 模式，推荐使用 XRDP（[Why?](https://cloudzy.com/rdp-vs-vnc-remote-desktop-comparison/)）

|         | 速度 | 实现原理     | 多用户           | 平台                           | 安全协议   |
| ------- | ---- | ------------ | ---------------- | ------------------------------ | ---------- |
| **RDP** | 快 | 计算资源共享 | 继承操作系统用户 | Linux, Windows, macOS, Android | SSL/TLS    |
| **VNC** | 慢 | 屏幕贡献     | 没有用户         | Linux, Windows, macOS          | SSH tunnel |

#### XRDP 连接

Windows 本地电脑自带的远程桌面客户后端支持 XRDP，所以连接桌面很方便  

1. 打开 开始菜单，输入”mstsc“ ，系统会搜索远程桌面连接工具  

2. 输入 **服务器公网IP** ，点击【连接】  
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-remoteip-websoft9.png)
   
   > 确保云控制台中服务器安全组 3389 端口是开启状态
  
3. 如果出现下面的提示，点击【是】继续  
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-remotereminder-websoft9.png)
  
4. XRDP 对话框中，输入服务器 root 账号和密码
  ![enter image description here](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gnome/gnome-login-websoft9.png)
 
   > 建议采用普通用户登录 Linux 桌面，而不是 root 用户。请参照下面命令创建普通用户：
    ```
    sudo su 
    adduser xxxuser # 根据提示完成密码设置
    ```

5. 成功登录后，就可以看到 Linux 桌面

6. 以 Gnome 为例，打开：【Setting】>【Region&Lanuage】>【Language】设置中文（重启后生效）
  ![enter image description here](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gnome/gnome-changelanguage-websoft9.png)

#### VNC 连接

VNC 是一种传统的连接 Linux 服务器桌面的方式：  

1. 使用 SSH 登录服务器，设置你的 VNC访 问密码
    ```
    sudo su
    rm -rf /root/.vnc/passwd
    vncpasswd
    ```
2. 本地电脑安装 [VNC viewer](https://www.realvnc.com/download/viewer/) 客户端

3. 登录云服务器控制台，为你的云服务器安全组中开启 **5901** 端口

4. 本地电脑打开 VNC 客户端，创建一个VNC连接（服务器公网IP地址：5901）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-connection001-websoft9.png)

5. 点击【Continue】进入下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-connection002-websoft9.png)

6. 输入VNC密码后登录即可进入图形化界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-connection003-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-setlanguage-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-startuse-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-gnomehome-websoft9.png)

7. 如果服务器处于下图所示的锁定状态，请输入你的**服务器的密码**进行解锁
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-connection-rootlogin-websoft9.png)


8. VCN 使用过程中可参考如下命令进行维护  
   ```
   # 查看已经运行的桌面编号
   vncserver -list

   # 终止2号桌面进程
   kill -9 :1

   # 管理桌面服务
   systemctl start vncserver@:1.service
   systemctl stop vncserver@:1.service
   systemctl status vncserver@:1.service
   systemctl restart vncserver@:1.service
   `

## 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考  **[故障排除](./desktop/admin#troubleshoot)** 章节。