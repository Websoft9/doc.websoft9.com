---
title: Redmine
slug: /redmine
tags:
  - 敏捷开发
  - 项目管理
---

import Meta from './_include/redmine.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Redmine 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

1. 使用本地 Chrome 或 Firefox 浏览器访问后， 进入Redmine主页。

2. 点击【登录】，进入系统
   ![Redmine 密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-login-websoft9.png)

3. 进入 Redmine 控制台，系统提示修改密码 
   ![Redmine 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-resetpwf-websoft9.png)

4. 打开：【项目】，新建一个项目
   ![Redmine 新建项目](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject-websoft9.png)

### 设置语言

1. 依次打开：【管理】>【配置】>【显示】，设置 Redmine 项目区语言
   ![Redmine 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-language-websoft9.png)

2. 依次打开：【管理】>【配置】>【用户】，设置 Redmine 用户语言（区别于项目区语言）
   ![Redmine SSH key](https://libs.websoft9.com/Websoft9/DocsPicture/en/redmine/redmine-userlanguage-websoft9.png)

### 创建项目

下面以 **Redmine 管理项目** 作为一个任务，帮助用户快速入门：

1. 登录 Redmine，依次打开：【项目】>【创建项目】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject001-websoft9.png)

2. 填写上面标题和英文缩写，保存
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject002-websoft9.png)

3. 打开项目页面，开始工作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-createproject003-websoft9.png)

4. [安装插件](#plugin)，增加更多所需的功能

### 安装和卸载插件

通过 Redmine 提供的[插件中心](https://www.redmine.org/plugins)可以扩展它的功能：

下面以一个具体的插件为例说明如何管理插件：  

1. 进入[Ajax Redmine Issue Dynamic Edit](https://www.redmine.org/plugins/redmine_issue_dynamic_edit) 插件页面，获取其下载地址

2. exec 到容器中，下载并解压插件到 /usr/src/redmine/plugins 中
   ```
   curl -L -o redmine_issue_dynamic_edit.zip https://www.redmine.org/attachments/download/25386/redmine_issue_dynamic_edit.zip && sudo unzip redmine_issue_dynamic_edit.zip -d /usr/src/redmine/plugins
   ```

3. 重启 Redmine 后生效
   
4. 登陆 Redmine 控制台查看插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-installplugindy-websoft9.png)

5. 插件卸载操作相反，即只需删除插件对应的目录

## 配置选项

- 站点目录：*/path/data/redmine*  
- 配置目录：*/path/data/redmine/config*  
- 配置文件：*//path/data/redmine/config/configuration.yml*  
- [CLI](https://pypi.org/project/Redmine-CLI/)
- [API](https://www.redmine.org/projects/redmine/wiki/Rest_api)
- SCM 支持：SVN, CVS, Git, Mercurial and Bazaar
- 多语言（√）
- [Email Configuration](https://www.redmine.org/projects/redmine/wiki/EmailConfiguration)

## 管理维护{#administrator}

### 设置 SMTP{#smtp}

1. 修改 `configuration.yml` 文件，找到 “production:”, 在 production 下面添加并完善你的 SMTP 参数:  
   ```
   production:
   delivery_method: :smtp
   smtp_settings:
      address: smtp.exmail.qq.com
      port: 465
      ssl: true
      enable_starttls_auto: true
      domain: websoft9.com
      authentication: :login
      user_name: help@websoft9.com
      password: ********

   ```
    > 注意缩进/空格,按照规定格式配置，否则Redmine报错

2. 重启 Redmine 容器服务后生效


3. 登录 Redmine 控制台，配置系统主机：【管理】-【配置】-【一般】-【主机名称】

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-sethost-websoft9.png)

4. 配置系统邮件发件人地址：【管理】-【配置】-【邮件通知】-【邮件发件人地址】,保存，点击最下方“发送测试邮件”进行测试
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/redmine/redmine-smtp-websoft9.png)


### 备份与恢复

参考：[《RedmineBackupRestore》](https://redmine.org/projects/redmine/wiki/RedmineBackupRestore)

## 故障

#### 新建工程名为中文时，系统报错？

数据库字符编码导致，需修改数据库字符编码为 utf8

#### 新注册用户不能登录？

新注册用户需要激活：通过【管理】>【用户】，在【状态】选项中选择 已注册用户，然后激活用户，该用户才能登陆。

