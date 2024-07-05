[Harbor](https://goharbor.io/) 是一个 **安全受信的容器镜像仓库平台**，它被用于 软件供应链 容器 制品仓库  等场景。Harbor 是一个开源注册表，它使用策略和基于角色的访问控制来保护工件，确保图像被扫描且没有漏洞，并将图像标记为受信任。


![Dashbord](https://libs.websoft9.com/Websoft9/DocsPicture/zh/harbor/harbor-gui-websoft9.png)


## 准备

在参阅本文档使用 Harbor 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口