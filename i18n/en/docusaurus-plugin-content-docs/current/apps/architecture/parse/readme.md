---
sidebar_position: 1
slug: /parseserver
tags:
  - Parse Server
  - PaaS
  - Serverless
---

# Parse Server Getting Started

[Parse Server ](https://parseplatform.org/) is an open source backend or an API server module that can be deployed to any infrastructure that can run Node.js.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/dashboard.png)  

If you have installed Websoft9 Parse Server, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80,9091** is allowed
3. **[Get](./user/credentials)** default username and password of Parse Server
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Parse Server  
  
## Parse Server Initialization

### Steps for you
  
Since Parse cannot be visited by IP, so your should bind Domain name for it first  
Refer to [Domain binding](./administrator/domain_step) to complete it now

1. Using local Chrome or Firefox to visit the URL *http://domain name*, go to login Parse Dashboard 
   ![Parse Dashboard login](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/ParseServer-loginpage-websoft9.png)

2. Input username and password([view credentials](./user/credentials)) and go to the Console page
   ![Parse Dashboard console gui](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/parse-backend-websoft9.png)

3. Suggest you to modify the Parse Dashboard's password now

> More useful Parse Server guide, please refer to [Parse Server Documentation](https://docs.parseplatform.org) 

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## Parse Server QuickStart
  
More guide about Parse Server, please refer to [Parse Server Documentation](https://docs.parseplatform.org)

## Parse Server Setup

Each of the following solutions has been proven to be effective and we hope to be helpful to you.

### Domain binding

Please complete the **domain name resolution** work before the domain name is bound, and confirm that the resolution is successful.

Parse Server domain name binding steps:

1. Use SSH to connect your Cloud Server and run the following command
   ``` shell
   wget https://raw.githubusercontent.com/Websoft9/ansible-Parse-Server/master/script/parse-set-domain.sh && chmod +x parse-set-domain.sh &&./parse-set-domain.sh
   ```
2. Enter two different domain names as prompted
   ```   
   Input Parse Server Domain: parseserver.websoft9.com
   Input Parse Dashboard Domain: parsedashboard.websoft9.com
   ```
3. If there is no problem with the domain name format, you will get a success message "Configure Done!"
4. Domain binding completed
  
## Domain modify

Modifying a domain name is different from binding a domain name. Please strictly refer to the following steps:

1. Using SFTP to connect Cloud Server
2. Modify the the two Domain name in the file */etc/nginx/conf.d/default.conf* 
3. Modify the the one Domain name in the file */etc/parse-server/parse-dashboard.json* 
4. Restart Service like below
   ```
   sudo systemctl restart parse-dashboard
   sudo systemctl restart parse-server
   sudo systemctl restart nginx
   ```
  
## Modify Parse Dashboard Credentials

Parse Dashboard's credentials is in its configuration file, refer to the following steps to modify it

1. Use SSH or SFTP tool to connect Cloud Server
2. Edit * /etc/parse-server/parse-server.json* file and modify **users** item
   ```
    "users": [
    {
      "user":"admin",
      "pass":"admin"
    } ]
   ```
3. Restart Parse Dashboard Service
   ```
   systemctl restart parse-dashboard
   ```  
  
## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Parse Server

### Path{#path}
  
**Parse Server**

Parse Server  installation directory: */usr/lib/node_modules/parse-server*  
Parse Server  configuration file: */etc/parse-server/parse-server.json*  
Parse Server  logs directory: */var/log/parse-server*  

> The database connection information is in the Parse Server configuration file, once you have changed the database you should change the configuration also

**Parse Dashboard**

Parse Dashboard  installation directory: */usr/lib/node_modules/parse-server*  
Parse Dashboard  configuration file: */etc/parse-server/parse-server.json*  
Parse Dashboard  logs: *you can view the logs on the Parse Dashboard Console*

### Port{#port}


| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 80 | HTTP requests for Parse Server  | Required |
| 443 | HTTPS requests Parse Server  | Optional |
| 20217 | Remote connect MongoDB | Optional |
| 9091 | Web managment GUI for MongoDB | Optional |

### Version{#version}

You can see the version from product page of Marketplace.

### Service{#service}

```shell
sudo systemctl start | stop | restart | status parse-server 
sudo systemctl start | stop | restart | status parse-dashboard
```

### CLI{#cli}


### API

[Parse API](https://docs.parseplatform.org/parse-server/guide/#using-parse-sdks-with-parse-server)