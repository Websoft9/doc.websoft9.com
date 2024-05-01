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

### 登陆重置密码{#wizard}

1. Websoft9 控制台安装 Redmine 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

2. 进入 Redmine 界面后，点击右上角【登录】

3. 根据系统提示，修改密码后正式访问控制台

### 管理插件

获取匹配的插件版本后，将插件下载解压到 Redmine 容器目录 */usr/src/redmine/plugins* 中，即安装插件

- 容器内下载解压插件的命令范例：
  ```
  apt update -y && apt install unzip
  curl -L -o plugin_name.zip https://url/plugin_name.zip
  unzip rplugin_name.zip -d /usr/src/redmine/plugins
  ```
- 删除插件目录即卸载插件
- 下载解压插件后，重启容器生效
- 插件版本不匹配会导致容器无法启动，需卸载插件

## 配置选项

- [插件中心](https://www.redmine.org/plugins)（✅）
- 多语言（✅）：支持项目多语言和用户多语言
- 站点目录（已挂载）：*/usr/src/redmine*  
- 配置目录（已挂载）：*/usr/src/redmine/config*  
- 配置文件（已挂载）：*/usr/src/redmine/config/configuration.yml*  
- [CLI](https://pypi.org/project/Redmine-CLI/)
- [API](https://www.redmine.org/projects/redmine/wiki/Rest_api)
- [SMTP](https://www.redmine.org/projects/redmine/wiki/EmailConfiguration)

## 管理维护{#administrator}

### 设置 SMTP{#smtp}

1. Redmine 容器中修改 `configuration.yml` 文件，在 production 下添加 SMTP:  

   - 确保 SMTP 主机/账号/密码等准确无误
   - 注意缩进/空格，否则 Redmine 报错
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

2. 重启 Redmine 容器服务后生效

3. Redmine 控制台设置 SMTP：“管理” > "配置" > "邮件通知"


### 备份与恢复

参考：[《RedmineBackupRestore》](https://redmine.org/projects/redmine/wiki/RedmineBackupRestore)

## 故障

#### 工程名为中文时，系统报错？

需修改数据库字符编码为 utf8

#### 新注册用户不能登录？

需管理员在后台激活，方可登陆

