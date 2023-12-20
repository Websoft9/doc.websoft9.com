---
sidebar_position: 1
slug: /xwiki
tags:
  - XWiki
  - Knowledge Management
---

# XWiki Getting Started

[XWiki](https://www.xwiki.org/xwiki/bin/view/Main/WebHome) 是一个 100% 开源的企业级 Wiki 系统，超过 600 个扩展：应用程序、宏、皮肤、插件、主题等。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-gui-websoft9.png)  

If you have installed Websoft9 XWiki, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of XWiki
4.  Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for XWiki.

## XWiki Initialization

### Steps for you

1. 本地浏览器访问:http://域名 或 http://公网IP 进入安装向导

2. Xwiki 开始初始化，耐心等待  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-initializing-websoft9.png)

3. 正式进入【安装向导】，点击【Continue】进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-wizard-websoft9.png)

4. 设置管理员用户信息，牢记账号密码
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-set-admin.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-admin-install-websoft9.png)

5. 安装可选的预制模板之一（标准版和演示版）, **此步骤不能跳过,否则无法使用**
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor1-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor2-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor3-websoft9.png)
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-flavor4-websoft9.png)

6. 预制模板安装完成后，点击【Continue】完成最后步骤
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xwiki/xwiki-install-complete-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more. 

**访问出现 502 错误？**  

主要原因是 XWiki 还未启动造成，需等待 1-2分钟再试。

## XWiki QuickStart

下面以 **使用 XWiki 构建知识管理系统** 作为一个任务，帮助用户快速入门：

## XWiki Setup


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage XWiki

通过运行`docker ps`，可以查看到 XWiki 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}

xwiki 配置文件目录: */etc/xwiki/*  
xwiki 程序目录: */usr/lib/xwiki*  
xwiki 相关插件/组件目录: */var/lib/xwiki*  
xwiki 数据库配置文件: */etc/xwiki/hibernate.cfg.xml* 

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 8080   | XWiki original port | Optional   |


### Version{#version}


### Service{#service}

```shell
```

### CLI{#cli}


### API
