---
sidebar_position: 1
slug: /codeserver
tags:
  - code-server
  - Online Code Editor
---

# code-server Getting Started

[code-server](https://github.com/cdr/code-server) is a web based IDE, it help you run VS Code on any machine anywhere and access it in the browser. It is also server-powered that take advantage of large cloud servers to speed up tests, compilations, downloads, and more.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/codeserver/codeserver-consolegui-websoft9.png)

If you have installed Websoft9 code-server, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for code-server
4. [Get](./user/credentials) default username and password of code-server

## code-server Initialization

### Steps for you

1. Use local Chrome or Firefox to access the URL *http://DNS* or *http://Cloud Server Internet IP*. You will enter login page of code-server.
   ![code-server login websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/en/codeserver/codeserver-login-websoft9.png)

2. Log in code-server web console. ([Don't have password?](./user/credentials)) 
   ![code-server console websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/en/codeserver/codeserver-consolegui-websoft9.png)

3. Open the WorkSpace directory at **code-server** console
   ![code-server directory](https://libs.websoft9.com/Websoft9/DocsPicture/en/codeserver/codeserver-openfolder-websoft9.png)

   > Default workspace directory is: */data/wwwroot/codeserver/volumes/config/workspace*  

4. Open the 【Terminal】windows, run the `node` command, you can view the its version
   ![code-server open Terminal](https://libs.websoft9.com/Websoft9/DocsPicture/en/codeserver/codeserver-terminal-websoft9.png)

5. You can install more software by yourself, refer to: [Set Develop Runtime](#install-software)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

## code-server QuickStart

Coming soon...

> More guide about code-server, please refer to [code-server Documentation](https://hub.docker.com/r/linuxserver/code-server).

## code-server Setup

### Reset Password

You can't reset code-server by web console, you should reset it by recreate container:

1. Use SFTP to login server, and modify **APP_PASSWORD** in the [.env file](#path) code-server directory
   ```
   APP_VERSION=latest
   APP_PORT=9001
   APP_PASSWORD=123456
   ```
2. Recreate code-server container
   ```
   sudo docker-compose up -d
   ```

### Modify port

Modify port is same with reset password, the difference is just modify the **APP_PORT** value

### Install software{#install-software}

You can install more software by **code-server console**, the below is installing Java for you:

1. Login to code-server console, and open the【Terminal】windows, then run the command `sudo su` 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-sudosu-websoft9.png)

   > Password is the same with code-server console

2. Update apt repository
   ```
   apt update
   ```

3. Install Java and verify it
   ```
   #1 Install JRE
   apt-get install openjdk-8-jre

   #2 Check Java version
   java -version
   ```

### Runtime Backup

Since code-server runs on containers, if you plan to back up the environment after the container is installed for a long time, you need to create a custom container image as follows:

1. Login your server
2. Run the docker commit command to create image
   ```
   #1 Create image
   sudo docker commit -m "add java" -a "your name" codeserver codeserver-java:latest

   #2 Look over image
   sudo docker image ls
   ```

### Multi-developer{#multi-developer}

The current deployment scheme has only one code-server by default. Since it does not support multiple users, it is not suitable for multiple development scenarios of collaborative work.  

So how can we support the collaborative use of code-server by multiple developers? Designed from a macro perspective, it needs to be used by multiple developers. Each developer can allocate the following resources to achieve this requirement:

1. Allocate a host port separately
2. Assign a code-server directory separately
3. Run a code-server container separately

You can refer the below sample:  

1. Run the below command to create new code-server directory for new user
   ```
   # CP directory to new folder user1
   cd /data/wwwroot
   cp -r codeserver user1

   # Delete the old data
   rm -rf user1/volumes
   ```

2. Edit the */data/wwwroot/user1/.env* file, set the you value for **APP_PORT,APP_PASSWORD,APP_CONTAINER_NAME**, save it
   ```
   APP_PORT=9001
   APP_PASSWORD=123456
   APP_CONTAINER_NAME=codeserver
   ```
   > APP_PORT and APP_CONTAINER_NAME must different from the already existing code-server


3. Recreate code-server for new user
   ```
   cd /data/wwwroot/user1
   sudo docker-compose  up -d
   ```

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage code-server
  

通过运行`docker ps`，可以查看到 code-server 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 code-server 本身的参数：

### Path{#path}

code-server 日志目录： */data/wwwroot/codeserver/volumes/config/data/logs*  
code-server 工作目录： */data/wwwroot/codeserver/volumes/config/workspace*  
code-server Extension 目录： */data/wwwroot/codeserver/volumes/config/extensions*  

### Port

无特殊端口


### Version

```shell
docker inspect -f '{{ index .Config.Labels "build_version" }}' codeserver
```

### Service

```shell
sudo docker start | stop | restart | stats codeserver
```

### CLI

```
code-server -h
```

### API



