---
sidebar_position: 10
slug: /oracle
tags:
  - Oracle Database
  - Cloude Native Database
---

# 快速入门

Oracle Database （简称 “Oracle”）是一个以领先的性能、可扩展性、可靠性和安全性著称的数据库管理系统。Oracle Database 目前主要与 Oracle 公司其他软件集成，形成广泛的解决方案。  

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle-database-1024x410.jpg)

部署 Websoft9 提供的 Oracle 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Oracle 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 Oracle，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## Oracle 初始化向导{#wizard}

### 详细步骤

1.  SSH 登录 Oracle Database 所在的服务器 

2.  输入 `sqlpus` 命令，根据系统要求输入账号密码，数据库登录成功    
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle11gex-sqlrun-websoft9.png)  

3.  运行一条命令测试可用性，例如：select * from v$version;  （查询数据库版本信息）  


### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

**Oracle 能打开，但总是出现 502 错误？**  

参阅：

## Oracle 使用入门{#quickstart}

下面以 **××××** 作为一个任务，帮助用户快速入门：

## Oracle 常用操作{#guide}

### 开启远程访问{#remote}

镜像默认已经设置好了远程连接，只需开启安全组 `TCP:1521` 端口即可启用远程访问

### 图形化客户端

Oracle Database支持第三方可视化数据库管理工具，例如 Navicat,Maestro,Oracle 企业管理器等。下面以使用最为广泛的 Navicat 为例来说明如何管理本镜像的数据库：

1.  [下载](http://www.navicat.com.cn/download/navicat-for-oracle)并安装Navicat For Oracle

2.  新建一个Oracle连接，填写好连接参数（用户名为：system，密码为：123456；端口1521不能更改，另外请确保云服务器控制台上的安全组打开了TCP:1521），点击“连接测试”，成功标明参数没有问题。  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle11gex-conn-websoft9.png)

3.  点击确认后，进入数据库管理界面
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle11gex-ui-websoft9.png)

### 重置管理员密码{#resetpw}

忘记管理员密码时，请参考如下方案重置密码：  


## 参数{#parameter}

Oracle 应用中包含 Docker, Oracle 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 Oracle 运行时所有的服务组件：   

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### 路径{#path}

Oracle Database 配置文件路径：*/u01/app/oracle/product/11.2.0/db1/network/admin/listener.ora*    

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 1521   | 远程连接 Oracle Database | 可选   |

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats oracle
```

### 命令行{#cli}

### API{#api}

### 版权与约束

Oracle Database XE 对安装主机的规模和 CPU 数量不作限制（每台计算机一个数据库），但 XE 将最多存储 11GB 的用户数据，最多使用 1GB 内存，使用主机上的一个 CPU。版权说明：在使用软件之前，建议阅读[ Oracle Database 快捷版 11*g* 第 2 版的 OTN 许可协议](http://www.oracle.com/technetwork/licenses/database-11g-express-license-459621.html)