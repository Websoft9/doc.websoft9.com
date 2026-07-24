---
sidebar_position: 1
slug: /faq
---

# FAQs

Please refer to the FAQ below to resolve your issue, if you cannot find the solution, please contact [Websoft9 support](/helpdesk). 

## Websoft9 Console

### Can't access Websoft9 Console?{#blank}

Common causes include:

* Security Group port **9000** not enabled (**most common cause**)
* Websoft9 installation failed
* Network access failed for your server
* Product failure itself

If none of the above solves your issue, contact [Support](/helpdesk).

### Console accessible but features not working?

When you can log in but cannot access App Store, My Apps, or other core features, run the following commands to diagnose:

```
# View Websoft9 container logs
docker logs websoft9

# Check container health
docker ps --filter "name=websoft9"
```

### Websoft9 service fails to start?

1. Check compute resource limits
    ```shell
    # View processes
    ps aux

    # Check disk space
    df -lh

    # View memory usage
    free -lh
    ```

2. Check Websoft9 container logs
    ```shell
    docker logs websoft9
    ```

3. Diagnose based on error logs

### How to reset admin password?

```bash
rm -f /opt/websoft9/data/config/product-auth/product-auth.sqlite
rm -f /opt/websoft9/data/config/setup-wizard/state.json
docker restart websoft9
```
After restart, the setup wizard will launch to create a new administrator account.

### Websoft9 default port conflict?{#portconflict}

Run `netstat -tunlp` to check which ports are already in use on the server.
    journalctl -u websoft9
    ``

### Websoft9 can not running at 9000 port?{#portconflict}

Running `netstat -tunlp` to check which process is using port 9000, then free the port with `kill -9 PID`.

### Docker starting failed?{#dockernotstart}

Running `systemctl status docker` and `journalctl -xe` to check error logs

### Recreate App error: data.forward_port should be >= 1

The reason is that you have delete `W9_URL` and `W9_HTTP_PORT` that exist `.env`, if don't need to publish your App, you should delete Proxy related one record at **Websoft9 Gateway**

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
