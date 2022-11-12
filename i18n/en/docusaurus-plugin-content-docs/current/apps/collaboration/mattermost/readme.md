---
sidebar_position: 1
slug: /mattermost
tags:
  - Mattermost
  - Team collaboration
  - Team communication
---

# Mattermost Getting Started

[Mattermost](https://mattermost.com/) is an open source, self-hosted Slack-alternative. As an alternative to proprietary SaaS messaging, Mattermost brings all your team communication into one place, making it searchable and accessible anywhere.

![](https://ucarecdn.com/8cd90d9d-8902-4845-a15b-f4664e5fcfb3/-/format/auto/-/quality/lighter/-/max_icc_size/10/-/resize/1288x/)

If you have installed Websoft9 Mattermost, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Mattermost
4. [Get](./user/credentials) default username and password of Mattermost


## Mattermost Initialization{#init}

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will enter the register interface of Mattermost
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-install-websoft9.png)
2. Set the username and password, start to create administrator account of Mattermost
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-createdaccount-websoft9.png)
3. Create a new team or Go to system console
4. Open **Settings** > **Display** to set your language
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-display-websoft9.png)
5. Quit and reload Mattermost, you can see your language is in effect

> More useful Mattermost guide, please refer to [Matterbase Administrator’s Guide](https://docs.mattermost.com/guides/administrator.html)


### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  


## Mattermost QuickStart


## Mattermost Setup

### Increase the number of Teams users

Log in to the console and set the [SITE CONFIGURATION] > [Users and Teams] > [Max Users Per Team] values to set the team size:  

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-maxusers-websoft9.png)

### Domain Binding（Modify URL）{#dns}

**[Domain name five-step setting](./administrator/domain_step)** After completion, you need to set the URL of Mattermost:

Log in Mattermost console, open: **ENVIRONMENT** > **Web Server**, modify **Site URL** value
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-urlset-websoft9.png)


### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in Mattermost Console, open **ENVIROMENT** > **SMTP**
   ![Set smtp](https://libs.websoft9.com/Websoft9/DocsPicture/en/mattermost/mattermost-smtpsendgrid-websoft9.png)

3. Enter the SMTP settings
   
4. Click the **Test Connection**, you can get the feedback *"no errors were..."* if SMTP is useful

### Install the plugin

For example, JITMI is used a lot.

### Language settings{#setlang}

Support multiple languages (including Chinese), log in to the console, open [SITE CONFIGURATION] > [Localization], set the language 

## Reference sheet{#parameter}

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Mattermost


Run `docker ps` command, view all Containers when Mattermost is running:

```bash
CONTAINER ID   IMAGE                                       COMMAND                  CREATED             STATUS                       PORTS                                                                NAMES
1c26e24d9c18   dpage/pgadmin4:latest                       "/entrypoint.sh"         About an hour ago   Up About an hour             443/tcp, 0.0.0.0:9090->80/tcp, :::9090->80/tcp                       pgadmin
1d96d7bd3dd8   mattermost/mattermost-team-edition:latest   "/entrypoint.sh matt…"   About an hour ago   Up About an hour (healthy)   8067/tcp, 8074-8075/tcp, 0.0.0.0:9001->8065/tcp, :::9001->8065/tcp   mattermost
4baf3c38539b   postgres:13-alpine                          "docker-entrypoint.s…"   About an hour ago   Up About an hour             5432/tcp                                                             mattermost-db
```


### Path{#path}

Mattermost installation directory:： */data/apps/mattermost*  
Mattermost data directory:： */data/apps/mattermost/data/mattermost_data*  
Mattermost log directory:： */data/apps/mattermost/data/mattermost_logs*  
Mattermost plugin directory:： */data/apps/mattermost/data/mattermost_plugins*  
Mattermost configuration file： */data/apps/mattermost/data/mattermost_config/config.json*  

> The config.json file contains database connection information

### Port{#port}

No special port

### Version{#version}

```shell
sudo docker exec -i mattermost /mattermost/bin/mattermost version
```

### Service{#service}

```shell
sudo docker start | stop | restart | stats mattermost
sudo docker start | stop | restart | stats mattermost-db
sudo docker start | stop | restart | stats pgadmin
```

### CLI{#cli}

Mattermost provides both 'mattermost' and 'mmctl' commands, [mattermost](https://docs.mattermost.com/administration/command-line-tools.html) is a server-side command, [mmctl]( https://docs.mattermost.com/administration/mmctl-cli-tool.html) API-based client commands

```
/opt/mattermost/bin/mattermost -h #In-container operations
/opt/mattermost/bin/mmctl -h
```

If you run /opt/mattermost/bin/mmctl version, the version will be slightly lower

### API

[Mattermost API Reference](https://api.mattermost.com/)