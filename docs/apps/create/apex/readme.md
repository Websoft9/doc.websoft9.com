---
sidebar_position: 100
slug: /apex
tags:
  - Web 面板
  - 可视化
  - GUI
---

# 快速入门

APEX 介绍

部署 Websoft9 提供的 APEX 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 APEX 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 APEX，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## APEX 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名:9001* 或 *http://服务器公网IP:9001*, 进入登录页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-init-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./user/credentials)），首次登陆必须修改用户密码  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-chpwd-websoft9.png)  

3. 密码修改完成后，开始体验后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-index-websoft9.png)    


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## APEX 使用入门{#quickstart}

下面以 **通过APEX创建一个基于模板数据的APP** 作为一个任务，帮助用户快速入门：

1. 完成初始化向导后，点击创建新的workspace
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-createwp-websoft9.png)

2. 输入工作区名，并创建新的schema
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-createschema-websoft9.png)

3. 输入工作区管理用户名、密码及邮件地址,点击下一步直至工作区创建成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-createuser-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-createdone-websoft9.png)

4. 注销退出，使用上步骤3设定的用户和密码登陆
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-exit-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-applogin-websoft9.png)

5. 根据模本数据创建一个APP应用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-appcreate-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-appinstall-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-template-websoft9.png)

6. 运行创建的APP，开始体验
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-runapp-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/apex/apex-appok-websoft9.png)

  > 新建的工作区才是APEX应用APP的工作区，默认internal是管理工作区

## APEX 常用操作{#guide}

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 填写 APEX 邮件相关配置

3. 测试邮件发送是否可用

### 安装插件{#plugin}

### 重置管理员密码{#resetpw}

忘记管理员密码时，请参考如下方案重置密码：  

### 域名额外配置（修改 URL）{#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需设置 APEX 的 URL:  

1. 步骤1

2. 步骤2

### HTTPS 额外设置{#https}

**[标准 HTTPS 配置](./administrator/domain_https)** 完成后，可能还需要如下步骤： 

1. 步骤1

2. 步骤2

## 参数{#parameter}

APEX 应用中包含 Docker, Oracle 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 APEX 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE                                                   COMMAND                  CREATED             STATUS                       PORTS                                                                                  NAMES
ebb93f61248b   container-registry.oracle.com/database/ords:latest      "/bin/bash -c 'echo …"   About an hour ago   Up About an hour             0.0.0.0:9001->8181/tcp, :::9001->8181/tcp                                              apex
eac8b12b397c   container-registry.oracle.com/database/express:latest   "/bin/sh -c 'exec $O…"   About an hour ago   Up About an hour (healthy)   0.0.0.0:1521->1521/tcp, :::1521->1521/tcp, 0.0.0.0:5500->5500/tcp, :::5500->5500/tcp   apex-db
```

### 路径{#path}
   
APEX 安装目录: */data/apps/apex*

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 5500   | Oracle express 的管理端口，须通过 | 可选   |

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats apex
sudo docker start | stop | restart | stats apex-db
```

### 命令行{#cli}

### API{#api}

https://apex.oracle.com/api/