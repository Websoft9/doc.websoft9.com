---
sidebar_position: 1
slug: /backend-service
---

#  Websoft9 Backend

Before reading this section, please read [Websoft9 Architecture](./developer/architecture) 

## Services

Maintaining and managing Websoft9's back-end services involves only the following two aspects: 

- [Containers of Websoft9 Console](./parameter#docker-services): Microservices for the Websoft9 Console
- [websoft9.service](./parameter#service): Systemd service that coordinates of Websoft9 containers

## Settings

### Set containers of Websoft9 backend

The Websoft9 container service is started using Docker Compose, via its [.env file](./parameter#path) and [docker-compose.yml file](./parameter#path). 

### Expose container ports for Gateway{#proxy-bind-port}

Websoft9 Gateway is running at container, and only expose container ports **80,443** to host server.   

You can expose more ports to host server by  [docker-compose.yml file](./parameter#path).