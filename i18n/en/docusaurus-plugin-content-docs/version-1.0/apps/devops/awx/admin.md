---
sidebar_position: 3
slug: /awx/admin
tags:
  - AWX
  - DevOps
---

# AWX Maintenance

This chapter is special guide for Jenkins maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Use an external PostgreSQL


AWX requires access to a PostgreSQL database, and by default, one will be created and deployed in a container, and data will be persisted to a host volume. In this scenario, Websoft9's deployment have set the value of postgres_data_dir to a path that can be mounted to the container. When the container is stopped, the database files will still exist in the specified path.

If you wish to use an external database (e.g [posgtresql](https://github.com/ansible/awx/blob/devel/INSTALL.md#docker-compose) ), following is the steps:

1. Backup all your data of AWX
2. Use SFTP to connect you AWX server and cd to AWS configure folder
   ```
   cd /data/.awx
   ```
2. Delete all dockers
   ```
   cd /data/.awx
   docker-compose -f docker-compose.yml down -v
   ```
3. Remove all **postgres** related items in the file *docker-compose.yml*  

   * Remove *- postgres* on the *depends_on:* 
   * Remove all paragraph of *postgres: ...*

   The following is the example after remove all **postgres** related items of docker-compose.yml

   ```
   version: '2'
   services:

     web:
       image: ansible/awx_web:11.2.0
       container_name: awx_web
       depends_on:
         - redis
         - memcached
       ports:
         - "80:8052"
       hostname: awxweb
       user: root
       restart: unless-stopped
       volumes:
         - supervisor-socket:/var/run/supervisor
         - rsyslog-socket:/var/run/awx-rsyslog/
         - rsyslog-config:/var/lib/awx/rsyslog/
         - "/data/.awx/SECRET_KEY:/etc/tower/SECRET_KEY"
         - "/data/.awx/environment.sh:/etc/tower/conf.d/environment.sh"
         - "/data/.awx/credentials.py:/etc/tower/conf.d/credentials.py"
         - "/data/.awx/nginx.conf:/etc/nginx/nginx.conf:ro"
         - "/data/.awx/redis_socket:/var/run/redis/:rw"
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 

     task:
       image: ansible/awx_task:11.2.0
       container_name: awx_task
       depends_on:
         - redis
         - memcached
         - web
       hostname: awx
       user: root
       restart: unless-stopped
       volumes:
         - supervisor-socket:/var/run/supervisor
         - rsyslog-socket:/var/run/awx-rsyslog/
         - rsyslog-config:/var/lib/awx/rsyslog/
         - "/data/.awx/SECRET_KEY:/etc/tower/SECRET_KEY"
         - "/data/.awx/environment.sh:/etc/tower/conf.d/environment.sh"
         - "/data/.awx/credentials.py:/etc/tower/conf.d/credentials.py"
         - "/data/.awx/redis_socket:/var/run/redis/:rw"
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 
         SUPERVISOR_WEB_CONFIG_PATH: '/supervisor.conf'

     redis:
       image: redis
       container_name: awx_redis
       restart: unless-stopped
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 
       command: ["/usr/local/etc/redis/redis.conf"]
       volumes:
         - "/data/.awx/redis.conf:/usr/local/etc/redis/redis.conf:ro"
         - "/data/.awx/redis_socket:/var/run/redis/:rw"
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"

     memcached:
       image: "memcached:alpine"
       container_name: awx_memcached
       command: ["-s", "/var/run/memcached/memcached.sock", "-a", "0666"]
       restart: unless-stopped
       environment:
         http_proxy: 
         https_proxy: 
         no_proxy: 
       volumes:
         - "/data/.awx/memcached_socket:/var/run/memcached/:rw"

   volumes:
     supervisor-socket:
     rsyslog-socket:
     rsyslog-config:

   ```
4. Modify the file */data/.awx/credentials.py* , make sure it is the correct connections for your external PostgreSQL
   ```
      DATABASES = {
       'default': {
           'ATOMIC_REQUESTS': True,
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': "awx",
           'USER': "awx",
           'PASSWORD': "yourpassword",
           'HOST': "pgm-j6cr72qyfadij3980o.pg.rds.websoft9.com",
           'PORT': "1433",
       }
   }

   BROADCAST_WEBSOCKET_SECRET = "al9mLS4tWTlmX1owN1FyOElJWDY="
   ```
5. Modify the file */data/.awx/environment.sh* , make sure it is the correct connections for your external PostgreSQL
   ```
   DATABASE_USER=awx
   DATABASE_NAME=awx
   DATABASE_HOST=pgm-j6cr72qyfadij3980o.pg.rds.websoft9.com
   DATABASE_PORT=1433
   DATABASE_PASSWORD=yourpassword
   AWX_ADMIN_USER=admin
   AWX_ADMIN_PASSWORD=password

   ```
6. Restart all dockers
   ```
   docker-compose -f docker-compose.yml up -d
   ```


### AWX High availability

Processing multiple AWXs in parallel through load balancing is a very common deployment solution for large enterprises.

AWX is based on Docker deployment, the name of the container that handles the web is: awx_web


### AWX Upgrade

Upgrading AWX involves rerunning the install playbook. Download a newer release from https://github.com/ansible/awx/releases and re-populate the inventory file with your customized variables.

For convenience, you can create a file called *update-vars.yml*:

1. Use **SFTP** to connect Server
2. Go to the directory */data/awx/* and update this repository from Github
   ```
   sudo cd /data/awx && git pull
   ```
3. Go to the directory: */data/awx/installer* 
4. Create new file named *update-vars.yml* and add the template to it like below(make sure all password is your correct password) 
   ```
   admin_password: 'adminpass'
   pg_password: 'pgpass'
   rabbitmq_password: 'rabbitpass'
   secret_key: 'mysupersecret'
   ```
5. Run the update commands like below
   ```
   ansible-playbook -i inventory install.yml -e @update-vars.yml
   ```


## Troubleshoot{#troubleshoot}

In addition to the AWX issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 受控端更换镜像后，AWX 再次连接报错？

找到主机缓存文件：*/var/lib/awx/.ssh/known_hosts*，删除其中的历史记录即可

#### 登录界面显示"is updating"？

等待更新完成后，重启服务器，再访问

#### A server error has occurred?

```
docker logs awx_web
```

#### Create manful Project from SCM type have error "WARNING: There are no available playbook directories in /var/lib/awx/projects...."

Reason: The directory /var/lib/awx/projects of AWX container not mounted to Server
Solution： Mounted the container's /var/lib/awx/projects to Server's path /data/wwwroot/awx/project.

#### awx_redis container start fail?

Reason: redis.sock permission problem  
Solution:  

1. Edit file */data/.awx/redis.conf* and add the line `unixsocketperm 750`
   ```
   unixsocket /var/run/redis/redis.sock
   unixsocketperm 660
   port 0
   bind 127.0.0.1
   unixsocketperm 750
   ```
2. Set redis socket directory permission with the command `chmod -R 777 /data/.awx/redis_socket`
3. Go to AWX directory and run the container again
   ```
   cd /data/.awx
   docker-compose down -v
   docker-compose up -d
   ```

#### I can login to AWX console, but run job failed?

The  most likely reason is the **awx_redis** container can not start, you can run the command `docker ps` to check the status of  **awx_redis**


## FAQ{#faq}

#### AWX support multi-language?

Yes, it supported [Locales](https://docs.ansible.com/ansible-tower/latest/html/release-notes/supported_locales.html). It automatically sets the locale preference based on the user’s browser settings. For Safari, Internet Explorer, and older versions of Chrome as well as FireFox, this is handled automatically.

#### How is AWX connected to PostgreSQL?

AWX connect PostgreSQL in Docker inner, and you can use external Database

#### AWX support Ansible Galaxy?
Yes, refer to [Ansible Galaxy Support](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html#ug-galaxy)

#### AWX support **var-prompt**?

Yes, refer to [Extra variable](../awx#extravar) charter of this docs

#### What's URL of AWX API?

http://AWX Server Internet IP/api/

#### If there is no domain name, can I deploy AWX?

Yes, visit AWX by *http://Internet IP*


#### Is there a web-base GUI database management tools?

No

#### Is it possible to modify the source path of AWX?

No

#### AWX 的命令行是什么？

awx 是 AWX 和 Red Hat Ansible Tower 的官方命令行客户端。它：

* 使用与 AWX HTTP API一致的命名和结构
* 提供一致的输出格式和可选的机器可解析格式
* 在可能的范围内，自动检测AWX和Red Hat Ansible Tower多个版本的API版本，可用的端点和功能支持。

潜在的用途包括：

* 配置和启动作业/剧本
* 检查作业运行的状态和输出
* 管理组织，用户，团队等对象。

更多详情请参考官方文档：[《AWX命令行界面》](https://docs.ansible.com/ansible-tower/latest/html/towercli/index.html)

