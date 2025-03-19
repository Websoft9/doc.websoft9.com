[Semaphore UI](https://semaphoreui.com/) 是一个 **Ansible, Terraform, OpenTofu, Bash, Pulumi 可视化平台**，它被用于 应用编排 CI/CD 流水线 运维自动化  等场景。Semaphore 是 Ansible、Terraform/OpenTofu、Bash 和 Pulumi 的现代 UI。它使您可以轻松运行 Ansible playbook，获取有关失败的通知，控制对部署系统的访问。


![控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/semaphore/semaphore-gui-websoft9.png)


## 准备

在参阅本文档使用 Semaphore UI 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Semaphore UI：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口