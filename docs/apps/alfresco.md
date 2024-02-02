---
title: Alfresco
slug: /alfresco
tags:
  - ECM
  - 文档管理
  - 内容管理
---

import Meta from './_include/alfresco.md';

<Meta name="meta" />



## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Alfresco 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。

> Alfresco 开机启动最少需要 10 分钟，请耐心等待

1. 访问地址打开后， 点击 "Alfresco Repository" > "Alfresco Share"
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](./user/credentials)），成功登录到 Alfresco 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-consolegui-websoft9.png)

3. Alfresco会自动根据浏览器语言来选择程序语言

### 快速了解

Alfresco 后台支持多语言切换（包括中文），支持用户主页（Alfresco 站点）。  

其他可能需要了解的内容：

#### 官方链接

- [Alfresco Community Edition 对比 Alfresco Content Services Enterprise](https://www.alfresco.com/alfresco-content-services-enterprise-vs-alfresco-community-edition)
- [Alfresco支持所有文件格式](https://www.alfresco.com.cn/alfresco-formats)
- 数据存储目录：dir.root
- 元数据：Alfreco 会自动对上传的文件创建后缀为 metadata.properties.xml 的[元数据文件](https://docs.alfresco.com/content-services/latest/develop/repo-ext-points/metadata-extractors/)
- 官方文档：[Alfresco Documentation](https://docs.alfresco.com/content-services/community/using/content/) 
- 官方视频[Alfresco Videos](https://docs.alfresco.com/content-services/latest/tutorial/video/)
- [ReST API Guide](https://docs.alfresco.com/content-services/latest/develop/rest-api-guide/)

#### 截图

常用的功能以及截图如下：  

- 后台仪表盘
  ![Alfresco台仪表盘](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-adminui-websoft9.png)

- 我的文档
  ![Alfresco我的文档](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-mydocs-websoft9.png)

- 共享文档
  ![Alfresco共享文档](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-sharedocs-websoft9.png)

- 增加多用户
  ![Alfresco增加多用户](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-addusers-websoft9.png)

- 增加组（部门）
  ![Alfresco增加组（部门）](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-addgroup-websoft9.png)

- 工作流（审批）
  ![Alfresco工作流（审批）](http://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-workflow-websoft9.png)


### 文档编辑与预览

支持几十种格式的文件预览，也支持文本文件的在线编辑。  

但是针对 Office 文档，Alfresco 只能[离线编辑或集成 Google Docs](https://docs.alfresco.com/content-services/community/using/content/files-folders/)



### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 填写 Alfresco 邮件相关配置

3. 测试邮件发送是否可用


## 管理维护{#administrator}

### 修改密码

1. 登录 Alfresco 后台，右上角依次打开：【Administrator】>【我的个人档案】
  ![Alfresco 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/alfresco/alfresco-modifypw-websoft9.png)

2. 点击【更改密码】，开始修改密码

### 找回密码

如果用户忘记了密码，需要通过修改数据库中的密码信息来重置密码：

1. 使用 **SSH** 连接到 Alfresco 所在的服务器

2. 进入到 alfresco 数据库的 PSQL 交互式状态
   ```
   docker exec -it alfresco-postgres psql -U alfresco -d alfresco
   ```

3. 运行如下的修改密码命令（新的密码为 **admin**）
   ```
   UPDATE alf_node_properties SET string_value='209c6174da490caeb422f3fa5a7ae634' WHERE node_id=4 and qname_id=10
   ```

4. 退出容器交互式模式，回到服务器命令行中重启所有容器后生效
   ```
   cd /data/wwwroot/alfresco
   docker-compose restart

### 备份与恢复

参考官方文档：[Back up and restore](https://docs.alfresco.com/content-services/community/admin/backup-restore/)

### 升级

参阅官方相关方案


## 故障

#### 中文 Markdown 格式预览乱码？

故障描述：【在浏览器中查看】不乱码，但是在 Alfreco 内置 document-details 中乱码  
问题原因：未知   
解决方案：暂无  