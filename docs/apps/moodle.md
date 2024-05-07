---
title: Moodle
slug: /moodle
tags:
  - 在线学习
  - LMS
  - 教学管理
  - 课程管理
---

import Meta from './_include/moodle.md';

<Meta name="meta" />

## 入门指南{#guide}

### 登录后台{#wizard}

1. Websoft9 控制台安装 Moodle 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

2. 点击右上角 "Login" 按钮，登陆进入 Moodle 后台
   ![](./assets/moodle-backend-websoft9.png)

### 注册官方会员{#register}

Moodle 初始化之后，建议向 Moodle 官方注册会员，便于在线安装插件

1. 以管理员身份登录 Moodle 后台，依次打开：【网站管理】>【注册】

3. 注册完成后登陆，这样你的 Moodle 与官方便建立了一个连接关系


### 安装插件{#plugin}

1. 以管理员身份登录 Moodle 后台

2. 依次打开：【网站管理】>【插件】，查看或安装插件

3. 支持两种插件的安装方式：
   
   - 在线安装：从 Moodle 插件目录安装插件
   - 离线安装：上传 zip 文件安装

### 安装主题{#theme}

1. Moodle 主题实际上是一个插件，通过【安装插件】的方式先进行安装

2. 打开【网站管理】>【外观】>【主题选择器】，更换主题


## 配置选项{#configs}

- [插件](https://moodle.org/plugins/)（✅）
- [主题](https://moodle.org/plugins/)（✅）：主题也是插件的一种类型
- 配置文件（已挂载）：*/bitnami/moodle/config.php*
- 媒体文件（✅）
- 多语言（✅）：【Site administration】>【language】>【Language Packs】
- SMTP（✅）：【网站管理】>【服务器】>【电子邮件】>【发送邮件设置】
- 移动端（✅）：【网站管理】>【移动应用程序】>【移动设备设置】>【为移动设备启用网络服务】
- [Plugins](https://docs.moodle.org/37/en/Installing_plugins)
- [Administration via command line](https://docs.moodle.org/311/en/Administration_via_command_line)
    ```
    $ sudo -u apache /usr/bin/php admin/cli/somescript.php --params
    $ sudo -u apache /usr/bin/php admin/cli/install.php --help
    ```
- [Core APIs](https://docs.moodle.org/dev/Core_APIs)
- 在线备份：【网站管理】>【课程】>【备份】

## 管理维护{#administrator}

- **找回密码**：修改 Moodle 数据库的 *mdl_user* 表，将其中的 `password` 字段的值用 `21232f297a57a5a743894a0e4a801fc3` 替换，密码被重置为`admin`

## 故障