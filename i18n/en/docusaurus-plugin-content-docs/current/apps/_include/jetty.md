[Jetty](https://hub.docker.com/_/jetty) 是一个 **Jetty and JRE runtime for web application**，它被用于 Java  等场景。This is multiply verion Jetty/JRE runtime for web application powered by Websoft9, it based on offcial Docker image. You can custom it by yourself very easy


![Architecture](https://libs.websoft9.com/Websoft9/DocsPicture/en/runtime/runtime-web-websoft9.png)


## 准备

在参阅本文档使用 Jetty 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口