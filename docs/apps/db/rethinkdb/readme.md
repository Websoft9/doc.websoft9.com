---
sidebar_position: 1
slug: /rethinkdb
tags:
  - RethinkDB
  - Cloud Native Database
---

# 快速入门

[RethinkDB](https://rethinkdb.com) 是一个曾经与 MongoDB 齐名的开源文档（JASON）数据库，目前完全由开源社区驱动。它支持多种数据类型，提供可视化的控制台，很方便部署和构建集群。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 RethinkDB 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 RethinkDB 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  RethinkDB，务必先完成 **[域名五步设置](./dns#domain)** 过程
## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)


## RethinkDB 初始化安装向导

### 详细步骤

1. 使用本地电脑的浏览器访问网址：*http://域名* 或 *http://服务器公网IP*，准备登陆 RethinkDB 控制台

2. 输入[用户名和密码](./setup/credentials#getpw)，成功登录到 RethinkDB 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-gui-websoft9.png)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## RethinkDB 使用入门

下面以 **演示如何增加 Database 和 Table** 作为一个任务，帮助用户快速入门：

1. 依次打开：【Tables】>【Add Database】，增加一个数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-adddb-websoft9.png)

2. 打开数据库，点击【Add Table】增加表
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-addtable-websoft9.png)

> 需要了解更多 RethinkDB 的使用，请参考官方文档：[RethinkDB Documentation](https://rethinkdb.com/docs)

## RethinkDB 常用操作

### 控制台密码管理

RethinkDB 控制台默认没有提供登录认证，本部署方案采用了  [Nginx auth_bacic](./nginx#auth_basic) 作为登录认证方案

### 远程访问

RethinkDB 远程访问的开关存储在：*/etc/rethinkdb/instances.d/instance.conf* 文件中。  

只需执行下面命令，然后重启服务，即可开启远程访问。

```
sudo sed -n "s/^#bind=/bind=0.0.0.0/g" /etc/rethinkdb/instances.d/instance.conf
```

### 用户管理

下面以**新增用户、密码和重置密码**作为范例进行说明：


1. 以 `admin` 用户身份连接数据库（只有 admin 用户具有用户系统表的访问权限，因此必须以 admin 用户连接到数据库）
   ```
   from rethinkdb import r

   # 无密码连接
   r.connect('localhost', 28015).repl()

   # 有密码连接
   r.connect('localhost', 28015, password='123456').repl()
   ```

2. 新增用户名和密码（用户信息存储在 **users** [系统表](https://rethinkdb.com/docs/system-tables/)中）
   ```
   r.db('rethinkdb').table('users').insert({id: 'bob', password: 'secret'})
   ```

3. 重置指定用户的密码

    ```
    # 重置为新密码
    r.db('rethinkdb').table('users').get('username').update({password: newpassword})

    # 重置为空密码
    r.db('rethinkdb').table('users').get('username').update({password: false})
    ```

### 重置密码

常用的 RethinkDB 重置密码相关的操作主要有修改密码和清空密码（将密码设置为空）两种方式。  

1. 登录 RethinkDB Web 界面，在【Data explorer】下输入所需的命令

   ```
   # 修改密码命令
   r.db('rethinkdb').table('users').get('admin').update({password: 'newpassword'})

   # 清空密码命令
   r.db('rethinkdb').table('users').get('admin').update({password: false})
   ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-editpassword-websoft9.png)

2. 点击【run】后生效


### 图形化工具

RethinkDB 可视化控制台是它的重要组成部分，是其重要的产品特征。  

1. 使用本地电脑的浏览器访问网址：*http://服务器公网IP*，准备登陆 RethinkDB 控制台

2. 输入用户名和密码（[不知道账号密码？](/zh/stack-accounts.md#rethinkdb)）

3. 成功登录到 RethinkDB 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-ok-websoft9.png)

4. 依次打开：【Tables】>【Add Database】，增加一个数据库
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-adddb-websoft9.png)

5. 打开数据库，点击【Add Table】增加表
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rethinkdb/rethinkdb-addtable-websoft9.png)

## RethinkDB 参数

RethinkDB 应用中包含 Nginx, Docker 等组件，可通过 **[通用参数表](../setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Jenkins 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 RethinkDB 本身的参数：

### 路径{#path}

* RethinkDB 配置文件： */etc/rethinkdb/instances.d/instance.conf *

### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | RethinkDB 控制台原始端口，已通过 Nginx 转发到 80 端口 | 可选   |
| 28015 | RethinkDB connect | 可选   |

### 版本

```shell
rethinkdb --version
```

### 服务

```shell
sudo systemctl start | stop | restart | status rethinkdb
```

### 命令行

#### 服务端

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

#### 客户端

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

### API

上述客户端命令即 API

