[AWX](https://www.ansible.com/community/awx-project) 是一个 **是Ansible Tower的开源版，Ansible Tower是一个可视化界面的服务器自动部署和运维管理平台。**，它被用于 流程机器人  等场景。AWX 是Ansible Tower的开源版，Ansible Tower是一个可视化界面的服务器自动部署和运维管理平台。可以通过可视仪表板，基于角色的访问控制，作业计划，集成通知和图形库存管理来集中和控制IT基础架构。


![login](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-login-websoft9.png)


## 准备

在参阅本文档使用 AWX 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）AWX：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口