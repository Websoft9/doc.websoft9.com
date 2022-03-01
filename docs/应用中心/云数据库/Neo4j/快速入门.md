---
sidebar_position: 1
slug: /neo4j
tags:
  - Neo4j 
  - Cloud Native Database
---

# 快速入门

[Neo4j](https://neo4j.com/) 是一个高性能的 NoSQL 图形数据库，它将事物之间的关系存储为数据库技术，广泛用于知识图谱，社交关系链，商品推荐，IT架构，商品主数据等领域。Neo4j 也可以被看作是一个高性能的图引擎，该引擎具有成熟数据库的所有特性。

Neo4j 官方提供了三个版本：Neo4j Community Edition, Neo4j Enterprise Edition, Neo4j Desktop

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-console-websoft9.png)

在云服务器上部署 Neo4j 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80 和 7687** 端口是否开启
3. 若想用域名访问 Neo4j，请先到 **域名控制台** 完成一个域名解析

## 账号密码


通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Neo4j

管理员用户名： `neo4j`  
管理员密码： `neo4j` 或 存储在您的服务器中的文件中 */credentials/password.txt*  

> 使用本地 Chrome 或 Firefox 访问：*http://Internet IP* 可以使用图形化GUI工具 Neo4j Browser


## Neo4j 安装向导

1. 使用 **SSH** 客户端连接 Neo4j 所在的服务器，输入 `cypher-shell` 命令，并登录（[不知道密码？](/zh/stack-accounts.md)）
   ```
   $cypher-shell
   username: neo4j
   password: *****
   Connected to Neo4j 4.1.0 at neo4j://localhost:7687 as user neo4j.
   Type :help for a list of available commands or :exit to exit the shell.
   Note that Cypher queries must end with a semicolon.
   neo4j@neo4j>
   ```
2. 输入命令 `CALL dbms.showCurrentUser();` 查看当前用户
   ```
   neo4j@neo4j> CALL dbms.showCurrentUser();
   +--------------------------+
   | username | roles | flags |
   +--------------------------+
   | "neo4j"  | admin  | []    |
   +--------------------------+
   1 row available after 22 ms, consumed after another 1 ms
   ```

3. 验证图形化管理工具 Neo4j Browser（[参考](/zh/solution-gui.md#neo4j-browser)）
   ![Neo4j Browser](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-connectfirst-websoft9.png)

> 需要了解更多 Neo4j 的使用，请参考官方文档：[Neo4j Documentation](https://neo4j.com/docs/)

## Neo4j 入门向导

下面以 Neo4j Browser 作为学习工具，完整的让大家快速使用 Neo4j 创建数据和分析数据：

### 用范例数据分析

控制台提供了一个经典范例 **Movie Graph**，根据范例提供的向导可以完成如下动作：

* 创建：将电影数据插入图形
* 查找：检索单个电影和演员
* 查询：发现相关的演员和导演
* 解决：分析某个演员的**六度空间**关系

1. 登录 Neo4j Browser
2. 打开：【Sample Scripts】>【Example Graphs】>【Movie Graph】，点击2/8页下的【Create】图标 
   ![Neo4j 使用范例数据](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-sampleonline001-websoft9.png)

3. 立即可见已经建立了关系的数据
   ![Neo4j 使用范例数据](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-sampleonline002-websoft9.png)

4. 根据向导依次完成后续的页面中的范例

### 自建数据并分析

1. 登录 Neo4j Browser，运行下面的命令录入三条节点数据
   ```
   create (n:Person { name: 'Tom Hanks', born: 1956 }) return n;
   create (n:Person { name: 'Robert Zemeckis', born: 1951 }) return n;
   create (n:Movie { title: 'Forrest Gump', released: 1951 }) return n;
   ```
   ![Neo4j 增加数据](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-inputnodedata001-websoft9.png)

3. 运行查询所有节点数据的命令，便可以看到图形化展示出的数据
   ```
   match(n) return n;
   ```
   ![Neo4j 增加数据](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-inputnodedata002-websoft9.png)

4. 接下来运行下面的命令，给节点创建关系
   ```
   MATCH (a:Person),(b:Movie)
   WHERE a.name = 'Robert Zemeckis' AND b.title = 'Forrest Gump'
   CREATE (a)-[r:DIRECTED]->(b)
   RETURN r;
   ```
5. 再次运行查询节点数据的命令 `match(n) return n;`
   ![Neo4j 增加数据](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-inputnodedata003-websoft9.png)


### 导入数据进行分析

参考：[KGData 行业图谱数据](https://github.com/muniao/KGData)

## 常用操作

### 使用图形化工具

Neo4j 提供了多种图形化工具，有基于 Web 的版本，也有支持 Windows, Linux, macOS 等桌面版本。

#### 开启远程访问

在使用图形化工具之前，请确保开启了远程访问：

1. Neo4j 所在的服务器的安全组，需开启 7687 端口

2. 确保[Neo4j 配置文件](/zh/stack-components.md#neo4j) 中没有限制外网IP访问（默认 0.0.0.0 表示允许）
   ```
   # With default configuration Neo4j only accepts local connections.
   # To accept non-local connections, uncomment this line:
   dbms.default_listen_address=0.0.0.0
   ```

#### Neo4j Browser

Neo4j Browser 是开发人员与图形进行交互的工具。它是Neo4j数据库的企业版和社区版的默认界面。

1. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP*, 访问 Neo4j Browser
![Neo4j Browser](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-connectfirst-websoft9.png)

2. 选择【bolt://】的URL模式，输入用户名和密码（[不知道密码？](/zh/stack-accounts.md)），可能还需提示立即修改密码
![修改Neo4j密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-snewpw-websoft9.png)

> Pick neo4j:// for a routed connection, bolt:// for a direct connection to a DBMS. 选择 bolt:// 速度更快

3. 系统登录到控制台，初始化安装完成
![Neo4j 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-ssui-websoft9.png)

4. 通过:【Database Information】>【server user add】 增加新用户
![Neo4j 增加用户](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-adduser-websoft9.png)

5. 通过:【Cloud Services】>【Clear local data】 退出 Neo4j Browser 
![Neo4j 增加用户](https://libs.websoft9.com/Websoft9/DocsPicture/zh/neo4j/neo4j-loginout-websoft9.png)

#### Neo4j Desktop

[Neo4j Desktop](https://neo4j.com/download-center/) 是开发人员使用本地Neo4j数据库的便捷方式。

1. [下载](https://neo4j.com/download-thanks-deskto)

2. 双击安装至完成，然后到 Neo4j 官网上注册，获取一个秘钥

3. 激活 Neo4j Desktop

4. 连接到远程 Neo4j 数据库，开始使用

#### Neo4j Bloom

探索和可视化图形数据，这是一个付费的工具。

### 用户管理

Neo4j 提供了详细的用户管理和角色管理功能（仅企业版支持）

```
# 显示所有用户
SHOW USERS;
CALL dbms.security.listUsers();

# 创建新用户，第三个参数表示 requridchangepassword 
CALL dbms.security.createUser('username','password',false);

# 删除用户
CALL dbms.security.deleteUser('username');   
```

详情参考官网文档：[User and role management](https://neo4j.com/docs/cypher-manual/current/administration/security/users-and-roles/#administration-security-users)

### 域名绑定

绑定域名的前置条件是：Neo4j Browser已经可以通过解析后的域名访问。  

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

Neo4j 域名绑定操作步骤：

1. 登录云服务器
2. 修改 [Nginx虚拟机主机配置文件](/zh/stack-components.md#nginx)，将其中的 **server_name** 项的值 *_* 修改为你的域名
   ```text
   server {
      listen 80;
      server_name  _; # 改为自定义域名
   ...
   ```
3. 保存配置文件，重启[Nginx服务](/zh/admin-services.md#nginx)

### SSL/HTTPS

HTTPS 是 [Neo4j 安全](https://neo4j.com/docs/operations-manual/current/security/)管理的一部分，完全域名绑定且可以通过 HTTP 访问之后，方可设置HTTPS。

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 Neo4j Browser ，才可以设置 HTTPS。

Neo4j 预装包，已安装 We b服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了证书，只需三个步骤，即可完成 HTTPS 配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 *server{ }* 中
 ``` text
   #-----HTTPS template start------------
   listen 443 ssl; 
   ssl_certificate /data/cert/xxx.crt;
   ssl_certificate_key /data/cert/xxx.key;
   ssl_trusted_certificate /data/cert/chain.pem;
   ssl_session_timeout 5m;
   ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
   ssl_prefer_server_ciphers on;
   #-----HTTPS template end------------
   ```
3. 重启[Nginx服务](/zh/admin-services.md#nginx)

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### 重置密码

常用的 Neo4j 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

修改密码只需登录服务器后运行一条命令即可：  

下面的示例是将旧密码`neo4j`更改为新密码`neo4j123`：


```
echo "
ALTER CURRENT USER SET PASSWORD FROM 'neo4j' TO 'neo4j123';
" | cypher-shell -u neo4j  -p neo4j  -d system
```

#### 找回密码

如果用户忘记了密码，通过配置文件临时去掉验证，然后设置密码，再复原的方法找回密码：

1. 停止 Neo4j
   ```
   sudo systemctl stop neo4j
   ```

2. 修改 [Neo4j 的配置文件](/zh/stack-components.md#neo4j)，将`#dbms.security.auth_enabled=false` 改成
   ```
   dbms.security.auth_enabled=false
   ```
3. 重新启动 Neo4j 服务后，开始修改密码
   ```
   sudo systemctl start neo4j
   cypher-shell -d system
   
   neo@system> ALTER USER neo4j SET PASSWORD 'mynewpass';
   neo@system> :exit
   ```

4. 复原配置文件
5. 重启 Neo4j 服务

以上方案来自官方文档：[Password and user recovery](https://neo4j.com/docs/operations-manual/current/configuration/password-and-user-recovery/)



## 异常处理

#### 浏览器打开IP地址，无法访问 Neo4j（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 能够访问 Neo4j Browser，但是连接数据库报错？

您的服务器对应的安全组 7687 端口没有开启（入规则），导致无法连接数据库

#### 为什么 Neo4j Browser 中 Roles 显示为空？

Neo4j 社区版不支持 Roles，故显示为空。

