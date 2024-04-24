---
sidebar_position: 100
slug: /apex
tags:
  - APEX
---

# APEX Getting Started

APEX introduce

If you have installed Websoft9 APEX, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Connect your Server and get **[default username and password](./user/credentials)** of APEX
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for APEX

## APEX Initialization

### Steps for you

1. Using local browser to visit the URL *http://DNS* or *http://Server's Internet IP*, you will enter initial wizard of APEX

2. Complete initialization

3. login to your APEX([Don't have password?](./user/credentials))

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**APEX interface 502 error?**  

Refer to：

## APEX QuickStart

This task **xxxx** is for your APEX QuickStart

1. 

2.  

## APEX Setup

### Configure  SMTP{#smtp}

1. Prepare your [SMTP parameter](./administrator/smtp)

2. Start to configure APEX

3. Test it

### DNS Additional Configure{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for APEX  

1. step1

2. step2

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage APEX

Run `docker ps`, view all containers when APEX is running:  

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}

APEX configuration file： *path/config.php*    

### Port{#port}

In addition to common ports such as 80, 443, etc., the following ports may be used:

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 8080   | APEX original port	 | Optional   |

### Version {#version}

View in console

### Service {#service}

```shell
sudo docker start | stop | restart | stats apex
```

### CLI {#cli}

### API {#api}