[Harbor](https://goharbor.io/) 是一个 **Trusted cloud native repository**，它被用于 Software supply chain Container Artifact Repository  等场景。Harbor is an open source registry that secures artifacts with policies and role-based access control, ensures images are scanned and free from vulnerabilities, and signs images as trusted. 


![Dashbord](https://libs.websoft9.com/Websoft9/DocsPicture/zh/harbor/harbor-gui-websoft9.png)


## 准备

在参阅本文档使用 Harbor 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口