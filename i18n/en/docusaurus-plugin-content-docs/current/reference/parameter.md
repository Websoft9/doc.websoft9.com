---
sidebar_position: 2.0
slug: /parameter
---

# Parameter

Various parameters such as server, network, port and path involved in Websoft9 are listed below:  

## Paths{#path}

### Websoft9 Console

- **Websoft9 installation configuration directory**: */data/websoft9/source*
- **Websoft9 Docker Compose directory**: */data/websoft9/source/docker*
- **Websoft9 Systemd configuration directory**: */opt/websoft9  
- **Websoft9 plugin directory**: */usr/share/cockpit  
- **Websoft9 backup directory**: */data/websoft9/vl_backup
- **Websoft9 application persistent storage directory**: */var/lib/docker/volumes* 

### Docker on the server

- Docker Volumes: */var/lib/docker/volumes*    
- Docker image directory: */var/lib/docker/image*   
- Docker program directory: */var/lib/docker*  
- Docker Server configuration file: */etc/docker/daemon.json*    
- Docker system service: */lib/systemd/system/docker.service*  

## Ports{#port}

Users can view the ports used on the server with `netstat -tunlp'.      

The following are the most commonly used ports, please go to the Security Group to **enable or disable** it. 

### Application access ports{#apps-port}

| Port number | Purpose | Necessity |
| --- | --- | --- |
| 9000 | Websoft9 Console | required |
| 80 | Websoft9 Console, Websoft9 Gateway, Apply HTTP Access | required |
| 443 | Websoft9 Gateway, Application HTTPS Access | required |
| 9001-9999 | Application Extranet Access | optional |


### Server management ports{#server-port}

| Port number | Purpose | Necessity |
| --- | --- | --- |
| 21 | Linux server FTP port | optional |
| 22 | Linux server SSH port | optional |
| 2375 or 2376 (TLS) | Docker daemon listening API | optional |

## Network{#network}

By default, a network named **websoft9** is created and all applications run on this network

## Services{#service}

You need to know Systemd and Docker services for administrator.  

### Systemd{#systemd}

Three Systemd services: **websoft9, docker, cockpit**

```
sudo systemctl start | top | restart | status docker
sudo systemctl start | top | restart | status cockpit
sudo systemctl start | top | restart | status websoft9
```

### Docker{#docker-services}

The **Containers** function module of the Websoft9 Console hides the Websoft9 containers, so you need to query them with the command `docker ps | grep websoft9-`. 

```
$ docker ps | grep websoft9-
8039d81eb0a1   websoft9dev/apphub:0.0.6                 "/websoft9/script/en…"   32 hours ago   Up 32 hours             8080-8081/tcp                                                                      websoft9-apphub
cc55650540e6   websoft9dev/deployment:2.19.0            "/init_portainer"        32 hours ago   Up 32 hours (healthy)   8000/tcp, 9000/tcp, 9443/tcp                                                       websoft9-deployment
527a07615809   websoft9dev/git:1.20.4                   "/usr/bin/entrypoint…"   32 hours ago   Up 32 hours             22/tcp, 3000/tcp                                                                   websoft9-git
bbea45d00358   websoft9dev/proxy:2.10.4                 "/init /bin/sh -c '/…"   32 hours ago   Up 32 hours             0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp, 81/tcp   websoft9-proxy
```

## CLI{#cli}

- [Websoft9 CLI](./cli)
- Docker CLI: `docker -h`, `docker compose -h`