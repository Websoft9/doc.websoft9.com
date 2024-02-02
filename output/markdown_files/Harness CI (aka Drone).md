# Harness CI (aka Drone)

Drone 是一个建立在容器技术之上的持续交付系统。Drone 使用一个简单的 YAML 构建文件，在 Docker 容器中定义和执行构建管道。

简而言之，[Harness CI (aka Drone)](https://drone.io/) 是一个 **持续集成平台**，它被用于 容器 流水线  等场景


![控制面板](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drone/drone-gui-websoft9.png)


## 准备

在参阅本文档使用 Harness CI (aka Drone) 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [Apache 2.0](https://opensource.org/licenses/Apache-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口