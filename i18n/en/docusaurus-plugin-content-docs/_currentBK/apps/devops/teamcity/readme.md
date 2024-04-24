---
sidebar_position: 100
slug: /teamcity
tags:
  - TeamCity
---

# TeamCity Getting Started

TeamCity introduce

If you have installed Websoft9 TeamCity, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Connect your Server and get **[default username and password](./user/credentials)** of TeamCity
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for TeamCity

## TeamCity Initialization

### Steps for you

1. Using local browser to visit the URL *http://DNS* or *http://Server's Internet IP*, you will enter initial wizard of TeamCity

2. Complete initialization

3. login to your TeamCity([Don't have password?](./user/credentials))

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**TeamCity interface 502 error?**  

Refer to：

## TeamCity QuickStart

This task **xxxx** is for your TeamCity QuickStart

1. 

2.  

## TeamCity Setup

### Configure  SMTP{#smtp}

1. Prepare your [SMTP parameter](./administrator/smtp)

2. Start to configure TeamCity

3. Test it

### DNS Additional Configure{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for TeamCity  

1. step1

2. step2

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage TeamCity

Run `docker ps`, view all containers when TeamCity is running:  

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}

TeamCity configuration file： *path/config.php*    

### Port{#port}

In addition to common ports such as 80, 443, etc., the following ports may be used:

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 8080   | TeamCity original port	 | Optional   |

### Version {#version}

View in console

### Service {#service}

```shell
sudo docker start | stop | restart | stats teamcity
```

### CLI {#cli}

### API {#api}