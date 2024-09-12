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

    - 在 **访问** 标签页中获取访问 URL
    - 在 **容器** 标签页中获取 **主容器**

2. 通过命令创建管理员账号（目前不支持在 web 页面创建管理员账号），命令执行后生成 **路径字符串**

    ```
    docker exec "步骤1中获取的 **主容器**" su -m -c "bin/cake passbolt register_user -u "YOUR_EMAIL" -f "YOUR_NAME" -l "YOUR_LASTNAME" -r admin" -s /bin/sh www-data
    ```

3. 使用本地浏览器访问 "URL + 步骤2生成的 **路径字符串**"

4. 根据提示完成安装 Passbolt 客户端插件、设置主密码等操作

5. 登陆后，**administration > Email server** 中设置 SMTP 配置

6. 管理员添加的新用户后，新用户通过邮件获取验证码注册登陆


## 配置选项{#configs}

- 多语言（√）：目前暂不支持中文

## 管理维护{#administrator}


## 故障
