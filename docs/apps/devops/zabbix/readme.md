---
sidebar_position: 1
slug: /zabbix
tags:
  - Zabbix 
  - DevOps
---

# 快速入门

[Zabbix](https://www.zabbix.com/cn) 是一个开源的企业级监控解决方案，支持实时监控数千台服务器，虚拟机和网络设备，采集百万级监控指标。支持分布式架构，通过统一的 Web 界面监控自动监控大型动态环境。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-gui-websoft9.png)


部署 Websoft9 提供的 Zabbix 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Zabbix 的 **[默认管理员账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  Zabbix，务必先完成 **[域名五步设置](./dns#domain)** 过程


## Zabbix 初始化向导

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登录界面
   ![Zabbix 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-login-websoft9.png)

2. 输入账号密码后登录到后台（[不知道账号密码？](#账号密码)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboard-websoft9.png)

3. 打开用户管理界面，更换所需的语言（如果语言为灰色状态，参考[启用语言方案](/zh/solution-more.md#zabbix-多语言)）
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-changelang-websoft9.png)  
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboardzh-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## Zabbix 使用入门

下面继续上一节，通过连接一个客户端的实际应用场景，帮助用户快速入门。  

1. 使用SSH连接 Zabbix 服务器

2. 获取服务器上 Zabbix-Agent 容器虚拟机的IP（用于演示并监控服务器自身）
   ```
   docker inspect zabbix-agent | grep IPAddress
   ```
   > 若监控其他服务器，需先[安装Zabbix-Agent](#安装客户端)，然后参数上述步骤

3. 登录到 Zabbix 控制台后， 依次打开：【配置】>【主机】，打开主机列表
   ![Zabbix 添加主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-edithost001-websoft9.png)

4. 输入第二步获取的 IP 地址，保存配置
   ![Zabbix 添加主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-edithost002-websoft9.png)

5. 回到主机列表页，启用主机监控，当主机【可用性】列变成**绿色**即表明监控已成功

> 需要了解更多 Zabbix 的使用，请参考官方文档：[Zabbix Documentation](https://www.zabbix.com/documentation/current/)

## Zabbix 常用操作

### SMTP

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 登录到 Zabbix 后台，完成 SMTP 参数设置  
  
   - 依次打开：【管理】>【报警媒介类型】，选择【Email】
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-opensmtp-websoft9.png)
   - 准确的填写你的 SMTP 参数
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-smtpsetting-websoft9.png) 

3. 自测是否可以发送邮件

### 设置多语言

Zabbix 默认已经内置多种语言包，非常方便进行在线切换。

1. 登录到 Zabbix 后台

2. 依次打开：【管理】>【用户】，编辑用户信息管理界面，更换所需的语言
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-changelang-websoft9.png)  
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboardzh-websoft9.png)

> 如果语言为灰色状态,参考官方字符编码安装方案：[How to install locale](https://zabbix.org/wiki/How_to/install_locale)

### 安装 Zabbix 客户端

1. 安装 [Zabbix-agent](https://www.zabbix.com/download?zabbix=5.0&os_distribution=centos&os_version=7&db=mysql&ws=apache) 
   ```shell
   rpm -Uvh https://repo.zabbix.com/zabbix/<ZABBIX_VERSION>/rhel/7/x86_64/zabbix-release-<ZABBIX_VERSION>-1.el7.noarch.rpm
   yum install zabbix-agent -y
   ```

2. 配置 /etc/zabbix/zabbix_agentd.conf
   ```
   Server=SERVER_IP   
   ServerActive=SERVER_IP (服务端ip)   
   Hostname=zabbix_web (客户端主机名)   
   ```

### 重置密码

常用的 Zabbix 重置密码相关的操作主要有修改密码和找回密码两种类型：

##### 修改密码

1. 登录 Zabbix 后台，依次打开：【管理】>【用户】，编辑目标用户
  ![Zabbix 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-modifypw-websoft9.png)

2. 点击【修改密码】

##### 找回密码

如果用户忘记了密码，需要通过修改数据库相关字段来重置密码：

1. 登录 phpMyAdmin，进入 Zabbix 数据库

2. 在 SQL 窗口运行重置密码的命令
   ```
   sudo mysql -uroot -p new_password -e "update zabbix.users set passwd=md5(new_password) where alias='Admin';"
   ```


## 参数

Zabbix 应用中包含 Nginx, Docker, MySQL 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。  

本部署方案中的 Zabbix 采用 Docker部署，运行 `docker ps` 查看运行的容器。

```
$ docker ps
CONTAINER ID   IMAGE                                              COMMAND                  CREATED       STATUS                 PORTS                                         NAMES
18540fbd8378   zabbix/zabbix-web-apache-mysql:centos-5.2-latest   "docker-entrypoint.sh"   7 hours ago   Up 7 hours (healthy)   0.0.0.0:80->8080/tcp, 0.0.0.0:443->8443/tcp   zabbix-web
ed7551e10595   zabbix/zabbix-agent:centos-5.2-latest              "/sbin/tini -- /usr/…"   7 hours ago   Up 7 hours             0.0.0.0:10050->10050/tcp                      zabbix-agent
584c72d4110c   zabbix/zabbix-server-mysql:centos-5.2-latest       "/sbin/tini -- /usr/…"   7 hours ago   Up 7 hours             0.0.0.0:10051->10051/tcp                      zabbix-server
cacb13aa8f36   zabbix/zabbix-java-gateway:centos-5.2-latest       "docker-entrypoint.s…"   7 hours ago   Up 7 hours             0.0.0.0:10052->10052/tcp                      zabbix-java-gateway
7f86df1ec563   zabbix/zabbix-snmptraps:centos-5.2-latest          "/usr/sbin/snmptrapd…"   7 hours ago   Up 7 hours             0.0.0.0:162->1162/udp                         zabbix-snmptraps
01bf45e40f13   phpmyadmin/phpmyadmin                              "/docker-entrypoint.…"   8 hours ago   Up 8 hours             0.0.0.0:9090->80/tcp                          phpmyadmin

```

下面列出 Zabbix 本身的参数：

### 路径{#path}

Zabbix 安装目录: */data/zabbix*  
Zabbix 配置文件（环境变量）: */data/zabbix/.env.xxx*    
Zabbix 持久存储：*/data/wwwroot/zabbix/zbx_env  
Zabbix-Web 数据库配置：*/data/wwwroot/zabbix/.env_db_mysql*  
Zabbix-Proxy 数据库配置：*/data/wwwroot/zabbix/.env_db_mysql_proxy*   


### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9006   | Zabbix 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本

```shell
docker images |grep zabbix-server
```

### 服务

```shell
sudo docker start | stop | restart | stats  zabbix-server
sudo docker start | stop | restart | stats  zabbix-web
sudo docker start | stop | restart | stats  zabbix-proxy
sudo docker start | stop | restart | stats  zabbix-server
```

### 命令行

Jenkins 提供 CLI 客户端和 SSH CLI [两种方式](https://www.jenkins.io/zh/doc/book/managing/cli/)，下面是推荐的 客户端 CLI：

```shell
java -jar jenkins-cli.jar [-s JENKINS_URL] [global options...] command [command options...] [arguments...]
```

### API

Jenkins 提供可供远程访问的 [类似 REST API](https://www.jenkins.io/doc/book/using/remote-access-api/) 以便更好的实现自动化。
```
curl JENKINS_URL/job/JOB_NAME/buildWithParameters \
  --user USER:TOKEN \
  --data id=123 --data verbosity=high
```

同时，也提供了 Java, Python, Ruby 等语言的 API SDK 开发包。 

