---
title: Portainer
slug: /portainer
tags:
  - console
  - other
---

import Meta from './_include/portainer.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Portaioner at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  
   ![](./assets/portainer-register-websoft9.png)

2. Follow the guide to complete the administrator account setup. After entering the backend, the system prompts you to set up Environments

   - To manage local containers (recommended): Delete the current installation of Portainer and use the Websoft9 console **Containers** management function directly

   - To manage local containers: Modify the Portaier orchestration file, delete the comment on the line `/var/run/docker.sock`, and it will take effect after you rebuild the application

   - To manage non-local containers: follow the Environments instructions to setup the connection method

3. After completing the Environments setup and connection, you can start managing containers

### Running commands in containers {#docker-exec}

Portainer provides the ability to run container commands visually, which equals to **docker exec -it**.

1. In the list of containers, click the **>_** icon under the **Quick actions** section of MySQL in the following image
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-containerlist-websoft9.png)

2. On the newly opened page, click the **Connetc** button to prepare the connection
    ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/potainer/portainer-createdatabase-websoft9.png)

    - Command: select available commands to execute (choose one of three, there is always one available)
    - user: default root (recommended)

3. Click **Connect**, if connect successfully then run the command

### Install the app in Portainer {#installapp}

If the Websoft9 App Store does not meet the installation requirements, users can install Docker applications in the container management platform in a self-defined way

- Custom installation of Docker-Compose apps: **Container > Stacks > Add Stack**
- Customized installation of Docker containers: **Containers > Containers > Add Container**

### Operation Guide

Reference: [Websoft9 Container Guide](./function/container)

## Configuration options{#configs}

- Enterprise Edition Free Range: 5 nodes
- [Portainer CLI](https://docs.portainer.io/advanced/cli)
- [Portainer API](https://docs.portainer.io/api/access)
- Managing K8s(✅)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Portainer cannot enter the initialization page?

Reason: Portainer's init page locks if not access after a few minutes of installation for security

#### Can I delete existing Environments?

If you delete the Environments after you have running containers, the containers will be unmanageable

#### Websoft9 Application VS Portarner Stack?

Portainer creates Websoft9 app containers through its Stack API for managemen

However, there is more to Websoft9 applications, that is, they cannot be completely equated
