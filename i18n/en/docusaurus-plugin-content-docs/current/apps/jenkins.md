---
title: Jenkins
slug: /jenkins
tags:
  - DevOps
  - CI/CD
  - 自动化
  - 持续集成
---

import Meta from './_include/jenkins.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Jenkins 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 使用本地电脑浏览器访问，进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-installstart-websoft9.png)

2. 根据提示到容器中获取密码

3. 成功登录到 Jenkins 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-installcustomer-websoft9.png)

4. 通过 Jenkins 后台，安装所需的插件  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-installing-websoft9.png)

5. 插件安装完成后，创建更多管理员用户  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-installusers-websoft9.png)


### Github + Jenkins 自动构建

下面以 **Github 上的项目通过 Jenkins 自动构建部署** 作为一个任务，帮助用户快速入门：

1. 在 GitHub设置 Personal access tokens，用于 Jenkins 连接
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard2-websoft9.png)

2. Jenkins全局系统设置中，连接 GitHub
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard3-websoft9.png)
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard4-websoft9.png)
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard5-websoft9.png)

3. 创建一个构建任务：输入任务名，按流程分别输入 Github项目 URL，账号密码等信息
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard6-websoft9.png)
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard7-websoft9.png)
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard8-websoft9.png)
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard9-websoft9.png)
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard10-websoft9.png)
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard11-websoft9.png)

4. 在对应Github 项目修改后，push提交；Jenkins完成自动化构建部署
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-wizard12-websoft9.png)

### 安装插件{#installplugin}

登录 Jenkins，依次打开：【【Manage Jenkins】>【Plugins Manager】

  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins_installemailplugin-websoft9.png)

## 配置选项{#configs}

- [多语言]((https://www.jenkins.io/doc/book/using/using-local-language/))（✅）
- SMTP：先安装 Jenkins 邮箱扩展插件 [Email Extension](https://plugins.jenkins.io/email-ext/)，然后【Manage Jenkins】>【Configure System】
- [Jenkins CLI](https://www.jenkins.io/zh/doc/book/managing/cli/) 
   ```
   java -jar jenkins-cli.jar [-s JENKINS_URL] [global options...] command [command options...] [arguments...]
   ```
- [REST API](https://www.jenkins.io/doc/book/using/remote-access-api/) 
   ```
   curl JENKINS_URL/job/JOB_NAME/buildWithParameters --user USER:TOKEN --data id=123 --data verbosity=high
   ```
- [插件](../jenkins#installplugin)

## 管理维护{#administrator}

### 备份与恢复

[Backup plugin](https://plugins.jenkins.io/backup/) 提供对 Jenkins 的备份和恢复功能。  

### 在线升级

Jenkins 内置升级功能，操作简单：

1. 登陆Jenkins后台，如果当前版本不是最新的稳定版本，会在右上角警告栏出现提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-warning-websoft9.png)

2. 点击警告，在弹出页面选择自动升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-selectauto-websoft9.png)

3. 在升级页面等待直到自动升级完成
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-autoupdate-websoft9.png)

4. 重启jenkins服务，Jenkins已经更新到最新稳定版  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-updatecok-websoft9.png)


## 故障