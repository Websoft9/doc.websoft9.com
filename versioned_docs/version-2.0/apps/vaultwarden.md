---
title: Vaultwarden
slug: /vaultwarden
tags:
  - 密码安全
  - 密码管理
  - vaultwarden
---

import Meta from './_include/vaultwarden.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. 登录到 Websoft9 控制台，点击左侧的 **网关** 菜单[为 Vaultwarden 应用设置 HTTPS 访问](./domain-https#console)（必要操作，否则无法使用）

2. Websoft9 控制台安装 Vaultwarden 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取访问 URL  

3. 根据向导完成注册、登录

### 设置管理页面

Websoft9 默认设置了明文的 `ADMIN_TOKEN`, 可正常使用。如果想设置 argon2 的密文作为 TOKEN，步骤如下:

1. 使用命令生成 argon2 的密文

   ```
   $ echo -n "MySecretPassword123" | argon2 "$(openssl rand -base64 32)" -e -id -k 65540 -t 3 -p 4
   $ $argon2id$v=19$m=65540,t=3,p=4$UTVtVDgyUkJLYkwrVjF6T3k3NjBnblk4M2JMZ3RYRW5BdUlHTXZhOVY3RT0$4uUKMzLRZHSPK0Fo3WmTdDI3suCdNGDi3F+IrZ8AQys
   ```

2. **我的应用 > 编排 > 马上修改**，编辑 .env 文件，将`ADMIN_TOKEN`的值设置为密文

3. 重建应用

4. 浏览器访问 https://URL/admin，输入密文对应的明文密码即可使用

## 配置选项{#configs}

- 多语言（√）

## 管理维护{#administrator}

## 故障