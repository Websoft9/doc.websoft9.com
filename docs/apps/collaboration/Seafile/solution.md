---
sidebar_position: 2
slug: /seafile/solution
tags:
  - Seafile
  - 网盘
  - 知识管理
  - 团队协作
---

# 场景方案

Seafile 可以与其他的软件平台**集成**一起使用，解决 构建企业网盘系统 过程中的各种[场景问题](#)。

## 集成 ONLYOFFICE Docs 实现文档编辑{#onlyoffice}

### Seafile 文档预览与编辑

Seafile 开源版支持集成 OnlyOffice Docs 作为 Office 格式的文档预览与编辑，且本部署方案默认安装 OnlyOffice Docs，无需设置即可使用

#### 前置条件

1. 在云控制台安全组中，检查 **TCP:9002** 端口是否开启
2. 使用本地电脑浏览器测试文档服务是否可用：*http://服务器公网IP:9002*，会看到 OnlyOffice Docs 正在运行的提示 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)
   
   > 如果 OnlyOffice Docs 设置好了 HTTPS 访问，请使用 9003 端口

#### 配置

1. 使用 SFTP 连接服务器，编辑 Seafile 配置文件/opt/seafile-data/seafile/conf/seahub_settings.py
2. 插入下面的模板（或对已经存在的模板进行修改）
   ```
   # Enable Only Office
   ENABLE_ONLYOFFICE = True
   VERIFY_ONLYOFFICE_CERTIFICATE = False
   ONLYOFFICE_APIJS_URL = 'http://example.seafile.com:9002/web-apps/apps/api/documents/api.js'
   ONLYOFFICE_FILE_EXTENSION = ('doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods')
   ONLYOFFICE_EDIT_FILE_EXTENSION = ('docx', 'pptx', 'xlsx')
   ```
   > ONLYOFFICE_APIJS_URL 字段中的 **example.seafile.com** 地址请更改为你的服务器公网IP地址或域名。如果 OnlyOffice 已启用 https，URL地址改成 https 开头

3. 重启 Seafile 容器服务
   ```
   sudo docker restart seafile
   ```

4. 打开 Seafile 控制台，试一试预览或编辑文档
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-onlyofficepr-websoft9.png)