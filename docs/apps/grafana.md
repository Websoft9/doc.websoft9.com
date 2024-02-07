---
title: Grafana
slug: /grafana
tags:
  - 分析
  - 可视化
  - 日志分析
  - 数据分析
---

import Meta from './_include/grafana.md';

<Meta name="meta" />

## 入门指南{#guide}

### 功能一览{#wizard}

Websoft9 控制台安装 Grafana 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

- Grafana 控制台页面  
   ![Grafana 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-dashboard-websoft9.png)

- 通过【Configuration】>【Plugins】添加插件  
   ![Grafana 添加插件](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-plugins-websoft9.png)

- 通过【Configuration】>【Data Sources】添加数据源（分析对象）  
   ![Grafana 添加数据源](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-datasource-websoft9.png)

- 通过【Configuration】>【Users】增加用户  
   ![Grafana 添加用户](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-users-websoft9.png)

## 配置选项{#configs}

- [Grafana API](https://grafana.com/docs/grafana/latest/http_api)
- 命令行：`grafana-cli`
- SMTP（✅）：配置文件中增加配置段，后在控制台【Alerting】>【Alert Rules】，新建一个【Email】
   ```
   #################################### SMTP / Emailing #####################
   [smtp]
   enabled = false
   host = localhost:25
   user =
   # If the password contains # or ; you have to wrap it with triple quotes. Ex """#password;"""
   password =
   cert_file =
   key_file =
   skip_verify = false
   from_address = admin@grafana.localhost
   from_name = Grafana
   ehlo_identity =

   [emails]
   welcome_email_on_sign_up = false
   templates_pattern = emails/*.html
   ```

   ![Grafana SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-sendmails-websoft9.png)

## 管理维护{#administrator}

### 重置管理员密码{#resetpw}

容器中运行如下命令：  

```
grafana-cli admin reset-admin-password admin123
```

### 升级

请参考官方提供的升级文档：[Upgrading Grafana](https://grafana.com/docs/installation/upgrading/)

## 故障