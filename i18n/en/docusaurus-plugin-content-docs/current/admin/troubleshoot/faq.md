---
sidebar_position: 1
slug: /faq
---

# FAQs

Please refer to the FAQ below to resolve your issue, if you cannot find the solution, please contact [Websoft9 support](./helpdesk). 

## Websoft9 Console

### 500 Internal Server Error?

**Description**: When checking the logs of websoft9-apphub container, 500 Internal Server Error appears.  

**Reason**: The websoft9-apphub container is working abnormally or it can not connect other websoft9 containers  

**Solution**: Run the following commands to check the cause of the error   

    ```
    docker exec -it websoft9-apphub cat /websoft9/apphub/logs/apphub_error.log
    ```

### Can not open App Store or My Apps?

**Description**: I can login Websoft9 Console, but can not open "App Store" or "My Apps" interface   

**Reason**: websoft9 containers working abnormally or **80** port not enabled

**Solution**: Run the following commands to check the cause of the error   

    ```
    docker logs websoft9-proxy
    docker exec -it websoft9-apphub cat /websoft9/apphub/logs/apphub_error.log
    ```

### Login Websoft9 failed{#login}

Using multiple reasons can cause login failure:

* Security Group port **9000** not enabled
* Websoft9 installation failed
* Network access failed for your instance
* Local browser's cookie or session
* Websoft9 Console(Cockpit) port is reset to **9090**
* Your Linux not allowed password login

#### Cockpit console port is reset to 9090?

When user running `yum update` or `apt upgrade`, Cockpit may be reset to **9090** port and you can not login to Websoft9 Console

1. Login to Websoft9 Console by `http://IP:9090`
2. Set port to **9090** by **Settings > System Settings**

> You can set port by repeating step2 to your default port

### websoft9.service starting failed?

1. Troubleshooting compute resource limit
    ```shell
    # View processes
    ps aux

    # Check disk space
    df -lh

    # View memory usage
    free -lh
    ```

2. Check the error logs
    ```shell
    # View the Websoft9 service container logs
    docker logs websoft9-apphub
    docker logs websoft9-git
    docker logs websoft9-proxy
    docker logs websoft9-deployment

    # View Websoft9 service status and logs
    systemctl status websoft9
    journalctl -u websoft9
    ``

### Websoft9 can not running at 9000 port?{#portconflict}

Running `netstat -tunlp` to check which process is using port 9000, then free the port with `kill -9 PID`.

### Docker starting failed?{#dockernotstart}

Running `systemctl status docker` and `journalctl -xe` to check error logs


## Applications

### Access application 502 error{#nginx502}

**Description**: Nginx 502 Bad Gateway  

**Reason**: Application container failure proxy by Nginx  

**Solution**: Troubleshoot the application container from

- Insufficient computing resources of server
- Application containers stopped running
- Application containers port error


### Application error when DB changed?

**Description**: Application error when modify database password from DB commands or DB tools  

**Reason**: Application can not connect when modify database password because DB connection string changed  

**Solution**: Modify database connection string at **Compose** of **My Apps**  
  

### Can't access application from Internet?{#no-remote}

**Description**: I can't access application from Internet, but I can access it from Intranet.  

**Reason**: Internet is not available or access from the Internet is denied   

**Solution**: Here are some of the common causes   

- Container port is not exposed to the host machine or does not have a proxy to the host machine.
- The container denies access from the Internet
- The port corresponding to the server's security group is not open.


## Related topics

- [FAQs for application deployment at Websoft9 Console](./deployment#troubleshoot)
- [FAQs for Application Compose](./app-compose#troubleshoot)
- [FAQs for Managing Docker](./docker-server#troubleshoot)
- [FAQs for Linux](./linux#troubleshoot)
- [FAQs for MySQL/MariaDB](./mysql#troubleshooting)
- [FAQs for PostgreSQL](./postgresql#troubleshooting)
- [FAQs for HTTPS Settings](./domain-https#troubleshoot)
