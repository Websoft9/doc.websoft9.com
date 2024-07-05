[NGINX](https://hub.docker.com/_/nginx) 是一个 **适用于静态网站部署的 NGINX 容器**，它被用于 HTTP 服务器 HTML  等场景。这是一个适用于部署静态网站（HTML/JS）的 NGINX 容器，也可以作为反向代理使用。NGINX 是高性能的 Web 代理服务器，具有优异的静态资源和高并发处理能力。


![architecture](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nginx/nginx-architecture-websoft9.png)


## 准备

在参阅本文档使用 NGINX 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [nginx](https://github.com/nginx/njs/blob/master/LICENSE) 开源许可协议

- 应用具备访问条件：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口