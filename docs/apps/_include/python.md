[Python](https://hub.docker.com/_/python) 是一个 **部署 Python 应用的容器环境，支持任选 Python 版本**，它被用于 Python  等场景。这是一个支持多版本 Python 应用部署的运行环境，它由 Websoft9 基于 Docker 官方的 Python 镜像制作，用户可以非常方便的对它进行客户化的设置。


![架构图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/python/python-gui-websoft9.png)


## 准备

在参阅本文档使用 Python 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [gpl-compatible](https://docs.python.org/3/license.html) 开源许可协议

- 应用具备访问条件：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口