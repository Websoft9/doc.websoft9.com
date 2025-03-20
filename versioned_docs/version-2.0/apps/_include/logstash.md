[Elastic Logstash](https://www.elastic.co/logstash) 是一个 **数据采集与转换软件**，它被用于 数据采集/编排/集成  等场景。Logstash 是免费且开放的服务器端数据处理管道，能够从多个来源采集数据，转换数据，然后将数据发送到您最喜欢的“存储库”中。


![控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard1-websoft9.png)


## 准备

在参阅本文档使用 Elastic Logstash 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Elastic Logstash：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [SSPL-v1](https://www.mongodb.com/licensing/server-side-public-license) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口