---
sidebar_position: 1
slug: /kodcloud
tags:
  - KodCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# KodCloud Getting Started

[KodCloud](https://kodcloud.com) （可道云）类似 Windows 体验的集在线文件管理、多云存储和协同办公于一体的开源系统。它界面优美和流畅，支持数百个文件格式预览，企业级的细粒度权限管控和信创认证让上云更加安全可靠。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodcloud/kodcloud-gui-websoft9.png)

If you have installed Websoft9 KodCloud, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for KodCloud
4. [Get](./user/credentials) default username and password of KodCloud


## KodCloud Initialization{#init}

### Steps for you

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）

2. 系统初始化：通过简单的 3 步，完成系统的初始化 admin 管理员用户的密码
    - 系统环境检测，选择【跳过】
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodcloud/kodcloud-install1-websoft9.png)
    
    - 数据库配置，获取[账号密码](./user/credentials)连接数据库
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodcloud/kodcloud-install2-websoft9.png)
    
    - 设置管理员账号
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodcloud/kodcloud-install3-websoft9.png)

3. 设置管理员账号后，系统转到登录界面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodcloud/kodcloud-login-websoft9.png)

4. 文件管理：登录成功，进入系统后台，默认进入【文件管理】界面，便于文件管理
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodcloud/kodcloud-file-websoft9.png)

5. 桌面管理：点击左边菜单【桌面】，进入系统桌面，常用工具放置在桌面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodcloud/kodcloud-home-websoft9.png)

6. 插件管理：点击桌面的【插件中心】，管理系统插件
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodcloud/kodcloud-plugins-websoft9.png)   

7. 系统设置：点击左下方个人图形，进入个人设置和系统设置（管理员），比如部门、成员、权限等等 
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/kodcloud/kodcloud-system-websoft9.png)


> 需要了解更多 KodCloud 的使用，请参考官方文档：[KodCloud Help](https://kodcloud.com/help/)


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## KodCloud QuickStart

下面以 **KodCloud 构建企业网盘系统** 作为一个任务，帮助用户快速入门：


## KodCloud Setup

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage KodCloud


通过运行`docker ps`，可以查看到 KodCloud 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 KodCloud 本身的参数：

### Path{#path}

KodCloud installation directory： */data/wwwroot/kodcloud*  

### Port{#port}

无特殊端口

### Version{#version}

控制台【账号信息】>【关于】中查看

### Service{#service}

```shell
sudo docker start | restart | stop | stats kodcloud
```

### CLI{#cli}

无

### API

[官方API](https://doc.kodcloud.com/v2/#/)

### 版权与限制

Kodcloud 采用 GPLV3 License，支持用户数 10 个，1个部门。  
