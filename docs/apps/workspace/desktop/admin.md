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

# 维护参考

## 故障处理

#### 登录后，不小心锁屏了怎么办？

登录密码无法解锁，只能重启服务器后再登录。建议登录桌面后，关闭锁屏功能。

以 Gnome 为例，关闭步骤：【Privacy】>【Screen Lock】，将【Automatic Screen Lock】设置为 off


#### "由于安全设置错误, 客户端无法连接到远程计算机." ？
![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-errorsafe-websoft9.png)

解决办法：

1. 打开"本地安全策略"- Win+R 并输入 secpol.msc (或者在"管理工具"中打开)；
2. 在本地安全策略中，打开“本地策略”下的“安全选项”；
3. 在右边的策略中，找到“系统加密：将FIPS算法用于加密 、哈希和签名”点击右键属性；
4. 将“本地安全设置”设置为“已禁用”，在单击“应用”，后”确定”，即可远程控制  
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/windows/windows-remoteanquan-websoft9.png)


## 常见问题

#### 桌面锁定状态下是否支持秘钥解锁？

不支持

#### Gnome 的开机 Logo 是否可以修改？

可以，具体参考[此处](https://www.dazhuanlan.com/2020/03/01/5e5ab2a1bd7d8/)

#### 预装的是哪个 VNC Server？

主要是 [TigerVNC](https://github.com/TigerVNC/tigervnc)

## 参数

### 端口

* XRDP 连接端口： 3389
* VNC 连接端口：5901

### 服务
```
sudo systemctl start | stop | restart | status vncserver
```
