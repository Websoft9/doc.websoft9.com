---
title: Metabase
slug: /metabase
tags:
  - 大数据分析
  - BI
  - 数据可视化
---

import Meta from './_include/metabase.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Metabase 后，通过【我的应用】进入它的编辑窗口，在 "访问" 标签页中获取登陆信息。  

1. 使用本地浏览器访问后，进入登陆页面
   ![Metabase登陆界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-login-websoft9.png)

2. 输入邮件地址和密码，登录到 Metabase 后台管理界面
   ![Metabase后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-dashborad-websoft9.png)

3. 进入了软件的引导加载
   ![Metabase初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-start-websoft9.png)

4. 耐心等待 1-3 分钟，直至出现如下的界面。
   ![开始安装Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-starty-websoft9.png)

5. 点击“让我们开始吧”，接下来首先设置登录账号，完成后进入下一步

6. 添加数据：可以选择使用的数据类型来连接一个需要分析的外部数据库。  
   如果没有也可以点击“我之后再添加”，这样系统会默认给 Metabase 增加一个 H2 演示数据
   ![配置Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-installdb-websoft9.png)

7. 安装成功后的界面，点击“带我去 Metabase”登录后台
   ![Metabase安装成功](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-installss-websoft9.png)

8. 以 H2 演示数据为例，开始数据分析工作
   ![Metabase H2演示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-dashborad-websoft9.png)

9. Metabase 有强大的系统管理能力：后台->设置，进入系统管理界面
   ![Metabase Admin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-admin-websoft9.png)

### 增加数据源

通过“添加一个数据库”来增加一个数据分析源
    ![Metabase 增加数据库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-adddb-websoft9.png)

### 管理用户

点击“人员管理”标签，管理使用 Metabase 用户，包括增加用户、修改密码等

    ![Metabase 人员管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-users-websoft9.png)

## 配置选项{#configs}

- SMTP：控制台【Settings】>【email】
- 多语言（✅）：根据浏览器自动选择
- 多用户（✅）
- [Matebase API](https://www.metabase.com/docs/latest/api-documentation.html)

## 管理维护{#administrator}

### 升级

Metabase 有升级包的时候，后台会及时给出提示。参考下面的步骤完成升级：

1. Metabase 后台->设置->升级，如果有新的升级包，系统会给与提示
   ![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereminder-websoft9.png)

2. 点击“更新”按钮后，系统会跳转到 Metabase 官方的安装页面。

3. 我们提供的部署包采用的是 jar 包安装模式，因此在安装页面我们选择“Custom install”模式，
   ![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatedl-websoft9.png)

4. 下载 Metabase.jar 包后，上传到服务器 `/data/wwwroot/metabase`, 覆盖已有的同名文件
   ![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereplace-websoft9.png)

5. 重新加载 Metabase，升级成功

## 故障