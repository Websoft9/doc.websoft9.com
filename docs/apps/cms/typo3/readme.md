---
sidebar_position: 1
slug: /typo3
tags:
  - Typo3
  - CMS
  - 站点管理
---

# 快速入门

[Typo3](https://typo3.org/) 是一个具有大型全球社区的开源企业内容管理系统，由TYPO3协会的大约900名成员支持,TYPO3被许多知名公司和组织使用。


部署 Websoft9 提供的 Typo3 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Typo3 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  Typo3 **[域名五步设置](./dns#domain)** 过程


## Typo3 初始化向导

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-installstart-websoft9.png)

   在 Typo3 的根目录下，新建一个名称为 **FIRST_INSTALL** 的空白文件

2. 系统进入环境检测步骤，通过后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty02.png)

3. 填写您的数据库参数（[查看数据库账号密码](./setup/credentials#getpw)）
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

### 配置 SMTP{#smtp}

### 配置域名{#dns}

参考： **[域名五步设置](./dns#domain)** 

### 配置 HTTPS{#https}

参考： **[HTTPS 配置](./dns#https)**

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

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 Typo3 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 Typo3 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Typo3 本身的参数：

### 路径{#path}

TYPO3 网站目录： */data/wwwroot/typo3*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | Typo3 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell
```

### 命令行{#cli}

### API

### 参考{#ref}

 [《PHP运行环境》](./runtime/php) 
