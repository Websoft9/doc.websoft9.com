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

1. 本地电脑浏览器访问, 进入引导页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-install-websoft9.png)

2. 设置后台管理员账号和密码，开始创建账号
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-createdaccount-websoft9.png)

3. 开始创建团队 或 登录到系统控制台

4. 打开：【Settings】>【Display】设置你所需的语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-display-websoft9.png)

5. 退出并重新登录，所选语言生效

### 增加团队用户数

系统控制台 【SITE CONFIGURATION】>【Users and Teams】> 【Max Users Per Team】值来设置团队人数：
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-maxusers-websoft9.png)

### Mattermost + Slack

阅读：[Mattermost vs Slack](https://mattermost.com/mattermost-vs-slack/)

## 配置选项{#configs}

- 配置文件：/path/mattermost_config/config.json
- 移动端（✅）：[下载地址](https://mattermost.com/download/#mattermostApps)
- 多语言（✅）
- SMTP（✅）：Mattermost控制台，打开【ENVIROMENT】>【SMTP】
- 服务端命令行：[mattermost](https://docs.mattermost.com/administration/command-line-tools.html)
- 客户端命令行：[mmctl](https://docs.mattermost.com/administration/mmctl-cli-tool.html)
  ```
  /opt/mattermost/bin/mattermost -h
  /opt/mattermost/bin/mmctl -h
  ```
- [Mattermost API Reference](https://api.mattermost.com/)

## 管理维护{#administrator}

### 更换 URL{#url}

更换域名后，需重新设置 URL: 控制台【ENVIRONMENT】>【Web Server】，修改 【Site URL】值   
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-urlset-websoft9.png)

## 故障