---
sidebar_position: 100
slug: /{{appname}}
tags:
  - {{trademark}}
---

# {{trademark}} Getting Started

{{trademark}} introduce

If you have installed Websoft9 {{trademark}}, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Connect your Server and get **[default username and password](./user/credentials)** of {{trademark}}
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for {{trademark}}

## {{trademark}} Initialization

### Steps for you

1. Using local browser to visit the URL *http://DNS* or *http://Server's Internet IP*, you will enter initial wizard of {{trademark}}

2. Complete initialization

3. login to your {{trademark}}([Don't have password?](./user/credentials))

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**{{trademark}} interface 502 error?**  

Refer to：

## {{trademark}} QuickStart

This task **xxxx** is for your {{trademark}} QuickStart

1. 

2.  

## {{trademark}} Setup

### Configure  SMTP{% raw %}{#smtp}{% endraw %}

1. Prepare your [SMTP parameter](./administrator/smtp)

2. Start to configure {{trademark}}

3. Test it

### DNS Additional Configure{% raw %}{#dns}{% endraw %}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for {{trademark}}  

1. step1

2. step2

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage {{trademark}}

Run `docker ps`, view all containers when {{trademark}} is running:  

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{% raw %}{#path}{% endraw %}

{{trademark}} configuration file： *path/config.php*    

### Port{% raw %}{#port}{% endraw %}

In addition to common ports such as 80, 443, etc., the following ports may be used:

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 8080   | {{trademark}} original port	 | Optional   |

### Version {% raw %}{#version}{% endraw %}

View in console

### Service {% raw %}{#service}{% endraw %}

```shell
sudo docker start | stop | restart | stats {{appname}}
```

### CLI {% raw %}{#cli}{% endraw %}

### API {% raw %}{#api}{% endraw %}