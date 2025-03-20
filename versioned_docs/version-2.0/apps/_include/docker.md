[Docker](https://www.docker.com/) 是一个 **部署 Docker 应用的模板环境，基于 Docker Compose**，它被用于 容器 Docker 家庭服务器  等场景。这是 Websoft9 创建的 docker-compose 的模板环境，通过修改 Docker Compose，您可以非常方便的运行任何类型的 Docker 应用。


![arch](https://libs.websoft9.com/Websoft9/DocsPicture/en/runtime/runtime-web-websoft9.png)


## 准备

在参阅本文档使用 Docker 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Docker：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口