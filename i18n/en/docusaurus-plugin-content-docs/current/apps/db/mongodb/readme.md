---
sidebar_position: 1
slug: /mongodb
tags:
  - MongoDB
  - Cloud Native Database
---

# MongoDB Getting Started

[MongoDB](https://www.mongodb.com/zh) is a scalable, high-performance, open source NoSQL database written in C++.MongoDB, Inc. is the company behind the database for GIANT ideas, offering the best of traditional databases as well as the flexibility, scale and performance today’s applications require. We build MongoDB and the drivers, offer software and services, run MongoDB University (which has trained over 350,000 engineers in MongoDB), and sponsor the MongoDB community.

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodb-gui-websoft9.png)


If you have installed Websoft9 MongoDB, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:27017,9091** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for MongoDB
4. [Get](./user/credentials) default username and password of MongoDB

## MongoDB Initialization

### Steps for you

You should verify the MongoDB when completed deployment:

**Check MongoDB**

1. Use the **SSH** to connect Server, and run the command below to view the installation information and running status
   ```
   sudo systemctl status mongod
   ```
2. You can ge the message from SSH " Active: active (running)... " when MongoDB is running

**Connect MongoDB**

1. Use the **SSH** to connect Server, and run `mongo` command 
   ~~~
   mongo

   ---
   MongoDB shell version v4.0.18
   connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
   Implicit session: session { "id" : UUID("e5c50eca-e51b-482e-b0bd-24edc2d1e433") }
   MongoDB server version: 4.0.18
   Welcome to the MongoDB shell.
   For interactive help, type "help".
   For more comprehensive documentation, see
         http://docs.mongodb.org/
   Questions? Try the support group
         http://groups.google.com/group/mongodb-user
   ~~~

2. List all databases and users
   ```
   # list all databases
   show dbs

   # use admin, and list all users
   use admin
   show users
   ```

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Does MongoDB enable account authentication by default?**

No, you should modify the configuration file */etc/mongod.conf* if you want 


## MongoDB QuickStart

> 需要了解更多 MongoDB 的使用，请官方文档 [MongoDB Administration](https://docs.mongodb.com/manual/administration/)

## MongoDB Setup

### Enable the MongoDB remote connection{#remote}

1. Use **SSH** to connect MongoDB server and modify the [MongoDB configuration file](#path): *etc/mongod.conf*
   ```
   #1 set authorization **disabled** to **enabled**
   security:
   authorization: enabled

   #2 set bindIP to 0.0.0.0
   net:
      port: 27017
      bindIp: 0.0.0.0
   ```
   > 0.0.0.0 means any Internet IP can connect your MongoDB

2. Restart MongoDB [service](#service)
   ```
   systemctl restart mongod
   ```
3. Go to the Cloud Console and enable the **TCP:27017** port of Security Group


### 开启 MongoDB 访问认证

为了方便试用，默认情况下 MongoDB 认证已关闭。所以，创建用户不需要登录。

打开 [MongoDB 配置文件](#path)，将 authorization字段改为 enabled 即启用认证。

```
security:
  authorization: disabled
```

重启 [MongoDB 服务](#service)后生效

### GUI

The GUI of MongoDB are divided into desktop version and web version. Each form of tool has some popular tools:

**Desktop**

- [MongoDB Compass Community](https://www.mongodb.com/download-center/compass) - A free tool for developing with MongoDB and includes a subset of the features of Compass.
- [dbKoda](https://www.dbkoda.com/) - Cross-platform and open-source IDE
- [MongoHub](https://github.com/jeromelebel/MongoHub-Mac) - Mac native client
- [Mongotron](http://mongotron.io/) - Cross-platform and open-source client built with Electron
- [NoSQLBooster](https://nosqlbooster.com/) - Feature-rich but easy-to-use cross-platform IDE (formerly MongoBooster)
- [Nosqlclient](https://github.com/nosqlclient/nosqlclient) - Cross-platform, self hosted and easy to use management tool (formerly Mongoclient)
- [Robo 3T](https://github.com/Studio3T/robomongo) - Free, native and cross-platform shell-centric GUI (formerly Robomongo)
- [Studio 3T](https://studio3t.com/) - Cross-platform GUI, stable and powerful (formerly MongoChef)

**Web GUI**

- [adminMongo](https://github.com/mrvautin/adminMongo) - Web-based user interface to handle connections and databases needs
- [mongo-express](https://github.com/mongo-express/mongo-express) - Web-based admin interface built with Express
- [mongoadmin](https://github.com/thomasst/mongoadmin) - Admin interface built with Django
- [mongri](https://github.com/dongri/mongri) - Web-based user interface written in JavaScript
- [Rockmongo](https://github.com/iwind/rockmongo) - PHPMyAdmin for MongoDB, sort of

Now, we will introduce how to use **MongoDB compass** and **adminMongo**

**Preparation**

You must enable the authorization of MongoDB and set credential for it before your using the GUI  

1. Use **SSH** to connect MongoDB server and modify the MongDB configuration file *etc/mongod.conf*
   ```
   #1 set authorization **disabled** to **enabled**
   security:
   authorization: enabled

   #2 set bindIP to 0.0.0.0
   net:
      port: 27017
      bindIp: 0.0.0.0
   ```
   > 0.0.0.0 means any Internet IP can connect your MongoDB

2. Restart MongoDB service
   ```
   systemctl restart mongod
   ```
3. Go to the Cloud Console and enable the **TCP:27017** port of Security Group

When completed the preparation, you can use the GUI now

**adminMongo**

adminMongo is a web GUI which installed by Docker for your MongoDB deployment solution

1. Go to the Cloud Console and enable the **TCP:9091** port of Security Group

2. Open Chrome or Firefox on your local PC to visit URL *http://Internet IP:9091*,you can enter the adminMongo page
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect001-websoft9.png)

3. Following is the examples for adminMongo connection(IP is Internet IP0)
   ```
   # use the **config** database
   mongodb://root:1cTFecwTEs@40.114.115.58
   # use the **admin** database
   mongodb://root:1cTFecwTEs@40.114.115.58/admin
   mongodb://parse:AxXFcV5zSz@40.114.115.58/parse
   ```

4. Start to connect
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect002-websoft9.png)

5. Go go adminMongo console when connect successfully
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect003-websoft9.png)

6. Please delete the connections when you don't use it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/adminmongo-connect004-websoft9.png)

**MongoDB Compass**

1. [Download](https://www.mongodb.com/products/compass) and install MongoDB Compass
2. Fill in the correct items and connect MongoDB
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodbcompass001-websoft9.png)
3. Go go MongoDB Compass console when connect successfully
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


### Useful MongoDB Command

**show all database, create database, insert data**

```shell

> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB

-------------------------

#2 create database test, if there have test, it's means switch to test, example
> use test
switched to db test

# show the current database
> db
test

# show the current database users
> show users

-------------------------

#3 Insert data into the database test, example
> db.test.insert({"name":"company"})
WriteResult({ "nInserted" : 1 })

-------------------------
```

**Delete the database**
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

**Create administrator user**

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

### Password management

**Modify password**

You can modify the password of **root** user which added on your MongoDB by the following command

```
mongo admin --u root --p YOURPASSWORD
MongoDB shell version v4.0.18
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
> db = db.getSiblingDB('admin')
admin
> db.changeUserPassword("root", "NEWPASSWORD")
> exit
```

**Reset password**

Reset password is the process of resetting a new password through special solutions in case the password has been forgotten.

1. Use **SSH** to connect MongoDB server and modify the MongoDB configuration file: *etc/mongod.conf*
   ```
   security:
   authorization: disabled
   ```
2. Restart the MongoDB service
   ```
   systemctl restart mongod
   ```
3. Run the MongoDB command to set new password
   ```
   mongo
   > db = db.getSiblingDB('admin')
   admin
   > db.changeUserPassword("root", "NEWPASSWORD")
   ```

4. Repeat step 1, but set authorization to disabled
5. Restart the MongoDB service again

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage MongoDB 


通过运行`docker ps`，可以查看到 MongoDB 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 MongoDB 本身的参数：

### Path{#path}

MongoDB 数据目录: */var/lib/mongodb*   
MongoDB 配置文件: */etc/mongod.conf*   
MongoDB logs file: */var/log/mongodb*   

### Port{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9091   | HTTP 访问 adminMongo	 | 可选   |
| 27017   | MongoDB Server | 可选   |

### Version

```shell
mongodb -V
```

### Service{#service}


```shell
sudo systemctl start | stop | restart | status mongod
sudo docker start | stop | restart | stats adminmongo
```

### CLI{#cmd}

**Server**

安装MongoDB后，启动 bin 目录下的可执行文件 mongod 就可以启动 MongoDB 服务，如果你配置了 Systemd，也可以通过 `systemctl start mongod` 以后台的形式启动 MongoDB。  

MongoDB 在启动的时候，可以通过命令接受一序列参数，也可以通过配置文件接受参数：  

**CLI Arguments**

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

**Configuration File**

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

**Client**

MongoDB Shell 是 MongoDB 自带的一个交互式 JavaScript shell，让您能够访问、配置和管理MongoDB数据库、用户等。使用这个shell可执行各种任务，从设置用户账户到创建数据库，再到查询数据库内容，无所不包。

```
# log in Mongo Shell without authenticating
mongo

# log in Mongo Shell witt authenticating
mongo admin --username root -p

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