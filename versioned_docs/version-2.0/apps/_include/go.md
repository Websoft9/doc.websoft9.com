[Go](https://hub.docker.com/_/golang) 是一个 **部署 Go 应用的容器环境，支持任选 Go 版本**，它被用于 Go  等场景。这是一个支持多版本 Go 应用部署的运行环境，它由 Websoft9 基于 Docker 官方的 Go 镜像制作，用户可以非常方便的对它进行客户化的设置。


![架构图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-web-websoft9.png)


## 准备

在参阅本文档使用 Go 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Go：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [bsd3Clause](https://opensource.org/licenses/BSD-3-Clause) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口