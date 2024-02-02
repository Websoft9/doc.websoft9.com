# Harness CI (aka Drone)

Drone is a continuous delivery system built on container technology. Drone uses a simple YAML build file, to define and execute build pipelines inside Docker containers.。  

简而言之，[Harness CI (aka Drone)](https://drone.io/) 是一个 ** Container-Native Continuous Delivery Platform**，它被用于   等场景。   


![Dashboard](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drone/drone-gui-websoft9.png)


## 准备

在参阅本文档使用 Harness CI (aka Drone) 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [](https://some_license_url) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口