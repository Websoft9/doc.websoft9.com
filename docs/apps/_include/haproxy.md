# HAProxy

提供高可用性、负载均衡，以及基于 TCP 和 HTTP 的应用程序代理，适用于负载特大的web站点。

简而言之，[HAProxy](http://www.haproxy.org/) 是一个 **一个提供高可用性、负载均衡，以及基于 TCP 和 HTTP 的应用程序代理的解决方案**，它被用于 负载均衡   等场景


![configuration](https://libs.websoft9.com/Websoft9/DocsPicture/zh/haproxy/HAProxy-configuration.png)


## 准备

在参阅本文档使用 HAProxy 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [GPL-2.0](https://opensource.org/licenses/GPL-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口