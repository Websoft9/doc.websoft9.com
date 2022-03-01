---
sidebar_position: 3
slug: /mattermost/study
tags:
  - Mattermost
  - 团队协作
  - 团队通讯
---

# 原理学习

[Mattermost](https://mattermost.com/) 是一个 Slack 的开源替代品。Mattermost 采用 Go 语言开发，这是一个开源的团队通讯服务。为团队带来跨 PC 和移动设备的消息、文件分享，提供归档和搜索功能。

![](https://ucarecdn.com/8cd90d9d-8902-4845-a15b-f4664e5fcfb3/-/format/auto/-/quality/lighter/-/max_icc_size/10/-/resize/1288x/)

## CLI

Mattermost 提供了 `mattermost` 和 `mmctl` 两种命令，[mattermost](https://docs.mattermost.com/administration/command-line-tools.html)是服务器端命令，[mmctl](https://docs.mattermost.com/administration/mmctl-cli-tool.html)基于API的客户端命令
 
```
/opt/mattermost/bin/mattermost -h
/opt/mattermost/bin/mmctl -h
```

如果运行 /opt/mattermost/bin/mmctl version 查询出的版本稍微低一点