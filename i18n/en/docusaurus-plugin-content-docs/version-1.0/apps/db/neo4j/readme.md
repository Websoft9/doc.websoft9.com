---
sidebar_position: 1
slug: /neo4j
tags:
  - Neo4j 
  - Cloud Native Database
---

# Neo4j Getting Started

[Neo4j](https://neo4j.com/) is the world’s leading Graph Database. It is a high performance graph store with all the features expected of a mature and robust database, like a friendly query language and ACID transactions. The programmer works with a flexible network structure of nodes and relationships rather than static tables — yet enjoys all the benefits of enterprise-quality database. For many applications, Neo4j offers orders of magnitude performance benefits compared to relational DBs.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-console-websoft9.png)

If you have installed Websoft9 Neo4j, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80,7687** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Neo4j
4. [Get](./user/credentials) default username and password of Neo4j

## Neo4j Initialization

### Steps for you

1. Use **SSH** to connect Neo4j Server, run the command `cypher-shell`, you should input your username and password for this command.([Don't known password?](./user/credentials))
   ```
   $cypher-shell
   username: neo4j
   password: *****
   Connected to Neo4j 4.1.0 at neo4j://localhost:7687 as user neo4j.
   Type :help for a list of available commands or :exit to exit the shell.
   Note that Cypher queries must end with a semicolon.
   neo4j@neo4j>
   ```
2. Run the command `CALL dbms.showCurrentUser();` to show all users
   ```
   neo4j@neo4j> CALL dbms.showCurrentUser();
   +--------------------------+
   | username | roles | flags |
   +--------------------------+
   | "neo4j"  | admin  | []    |
   +--------------------------+
   1 row available after 22 ms, consumed after another 1 ms
   ```

3. Try the GUI tool **Neo4j Browser**([Neo4j Browser](#browser))
   ![Neo4j Browser](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-connectfirst-websoft9.png)

> More useful Neo4j guide, please refer to [Neo4j Documentation](https://neo4j.com/docs/)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**I can visit Neo4j Browser but database connection error?**

Your TCP:7687 of Security Group Rules is not allowed so that Neo4j Browser can't connect Neo4j from this port

**WhyNeo4j Browser roles is null?**

Neo4j Community Edition not support roles


## Neo4j QuickStart

We will provide a quick guide for you to use Neo4j Browser, you can get a complete data analysis.

**Use sample data for analysis**

You can use the sample **Movie Graph** on the Neo4j Browser console for the following steps:

* Create data
* Query node
* Solve relationship

1. Login to Neo4j Browser

2. Open:【Sample Scripts】>【Example Graphs】>【Movie Graph】, click 【Create】icon at 2/8
   ![Neo4j use sample](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-sampleonline001-websoft9.png)

3. You can see the relationship graph
   ![Neo4j use sample](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-sampleonline002-websoft9.png)

4. Complete the more steps

**Create data for analysis**

1. Login Neo4j Browser, run the following command to create Node data
   ```
   create (n:Person { name: 'Tom Hanks', born: 1956 }) return n;
   create (n:Person { name: 'Robert Zemeckis', born: 1951 }) return n;
   create (n:Movie { title: 'Forrest Gump', released: 1951 }) return n;
   ```
   ![Neo4j add data](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-inputnodedata001-websoft9.png)

2. Run the query command to show graph
   ```
   match(n) return n;
   ```
   ![Neo4j add data](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-inputnodedata002-websoft9.png)

3. Create relationship by the following command
   ```
   MATCH (a:Person),(b:Movie)
   WHERE a.name = 'Robert Zemeckis' AND b.title = 'Forrest Gump'
   CREATE (a)-[r:DIRECTED]->(b)
   RETURN r;
   ```
4. Run the query `match(n) return n;`
   ![Neo4j show graph](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-inputnodedata003-websoft9.png)

**Import data for analysis**

  > Refer to ：[KGData Industry Graph Data](https://github.com/muniao/KGData)

## Neo4j Setup

### Enable remote connection{#remote}

1. Check **[Inbound of Security Group Rule](https://support.websoft9.com/docs/faq/tech-instance.html)** of Cloud Console to ensure the 7687 allowed

2. Check [Neo4j configuration file](#path) have accept all IP connection(0.0.0.0 mean allowed)
   ```
   # With default configuration Neo4j only accepts local connections.
   # To accept non-local connections, uncomment this line:
   dbms.default_listen_address=0.0.0.0
   ```


### Manage Users

First you can read the official docs: [User and role management](https://neo4j.com/docs/cypher-manual/current/administration/security/users-and-roles/#administration-security-users) to get basic knowledge.  

The following is some useful command for user management:  

```
# Show all users
SHOW USERS;

# Create new user
```

```
# Show all users
SHOW USERS;
CALL dbms.security.listUsers();

# Create new user, the third parameter is requridchangepassword 
CALL dbms.security.createUser('username','password',false);

# Delete user
CALL dbms.security.deleteUser('username');   
```

### GUI

Neo4j have some useful GUI tools, include web-based and desktop, support Windows, Linux, macOS.

Before use GUI tool, you should [enable remote connection](#remote)

#### Neo4j Browser{#browser}

Neo4j Browser is a web-base tool for Neo4j, included in the Neo4j Server by default

1. Using local Chrome visit the URL *http://domain* or *http://Server's Internet IP*, access to Neo4j Browser

![Neo4j Browser](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-connectfirst-websoft9.png)

2. Select 【bolt://】URL mode, and input the [default username and password](./user/credentials), then the system may force a password change.

![modify Neo4j password](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-snewpw-websoft9.png)

> Pick neo4j:// for a routed connection, bolt:// for a direct connection and fast than neo4j://

4. After modifying the new password, the system logs in to the console and initializes the installation.

![Neo4j Console](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-ssui-websoft9.png)

5. You can add user by **Database Information** > **server user add** (Enterprise Edition)

![Neo4j add user](https://libs.websoft9.com/Websoft9/DocsPicture/en/neo4j/neo4j-adduser-websoft9.png)

#### Neo4j Desktop{#desktop}

[Neo4j Desktop](https://neo4j.com/download-center/) is a local tool for developer.

#### Neo4j Bloom

Neo4j Bloom is the graph visualization and exploration tool 


### Reset Password

There are two main measures to reset password for Neo4j

**Changing password**

You can change password using jut one command below sample:

```
# Change old password "neo4j" to new password "neo4j123"

echo "
ALTER CURRENT USER SET PASSWORD FROM 'neo4j' TO 'neo4j123';
" | cypher-shell -u neo4j  -p neo4j  -d system
```

**Forgot Password**

Try to retrieve your password through the following steps when forgot it:

1. Stop Neo4j server
   ```
   sudo systemctl stop neo4j
   ```

2. Modify [Neo4j configuration file](#path), set `#dbms.security.auth_enabled=false` to the following value
   ```
   dbms.security.auth_enabled=false
   ```

3. Restart Neo4j and set a new password
   ```
   sudo systemctl start neo4j
   cypher-shell -d system
   
   neo@system> ALTER USER neo4j SET PASSWORD 'mynewpass';
   neo@system> :exit
   ```

4. Recovery Neo4j configuration file

5. Restart the Neo4j service
   ```
   sudo systemctl restart neo4j
   ``` 

More details please refer to: [Password and user recovery](https://neo4j.com/docs/operations-manual/current/configuration/password-and-user-recovery/)


## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Neo4j 


下面仅列出 Neo4j 本身的参数：

### Path{#path}

运行 `neo4j console` 命令查看安装相关的路径：

Neo4j 程序路径：*/var/lib/neo4j*  
Neo4j 配置文件路径：*/etc/neo4j/neo4j.conf*   
Neo4j 日志路径：*/var/log/neo4j*  
Neo4j 插件路径：*/var/lib/neo4j/plugins*  
Neo4j 数据路径：*/var/lib/neo4j/data*  
Neo4j 证书路径：*/var/lib/neo4j/certificates*  
Neo4j 启动路径：*/var/run/neo4j*  

> 更多安装路径请查看 *neo4j.conf* 文件，配置文件设置参考[此处](https://neo4j.com/docs/operations-manual/current/configuration)

### Port

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 7687   | Neo4j Browser 远程连接 Neo4j database | 可选   |

更多的端口：[Port on Configuration file](https://neo4j.com/docs/operations-manual/current/configuration/ports/)

### Version

```shell
neo4j-admin -V
neo4j version
```

### Service

```shell
sudo systemctl start | stop | restart | status neo4j
```

### CLI

Neo4j 通过了一系列的命令行工具，用于管理服务、导入数据、分析数据，详情参考：[Neo4j Tools](https://neo4j.com/docs/operations-manual/current/tools/)

**Cypher Shell**

[Cypher Shell](https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/) is a command-line tool that comes with the Neo4j installation. Cypher Shell is used to run queries and perform administrative tasks. It communicates via the encrypted binary protocol Bolt.

```
root@neo4j-test:~# cypher-shell
username: neo4j
password: *****
Connected to Neo4j 3.5.14 at bolt://localhost:7687 as user neo4j.
Type :help for a list of available commands or :exit to exit the shell.
Note that Cypher queries must end with a semicolon.
neo4j>
```

**neo4j-admin**

[Neo4j Admin](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/) is the primary tool for managing your Neo4j instance. It is a command-line tool that is installed as part of the product and can be executed with a number of commands. Some of the commands are described in more detail in separate sections.

```
$ neo4j-admin help
Usage: neo4j-admin [-hV] [COMMAND]
Neo4j database administration tool.
  -h, --help      Show this help message and exit.
  -V, --version   Print version information and exit.
Commands:
  help                  Displays help information about the specified command
  memrec                Print Neo4j heap and pagecache memory settings recommendations.
  dump                  Dump a database into a single-file archive.
  store-info            Print information about a Neo4j database store.
  report                Produces a zip/tar of the most common information needed for remote assessments.
  load                  Load a database from an archive created with the dump command.
  check-consistency     Check the consistency of a database.
  import                Import a collection of CSV files.
  set-default-admin     Sets the default admin user.
                        This user will be granted the admin role on startup if the system has no roles.
  set-initial-password  Sets the initial password of the initial admin user ('neo4j'). And removes the requirement to
                          change password on first login.
```

**neo4j**

```
$neo4j -h
Usage: neo4j { console | start | stop | restart | status | version }
```

### API

[The Neo4j REST API Documentation](https://neo4j.com/docs/rest-docs/current/)