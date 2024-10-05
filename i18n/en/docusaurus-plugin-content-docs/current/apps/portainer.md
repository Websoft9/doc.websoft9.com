---
title: Portainer
slug: /portainer
tags:
  - console
  - other
---

import Meta from './\_include/portainer.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of Portainer via the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from **My Apps**.  
   ![](./assets/portainer-register-websoft9.png)

2. Follow the guide to complete the administrator account setup. After entering the backend, the system prompts you to set up Environments.

   - To manage local containers (recommended): Delete the current installation of Portainer and use the Websoft9 console **Containers** management function directly.

   - To manage local containers: Modify the Portainer orchestration file, delete the comment on the line `/var/run/docker.sock`, and it will take effect after you rebuild the application.

   - To manage non-local containers: Follow the Environments instructions to set up the connection method.

3. After completing the Environments setup and connection, you can start managing containers.

### Running Commands in Containers {#docker-exec}

Portainer provides the ability to run container commands visually, which is equivalent to **docker exec -it**.

1. In the list of containers, click the **>\_** icon under the **Quick actions** section of MySQL, as shown below:
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/potainer/portainer-containerlist-websoft9.png)

2. On the newly opened page, click the **Connect** button to prepare the connection.
   ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/potainer/portainer-createdatabase-websoft9.png)

   - **Command**: Select available commands to execute (choose one of three, there is always one available).
   - **User**: Default is root (recommended).

3. Click **Connect**, and if the connection is successful, run the command.

### Install the App in Portainer {#installapp}

If the Websoft9 App Store does not meet your installation requirements, you can install Docker applications on the container management platform in a self-defined way:

- Custom installation of Docker-Compose apps: **Container > Stacks > Add Stack**.
- Custom installation of Docker containers: **Containers > Containers > Add Container**.

## Configuration Options {#configs}

- Enterprise Edition Free Range: 5 nodes.
- [Portainer CLI](https://docs.portainer.io/advanced/cli)
- [Portainer API](https://docs.portainer.io/api/access)
- Managing K8s (✅)

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### Portainer Cannot Enter the Initialization Page?

**Reason**: For security reasons, Portainer will lock the initialization page if it is not accessed within a few minutes after installation.

**Solution**: Restart the Portainer application.

#### Can I Delete Existing Environments?

If you delete the Environments after you have running containers, the containers will become unmanageable.

#### Websoft9 Application VS Portainer Stack?

Portainer creates Websoft9 app containers through its Stack API for management.

However, there is more to Websoft9 applications, meaning they cannot be completely equated.
