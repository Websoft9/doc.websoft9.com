---
sidebar_position: 3
slug: /mongodb/study
tags:
  - MongoDB
  - Cloud Native Database
---

# 原理学习

## 概念

### NoSQL

NoSQL 即 Not only SQL的简称，并非 Not SQL，也即意味着 NoSQL 数据库也有着类似 SQL 的查询概念。 NoSQL 是一个包罗万象的术语，涵盖了除传统的关系型数据库（RDBMS）之外的所有数据库。NoSQL 试图放弃关系型数据库的传统结构，让开发人员能够以更接近系统数据流需求的方式实现模型。当前有多种不同的 NoSQL 技术，包括：

* 文档存储数据库
* 健/值数据库
* 列存储数据库
* 图存储数据库

MongoDB 就属于文档存储数据库的杰出代表。文档数据库采用面向文档的方法存储数据，其背后的理念是，可以将单个实体的所有数据存放在一个文档中，而文档以**集合**的形式组合起来。  

MongoDB 采用 BSON（一种轻量级的二进制JSON）格式存储数据，每个文档最大不能超过16MB，避免查询占用太多内存或频繁访问文件系统，因此性能非常高。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/mongodb-gui-websoft9.png)

### SQL vs MongoDB

The basic concepts in mongodb are document, collection, and databases. let's take SQL as an example to help you better understand MongoDB.

| SQL Term/concept | MongoDB Term/concept | explain |
| :--- | :--- | :--- |
| database | database | Database Instance |
| table | collection | databae table/collection |
| row | document | table row/document |
| column | field | Data field/domain |
| index | index | index |
| table joins |   | MongoDB no this |
| primary key | primary key | keyPrimary key, MongoDB automatically sets the _id field as the primary key |

Through the example below, we can also understand some concepts in Mongo more intuitively:

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mongodb/nosqlvssql-websoft9.png)


### MongoDB 数据类型

MongoDB 的数据类型非常类似 JavaScript 对象。

**字符串** - 这是用于存储数据的最常用的数据类型。MongoDB中的字符串必须为`UTF-8`。

**整型** - 此类型用于存储数值。 整数可以是`32`位或`64`位，具体取决于服务器。

**布尔类型** - 此类型用于存储布尔值(`true` / `false`)值。

**双精度浮点数** - 此类型用于存储浮点值。

**最小/最大键** - 此类型用于将值与最小和最大`BSON`元素进行比较。

**数组** - 此类型用于将数组或列表或多个值存储到一个键中。

**时间戳** - `ctimestamp`，当文档被修改或添加时，可以方便地进行录制。

**对象** - 此数据类型用于嵌入式文档。

**对象** - 此数据类型用于嵌入式文档。

**Null** - 此类型用于存储`Null`值。

**符号** - 该数据类型与字符串相同; 但是，通常保留用于使用特定符号类型的语言。

**日期** - 此数据类型用于以UNIX时间格式存储当前日期或时间。您可以通过创建日期对象并将日，月，年的日期进行指定自己需要的日期时间。

**对象ID** - 此数据类型用于存储文档的ID。

**二进制数据** - 此数据类型用于存储二进制数据。

**代码** - 此数据类型用于将JavaScript代码存储到文档中。

**正则表达式** - 此数据类型用于存储正则表达式。

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

## 配置

### 启动

安装MongoDB后，启动 bin 目录下的可执行文件 mongod 就可以启动 MongoDB 服务，如果你配置了 Systemd，也可以通过 `systemctl start mongod` 以后台的形式启动 MongoDB。  

MongoDB 在启动的时候，可以通过命令接受一序列参数，也可以通过配置文件接受参数：  

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

### MongoDB shell

MongoDB shell 是一个可执行文件，位于安装路径的 bin 目录下，执行 `mongo` 命令即可启动 MongoDB shell。它是基于 JavaScript 语法的，即可以使用 JavaScript 语法与数据库进行交付。

```
[root@mongodb-test-centos7 ~]# mongo
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


### 账户和访问控制

MongoDB 支持账号访问控制方式，也支持 Kerberos, LDAP 等外部身份验证机制。本章我们只介绍账户方式相关的四个关键要点：

#### 数据库、用户和角色

通过阅读下面的代码理解用户、数据库和角色的关系
```
use reporting
db.createUser(
  {
    user: "reportsUser",
    pwd: "12345678",
    roles: [
       { role: "read", db: "reporting" },
       { role: "read", db: "products" },
       { role: "read", db: "sales" },
       { role: "readWrite", db: "accounts" }
    ]
  }
)
```
对MongoDB来说，每个用户都存在一个数据库中（区别于MySQL中所有的用户存储在一个系统数据库中）  

系统默认，会自动创建 admin 数据库，这是一个特殊数据库，提供了普通数据库没有的功能，对于具备全局管理权限的数据库用户，必须存储在这个 admin 数据中。

#### 启用认证

创建了用户，并不会要求登录，只有开启了认证才会要求登录访问数据库。

打开MongoDB配置文件：*/etc/mongod.conf*，将authorization字段改为 enabled 即启用认证。

```
security:
  authorization: disabled
```

为了方便试用，默认情况下认证已关闭。


## 使用

### 应用程序访问

MongoDB支持主流的开发程序直接访问，包括：PHP、Java、Python、Node.js等

### 工具

MongoDB 官方提供了更多的工具，包括：

**MongoDB Atlas Open Service Broker**  
Learn how you can use the Atlas Open Service Broker to deploy Atlas clusters and manage database users from within Kubernetes.

**MongoDB BI Connector**  
Reference guide for the MongoDB BI Connector. Learn how you can use business intelligence tools and SQL to query data stored in MongoDB.

**MongoDB Charts**  
Reference guide for MongoDB Charts. Learn how to create visualizations of MongoDB data quickly and easily.

**MongoDB Command Line Interface**  
Learn how to use the MongoDB Command Line Interface to quickly interact with your MongoDB deployments for easier testing and scripting.

**MongoDB Compass**  
Reference guide for MongoDB Compass. Learn to use MongoDB Compass's graphical user interface to view and analyze data stored in MongoDB.

**MongoDB Database Tools**  
Tools for interfacing with a MongoDB cluster, such as importing/exporting data.

**MongoDB Kafka Connector**  
Learn how to persist data from Kafka topics as a data sink into MongoDB as well as publish changes from MongoDB into Kafka topics as a data source.

**MongoDB Kubernetes Operator**  
Learn how you can use the Kubernetes Operator to run MongoDB Enterprise on Kubernetes and configure Cloud or Ops Manager for backup and monitoring.

**MongoDB Spark Connector**  
Reference guide for the MongoDB Spark Connector. Learn how you can use MongoDB with Apache Spark.

## MongoDB shell

MongoDB Shell 是 MongoDB 自带的一个交互式 JavaScript shell，让您能够访问、配置和管理MongoDB数据库、用户等。使用这个shell可执行各种任务，从设置用户账户到创建数据库，再到查询数据库内容，无所不包。

### 启动 MongoDB shell

使用 Websoft9 提供的 MongoDB 部署方案，默认已经配置好了环境变量。只需登录服务器，运行`mongo`命令，即可进入 MongoDB shell

```shell
# log in Mongo Shell without authenticating
mongo

# log in Mongo Shell witt authenticating
mongo admin --username root -p


MongoDB Enterprise > help
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


### 常见命令

#### 显示、创建和切换数据库

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


#### 删除数据库
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

#### 创建管理员账号

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

## 参考

本文档在写作过程中，一方面来源于实践，另一方面参考了大量书籍、资料和文献，感谢 MongoDB 生态中各种优秀的技术传播者

下面列出主要参考书目：
* [《菜鸟教程：MongoDB》](https://www.runoob.com/mongodb/mongodb-tutorial.html)