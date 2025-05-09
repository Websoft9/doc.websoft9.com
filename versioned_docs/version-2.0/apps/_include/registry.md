[Docker registry](https://github.com/distribution/distribution/) 是一个 **镜像仓库系统，DockerHub 背后的平台**，它被用于 制品仓库 一站式 DevOps 应用  等场景。注册表是一个无状态、高度可伸缩的服务器端应用程序，用于存储 并允许您分发容器映像和其他内容。


![架构图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/docker/docker-registry-gui.webp)


## 准备

在参阅本文档使用 Docker registry 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Docker registry：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口