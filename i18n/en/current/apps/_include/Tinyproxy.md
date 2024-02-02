# Tinyproxy

Tinyproxy is a small, efficient HTTP/SSL proxy daemon released under the GNU General Public License. Tinyproxy is very useful in a small network setting, where a larger proxy would either be too resource intensive, or a security risk. One of the key features of Tinyproxy is the buffering connection concept. 

简而言之，[Tinyproxy](https://github.com/tinyproxy/tinyproxy) 是一个 **A light-weight HTTP/HTTPS proxy software**，它被用于 HTTP Server Application Gateway  等场景


![Dashboard](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tinyproxy/tinyproxy-gui-websoft9.png)


## 准备

在参阅本文档使用 Tinyproxy 时，需要确保如下几点：

- 应用是基于 Websoft9 安装的

- 应用的用途符合 [GPL-2.0](https://opensource.org/licenses/GPL-2.0) 开源许可协议

- 应用具备访问条件：[配置域名](./guide/appsetdomain) 或 **服务器安全组**开启网外端口