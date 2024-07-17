[Trivy](https://trivy.dev/) 是一个 **开源安全漏洞扫描**，它被用于 扫描监测  等场景。Trivy 是一个开源工具，用于扫描容器镜像、文件系统和代码仓库的漏洞。


![architecture](https://libs.websoft9.com/Websoft9/DocsPicture/zh/clamav/clamav-arch-websoft9.webp)


## 准备

在参阅本文档使用 Trivy 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口