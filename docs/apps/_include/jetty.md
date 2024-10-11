[Jetty](https://hub.docker.com/_/jetty) 是一个 **部署 Java 应用的容器环境，支持 Jetty 和 JRE 多版本**，它被用于 Java  等场景。这是一个支持多版本 Jetty/JRE 运行环境，它由 Websoft9 基于 Docker 官方的 Jetty 镜像制作，用户可以非常方便的对它进行客户化的设置。


![架构图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-web-websoft9.png)


## 准备

在参阅本文档使用 Jetty 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议

- 应用具备访问条件：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口