[Logstash](https://www.elastic.co/logstash) 是一个 **Centralize, transform & stash your data**，它被用于 Data Collection  等场景。Logstash is a free and open server-side data processing pipeline that ingests data from a multitude of sources, transforms it, and then sends it to your favorite "stash."


![gui](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-gui-websoft9.gif)


## 准备

在参阅本文档使用 Logstash 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [SSPL](https://www.mongodb.com/licensing/server-side-public-license) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口