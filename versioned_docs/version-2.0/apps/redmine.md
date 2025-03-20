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

2. 进入 Redmine 界面后，点击右上角**登录**

3. 根据系统提示，修改密码后正式访问控制台

### 管理插件

获取匹配的插件版本后，两个步骤即可安装插件：

1. 将插件下载解压（或 git clone）到 Redmine 容器目录 */usr/src/redmine/plugins* 中
2. 重启 Redmine 容器后生效

> 插件版本不匹配会导致容器无法启动，需立即删除插件

#### 下载插件范例

```
# 下载并解压插件
apt update -y && apt install unzip
curl -L -o plugin_name.zip https://url/plugin_name.zip
unzip plugin_name.zip -d /usr/src/redmine/plugins

# git clone 插件
cd /usr/src/redmine/plugins
git clone https://github.com/Ilogeek/redmine_issue_dynamic_edit.git
```

#### 卸载插件

删除插件目录，即卸载插件

#### 迁移插件

如果 Redmine 容器中的插件目录已经挂载到宿主机，那么[升级 Redmine](https://www.redmine.org/projects/redmine/wiki/RedmineUpgrade) 时，插件可能无法适用新的 Redmine 版本而导致 Redmine 升级失败。    

Redmine 插件的 ruby 版本以及 gem 包依赖可能会与 Redmine 主程序产生冲突，导致 Redmine 无法启动。    

因此，Websoft9 标准的 Redmine 启动程序并没有将容器中的插件目录挂载到宿主机。    

正确的做法是：在升级 Redmine 之前，需要将插件目录移动到其他位置作为备份，待 Redmine 升级成功后，方可将插件逐一拷贝到插件目录。    


### 设置 SMTP{#smtp}

1. Redmine 编排模式下，修改 `configuration.yml` 文件中的 [SMTP](https://www.redmine.org/projects/redmine/wiki/EmailConfiguration) 相关参数

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

2. 重启 Redmine 容器后生效

3. Redmine 控制台设置 SMTP：**管理 > 配置 > 邮件通知**

## 配置选项

- [插件中心](https://www.redmine.org/plugins)（✅）
- 多语言（✅）：支持项目多语言和用户多语言
- 容器数据目录（已挂载）：*/usr/src/redmine/files*  
- 容器配置文件（已挂载）：*/usr/src/redmine/config/configuration.yml*  
- 容器插件目录：*/usr/src/redmine/files/plugins*  
- [CLI](https://pypi.org/project/Redmine-CLI/)
- [SMTP](https://www.redmine.org/projects/redmine/wiki/EmailConfiguration)

## 管理维护{#administrator}

- 备份与恢复：[《RedmineBackupRestore》](https://redmine.org/projects/redmine/wiki/RedmineBackupRestore)

## 故障

#### 工程名为中文时，系统报错？

需修改数据库字符编码为 utf8

#### 新注册用户不能登录？

需管理员在后台激活，方可登陆

#### 安装插件导致 Redmine 无法启动？

问题分析：这个现象是正常的，因为安装插件可能会改变依赖包版本，使得 Redmine 主程序无法启动。   
解决方案：删除插件目录，重启 Redmine

