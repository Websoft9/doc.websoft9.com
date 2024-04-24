---
sidebar_position: 3
slug: /guide/deploy-app
---

# 从应用商店之外部署应用

虽然 Websoft9 应用商店包含很多优秀的软件，但终究不能列出全世界所有的软件。  

故，Websoft9 在设计的时候，是充分考量了自主安装应用的需求（不从应用商店安装）：

1. **安装**：参考 [安装自定义应用](../quick/installapp.md#not-from-appstore)，选择一种安装应用的方式

2. **测试**：软件安装完成之后通过 curl 测试是否可用

3. **发布**：打开 Websoft9 控制台的 [网关](../function/gateway)，为应用增加一个 **[Proxy Hosts](../function/gateway#add-proxhost)**，即为应用配置域名和证书，并对外发布。  