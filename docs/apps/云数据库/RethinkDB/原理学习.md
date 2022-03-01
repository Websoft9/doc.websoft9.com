---
sidebar_position: 3
slug: /rethinkdb/study
tags:
  - RethinkDB
  - Cloud Native Database
---

# 原理学习

RethinkDB 是一个与 MongoDB 对标的开源数据库，RethinkDB 定位于实时数据库应用：

- 协作式Web和移动应用程序
- 流分析应用
- 多人游戏
- 实时市场
- 连接的设备

## 用户权限

RethinkDB 中的用户类似于大多数其他数据库系统中的用户。  

### 用户管理

#### 管理密码

默认管理员用户名为 `admin`，密码为空。通过服务端命令行，可以很方便的设置管理员密码：

```
rethinkdb --initial-password yourpassword
```

#### 创建用户

RethinkDB 不仅仅支持管理员用户，用户也可以增加更多的用户，所有的用户信息存储在 **users** [系统表](https://rethinkdb.com/docs/system-tables/)中。  

由于系统表只有 admin 用户采用访问权限，因此必须以 admin 用户连接到数据库之后，再参考下面命令创建新用户：  

```
# 创建带密码的用户
r.db('rethinkdb').table('users').insert({id: 'username', password: 'secret'})
```

#### 重置密码

```
# 重置为新密码
r.db('rethinkdb').table('users').get('username').update({password: newpassword})

# 重置为空密码
r.db('rethinkdb').table('users').get('username').update({password: false})
```

### 权限

权限存储在 permissions 系统表中。虽然您可以通过修改该表中的文档来更改权限，但使用grant命令要方便得多。

默认支持四种权限：

* read
* write
* config
* connect

有三种权限范围：  

* 表（仅影响表）
* 数据库（影响数据库和其中的表）
* 全局（影响所有数据库和其中的表）


## 访问控制

RethinkDB 默认启动不支持远程访问，修改它的配置文件：*/etc/rethinkdb/instances.d/instance.conf*  中的 bind 项。  
```
bind=0.0.0.0
```


## 数据

### 系统表

RethinkDB 维护特殊的[系统表](https://rethinkdb.com/docs/system-tables/)，其中包含有关服务器、数据库、单个表和集群问题的配置和状态信息。

### 备份

运行 `rethinkdb dump` 备份数据

### 导入

运行 `rethinkdb import` 导入数据

## 集群


## ReQL

RethinkDB 不支持传统是数据库语言 SQL 。但是，RethinkDB的查询语言 [ReQL](https://rethinkdb.com/docs/introduction-to-reql/) 几乎可以执行 SQL 所能做的一切，包括表联接和聚合功能，并且功能强大，表达力强且易于学习。  

ReQL还可以完成SQL无法完成的许多工作，包括将查询与JavaScript表达式和map-reduce混合使用。

## CLI

### 服务端

RethinkDB 提供了强大的的**服务端**命令行工具 `rethinkdb`  

```
$rethinkdb -h

Running 'rethinkdb' will create a new data directory or use an existing one,
  and serve as a RethinkDB server.
File path options:
  -d [ --directory ] path                     specify directory to store data and
                                              metadata
  --io-threads n                              how many simultaneous I/O operations
                                              can happen at the same time
  --direct-io                                 use direct I/O for file access
  --cache-size mb                             total cache size (in megabytes) for
                                              the process. Can be 'auto'.

Server options:
  -n [ --server-name ] arg                    the name for this server (as will
                                              appear in the metadata).  If not
                                              specified, one will be generated from
                                              the hostname and a random
                                              alphanumeric string.
  -t [ --server-tag ] arg                     a tag for this server. Can be
                                              specified multiple times.

Network options:
  --bind {all | addr}                         add the address of a local interface
                                              to listen on when accepting
                                              connections, loopback addresses are
                                              enabled by default. Can be overridden
                                              by the following three options.
  --bind-cluster {all | addr}                 override the behavior specified by
                                              --bind for cluster connections.
  --bind-driver {all | addr}                  override the behavior specified by
                                              --bind for client driver connections.
  --bind-http {all | addr}                    override the behavior specified by
                                              --bind for web console connections.
  --no-default-bind                           disable automatic listening on
                                              loopback addresses
  --cluster-port port                         port for receiving connections from
                                              other servers
  --driver-port port                          port for rethinkdb protocol client
                                              drivers
  -o [ --port-offset ] offset                 all ports used locally will have this
                                              value added
  -j [ --join ] host[:port]                   host and port of a rethinkdb server
                                              to connect to
  --reql-http-proxy [protocol://]host[:port]  HTTP proxy to use for performing
                                              `r.http(...)` queries, default port
                                              is 1080
  --canonical-address host[:port]             address that other rethinkdb
                                              instances will use to connect to us,
                                              can be specified multiple times
  --join-delay seconds                        hold the TCP connection open for
                                              these many seconds before joining
                                              with another server
  --cluster-reconnect-timeout seconds         maximum number of seconds to attempt
                                              reconnecting to a server before
                                              giving up, the default is 24 hours

TLS options:
  --http-tls-key key_filename                 private key to use for web
                                              administration console TLS
  --http-tls-cert cert_filename               certificate to use for web
                                              administration console TLS
  --driver-tls-key key_filename               private key to use for client driver
                                              connection TLS
  --driver-tls-cert cert_filename             certificate to use for client driver
                                              connection TLS
  --driver-tls-ca ca_filename                 CA certificate bundle used to verify
                                              client certificates; TLS client
                                              authentication disabled if omitted
  --cluster-tls-key key_filename              private key to use for intra-cluster
                                              connection TLS
  --cluster-tls-cert cert_filename            certificate to use for intra-cluster
                                              connection TLS
  --cluster-tls-ca ca_filename                CA certificate bundle used to verify
                                              cluster peer certificates
  --tls-min-protocol protocol                 the minimum TLS protocol version that
                                              the server accepts; options are
                                              'TLSv1', 'TLSv1.1', 'TLSv1.2';
                                              default is 'TLSv1.2'
  --tls-ciphers cipher_list                   specify a list of TLS ciphers to use;
                                              default is 'EECDH+AESGCM'
  --tls-ecdh-curve curve_name                 specify a named elliptic curve to use
                                              for ECDHE; default is 'prime256v1'
  --tls-dhparams dhparams_filename            provide parameters for DHE key
                                              agreement; REQUIRED if using DHE
                                              cipher suites; at least 2048-bit
                                              recommended

Authentication options:
  --initial-password {auto | password}        sets an initial password for the
                                              "admin" user on a new server.  If set
                                              to auto, a random password will be
                                              generated.

Web options:
  --web-static-directory directory            the directory containing web
                                              resources for the http interface
  --http-port port                            port for web administration console
  --no-http-admin                             disable web administration console

CPU options:
  -c [ --cores ] n                            the number of cores to use

Service options:
  --pid-file path                             a file in which to write the process
                                              id when the process is running
  --daemon                                    daemonize this rethinkdb process

Set User/Group options:
  --runuser user                              run as the specified user
  --rungroup group                            run with the specified group

Help options:
  -h [ --help ]                               print this help
  -v [ --version ]                            print the version number of rethinkdb

Log options:
  --log-file file                             specify the file to log to, defaults
                                              to 'log_file'
  --no-update-check                           obsolete.  Update checking has been
                                              removed.

Configuration file options:
  --config-file                               take options from a configuration
                                              file


There are a number of subcommands for more specific tasks:
    'rethinkdb create': prepare files on disk for a new server instance
    'rethinkdb serve': use an existing data directory to host data and serve queries
    'rethinkdb proxy': serve queries from an existing cluster but don't host data
    'rethinkdb export': export data from an existing cluster into a file or directory
    'rethinkdb import': import data from from a file or directory into an existing cluster
    'rethinkdb dump': export and compress data from an existing cluster
    'rethinkdb restore': import compressed data into an existing cluster
    'rethinkdb index-rebuild': rebuild outdated secondary indexes
    'rethinkdb repl': start a Python REPL with the RethinkDB driver

For more information, run 'rethinkdb help [subcommand]'.
```

### 客户端

RethinkDB 官方没有客户端 CLI，但提供了Python, Java, Node 等开发语言的 [RethinkDB client drivers](https://rethinkdb.com/docs/install-drivers/)。  

用户通过这些 drivers 以程序的方式连接 RethinkDB 服务，然后进行场景的数据库操作。  

下面以 Python 为例描述如何具体使用：

1. 安装 rethinkdb 驱动
   ```
   pip3 install rethinkdb
   ```

2. 编写 Python 程序，连接 RethinkDB 服务器
   ```
   from rethinkdb import r
   r.connect('localhost', 28015).repl()
   r.db('test').table_create('tv_shows').run()
   r.table('tv_shows').insert({ 'name': 'Star Trek TNG' }).run()
   ```