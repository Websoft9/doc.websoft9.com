---
sidebar_position: 1
slug: /scratch
tags:
  - Scratch
  - Block-based Visual Programming
---

# Scratch Getting Started

[Scratch](https://scratch.mit.edu/) is a free programming language and online community where you can create your own interactive stories, games, and animations.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/scratch/scratch-gui-websoft9.png)

If you have installed Websoft9 Scratch, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Scratch
4. [Get](./user/credentials) default username and password of Scratch

## Scratch Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://Domain* or *http://Internet IP*, you can use Scratch
   ![Scratch GUI](https://libs.websoft9.com/Websoft9/DocsPicture/en/scratch/scratch-gui-websoft9.png)

2. Scratch loads data for more than 20M for the first time. If your network bandwidth is insufficient, the loading will be slow and wait patiently.

> More useful Scratch guide, please refer to [Scratch Documentation](https://en.scratch-wiki.info)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**[Scratch opens slowly?](./scratch/admin#slowly)**

## Scratch QuickStart


## Scratch Setup

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Scratch 

Run `docker ps` command, view all Containers when Scratch is running:  

```bash
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                                   NAMES
537d4d38eef3   websoft9dev/scratch:latest   "nginx -g 'daemon of…"   58 seconds ago   Up 57 seconds   0.0.0.0:9001->80/tcp, :::9001->80/tcp   scratch
```


### Path{#path}

Scratch installation directory： */data/apps/scratch*  
Scratch site directory： */data/apps/scratch/data/scratch/build*   

### Port{#port}

No special port  

### Version{#version}


### Service{#service}

```shell
sudo docker start | stop | restart scratch
```

### CLI{#cli}


### API

[Scratch API](https://en.scratch-wiki.info/wiki/Scratch_API)

