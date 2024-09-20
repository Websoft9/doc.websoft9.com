---
title: Passbolt
slug: /passbolt
tags:
  - Passbolt
  - 密码安全
  - 密码管理
---

import Meta from './_include/passbolt.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Passbolt 后，通过 **我的应用** 查看应用详情

    - 在 **概览** 标签页中获取 **应用Id**  
    - 在 **访问** 标签页中获取 **访问 URL**  


2. 宿主机运行下面的命令后，创建管理员账号，并生成一个用于初始化安装的 **URL 后缀路径**

    ```
    docker exec <应用Id> su -m -c "bin/cake passbolt register_user -u "YOUR_EMAIL" -f "YOUR_NAME" -l "YOUR_LASTNAME" -r admin" -s /bin/sh www-data
    ```

3. 使用本地浏览器访问: `http://URL/后缀路径`，进入初始化向导依次完成：

   - 安装 Passbolt 浏览器插件
   - 设置管理员密码

4. 完成初始化后，登录到 Passbolt 控制台，设置 SMTP 后方可通过邮件邀请其他用户注册


## 配置选项{#configs}

- 多语言（√）：目前暂不支持中文
- SMTP：控制台 **administration > Email server**

## 管理维护{#administrator}


## 故障
