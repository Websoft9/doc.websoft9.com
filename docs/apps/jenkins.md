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

1. 使用本地电脑浏览器访问，进入初始化页面，Jenkins 提示需要解锁
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-installstart-websoft9.png)

2. Websoft9 应用管理或宿主机命令行，进入容器的命令模式，获得解锁密码

   ```
   cat /var/jenkins_home/secrets/initialAdminPassword
   ```

3. 成功登陆后，完成后续步骤：安装插件、创建管理员等  

4. 进入控制台，开始使用
   ![](./assets/jenkins-backend-websoft9.png)

### Github + Jenkins 自动构建

下面以 **Github 上的项目通过 Jenkins 自动构建部署** 作为一个任务，帮助用户快速入门：

1. 在 GitHub设置 Personal access tokens，用于 Jenkins 连接

2. Jenkins 确保安装并启用 Github 插件

3. 创建 Job，配置过程中设置源码位 Github 地址，并设置好触发策略

## 配置选项{#configs}

- 安装与管理插件："Manage Jenkin" > "Plugins"
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
- 在线更新（✅）：当有更新时，后台会提示，并可以通过后台在线更新

## 管理维护{#administrator}

### 备份与恢复

[Backup plugin](https://plugins.jenkins.io/backup/) 提供对 Jenkins 的备份和恢复功能。  

### 在线升级

Jenkins 控制台提供在线升级功能

## 故障