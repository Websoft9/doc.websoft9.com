---
sidebar_position: 1
slug: /mingdao
tags:
  - Mingdao
  - APaaS
  - No-code Development Platform
---

# Mingdao  Getting Started

[Mingdao ](https://www.mingdao.com/en/about) is leader of APaaS, No Code Platform, it provide rapid development Tool and middle-ground application solution for enterprise customer.

![](https://alifile.mingdaocloud.com/wwwhome/dist/pack/static/src-common-mdfeature-img-2x-yy02.jpg)

> Access [Mingdao official docs](https://docs.pd.mingdao.com/) to get more reference when you use this deployment solution

Websoft9 provides the free version of Mingdao Private Deployment. It has the following limitations over paid versions such as Standard and Professional:  

- The number of users does not exceed 30
- Maximum number of rows per worksheet: 100,000 rows

If you have installed Websoft9 Mingdao , the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:38881,8880** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Mingdao 
4. [Get](./user/credentials) default username and password of Mingdao 

## Mingdao  Initialization

### Steps for you

1. Use local browser to access the URL *http://DNS:38881* or *http://Server's Internet IP:38881* to access installation wizard

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-initial1-websoft9.png)

   > You can set any other port which you want to use

2. Then, go to 【Next】 step, start the initialization (need 3-5 minutes)

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-initial2-websoft9.png)

3. When complete the initialization, then start to **Data installation**

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-install1-websoft9.png)
   
   > You should register from official website to get the credential 

4. At last, **Register the administrator** account

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-set-admin-websoft9.png)

5. Access the Mingdao's URL (e.g **http://Server's IP:8880**) to login the backend
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-login-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-main-app-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-main-lib-websoft9.png)


> More guide about MingDao, please refer to [MingDao Documentation](https://docs.pd.mingdao.com/).

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Can't visit the start page of MingDao?**

Your TCP:38881 of Security Group Rules is not allowed, so there is no response from Chrome or Firefox.

**Can the port number of the access address not need **8880**?**

Yes, but you should enable your port at **[Inbound of Security Group Rule](https://support.websoft9.com/docs/faq/tech-instance.html)** of Cloud console


**After the server restarts or the IP changes, some services such as workflows cannot be used**

[Reference](./mingdao/admin#workflow)

**After server restart, the program cannot start**

[Reference](./mingdao/admin#restart)

## Mingdao QuickStart

Mingdao provides [tutorials and videos](https://help.mingdao.com/)

## Mingdao customized service

Websoft9, as a partner of Mindao, has the ability to quickly build software based on Mingdao. We can provide the following services to our customers:

* Quickly establish the basic data model based on actual business
* Refine the management process and integrate the business into the software operation
* Integrate Mingdao Cloud connections with other systems to break down enterprise data silos

![](https://alifile.mingdaocloud.com/wwwhome/dist/pack/static/src-common-partnerIntroduction-img-jj2.png)

Welcome customers and industry cooperation [contact us](./helpdesk#contact).

## Mingdao Setup

### Configuration 

Refer to [official docs](https://docs.pd.mingdao.com)

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in MingDao Console and go to 【Email settings】 at 【System settings】
   ![Mingdao SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/mingdao/mingdao-smtp-websoft9.png)

3. SMTP completed  

### Reset Password

There are two main measures to reset password.

### Changing password

Take the steps below:

1. Log in the MingDao backend, open 【System Setting】 to find the user account, of which you want to change password;

2. Start to change the password.

### Forgot Password

Try to retrieve your password through e-mail when forgot it.

Follow the steps below:

Coming soon...

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Mingdao 


Run `docker ps` command, view all Containers when Mingdao is running:

```bash
CONTAINER ID   IMAGE                                                                   COMMAND                  CREATED       STATUS       PORTS                       NAMES
1100b00c55ec   registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-community:3.7.0   "/Housekeeper/main -…"   2 hours ago   Up 2 hours   0.0.0.0:8880->8880/tcp      script_app_1
d6fa950fb107   registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-doc:1.2.0         "/bin/sh -c /app/ds/…"   2 hours ago   Up 2 hours   80/tcp, 443/tcp, 8000/tcp   script_doc_1
```



### Path{#path}

Mingdao installation directory： */data/apps/mingdao*  
Mingdao installation manager directory： */data/apps/mingdao/installer*  
Mingdao data directory： */data/mingdao/script/volume*   
Mingdao configuration file： */data/mingdao/script/docker-compose.yaml*  

### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 38881   | HTTP access to the Mingdao initialization page | Required   |
| 8880   | HTTP access to the Mingdao  | Optional   |


### Version{#version}

View in the console

### Service{#service}

```shell
cd /data/apps/mingdao/installer/
./service.sh restartall
```

### CLI{#cli}

[CLI](https://docs.pd.mingdao.com/deployment/docker-compose/command.html)

### API

[API](https://help.mingdao.com/API1.html)
