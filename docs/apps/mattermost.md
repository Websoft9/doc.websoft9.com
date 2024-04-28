---
title: Mattermost
slug: /mattermost
tags:
  - 团队协作
  - 团队通讯
---

import Meta from './_include/mattermost.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Mattermost 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 本地电脑浏览器访问 URL，进入初始化向导

2. 根据向导依次完成后续步骤：创建管理账号、创建团队等

3. 登录后台开始使用
   ![](./assets/mattermost-backend-websoft9.png)

## 配置选项{#configs}

- 配置文件：/path/mattermost_config/config.json
- 移动端（✅）：[下载地址](https://mattermost.com/download/#mattermostApps)
- 多语言（✅）：【Settings】>【Display】设置
- SMTP（✅）：Mattermost控制台，打开【ENVIROMENT】>【SMTP】
- 服务端命令行：[mattermost](https://docs.mattermost.com/administration/command-line-tools.html)
- 客户端命令行：[mmctl](https://docs.mattermost.com/administration/mmctl-cli-tool.html)
  ```
  /opt/mattermost/bin/mattermost -h
  /opt/mattermost/bin/mmctl -h
  ```
- [Mattermost API Reference](https://api.mattermost.com/)
- 设置团队最大用户数："SITE CONFIGURATION" > "Users and Teams" > "Max Users Per Team"

## 管理维护{#administrator}

### 更换 URL 额外操作{#url}

通过 Websoft9 控制台更换域名后，还需要在 Mattermost 后台修改 "Site URL"："ENVIRONMENT" > "Web Server"

## 问题与故障

#### Mattermost vs Slack？

[Mattermost vs Slack](https://mattermost.com/mattermost-vs-slack/)