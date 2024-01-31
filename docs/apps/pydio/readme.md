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

 [Pydio Cells](https://pydio.com/) 是自托管企业文档共享与协作 (DSC) 市场的开源软件，努力打造一个符合高级安全要求、合规性的企业的文档协作系统。  

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/cells/cells-gui-websoft9.png)


## 准备

部署 Websoft9 提供的 Pydio Cells 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Pydio Cells 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Pydio Cells **[域名五步设置](./administrator/domain_step)** 过程


## Pydio Cells 初始化向导{#init}

### 详细步骤

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   
2. 接受【安装协议】后，进入下一步  

4. 设置数据库连接（[不知道数据库账号密码](./user/credentials)），然后进入下一步
   ![cells 设置数据库连接](http://libs.websoft9.com/Websoft9/DocsPicture/en/cells/cells-installdbconfig-websoft9.png)

5. 设置管理员账号密码，并牢记之

6. 依次完成后续安装步骤，直至看到安装成功的提示
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/cells/cells-installdbss-websoft9.png)

7. 点击【Reload】后，登录进入 Cells 后台界面


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：


## Pydio Cells 使用入门

下面以 **Pydio Cells 构建文档管理系统** 作为一个任务，帮助用户快速入门：


## Pydio Cells 常用操作


## 参数{#parameter}

Pydio Cells 应用中包含 Nginx, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Pydio Cells 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
aed8241d7dec   mysql:5.7            "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   cells-db
1858341ccd48   pydio/cells:latest   "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:9001->8080/tcp, :::9001->8080/tcp              cells
```


下面仅列出 Pydio Cells 本身的参数：

### 路径{#path}

Pydio Cells 安装目录： */data/wwwroot/cells*  

### 端口{#port}

无特殊端口

### 版本{#version}

```shell
docker inspect cells | grep com.docker.compose.version
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats cells
```

### 命令行{#cli}

[Cells Client](https://pydio.com/en/docs/developer-guide/cells-client)

### API

[API Documentation](https://pydio.com/en/docs/developer-guide)

