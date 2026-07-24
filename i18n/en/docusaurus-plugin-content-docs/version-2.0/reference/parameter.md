---
sidebar_position: 2.0
slug: /parameter
---

# Parameter

Various parameters such as server, network, port and path involved in Websoft9 are listed below:  

## Paths{#path}

### Websoft9 Console

- **Websoft9 installation directory**: */opt/websoft9*
- **Websoft9 data directory**: */opt/websoft9/data*  
- **Websoft9 backup directory**: */opt/websoft9/data/backups*
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

Websoft9 runs as a Docker container. The main Systemd service is Docker:

```
sudo systemctl start | stop | restart | status docker
```

### Docker{#docker-services}

Websoft9 runs as a single container. Query it with `docker ps | grep websoft9`:

```
$ docker ps | grep websoft9
abc123def456   websoft9dev/websoft9:latest   ...   Up 2 hours   0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp, 0.0.0.0:9000->9000/tcp   websoft9
```

## CLI{#cli}

- [Websoft9 CLI](./cli)
- Docker CLI: `docker -h`, `docker compose -h`