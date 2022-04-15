---
sidebar_position: 1
slug: /typo3
tags:
  - Typo3
  - CMS
  - 站点管理
---

# 快速入门

[Typo3](https://typo3.org/) 是一个由成熟社区驱动的**企业级** CMS，充满活力的专业社区和[商业生态伙伴](https://typo3.com/partners/professional-service-listing)为企业客户提供全面的服务。TYPO3 可以轻松的与数字资产管理、电子商务、翻译服务、营销自动化、分析等无缝[集成](https://typo3.com/partners/technology-partners)。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/typo3-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 Typo3 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Typo3 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Typo3 **[域名五步设置](./administrator/domain_step)** 过程


## Typo3 初始化向导

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-installstart-websoft9.png)

   在 Typo3 的根目录下，新建一个名称为 **FIRST_INSTALL** 的空白文件

2. 系统进入环境检测步骤，通过后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty02.png)

3. 填写您的数据库参数（[查看数据库账号密码](./user/credentials)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty03.png)

4. 选择一个数据库 或 新建一个
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty04.png)

5. 设置管理员账号  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty05.png)

6. 安装完成，根据提示进入后台  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty06.png)

7. 登录后台   
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-login-websoft9.png)

8. Typo3 后台界面  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty08.png)


> 需要了解更多 Typo3 的使用，请参考官方文档：[Typo3 Documentation](https://typo3.org/help/documentation/)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## Typo3 使用入门

下面以 **使用 Typo3 构建内容管理系统** 作为一个任务，帮助用户快速入门：


## Typo3 常用操作

### 扩展管理

TYPO3 CMS 提供大量扩展，以增强系统功能。

1. 登录 Typo3后台，打开【ADMIN TOOLS】> 【Extensions】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManager-websoft9.png)

2. 顶部下拉菜单中选择【Get extensions】查看扩展
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerInstall-websoft9.png)

3. 安装、更新扩展  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerExtensionVersions-websoft9.png)

### 模板管理

TYPO3 CMS 的模板管理非常细致，能够对模板最小元素进行细微的设置

1. 登录 Typo3后台，打开【WEB】>【Template】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-template-websoft9.png)

2. 配置模板

## 参数{#parameter}

Typo3 应用中包含 PHP, Nginx, Apache, Docker, MySQL 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行`docker ps`，可以查看到 Typo3 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Typo3 本身的参数：

### 路径{#path}

TYPO3 网站目录： */data/wwwroot/typo3*  

### 端口{#port}

无特殊端口

### 网址

后端：*http://URL/typo3*  

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats typo3
```

### 命令行{#cli}

[Symfony Console Commands (cli)](https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/ApiOverview/CommandControllers/Index.html)

### API

[TYPO3 API Documentation](https://api.typo3.org/)