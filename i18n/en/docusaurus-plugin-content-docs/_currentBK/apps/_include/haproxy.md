[HAProxy](http://www.haproxy.org/) 是一个 **a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications**，它被用于 Load Balancer  等场景。Provides a high availability load balancer and proxy server for TCP and HTTP-based applications.


![configuration](https://libs.websoft9.com/Websoft9/DocsPicture/zh/haproxy/HAProxy-configuration.png)


## 准备

在参阅本文档使用 HAProxy 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [GPL-2.0](https://opensource.org/licenses/GPL-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口