[JupyterHub](https://jupyter.org/) 是一个 **多用户版的 Jupyter notebooks**，它被用于 源码仓库 在线 IDE  等场景。JupyterHub将笔记本的强大功能带给用户组。它给 用户无需负担即可访问计算环境和资源 具有安装和维护任务的用户。


![Notebook](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jupyterhub/jupyterhub-gui-websoft9.webp)


## 准备

在参阅本文档使用 JupyterHub 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）JupyterHub：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [bsd3Clause](https://opensource.org/licenses/BSD-3-Clause) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口