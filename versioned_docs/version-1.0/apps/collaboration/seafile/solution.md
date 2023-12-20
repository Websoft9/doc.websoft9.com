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

## Seafile 集成 ONLYOFFICE Docs{#onlyoffice}

Seafile 开源版支持集成 OnlyOffice Docs 作为 Office 格式的文档预览与编辑，且本部署方案已配置好 OnlyOffice Docs，开机即用。

但是，为了便于用户维护，下面我们把配置的详细步骤列出，以供需要时参考：  

1. 首先，确保 [OnlyOffice Docs](../onlyofficedocs) 可访问
2. 然后，SFTP 连接服务器，编辑 Seafile 配置文件/data/apps/seafile/data/seafile_data/seafile/conf/seahub_settings.py
3. 插入下面的模板（或对已经存在的模板进行修改）
   ```
   # Enable Only Office
   ENABLE_ONLYOFFICE = True
   VERIFY_ONLYOFFICE_CERTIFICATE = False
   ONLYOFFICE_APIJS_URL = 'http://example.seafile.com:9002/web-apps/apps/api/documents/api.js'
   ONLYOFFICE_FILE_EXTENSION = ('doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods')
   ONLYOFFICE_EDIT_FILE_EXTENSION = ('docx', 'pptx', 'xlsx')
   ```
   > ONLYOFFICE_APIJS_URL 字段中的 **example.seafile.com** 地址请更改为你的服务器公网IP地址或域名。如果 OnlyOffice 已启用 https，URL地址改成 https 开头

4. 重启 Seafile 容器服务
   ```
   sudo docker restart seafile
   ```

5. 测试预览或编辑文档功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-onlyofficepr-websoft9.png)