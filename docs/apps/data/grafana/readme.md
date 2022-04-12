---
sidebar_position: 1
slug: /grafana
tags:
  - Grafana
  - 大数据分析
  - BI
---

# 快速入门

[Grafana](https://github.com/grafana/grafana) 是一个开源的度量分析与可视化套件。经常被用作基础设施的时间序列数据和应用程序分析的可视化，它在其他领域也被广泛的使用包括工业传感器、家庭自动化、天气和过程控制等。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-dashboardui.png)

## 准备

部署 Websoft9 提供的 Grafana 之后，请参考下面的步骤快速入门。

1. 在云控制台获取您的 **服务器公网 IP 地址**
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:3000** 端口是否开启
3. 在服务器中查看 Grafana 的 **[默认账号和密码](./user/credentials)**
4. 若想用域名访问 Grafana，务必先完成**[域名五步设置](./administrator/domain_step)** 过程

## Grafana 初始化向导

### 详细步骤

1. 使用本地电脑的浏览器访问网址： *http://域名* 或  *http://服务器公网IP*, 就进入登录页面
   ![Grafana 登录](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-login-websoft9.png)

2. 输入默认的用户名和密码（[查看](/zh/stack-accounts.md#grafana)），系统会提示修改密码
   ![Grafana 强提示修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-forcechangepw-websoft9.png)

3. 登录到 Grafana 控制台页面  
   ![Grafana 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-dashboard-websoft9.png)

4. 通过【Configuration】>【Plugins】添加插件  
   ![Grafana 添加插件](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-plugins-websoft9.png)

5. 通过【Configuration】>【Data Sources】添加数据源（分析对象）  
   ![Grafana 添加数据源](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-datasource-websoft9.png)

6. 通过【Configuration】>【Users】增加用户  
   ![Grafana 添加用户](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-users-websoft9.png)

> 需要了解更多 Grafana 的使用，请参考官方文档：[Grafana Documentation](https://grafana.com/docs)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或 **[FAQ](./faq#setup)** 尝试快速解决问题。

## Grafana 使用入门

下面以 xxx 配置数据监控作为范例。

## Grafana 常用操作

### 配置 SMTP

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 修改[Grafana 配置文件](#path)，增加如下的 SMTP 配置段

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

3. 重启服务
   ```
   sudo systemctl restart grafana-server
   ```
   
4. 登录 Grafana 控制台，打开：【Alerting】>【Alert Rules】，新建一个【Email】通知渠道
   ![Grafana SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/grafana/grafana-sendmails-websoft9.png)

5. 点击【Send Test】

### 重置密码

SSH 登录服务器，运行下面的命令即可

```
# 修改管理员密码
grafana-cli admin reset-admin-password admin123
```

## Grafana 参数

Grafana 应用中包含 Nginx, SQLite 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

下面仅列出 Grafana 本身的参数：

### 路径{#path}

Grafana 安装目录： */usr/share/grafana*  
Grafana 配置文件：  */usr/share/grafana/conf/defaults.ini*  
Grafana 日志文件：  */var/log/grafana/grafana.log*  
Grafana 数据存储路径： */usr/share/grafana/data*  
Grafana 数据日志路径： */usr/share/grafana/data/log*

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 3000   | Grafana 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |

### 版本

```shell
# Grafana Version
grafana-cli -v
```

### 服务

```
sudo systemctl start | stop | restart | status grafana-server
```

### 命令行

Grafana 提供命令行工具`grafana-cli`用于全面管理和配置 Grafana

```
[root@iZj6cfvehfql1u0bth47acZ ~]# grafana-cli -h
NAME:
   Grafana CLI - A new cli application

USAGE:
   grafana-cli [global options] command [command options] [arguments...]

VERSION:
   8.4.4

AUTHOR:
   Grafana Project <hello@grafana.com>

COMMANDS:
   plugins  Manage plugins for grafana
   admin    Grafana admin commands
   cue      Cue validation commands
   help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --pluginsDir value       Path to the Grafana plugin directory (default: "/var/lib/grafana/plugins") [$GF_PLUGIN_DIR]
   --repo value             URL to the plugin repository (default: "https://grafana.com/api/plugins") [$GF_PLUGIN_REPO]
   --pluginUrl value        Full url to the plugin zip file instead of downloading the plugin from grafana.com/api [$GF_PLUGIN_URL]
   --insecure               Skip TLS verification (insecure) (default: false)
   --debug                  Enable debug logging (default: false)
   --configOverrides value  Configuration options to override defaults as a string. e.g. cfg:default.paths.log=/dev/null
   --homepath value         Path to Grafana install/home path, defaults to working directory
   --config value           Path to config file
   --help, -h               show help (default: false)
   --version, -v            print the version (default: false)
```

### API

[Grafana API](https://grafana.com/docs/grafana/latest/http_api) 采用 REST API 2.0 规范。
