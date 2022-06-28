---
sidebar_position: 1
slug: /cells
tags:
  - Pydio Cells
  - File sync and share
  - knowledge Management
---

# Pydio Cells Getting Started

 [Pydio Cells](https://pydio.com/) 是自托管企业文档共享与协作 (DSC) 市场的开源软件，努力打造一个符合高级安全要求、合规性的企业的文档协作系统。  

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/cells/cells-gui-websoft9.png)

If you have installed Websoft9 Pydio Cells, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Pydio Cells
4. [Get](./user/credentials) default username and password of Pydio Cells


## Pydio Cells Initialization{#init}

### Steps for you

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   
2. 接受【安装协议】后，进入下一步  

4. 设置数据库连接（[不知道数据库账号密码](./user/credentials)），然后进入下一步
   ![cells 设置数据库连接](http://libs.websoft9.com/Websoft9/DocsPicture/en/cells/cells-installdbconfig-websoft9.png)

5. 设置管理员账号密码，并牢记之

6. 依次完成后续安装步骤，直至看到安装成功的提示
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/cells/cells-installdbss-websoft9.png)

7. 点击【Reload】后，登录进入 Cells 后台界面

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
aed8241d7dec   mysql:5.7            "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   cells-db
1858341ccd48   pydio/cells:latest   "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:9001->8080/tcp, :::9001->8080/tcp              cells
```


下面仅列出 Pydio Cells 本身的参数：

### Path{#path}

Pydio Cells installation directory： */data/wwwroot/cells*  

### Port{#port}

无特殊端口

### Version{#version}

```shell
docker inspect cells | grep com.docker.compose.version
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats cells
```

### CLI{#cli}

[Cells Client](https://pydio.com/en/docs/developer-guide/cells-client)

### API

[API Documentation](https://pydio.com/en/docs/developer-guide)

