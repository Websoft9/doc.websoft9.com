---
sidebar_position: 10
slug: /oracle
tags:
  - Oracle Database
  - Cloude Native Database
---

# 快速入门

Oracle Database （简称 “Oracle”）是一个以领先的性能、可扩展性、可靠性和安全性著称的数据库管理系统。Oracle Database 目前主要与 Oracle 公司其他软件集成，形成广泛的解决方案。  

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-database-1024x410.jpg)

部署 Websoft9 提供的 Oracle 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:1521 和 TCP:5500** 端口已经开启
3. 在服务器中查看 Oracle 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 Oracle，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程
5. 针对于 **Oracle Database 企业版或标准版**，用户需额外如下几个步骤：

   - 到 Oracle 官方网站[注册](https://profile.oracle.com/myprofile/account/create-account.jspx)一个免费用户账号

   - 登录 [Oracle Database Repositories](https://container-registry.oracle.com/) 网站，阅读并同意 **Oracle Standard Terms and Restrictions**

      ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-registryagree-websoft9.png)
      ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-registryagreess-websoft9.png)

   - 连接到云服务器，运行下面的命令，拉取并启动 Oracle 数据库镜像
     ```
     cd /data/apps/oracle
     docker login container-registry.oracle.com/database/enterprise
     docker compose up -d
     ```

## Oracle 初始化向导{#wizard}

### 详细步骤

1. 本地浏览器访问：*https://服务器公网IP:5500/em* 进入 Oracle EM 登录界面 

   > 必须使用 https 访问

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-emlogin-websoft9.png)

2. 输入默认用户密码和密码后，进入 Oracle EM 控制台

   ![Oracle EM 登录](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-emgui-websoft9.png)

3. 完成以上步骤，即表明 Oracle 服务运行正常。 

4. 运行下面的命令，进入 Oracle 数据库容器中
   ```
   sudo docker exec -it oracle bash
   sqlplus SYS  AS SYSDBA
   ```


### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## Oracle 使用入门{#quickstart}

下面以 **新建一个数据表** 作为一个任务，帮助用户快速入门：

1. 使用 [CloudBeaver 连接 Oracle](#cloudbeaver) 数据库

2. 创建一个数据表

3. 向数据表中增加内容

4. 查看新增的数据

## Oracle 常用操作{#guide}

### 开启远程访问{#remote}

应用自身已经开启远程访问，只需在云控制台安全组启用 `TCP:1521` 端口即可。  

### 重置管理员密码{#resetpw}

忘记管理员密码时，运行下面的命令重置密码:  
```
docker exec oracle ./setPassword.sh <your_password>
```

### 获取 SID 或 Servce Name{#getsid}

1. 进入 sqlplus 
    ```
    $ docker exec -it oracle sqlplus / as sysdba 
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


### 客户端工具{#client}

Oracle Database 支持多种客户端，有第三方工具，也有官方工具。

连接客户端所需的主要连接信息如下：

* 用户名: sys
* Role：SYSDBA
* Port: 1521 或 其他自定义的端口
* [服务名称或 SID](#getsid)

#### Web 可视化客户端 CloudBeaver{#cloudbeaver}

1. 本地浏览器访问：*http://服务器公网IP:9090*，访问 [CloudBeaver](./cloudbeaver)

2. 新建一个 Oracle 数据库连接
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-cloudbeaver001-websoft9.png)

3. 连接成功的界面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-cloudbeaver002-websoft9.png)

#### 本地图形客户端 Navicat

1. 下载并安装 Navicat for Oracle

2. 新建一个 Oracle 数据库连接，主要参数说明：  

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-navicat001-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-navicat002-websoft9.png)

3.  连接成功后的界面
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle/oracle-navicat003-websoft9.png)

#### 命令行客户端 SQL*Plus

SQL*Plus 是官方提供的命令行客户端，运行下面的命令即可进入 **SQLPlus** 的操作模式：  

```
docker exec -it oracle sqlplus / as sysdba
```

#### 本地开发者客户端 SQL Developer

SQL Developer是 SQL*Plus 的图形版本，用 Java 编写，支持 SQL 和 PL/SQL 开发。您可以使用标准数据库身份验证连接到任何 Oracle 数据库模式。

#### Web 应用程序客户端 APEX

[APEX](./apex) 是用于 Oracle 数据库的 Web 应用程序开发工具。

## 参数{#parameter}

Oracle 应用中包含 Docker, Oracle, CloudBeaver 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 Oracle 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE                                                   COMMAND                  CREATED        STATUS                 PORTS                                                                                                                                                      NAMES
0bd5dabde1ff   container-registry.oracle.com/database/express:latest   "/bin/sh -c 'exec $O…"   19 hours ago   Up 3 hours (healthy)   0.0.0.0:1521->1521/tcp, :::1521->15                                                                    21/tcp, 0.0.0.0:5500->5500/tcp, :::5500->5500/tcp   oracle
e8214ddd441c   dbeaver/cloudbeaver:latest                              "./run-server.sh"        2 hours ago    Up 2 hours             0.0.0.0:9093->8978/tcp, :::9093->89                                                                    78/tcp                                              cloudbeaver
```

### 路径{#path}

Oracle Database 配置文件路径：*/data/apps/oracle/dbconfig*     

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 1521   | 远程连接 Oracle Database | 可选   |
| 5500   | HTTPS 访问 Oracle EM  | 可选   |

### 版本{#version}

```
docker exec -it oracle sqlplus / as sysdba
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats oracle
```

### 命令行{#cli}

Oracle Database 提供了大量的命令工具：

* sqlplus 客户端工具
* expdp 导出
* impdp 导出
* rman 备份与恢复

### API{#api}

Oracle 通过 [Oracle REST Data Services](https://www.oracle.com/database/technologies/appdev/rest.html)  实现安全访问 Oracle 数据库。  

### 版权与约束

Oracle Database XE 对安装主机的规模和 CPU 数量不作限制（每台计算机一个数据库），但 XE 将最多存储 11GB 的用户数据，最多使用 1GB 内存，使用主机上的一个 CPU。  

在使用软件之前，建议阅读[ Oracle Database 快捷版 11*g* 第 2 版的 OTN 许可协议](http://www.oracle.com/technetwork/licenses/database-11g-express-license-459621.html)