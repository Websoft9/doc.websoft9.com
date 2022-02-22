---
title: Linux 桌面
sidebar_position: 1
slug: /linux/desktop
tags:
  - 可视化
  - Linux
---



# Linux 桌面

Linux 系统的桌面就是指类似 Windows 系统的图形化管理界面，一般来说 Linux 默认情况下并不会安装桌面，需要用户自主安装配置才可以使用。

> 如果你使用了 Websoft9 提供的 Linux+桌面 镜像，便可以直接使用

主流的桌面有：GNOME, KDE, Xfce, Mate 等

   * **Gnome Desktop**
   ![Gnome Desktop](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-desktop-gnome-websoft9.jpg)
   
   * **KDE Desktop**
   ![Gnome Desktop](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-desktop-kde-websoft9.jpg)

   * **Mate Desktop**
   ![Gnome Desktop](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-desktop-mate-websoft9.png)

   * **Xfce Desktop**
   ![Gnome Desktop](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-desktop-xfce-websoft9.png)

## 连接桌面

主流的 Linux 桌面连接方式有两种：

* XRDP 模式，即 Windows 远程桌面连接模式
* VNC 模式

### Windows 远程桌面（推荐）

XRDP 连接方式简单可靠，由于 Windows 系统自带的远程桌面支持 XRDP，所以连接 Linux 桌面很方便：  

1. 打开本地电脑 Windows 的远程桌面工具，输入 **服务器公网IP** 开始连接
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-remoteip-websoft9.png)
   
   > 确保云控制台中服务器安全组 3389 端口是开启状态
  
2. 如果出现下面的提示，点击【是】继续  
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-remotereminder-websoft9.png)
  
3. XRDP 对话框中，输入服务器 root 账号和密码
  ![enter image description here](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gnome/gnome-login-websoft9.png)
 
   > 建议采用普通用户登录 Linux 桌面，而不是 root 用户

4. 成功登录后，就可以看到 Linux 桌面

5. 以 Gnome 为例，打开：【Setting】>【Region&Lanuage】>【Language】设置中文（重启后生效）
  ![enter image description here](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gnome/gnome-changelanguage-websoft9.png)

### VNC

VNC 是一种老式的连接方式。我们提供的桌面进行，默认预装了 VNC Server。参考下面的步骤使用 VNC 连接桌面：  

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
   ```

## 常见问题

#### 不知道 VNC 的连接密码？

使用 SSH 连接到服务器后，输入如下的命令设置密码即可
```
vncpasswd
systemctl restart vnc
```

#### 桌面锁定状态是否支持秘钥解锁？

不支持

#### Gnome 的开机 Logo 是否可以修改？

可以，具体参考[此处](https://www.dazhuanlan.com/2020/03/01/5e5ab2a1bd7d8/)

#### 镜像中预装的是哪个 VNC Server？

主要是 [TigerVNC](https://github.com/TigerVNC/tigervnc)

#### 使用 Windows 远程桌面连接出现 "由于安全设置错误, 客户端无法连接到远程计算机.." 错误？
![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-errorsafe-websoft9.png)

解决办法：

1. 打开"本地安全策略"- Win+R 并输入 secpol.msc (或者在"管理工具"中打开)；
2. 在本地安全策略中，打开“本地策略”下的“安全选项”；
3. 在右边的策略中，找到“系统加密：将FIPS算法用于加密 、哈希和签名”点击右键属性；
4. 将“本地安全设置”设置为“已禁用”，在单击“应用”，后”确定”，即可远程控制  
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/windows/windows-remoteanquan-websoft9.png)

#### 只有秘钥对的 Linux 系统账号是否可以连接桌面？

不可以，请先使用 **SSH** 登录服务器后，运行 `passwd` 命令为 root 用户设置登录密码

#### 以 root 身份登录后，不小心锁屏了怎么办？

登录密码无法解锁，只能重启服务器后再登录。建议登录桌面后，关闭锁屏功能。

以 Gnome 为例，关闭步骤：【Privacy】>【Screen Lock】，将【Automatic Screen Lock】设置为 off
