---
sidebar_position: 1
slug: /metabase
tags:
  - Metabase
  - Data Analysis
  - BI
---

# Metabase Getting Started

[Metabase](https://www.metabase.com/) is the easy, open source way for everyone in your company to ask questions and learn from data.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-product-screenshot.png)

If you have installed Websoft9 Metabase, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Metabase
4. [Get](./user/credentials) default username and password of Metabase

## Metabase Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will enter the login page(if the page is not a login page, please follow steps 3-7)  
![Metabase login](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-login-websoft9.png)

2. Login it to Metabase console [(Don't know password?)](./user/credentials) 
![Metabase admin](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-dashborad-websoft9.png)

3. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will enter the register interface of Metabase
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-start-websoft9.png)
4. You may wait for 1-3 Minutes for the loading of Metabase
![Start Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-starty-websoft9.png)

5. Click the **Let's get started** button and set your administrator account, then go to next step
6. Add your data: you can select the type of Database which will be analyzed or  click **I'll add my data later** then Metabase will create a Demo from H2 Database
![Add data to Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-installdb-websoft9.png)

7. Once you have completed the installation, click the button **Take me to Metabase** to log in Metabase Console
![Metabase installation successful](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-installss-websoft9.png)

8. Take the H2 demo data as an example to start data analysis work.
![Metabase H2](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-dashborad-websoft9.png)

9. Log in Metabase Console, go to **Metabase Admin** page like below
![Metabase Admin](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-admin-websoft9.png)

10. Click **Add a database** to add a new data source for Metabase
![Metabase Data source](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-adddb-websoft9.png)

11. Click **People** tab on the top of Metabase Admin, you can add user and modify password
![Metabase People](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-users-websoft9.png)

> More useful Metabase guide, please refer to [Metabase Documentation](https://metabase.com/docs/latest/)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Metabase QuickStart

下面以 xxx 进行数据分析作为范例。

## Metabase Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in Metabase Console
3. 
4. Enter the SMTP settings
![Metabase SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-smtp-websoft9.png)

4. Click the **Test Connection**, you can get the feedback *"no errors were..."* if SMTP is useful

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Metabase


通过运行`docker ps`，可以查看到 Metabase 运行时所有的 Container：

```
CONTAINER ID   IMAGE                      COMMAND                  CREATED       STATUS       PORTS                                                  NAMES
cf73ba27aee6   metabase/metabase:latest   "/app/run_metabase.sh"   2 hours ago   Up 2 hours   0.0.0.0:9001->3000/tcp, :::9001->3000/tcp              metabase
146ea6d51aab   mysql:5.7                  "docker-entrypoint.s…"   2 hours ago   Up 2 hours   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   metabase-mysql
5498e289af92   phpmyadmin                 "/docker-entrypoint.…"   2 hours ago   Up 2 hours   0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin

```

下面仅列出 Metabase 本身的参数：

### Path{#path}

Metabase 源码目录： */data/wwwroot/metabase/data*  
Metabase 插件目录： */data/wwwroot/metabase/plugins*  
Metabase 配置文件： */data/wwwroot/metabase/metabase.conf*  

### Port{#port}

| 端口号 | 用途                                           | 必要性 |
| ------ | ---------------------------------------------- | ------ |
| 9001   | Metabase 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |

### Version{#version}

```shell
# Matebase Version
curl https://api.github.com/repos/metabase/metabase/releases/latest |jq -r .tag_name
```

### Service{#service}

```shell
sudo docker  start | stop | restart | status metabase
sudo docker  start | stop | restart | status metabase-mysql
```

### CLI{#cli}

Matebase 暂时未提供命令行工具

### API

[Matebase API](https://www.metabase.com/docs/latest/api-documentation.html)
