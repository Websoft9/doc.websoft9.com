---
title: Zulip
slug: /zulip
tags:
  - Zulip
  - 团队协作
  - 团队通讯
---

import Meta from './_include/zulip.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. 登录到 Websoft9 控制台，点击左侧的 **网关** 菜单[为 Zulip 应用设置 HTTPS 访问](./domain-https#console)（必要操作，否则无法使用）

2. Websoft9 控制台安装 Zulip 后，通过 **我的应用** 查看应用详情 

    - 在 **访问** 标签页中获取 **URL**
    - 在 **容器** 标签页中获取 **主容器ID**

3. 进入容器执行命令，生成一个链接来创建新组织

    ```
    docker exec  -u zulip  步骤2获取的主容器ID  /home/zulip/deployments/current/manage.py generate_realm_creation_link
    ```

4. 本地浏览器访问步骤3返回的 URL，创建组织以及用户完成初始化

## 配置选项{#configs}

- 多语言（√）

## 管理维护{#administrator}

## 故障
