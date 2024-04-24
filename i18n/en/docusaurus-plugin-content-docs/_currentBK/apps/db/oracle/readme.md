---
sidebar_position: 100
slug: /oracle
tags:
  - Oracle
---

# Oracle Getting Started

Oracle Database offers market-leading performance, scalability, reliability, and security.

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/oracle/oracle-database-1024x410.jpg)

If you have installed Websoft9 Oracle, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Connect your Server and get **[default username and password](./user/credentials)** of Oracle
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Oracle
5. If you want to enable **Oracle Database Enterprise or Standard**, you should complete the below steps:  

   - [Register you Oracle free user account](https://profile.oracle.com/myprofile/account/create-account.jspx)

   - Login to [Oracle Database Repositories](https://container-registry.oracle.com/) and accept **Oracle Standard Terms and Restrictions**

      ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/oracle/oracle-registryagree-websoft9.png)
      ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/oracle/oracle-registryagreess-websoft9.png)

   - Connect your Server and run the below commands to run Oracle Database by yourself.

     ```
     cd /data/apps/oracle
     docker login container-registry.oracle.com/database/enterprise
     docker compose up -d
     ```

## Oracle Initialization

### Steps for you

1. Using local browser to visit the URL *`<https://Server's Internet IP:5500/em>`*, you will enter Oracle EM login page

   > URL must use https

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/oracle/oracle-emlogin-websoft9.png)

2. Input your Oracle Database credential([Don't have password?](./user/credentials)) and login it successfully

   ![Oracle EM](http://libs.websoft9.com/Websoft9/DocsPicture/en/oracle/oracle-emgui-websoft9.png)

3. When you can see Oracle EM, it means you Oracle instance is running.  

4. Then you can use sqlplus by below commands

   ```
   sudo docker exec -it oracle bash
   sqlplus SYS  AS SYSDBA
   ```

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Oracle QuickStart

This task **Create new table** is for your Oracle QuickStart

1. 使用 [CloudBeaver 连接 Oracle](#cloudbeaver) 数据库

2. 创建一个数据表

3. 向数据表中增加内容

4. 查看新增的数据

## Oracle Setup

### Oracle Remote access{#remote}

应用自身已经开启远程访问，只需在云控制台安全组启用 `TCP:1521` 端口即可。  

### Reset Oracle password{#resetpw}

忘记管理员密码时，运行下面的命令重置密码:  

```
docker exec -it oracle ./setPassword.sh <your_password>
```

### Get SID Or Servce Name{#getsid}

1. 进入 sqlplus

    ```
    docker exec -it oracle sqlplus / as sysdba 
    ```

2. 运行查询实例信息的 SQL 命令，instance_name 即所需的信息

    ```
    SQL> show parameter instance

    NAME                                 TYPE        VALUE
    ------------------------------------ ----------- ------------------------------
    active_instance_count                integer
    instance_abort_delay_time            integer     0
    instance_groups                      string
    instance_mode                        string      READ-WRITE
    instance_name                        string      XE
    instance_number                      integer     0
    instance_type                        string      RDBMS
    open_links_per_instance              integer     4
    parallel_instance_group              string
    ```

### Oracle Clients{#client}

Oracle Database 支持多种客户端，有第三方工具，也有官方工具。

连接客户端所需的主要连接信息如下：

- 用户名: sys
- Role：SYSDBA
- Port: 1521 或 其他自定义的端口
- [服务名称或 SID](#getsid)

#### Web Based client: CloudBeaver{#cloudbeaver}

1. 本地浏览器访问：*`http://服务器公网IP:9090`*，访问 [CloudBeaver](./cloudbeaver)

2. 新建一个 Oracle 数据库连接
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-cloudbeaver001-websoft9.png)

3. 连接成功的界面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-cloudbeaver002-websoft9.png)

#### Local GUI client: Navicat

1. 下载并安装 Navicat for Oracle

2. 新建一个 Oracle 数据库连接，主要参数说明：  

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-navicat001-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-navicat002-websoft9.png)

3. 连接成功后的界面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-navicat003-websoft9.png)

#### Command line client: SQL*Plus

SQL*Plus 是官方提供的命令行客户端，运行下面的命令即可进入 **SQLPlus** 的操作模式：  

```
docker exec -it oracle sqlplus / as sysdba
```

#### Local develop client: SQL Developer

SQL Developer是 SQL*Plus 的图形版本，用 Java 编写，支持 SQL 和 PL/SQL 开发。您可以使用标准数据库身份验证连接到任何 Oracle 数据库模式。

#### Web develop client: APEX

[APEX](./apex) 是用于 Oracle 数据库的 Web 应用程序开发工具。

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Oracle

Run `docker ps`, view all containers when Oracle is running:  

```bash
CONTAINER ID   IMAGE                                                   COMMAND                  CREATED        STATUS                 PORTS                                                                                                                                                      NAMES
0bd5dabde1ff   container-registry.oracle.com/database/express:latest   "/bin/sh -c 'exec $O…"   19 hours ago   Up 3 hours (healthy)   0.0.0.0:1521->1521/tcp, :::1521->15                                                                    21/tcp, 0.0.0.0:5500->5500/tcp, :::5500->5500/tcp   oracle
e8214ddd441c   dbeaver/cloudbeaver:latest                              "./run-server.sh"        2 hours ago    Up 2 hours             0.0.0.0:9093->8978/tcp, :::9093->89                                                                    78/tcp                                              cloudbeaver
```

### Path{#path}

Oracle configuration file： */data/apps/oracle/dbconfig*

### Port{#port}

In addition to common ports such as 80, 443, etc., the following ports may be used:

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 1521   | Oracle Database Server | Optional   |
| 5500   | HTTPS access Oracle EM  | Optional   |

### Version {#version}

```
docker exec -it oracle sqlplus / as sysdba
```

### Service {#service}

```shell
sudo docker start | stop | restart | stats oracle
```

### CLI {#cli}

Oracle Database 提供了大量的命令工具：

- sqlplus 客户端工具
- expdp 导出
- impdp 导出
- rman 备份与恢复

### API {#api}

Oracle 通过 [Oracle REST Data Services](https://www.oracle.com/database/technologies/appdev/rest.html)  实现安全访问 Oracle 数据库。  
