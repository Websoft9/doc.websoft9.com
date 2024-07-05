[Node.js](https://hub.docker.com/_/node) 是一个 **部署 Node.js 应用的容器环境，支持任选 Node 版本**，它被用于 Node  等场景。这是一个支持多版本 Node.js 应用部署的运行环境，它由 Websoft9 基于 Docker 官方的 Node.js 镜像制作，用户可以非常方便的对它进行客户化的设置。


![架构图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nodejs/nodejs-gui-websoft9.png)


## 准备

在参阅本文档使用 Node.js 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议

- 应用具备访问条件：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口