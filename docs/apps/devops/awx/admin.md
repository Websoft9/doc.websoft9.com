---
sidebar_position: 3
slug: /awx/admin
tags:
  - AWX
  - DevOps
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### AWX 使用外部 PostgreSQL

默认安装下，使用的是Docker版本的PostgreSQL数据库，并设置了持久化存储。  

如果你想将数据库更换为外部PostgreSQL数据库（自建或云数据库），请参考如下步骤：

1. 备份好已有的AWX数据
2. 进入到AWX的配置文件夹
   ```
   cd /data/.awx
   ```
2. 删除目前AWX项目的所有容器
   ```
   cd /data/.awx
   docker-compose -f docker-compose.yml down -v
   ```
3. 修改 *docker-compose.yml* 文件，去掉两处 *depends_on:* 项中的 *- postgres*，并删除 *postgres: ...* 整段，最后文件的内容如下： 
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
4. 修改 */data/.awx/credentials.py* 文件中数据库账号信息，确保为外部PostgreSQL的连接信息
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
5. 修改 */data/.awx/environment.sh* 文件中数据库账号信息，确保为外部PostgreSQL的连接信息
   ```
   DATABASE_USER=awx
   DATABASE_NAME=awx
   DATABASE_HOST=pgm-j6cr72qyfadij3980o.pg.rds.websoft9.com
   DATABASE_PORT=1433
   DATABASE_PASSWORD=yourpassword
   AWX_ADMIN_USER=admin
   AWX_ADMIN_PASSWORD=password

   ```
6. 重新创建容器
   ```
   docker-compose -f docker-compose.yml up -d
   ```


### AWX 负载均衡部署

通过负载均衡处理多台 AWX 并行工作，对于大型企业来说这是一种很常见的部署方案。

### AWX 升级

升级 AWX 通过重新安装来完成。

1. 使用SSH登录服务器
2. 进入到 */data/awx/* 目录，从 Github 更新AWX源码
   ```
   git pull
   ```
3. 进入到 */data/awx/installer* 目录
4. 增加一个 update-vars.yml 文件，其中的内容如下（其中的密码为真实值）：
   ```
   admin_password: 'adminpass'
   pg_password: 'pgpass'
   rabbitmq_password: 'rabbitpass'
   secret_key: 'mysupersecret'
   ```
5. 运行如下命令，开始升级
   ```
   ansible-playbook -i inventory install.yml -e @update-vars.yml
   ```


## 故障排除

除以下列出的 AWX 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

#### 受控端更换镜像后，AWX 再次连接报错？

找到主机缓存文件：*/var/lib/awx/.ssh/known_hosts*，删除其中的历史记录即可

#### 登录界面显示"is updating"？

等待更新完成后，重启服务器，再访问

#### 创建项目选择手动（SCM 类型）提示 "WARNING..."？

错误信息：WARNING: There are no available playbook directories in /var/lib/awx/projects....  

原因：AWX容器的项目路径没有挂在到宿主机上  
方案：将/var/lib/awx/projects 映射到宿主机目录  /data/wwwroot/awx/projects

#### awx_redis 容器无法启动？

原因：redis.sock 权限不足导致  
方案：给 /data/.awx/redis_socket 文件夹授权

1. 编辑 */data/.awx/redis.conf* 文件中增加一行权限配置 `unixsocketperm 750`
   ```
   unixsocket /var/run/redis/redis.sock
   unixsocketperm 660
   port 0
   bind 127.0.0.1
   unixsocketperm 750
   ```
2. Redis 通信目录授权 `chmod -R 777 /data/.awx/redis_socket`
3. 进入到 AWX 目录后，重新运行容器即可
   ```
   cd /data/.awx
   docker-compose down -v
   docker-compose up -d
   ```

#### 可进入 AWX 控制台，但无法运行 Job？

很有可能是 awx_redis 容器没有正常运行导致，通过命令 `docker ps` 查看 awx_redis 运行状态


## 问题解答

#### AWX 支持多语言吗？

支持[多种语言](https://docs.ansible.com/ansible-tower/latest/html/release-notes/supported_locales.html)，包括中文。它不提供语言切换菜单，而是自动适用浏览器首选语言。

#### AWX 是如何与 PostgreSQL 连接的？

容器内部连接，即容器编排

#### AWX 是否支持 Ansible Galaxy？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-setgalax-websoft9.png)

支持，参考官方文档 [Ansible Galaxy Support](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html#ug-galaxy)

#### AWX 是否支持交互式变量？

支持

#### AWX API 地址是多少？

http://AWX Server 服务器公网IP/api/

#### AWX 是否支持 Ansible Galaxy？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/awx/awx-setgalax-websoft9.png)

支持，参考官方文档 [Ansible Galaxy Support](https://docs.ansible.com/ansible-tower/latest/html/userguide/projects.html#ug-galaxy)

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

