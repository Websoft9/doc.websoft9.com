---
sidebar_position: 1
slug: /pydio
tags:
  - Pydio Cells
  - File sync and share
  - knowledge Management
---

# Pydio Cells Getting Started

 [Pydio Cells](https://pydio.com/) 是自托管企业文档共享与协作 (DSC) 市场的开源软件。Pydio Cells 弥合了快速发展的开源软件和企业级解决方案之间的差距，为具有安全意识的组织提供了一个他们可以依靠的平台来共享文档和安全协作。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-gui-websoft9.png)

If you have installed Websoft9 Jenkins, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Pydio Cells
4. [Get](./user/credentials) default username and password of Pydio Cells


## Pydio Cells Initialization{#init}

### Steps for you

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   
2. 选择语言，点击"Start Wizard"
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install001-websoft9.png)

3. 设置管理员账号，进入下一步
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install002-websoft9.png)

4. 选择Mysql数据库，填写数据库信息（[查看数据库账号密码](./user/credentials)），点击“test db connection”进入下一步
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install003-websoft9.png)

5. 进入高级设置，设置默认语言为“简体中文”，点击“Install Pydio”，开始安装
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install004-websoft9.png)

6. 安装完成后，登录后台
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-login-websoft9.png)

7. 后台界面
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-bk-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


## Pydio Cells QuickStart

下面以 **Pydio Cells 构建文档管理系统** 作为一个任务，帮助用户快速入门：

## Pydio Cells Setup

## Reference sheet{#parameter}

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Pydio Cells

通过运行`docker ps`，可以查看到 Pydio Cells 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 Pydio Cells 本身的参数：

### Path{#path}

Pydio Cells installation directory： */data/wwwroot/cells*  

### Port{#port}

无特殊端口

### Version{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats pydio
```

### CLI{#cli}

[Cells Client](https://pydio.com/en/docs/developer-guide/cells-client)

### API

[API Documentation](https://pydio.com/en/docs/developer-guide)

