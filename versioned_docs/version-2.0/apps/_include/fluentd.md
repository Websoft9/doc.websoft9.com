[Fluentd](https://www.fluentd.org/) 是一个 **数据收集和日志管理工具**，它被用于 日志分析 BI与数据可视化  等场景。Fluentd 是一个开源的数据收集器，能够统一处理和转发日志数据，支持多种数据源和输出目标。


![界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/fluentd/fluentd-gui-websoft9.png)


## 准备

在参阅本文档使用 Fluentd 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Fluentd：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口