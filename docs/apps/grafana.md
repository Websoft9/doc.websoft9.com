---
title: Grafana
slug: /grafana
tags:
  - 分析
  - 可视化
  - 日志分析
  - 时序数据
  - 物联网
  - 数据分析
---

import Meta from './_include/grafana.md';

<Meta name="meta" />

## 入门指南{#guide}

### 验证安装{#wizard}

Websoft9 控制台安装 Grafana 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

- Grafana 控制台页面  
   ![Grafana 控制台](./assets/grafana-dashboard-websoft9.png)

- 通过【Configuration】>【Plugins】添加插件  
   ![Grafana 添加插件](./assets/grafana-plugins-websoft9.png)

- 通过【Configuration】>【Data Sources】添加数据源（分析对象）  
   ![Grafana 添加数据源](./assets/grafana-datasource-websoft9.png)

## 配置选项{#configs}

- 配置文件（容器内路径）：/etc/grafana/grafana.ini
- [Grafana API](https://grafana.com/docs/grafana/latest/http_api)
- 命令行：`grafana-cli`
- 默认数据库：内置的 SQLite

## 管理维护{#administrator}

- **SMTP 配置**：配置文件中增加 SMTP 配置段

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

- **重置管理员密码**：容器中运行命令 `grafana-cli admin reset-admin-password admin123`

- **升级**：[Upgrading Grafana](https://grafana.com/docs/installation/upgrading/)

## 问题和故障

#### 如何更换数据库？

准备好数据库，然后在编排 .env 文件中增加 GF_DATABASE_URL 环境变量，重建应用后生效。
```
# mysql example
GF_DATABASE_URL=mysql://grafana:123456@172.17.0.1:3306/grafana
```