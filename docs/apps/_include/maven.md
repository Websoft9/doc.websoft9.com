[Maven](https://hub.docker.com/_/maven) 是一个 **Maven 容器环境，支持多个 JDK 版本**，它被用于 Java  等场景。这是一个支持多版本 Maven/JDK 构建环境，它由 Websoft9 基于 Docker 官方的 Maven 镜像制作，用户可以非常方便的对它进行客户化的设置。


![架构图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-web-websoft9.png)


## 准备

在参阅本文档使用 Maven 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Maven：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口