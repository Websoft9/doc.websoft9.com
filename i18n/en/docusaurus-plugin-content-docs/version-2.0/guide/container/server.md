---
sidebar_position: 2
slug: /docker-server
---

# Set your Docker

You may need to set your Docker when using Websoft9 for applications hosting.     

## Tutorials


### Install Docker{#install}

If there not have Docker on your server, please run below command to install it.

```
wget -O - https://websoft9.github.io/websoft9/install/install_docker.sh | bash
```

### Add your registry-mirrors{#imagespeed}

You will need to set up docker registry-mirrors if the server is having network issues accessing DockerHub.  

1. Prepare your [registry mirrors](./software-repos#docker)

2. Edit `/etc/docker/daemon.json` and add the **registry-mirrors** key and value, to make the change
    ```
    {
      "registry-mirrors": ["https://registry.docker-cn.com","http://hub-mirror.c.163.com"]
    }
    ```

3. Restart docker service
   ```
   sudo systemctl restart docker
   ```

### Change docker volume path{#changepath}

The default docker volume path is */var/lib/docker/volumes*, you can change it by below steps:

1. Stop you docker service
   ```
   sudo systemctl stop docker
   ```

2. Edit `/etc/docker/daemon.json` and add the **data-root** key and value, to make the change
    ```
    {
        "data-root": "/new/path/to/docker-data"
    }
    ```
3. Move the data to new path
   ```
   sudo mv /var/lib/docker /new/path/to/docker-data
   ```

4. Restart docker service
   ```
   sudo systemctl restart docker
   ```

## Related topics

- [Docker parameters](./parameter#path)
- [Docker CLI](./parameter#cli)
- [Enable Docker API](https://docs.docker.com/reference/cli/dockerd/#daemon-socket-option)
- [Docker docs](https://docs.docker.com/)

## Troubleshoot{#troubleshoot}

### docker-containerd.socket: timeout?

Please turn off SELinux. If SELinux is on, docker will not start.    


