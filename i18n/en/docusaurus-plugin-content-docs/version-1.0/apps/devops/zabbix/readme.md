---
sidebar_position: 1
slug: /zabbix
tags:
  - Zabbix 
  - DevOps
---

# zabbix Getting Started

[Zabbix](https://www.zabbix.com) is the ultimate enterprise-level software designed for real-time monitoring of millions of metrics collected from tens of thousands of servers, virtual machines and network devices. 

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-gui-websoft9.png)


If you have installed Websoft9 zabbix, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for zabbix
4. [Get](./user/credentials) default username and password of zabbix


## Zabbix  Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *https://DNS* or *https://Server's Internet IP*, you can access the login page of Zabbix  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-login-websoft9.png)

2. Login to Zabbix console([default username and password](./user/credentials))

3. You can see the Zabbix dashboard
   ![Zabbix Dashboard](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboard-websoft9.png)

4. Go to the User profile of Zabbix Administrator, change your language if you want
   ![Zabbix change language](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-changelang-websoft9.png)
   ![Zabbix change language](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboardzh-websoft9.png)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Zabbix QuickStart

1. Use SSH to connect Zabbix Server

2. Get the IP installed Zabbix-Agent which for monitor Zabbix-Server itself
   ```
   docker inspect zabbix-agent | grep IPAddress
   ```
   > You should install [Zabbix-Agent](#zabbix-agent) if you want to test it on another Server

3. Login to Zabbix console, open:【Configuration】>【Hosts】 to list all hosts
   ![Zabbix add host](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-edithost001-websoft9.png)

4. Fill the IP in the form and save it
   ![Zabbix add host](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-edithost002-websoft9.png)

5. Return to hosts list page and enable you host. 

6. You can see the green status of Availability if monitor running

> More useful Zabbix guide, please refer to [Zabbix Documentation](https://www.zabbix.com/documentation/current)

## Zabbix Setup

### SMTP

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in Zabbix console as administrator, configure SMTP  
   - Open【Administrator】>【Media types】, selecting【Email】
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-opensmtp-websoft9.png)
   - Configure your settings of SMTP
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-smtpsetting-websoft9.png) 

3. Send test mail

### Zabbix language{#i18}

1. Login to Zabbix Console

2. Go to the User profile of Zabbix Administrator, change your language if you want
   ![Zabbix change language](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-changelang-websoft9.png)

> If you can't select language, refer to [https://zabbix.org/wiki/How_to/install_locale](https://zabbix.org/wiki/How_to/install_locale)

### Install Zabbix-Agent{#zabbix-agent}

1. Install [Zabbix-agent](https://www.zabbix.com/download?zabbix=5.0&os_distribution=centos&os_version=7&db=mysql&ws=apache) 
   ```shell
   rpm -Uvh https://repo.zabbix.com/zabbix/<ZABBIX_VERSION>/rhel/7/x86_64/zabbix-release-<ZABBIX_VERSION>-1.el7.noarch.rpm
   yum install zabbix-agent -y
   ```

2. Configure it by the file: */etc/zabbix/zabbix_agentd.conf*
   ```
   Server=SERVER_IP   
   ServerActive=SERVER_IP 
   Hostname=zabbix_web
   ```


### Resetting Password

There are two main measures to reset password.

**Changing password**

Take the steps below:

1. Login to Zabbix console, go to: 【Administrator】>【Users】, edit the target user
  ![Zabbix modify password](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-modifypw-websoft9.png)

2. Click 【Change Password】

**Forgot Password**

Try to retrieve your password through database modification when forgot it.  

Follow the steps below:

1. Login phpMyAdmin and open Zabbix database

2. Run the SQL command to reset your password
   ```
   sudo mysql -uroot -p new_password -e "update zabbix.users set passwd=md5(new_password) where alias='Admin';"


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Zabbix


Run `docker ps` command, view all Containers when Zabbix is running:

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


### Path{#path}

Zabbix installation directory: */data/zabbix*  
Zabbix configuration file: */data/zabbix/.env.xxx*    
Zabbix Persistent storage：*/data/wwwroot/zabbix/zbx_env  
Zabbix-Web Database configuration：*/data/wwwroot/zabbix/.env_db_mysql*  
Zabbix-Proxy Database configuration：*/data/wwwroot/zabbix/.env_db_mysql_proxy*   


### Port


### Version

```shell
docker images |grep zabbix-server
```

### Server

```shell
sudo docker start | stop | restart | stats  zabbix-server
sudo docker start | stop | restart | stats  zabbix-web
sudo docker start | stop | restart | stats  zabbix-proxy
sudo docker start | stop | restart | stats  zabbix-server
```

### CLI

### API

