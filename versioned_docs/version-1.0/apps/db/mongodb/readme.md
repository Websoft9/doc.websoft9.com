---
sidebar_position: 1
slug: /mongodb
tags:
  - MongoDB
  - Cloud Native Database
---

# 快速入门

[MongoDB](https://www.mongodb.com/zh) 是通用、基于文档的分布式数据库，帮助现代应用程序开发人员迎接云时代的到来。它在类似 JSON 的文档内存储数据。这种面对数据的数据存储方法非常自然，比传统的排/列模型更加直观和强大。MongoDB 也是一个真正的具有全套工具的数据平台，能帮助开发人员、分析师和数据科学家等各类人群更方便地处理数据。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodb-gui-websoft9.png)


## 准备

部署 Websoft9 提供的 MongoDB 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 TCP：**27017 和 9091** 端口已经开启
3. 在服务器中查看 MongoDB 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  MongoDB，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## MongoDB 初始化向导

### 详细步骤

部署 MongoDB 之后，依次完成下面的步骤，验证其可用性：

1. 使用 SSH 连接 MongoDB 所在的服务器，运行下面的命令，查看 MongoDB 的运行状态
   ```
   cd /data/apps/mongodb && sudo docker compose ls
   ```
    MongoDB 正常运行会得到 " STATUS: running(1) " 的反馈

2. 运行 MongoDB Shell 命令（[不知道账号密码？](./user/credentials)）
   ~~~
   $ docker exec -it mongodb mongosh admin -u root -p YOURPASSWORD
   MongoDB shell version v5.0.10
   connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
   {"t":{"$date":"2022-08-10T03:05:34.194Z"},"s":"I",  "c":"NETWORK",  "id":5693100, "ctx":"js","msg":"Asio socket.set_option failed with std::system_error","attr":{"note":"connect (sync) TCP fast open","option":{"level":6,"name":30,"data":"01 00 00 00"},"error":{"what":"set_option: Protocol not available","message":"Protocol not available","category":"asio.system","value":92}}}
   Implicit session: session { "id" : UUID("030a4e0b-54cf-4f93-aa90-792b10c478f7") }
   MongoDB server version: 5.0.10
   ================
   Warning: the "mongo" shell has been superseded by "mongosh",
   which delivers improved usability and compatibility.The "mongo" shell has been deprecated and will be removed in
   an upcoming release.
   For installation instructions, see
   https://docs.mongodb.com/mongodb-shell/install/
   ================
   > 
   ~~~

3. 分别列出默认数据库和用户
   ```
   # 列出所有数据库
   show dbs

   # 切换到 admin 数据库，列出所有用户
   use admin
   show users
   ```

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

**MongoDB 默认启用账号认证吗？**  
默认情况下 MongoDB 认证已开启。


## MongoDB 入门指南

> 需要了解更多 MongoDB 的使用，请官方文档 [MongoDB Administration](https://docs.mongodb.com/manual/administration/)

## MongoDB 常用操作

### 开启 MongoDB 远程访问{#remote}

默认MongoDB 远程访问已经开启，如果因为其它因素无法远程，可如下操作：  

1. 修改 [MongDB 配置文件](#path)
   ```
   # 将 bindIP 修改为 0.0.0.0 或 本地电脑公网IP
   net:
      port: 27017
      bindIp: 0.0.0.0
   ```
   > 0.0.0.0 代表任意公网IP均可访问

2. 重启 [MongoDB 服务](#service)
   ```
   sudo docker restart mongodb
   ```      

### 关闭 MongoDB 访问认证

默认情况下 MongoDB 认证已开启，可按照下面流程关闭：

1. 打开 [MongoDB compose 文件](#path)，将环境变量用户以及密码注释掉。

   ```
   services:
     mongo:
       image: mongo:${APP_VERSION}
       restart: always
       container_name: ${APP_NAME}
       ports:
         - ${APP_MONGO_PORT}:27017
       #environment:
       #  MONGO_INITDB_ROOT_USERNAME: ${APP_USER}
       #  MONGO_INITDB_ROOT_PASSWORD: ${APP_PASSWORD}
   ```

2. 重新创建 MongoDB 容器
   ```
   cd /data/apps/mongodb
   sudo docker compose up -d
   ```

### 图形化 Web 端(MongoDB Compass)

MongoDB Compass 官方提供的客户端工具，我们的部署方案已经将它预装到一个 Web 环境中：  

使用 MongoDB Compass 的前置条件：

* 开启 MongoDB的访问认证
* 开启服务器安全组 **TCP:9091** 端口


1. 本地电脑浏览器访问：*https://服务器公网IP:9091* ，根据提示输入用户名和密码登陆web桌面（[不知道账号密码？](./user/credentials)）

2. 点击web桌面的 MongoDB Compass 图标，进入MongoDB Compass
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodbcompass-click-websoft9.png)

3. 填写准确的字段，连接 MongoDB
   ```
   # 示例连接字符串
   mongodb://root:1cTFecwTEs@mongodb:27017
   ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodbcompass001-websoft9.png)

4. 连接成功，进入控制台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodbcompass002-websoft9.png)

### 规划数据模型

MongoDB 作为一种数据库，与传统的 RDBMS 的使用方式也有相似之处，即规划数据模型，建立数据库范式。只有这种，才能更好的发挥数据库的性能。  

![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mongodb/mongodb-datamodel-websoft9.png)

数据规划的主要设计要点包括：

* 使用数据范式
* 使用嵌入式文档反范式
* 使用固定集合
* 考虑文档增大
* 规划索引、分片和复制
* 规划数据生命周期


### 命令速查

下面列出最常用的 MongoDB 命令供用户参考：  

##### 显示、创建和切换数据库

```shell

> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB

# 创建test数据库（如果不存在test数据库，就会自动创建它）
> use test
switched to db test

# 显示当前数据库
> db
test

# 显示当前所有用户数据
> show users

#3 插入数据到数据库
> db.test.insert({"name":"company"})
WriteResult({ "nInserted" : 1 })
```


##### 删除数据库
```
> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB
test      0.000GB
websoft9  0.000GB

> use test
switched to db test
> use test
> db.dropDatabase()
{ "dropped" : "test", "ok" : 1 }
> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB
websoft9  0.000GB
```

##### 创建管理员账号

```
> mongo
> use admin
switched to db admin
> db.createUser( { user: "webs_admin", pwd: "websoft9", roles: ["userAdminAnyDatabase"] } )
Successfully added user: { "user" : "webs_admin", "roles" : [ "userAdminAnyDatabase" ] }


# 显示账号
> show users
{
        "_id" : "admin.webs_admin",
        "user" : "webs_admin",
        "db" : "admin",
        "roles" : [
                {
                        "role" : "userAdminAnyDatabase",
                        "db" : "admin"
                }
        ],
        "mechanisms" : [
                "SCRAM-SHA-1",
                "SCRAM-SHA-256"
        ]
}
```


### 密码管理

#### 修改密码

参考下面的命令，修改已经创建的管理员账号root的密码

```
$ docker exec -it mongodb mongo admin -u root -p YOURPASSWORD
MongoDB shell version v4.0.18
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
> db = db.getSiblingDB('admin')
admin
> db.changeUserPassword("root", "NEWPASSWORD")
> exit
```

#### 重置密码

重置密码即已经忘记密码的情况下，通过特殊手段重新设置新密码的过程。


1. 修改 [MongoDB compose 文件](#path)，将环境变量用户以及密码注释掉
   ```
   services:
     mongo:
       image: mongo:${APP_VERSION}
       restart: always
       container_name: ${APP_NAME}
       ports:
         - ${APP_MONGO_PORT}:27017
       #environment:
       #  MONGO_INITDB_ROOT_USERNAME: ${APP_USER}
       #  MONGO_INITDB_ROOT_PASSWORD: ${APP_PASSWORD}
   ```

2. 重启 MongoDB 服务
   ```
   cd /data/apps/mongodb
   sudo docker compose up -d
   ```

3. 进入mongodb容器
   ```
   docker exec -it mongodb bash
   ```

4. 重新设置密码
   ```
   mongo
   > db = db.getSiblingDB('admin')
   admin
   > db.changeUserPassword("root", "NEWPASSWORD")
   ```

5. 修改 [MongoDB compose文件](#path)，使环境变量用户以及密码生效
   ```
   services:
     mongo:
       image: mongo:${APP_VERSION}
       restart: always
       container_name: ${APP_NAME}
       ports:
         - ${APP_MONGO_PORT}:27017
       environment:
         MONGO_INITDB_ROOT_USERNAME: ${APP_USER}
         MONGO_INITDB_ROOT_PASSWORD: ${APP_PASSWORD}
   ```

6. 重新创建 MongoDB 容器，新密码立即生效
   ```
   cd /data/apps/mongodb
   sudo docker compose up -d
   ```

## MongoDB 参数

MongoDB 应用中包含 Docker，  MongoCompass 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 MongoDB 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                                                   COMMAND                  CREATED         STATUS                  PORTS                                                                                  NAMES
80130e1088b2   websoft9dev/mongocompass:v1.31                          "/dockerstartup/kasm…"   2 minutes ago   Up About a minute       4901/tcp, 5901/tcp, 0.0.0.0:9091->6901/tcp, :::9091->6901/tcp                          mongocompass
c17d12157c01   mongo:latest                                            "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes            0.0.0.0:27017->27017/tcp, :::27017->27017/tcp                                          mongodb
```

下面仅列出 MongoDB 本身的参数：

### 路径{#path}

MongoDB 安装目录： */data/apps/mongodb*  
MongoDB 数据目录： */data/apps/mongodb/data/mongo_data*   
MongoDB 配置文件： */data/apps/mongodb/src/mongod.conf*   
MongoDB compose文件： */data/apps/mongodb/docker-compose.yml*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9091   | HTTP 访问 MongoCompass | 可选   |
| 27017   | MongoDB Server | 可选   |

### 版本

```shell
docker exec -i mongodb mongosh 
```

### 服务{#service}


```shell
sudo docker start | stop | restart  mongodb
sudo docker start | stop | restart  mongocompass
```

### 命令行{#cmd}

#### 服务端

MongoDB 的服务端叫mongod，进入容器后，可以通过mongod命令接受一序列参数，也可以通过配置文件接受参数：  

**命令行参数**

```
  -v [ --verbose ] [=arg(=v)]           be more verbose (include multiple times
                                        for more verbosity e.g. -vvvvv)
  --quiet                               quieter output
  --port arg                            specify port number - 27017 by default
  --logpath arg                         log file to send write to instead of
                                        stdout - has to be a file, not
                                        directory
  --syslog                              log to system's syslog facility instead
                                        of file or stdout
  --syslogFacility arg                  syslog facility used for mongodb syslog
                                        message
  --logappend                           append to logpath instead of
                                        over-writing
  --logRotate arg                       set the log rotation behavior
                                        (rename|reopen)
  --timeStampFormat arg                 Desired format for timestamps in log
                                        messages. One of ctime, iso8601-utc or
                                        iso8601-local
  --setParameter arg                    Set a configurable parameter
  -h [ --help ]                         show this usage information
  --version                             show version information
  -f [ --config ] arg                   configuration file specifying
                                        additional options
  --bind_ip arg                         comma separated list of ip addresses to
                                        listen on - localhost by default
  --bind_ip_all                         bind to all ip addresses
  --ipv6                                enable IPv6 support (disabled by
                                        default)
  --listenBacklog arg (=128)            set socket listen backlog size
  --maxConns arg                        max number of simultaneous connections
                                        - 1000000 by default
  --pidfilepath arg                     full path to pidfile (if not set, no
                                        pidfile is created)
  --timeZoneInfo arg                    full path to time zone info directory,
                                        e.g. /usr/share/zoneinfo
  --keyFile arg                         private key for cluster authentication
  --noauth                              run without security
  --transitionToAuth                    For rolling access control upgrade.
                                        Attempt to authenticate over outgoing
                                        connections and proceed regardless of
                                        success. Accept incoming connections
                                        with or without authentication.
  --clusterAuthMode arg                 Authentication mode used for cluster
                                        authentication. Alternatives are
                                        (keyFile|sendKeyFile|sendX509|x509)
  --nounixsocket                        disable listening on unix sockets
  --unixSocketPrefix arg                alternative directory for UNIX domain
                                        sockets (defaults to /tmp)
  --filePermissions arg                 permissions to set on UNIX domain
                                        socket file - 0700 by default
  --fork                                fork server process
  --slowms arg (=100)                   value of slow for profile and console
                                        log
  --slowOpSampleRate arg (=1)           fraction of slow ops to include in the
                                        profile and console log
  --networkMessageCompressors [=arg(=disabled)] (=snappy)
                                        Comma-separated list of compressors to
                                        use for network messages
  --auth                                run with security
  --clusterIpSourceWhitelist arg        Network CIDR specification of permitted
                                        origin for `__system` access.
  --profile arg                         0=off 1=slow, 2=all
  --cpu                                 periodically show cpu and iowait
                                        utilization
  --sysinfo                             print some diagnostic system
                                        information
  --noIndexBuildRetry                   don't retry any index builds that were
                                        interrupted by shutdown
  --noscripting                         disable scripting engine
  --notablescan                         do not allow table scans
  --shutdown                            kill a running server (for init
                                        scripts)

Replication options:
  --oplogSize arg                       size to use (in MB) for replication op
                                        log. default is 5% of disk space (i.e.
                                        large is good)
  --master                              Master/slave replication no longer
                                        supported
  --slave                               Master/slave replication no longer
                                        supported

Replica set options:
  --replSet arg                         arg is <setname>[/<optionalseedhostlist
                                        >]
  --replIndexPrefetch arg               specify index prefetching behavior (if
                                        secondary) [none|_id_only|all]
  --enableMajorityReadConcern [=arg(=1)] (=1)
                                        enables majority readConcern

Sharding options:
  --configsvr                           declare this is a config db of a
                                        cluster; default port 27019; default
                                        dir /data/configdb
  --shardsvr                            declare this is a shard db of a
                                        cluster; default port 27018

SSL options:
  --sslOnNormalPorts                    use ssl on configured ports
  --sslMode arg                         set the SSL operation mode
                                        (disabled|allowSSL|preferSSL|requireSSL
                                        )
  --sslPEMKeyFile arg                   PEM file for ssl
  --sslPEMKeyPassword arg               PEM file password
  --sslClusterFile arg                  Key file for internal SSL
                                        authentication
  --sslClusterPassword arg              Internal authentication key file
                                        password
  --sslCAFile arg                       Certificate Authority file for SSL
  --sslClusterCAFile arg                CA used for verifying remotes during
                                        outbound connections
  --sslCRLFile arg                      Certificate Revocation List file for
                                        SSL
  --sslDisabledProtocols arg            Comma separated list of TLS protocols
                                        to disable [TLS1_0,TLS1_1,TLS1_2]
  --sslWeakCertificateValidation        allow client to connect without
                                        presenting a certificate
  --sslAllowConnectionsWithoutCertificates
                                        allow client to connect without
                                        presenting a certificate
  --sslAllowInvalidHostnames            Allow server certificates to provide
                                        non-matching hostnames
  --sslAllowInvalidCertificates         allow connections to servers with
                                        invalid certificates
  --sslFIPSMode                         activate FIPS 140-2 mode at startup

Storage options:
  --storageEngine arg                   what storage engine to use - defaults
                                        to wiredTiger if no data files present
  --dbpath arg                          directory for datafiles - defaults to
                                        /data/db
  --directoryperdb                      each database will be stored in a
                                        separate directory
  --noprealloc                          disable data file preallocation - will
                                        often hurt performance
  --nssize arg (=16)                    .ns file size (in MB) for new databases
  --quota                               limits each database to a certain
                                        number of files (8 default)
  --quotaFiles arg                      number of files allowed per db, implies
                                        --quota
  --smallfiles                          use a smaller default file size
  --syncdelay arg (=60)                 seconds between disk syncs (0=never,
                                        but not recommended)
  --upgrade                             upgrade db if needed
  --repair                              run repair on all dbs
  --repairpath arg                      root directory for repair files -
                                        defaults to dbpath
  --journal                             enable journaling
  --nojournal                           disable journaling (journaling is on by
                                        default for 64 bit)
  --journalOptions arg                  journal diagnostic options
  --journalCommitInterval arg           how often to group/batch commit (ms)

WiredTiger options:
  --wiredTigerCacheSizeGB arg           maximum amount of memory to allocate
                                        for cache; defaults to 1/2 of physical
                                        RAM
  --wiredTigerJournalCompressor arg (=snappy)
                                        use a compressor for log records
                                        [none|snappy|zlib]
  --wiredTigerDirectoryForIndexes       Put indexes and data in different
                                        directories
  --wiredTigerMaxCacheOverflowFileSizeGB arg (=0)
                                        Maximum amount of disk space to use for
                                        cache overflow; Defaults to 0
                                        (unbounded)
  --wiredTigerCollectionBlockCompressor arg (=snappy)
                                        block compression algorithm for
                                        collection data [none|snappy|zlib]
  --wiredTigerIndexPrefixCompression arg (=1)
                                        use prefix compression on row-store
                                        leaf pages

Free Monitoring options:
  --enableFreeMonitoring arg            Enable Cloud Free Monitoring
                                        (on|runtime|off)
  --freeMonitoringTag arg               Cloud Free Monitoring Tags

```

**配置文件参数**

配置文件所用的参数与命令行有一些差异，MongoDB 当前采用配置组+配置段的方式组织[配置文件](https://docs.mongodb.com/v4.0/reference/configuration-options/#conf-file)，配置组主要包括：

* systemLog Options
* processManagement Options
* cloud Options
* net Options
* security Options
* setParameter Option
* storage Options
* operationProfiling Options
* replication Options
* sharding Options
* auditLog Options
* snmp Options 

下面是一个典型的配置文件内容：  

```
processManagement:
   fork: true
net:
   bindIp: localhost
   port: 27017
storage:
   dbPath: /var/lib/mongo
systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true
storage:
   journal:
      enabled: true
```

#### 客户端

MongoDB Shell 是 MongoDB 自带的一个交互式 JavaScript shell，让您能够访问、配置和管理MongoDB数据库、用户等。使用这个shell可执行各种任务，从设置用户账户到创建数据库，再到查询数据库内容，无所不包。

```
# log in Mongo Shell without authenticating
docker exec -it mongodb mongosh

# log in Mongo Shell witt authenticating
docker exec -it mongodb mongosh admin --username root -p

MongoDB shell version v4.0.18
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("e808b886-30db-41dd-9464-40b52f041107") }
MongoDB server version: 4.0.18
> help
        db.help()                    help on db methods
        db.mycoll.help()             help on collection methods
        sh.help()                    sharding helpers
        rs.help()                    replica set helpers
        help admin                   administrative help
        help connect                 connecting to a db help
        help keys                    key shortcuts
        help misc                    misc things to know
        help mr                      mapreduce

        show dbs                     show database names
        show collections             show collections in current database
        show users                   show users in current database
        show profile                 show most recent system.profile entries with time >= 1ms
        show logs                    show the accessible logger names
        show log [name]              prints out the last segment of log in memory, 'global' is default
        use <db_name>                set current database
        db.foo.find()                list objects in collection foo
        db.foo.find( { a : 1 } )     list objects in foo where a == 1
        it                           result of the last line evaluated; use to further iterate
        DBQuery.shellBatchSize = x   set default number of items to display on shell
        exit                         quit the mongo shell

```

MongoDB shell 有两种方式与数据库进行交互：

* 命令行交互式操作
* 运行存放在文件中的命令脚本（例如：shell_script.js）

### API

[MongoDB Drivers API Documentation](https://api.mongodb.com/)