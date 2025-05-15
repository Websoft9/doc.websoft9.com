---
title: ZITADEL
slug: /zitadel
tags:
  - 用户认证
  - 身份管理
  - zitadel
---

import Meta from './_include/zitadel.md';

<Meta name="meta" />

## 入门指南{#guide}

### 登录后台{#console}

1. Websoft9 控制台安装 ZITADEL 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取访问 URL

2. 本地浏览器访问 URL, 输入邮箱和密码即可登陆使用

### 创建用户

1. 自我注册模式： 需要 SMTP 服务器配置和电子邮件验证。

2. 管理员添加用户： 可标记为 “电子邮件已验证”，以跳过电子邮件验证。

### 开启 TLS 模式

1. 有三种操作模式：disabled, external, enabled（默认为禁用）。

2. 通过 Websoft9 配置 SSL：需要将模式设置为外部模式，这涉及到修改 docker-compose 文件：
    ```
    command: start-from-init --masterkey "MasterkeyNeedsToHave32Characters" --tlsMode external
    ```
    
3. 必须明确启用 HTTP/2。

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障
