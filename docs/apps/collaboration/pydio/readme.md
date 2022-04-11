---
sidebar_position: 1
slug: /pydio
tags:
  - Pydio Cells
  - 网盘
  - 知识管理
  - 团队协作
---

# 快速入门

 [Pydio Cells](https://pydio.com/) 是自托管企业文档共享与协作 (DSC) 市场的开源软件。Pydio Cells 弥合了快速发展的开源软件和企业级解决方案之间的差距，为具有安全意识的组织提供了一个他们可以依靠的平台来共享文档和安全协作。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-gui-websoft9.png)


## 准备

部署 Websoft9 提供的 Pydio Cells 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Pydio Cells 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  Pydio Cells **[域名五步设置](./administrator/domain_step)** 过程


## Pydio Cells 初始化向导{#init}

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   
2. 选择语言，点击"Start Wizard"
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install001-websoft9.png)

3. 设置管理员账号，进入下一步
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install002-websoft9.png)

4. 选择Mysql数据库，填写数据库信息（[查看数据库账号密码](./setup/credentials)），点击“test db connection”进入下一步
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install003-websoft9.png)

5. 进入高级设置，设置默认语言为“简体中文”，点击“Install Pydio”，开始安装
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-install004-websoft9.png)

6. 安装完成后，登录后台
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-login-websoft9.png)

7. 后台界面
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/pydio/pydio-bk-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


## Pydio Cells 使用入门

下面以 **Pydio Cells 构建文档管理系统** 作为一个任务，帮助用户快速入门：


## Pydio Cells 常用操作


## 参数{#parameter}

Pydio Cells 应用中包含 Nginx, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Pydio Cells 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Pydio Cells 本身的参数：

### 路径{#path}

Pydio Cells 安装目录： */data/wwwroot/cells*  

### 端口{#port}

无特殊端口

### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats pydio
```

### 命令行{#cli}

[Cells Client](https://pydio.com/en/docs/developer-guide/cells-client)

### API

[API Documentation](https://pydio.com/en/docs/developer-guide)

