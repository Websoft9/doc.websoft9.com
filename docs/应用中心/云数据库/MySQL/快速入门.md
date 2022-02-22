---
sidebar_position: 1
slug: /mysql
tags:
  - MySQL
  - Cloude Native Database
---

# 快速入门

[MySQL](https://www.mysql.com/products/community/) 是全球知名的关系型数据库管理系统，由瑞典MySQL AB国内公司开发，几经易手目前属于Oracle旗下产品。考虑到Oracle可能会逐渐关闭MySQL开源版，原MySQL创始人Michael Widenius于2014年联合旧部在芬兰主导了MySQL的分支MariaDB，这个名称来自他的女儿Maria的名字，未来MySQL一旦被Oracle叫停，MariaDB完全可以替代甚至更好。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql-mariadb-ui-websoft9.png)

在云服务器上部署 MySQL 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 如果想从本地客户端远程连接 MySQL，登录云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:3306** 端口是否开启
3. 如果想使用可视化管理工具 phpMyAdmin，登录云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:9090** 端口是否开启

## 账号密码

使用MySQL，可能会用到的几组账号密码如下：

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器指定文件中   

  - Linux 系统  

     **密码存储路径**：*/credentials/password.txt*    
     **获取方式**： 建议通过云控制台的命令终端，运行下图**红框**所示命令，获取数据库密码   
     ![运行cat命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

  - Windows 系统  

     **密码存储路径**：*C:/credentials/password.txt*     
     **获取方式**： 远程桌面到服务器，打开此文件即可   

  **注意**：若服务器上不存在 password.txt 文件，那么数据库密码是 `123456`。此时务必修改为强密码，类似于：`f@N7eUUm25xAjP!$` ，这样有助于提高数据库的安全性，减少数据库密码被破解的风险。

 > 需要登录MySQL，请参考 [图形化工具：phpMyAdmin](/zh/solution-phpmyadmin.md)


## MySQL 入门向导

部署 MySQL 之后，依次完成下面的步骤，验证其可用性

1. 使用 SSH 连接 MySQL 所在的服务器，运行下面的命令，查看 MySQL 的安装信息和运行状态
   ```
   sudo systemctl status mysqld
   或
   sudo systemctl status mysql
   ```
2. 运行服务状态查询命令，MySQL 正常运行会得到 " Active: active (running)... " 的反馈

镜像安装完成后，MySQL就可以使用了。使用MySQL有两种方式

### 命令方式连接 MySQL

1. 使用Putty远程登录到Linux服务器（或远程桌面登录到Windows-CMD窗口），运行命令
   ~~~
   #假设初始密码是：123456
   mysql -uroot –p123456
   ~~~

2. 查看反馈的信息中MySQL版本
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/mysql/mysql01.png)


### phpMyAdmin 连接 MySQL

如果部署方案中包含 phpMyAdmin 等图形化工具，使用就更加便捷方便：

1. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)
2. 输入数据库用户名和密码([不知道密码？](/zh/stack-accounts.md#mysql))
3. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 需要了解更多 phpMyAdmin 的使用，请参考本文档 [phpMyAdmin 章节](/zh/solution-phpmyadmin.md)


## 常用操作


### 修改密码

修改密码，即使用已有密码登录MySQL，然后修改成另外一个密码  
重置密码，即忘记了密码，需要通过重置密码找回

#### 修改密码

可以通过MySQL管理工具修改密码，也通过命令上修改密码

### phpMyAdmin修改密码

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/websoft9-modifymysqlpw.gif)

#### 命令行修改密码

执行一下命令:
```
mysqladmin -u 用户名 -p 旧密码 password '新密码' 
```

### 重置密码

如果忘记了root密码，就需要通过命令操作，实现MySQL密码重置。下面有两种方案可供使用：

#### 快捷方案（推荐）

1. 使用SSH远程连接到MySQL服务器
2. 运行如下命令，按提示输入新密码即可。
   ```
   wget -N https://ghproxy.com/https://raw.githubusercontent.com/websoft9dev/role_mysql/master/tools/reset_password.sh; bash reset_password.sh

### 设置 MySQL 远程访问

当你想通过本地的电脑的MySQL客户端（例如：Navicat）连接服务器上的MySQL的时候，就需要设置 MySQL 的远程访问。

数据库是高安全应用，设置远程访问，最少两个独立的步骤：

#### 安全组放通3306端口

一般来说，MySQL使用的是3306端口。

首先，我们要登录到云控制台，打开云服务器所在的安全组中，保证3306端口是开启的。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql3306-websoft9.png)


#### 开启MySQL远程连接

安全组开启后，还没有完成MySQL远程方案的设置。  

接下来，还需要对 MySQL 自身进行设置，以便其接受外部网络的访问

我们提供两种开启MySQL的远程连接的方案，第一种是可视化方式，第二种是命令方式：  

##### 可视化开启（推荐）

在phpMyAdmin中开启远程只需要将root账号的访问方式改成“任意方式访问”，具体如下：

1. 打开账户->找到主机名为127.0.0.1的root用户，点击“修改权限”
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql-openremote001-websoft9.png)
2. 在“登录信息”选项卡中，将“主机名”下拉菜单选项更改为“任意主机”，点击执行
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/mysql-openremote002-websoft9.png)
3. 以上两步就完成了开启远程连接的工作

##### 命令开启

如果您的镜像中没有安装phpMyAdmin，那么就需要通过命令方式开启远程连接。具体如下：

1. 使用SSH连接到服务器，登录到MySQL
   ```
   mysql -u root -p 数据库root密码
   ```
 
2. 写入SQL语句,开启远程访问
   ```
   mysql>  use mysql;
   mysql>  update user set host = '%' where user = 'root';
   ```

3. 运行下面的语句，查看设置是否生效（显示%的值）
   ```
   select host,user from user where user='root'
   ```
4. 退出MySQL命令，回到Linux命名模式，重启MySQL
   ```
   systemctl restart mysqld
   ```
   > 本步骤是必须的，否则在用Navicat Premium/MySQL-Front等工具测试远程的时候会报错误信息

### 更换MySQL数据目录

MySQL 的数据目录默认设置为 */data/mysql*。 想修改 MySQL 数据目录，按以下步骤操作：

1. 停止 MySQL 服务
   ```shell
   sudo sytemctl stop mysqld
   ```
2. 将 */data/mysql* 移动到目标新目录，例如 */data/mysql2*
3. 修改配置文件`/etc/my.cnf`文件的 datadir 配置：
   ```shell
   datadir=/data/mysql2
   ```
4. 重启服务
   ```shell
   sudo sytemctl start mysqld
   ```


### 设置 Binary Log

二进制日志包含描述数据库更改的“操作”，例如创建表操作或更改表数据。 它还包含可能已进行更改的语句的操作（例如，不匹配任何行的 DELETE）。 二进制日志还包含有关每条语句使用更新数据的时间信息。

#### 二进制日志配置

修改 MySQL 配置  /etc/my.cnf 以更改二进制日志的设置

```
log_bin = mysql-bin      # enable Binary log
binlog_format = mixed    # Binary log format
expire_logs_days = 7     # Binary log expire time
```

#### 二进制日志文件大小

有时候，数据库发生了很多事件，二进制日志文件大小增长非常快，你的磁盘空间可能不够用，如果磁盘上没有空间，MySQL 服务就无法启动。

如果您的二进制日志文件太大，建议将 expire_logs_day 更改为更小，定时清理日志文件。

### 权限设置

###  图形化工具：phpMyAdmin

phpMyAdmin是很受欢迎的MySQL数据库管理工具，下面介绍常见的phpMyAdmin操作

#### 修改root密码

1. 登录phpMyAdmin后，默认页面-常规设置，点击“修改密码” ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-modifypw-websoft9.png)
2. 修改密码-&gt;保存-&gt;退出登录，刷新浏览器后便可以使用新密码登录了

#### 新增数据库

1. 登录phpMyAdmin后，点击左侧菜单栏的“新建”，进入如下的数据库创建界面 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)
2. 填写数据库名-&gt;点击创建按钮，一个新的数据库变建立成功
3. 默认情况下，root拥有新建的数据库的全部权限

#### 新增数据库用户

> 数据库用户与数据库是分离的，是“多对多”的关系。可以通过关联使得某个用户具有某个数据库的权限

1. 登录phpMyAdmin后，点击左侧菜单栏中新打算对其新增用户的数据库（例如：mywebsoft9）
2. 点击顶部菜单栏的“权限”，找到“新增用户账户”，如下新增用户界面 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adduser-websoft9.png)
3. 根据上图填写用户名、主机地址和密码，然后关联对应的数据库和勾选权限设置
4. 点击“执行”，就完成新增用户和数据库关联了

说明：也可以登录phpMyAdmin的默认页面后，点击顶部菜单上“账户”，对用户和权限进行管理

#### 数据库导入和导出

> 导出即备份数据库，导入即恢复数据库。这个两个操作对 phpMyAdmin 来说比较简单，具体如下：

1. 登录phpMyAdmin后，选择您需要操作的数据库后，点击顶部菜单栏的“导出” 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-export-websoft9.png)

2. 选择导出方式（默认为“快速”）和格式（默认为“SQL”），点击“执行”按钮

3. 数据库备份文件（.sql后缀）生成后，保存到本地完成导出工具

4. 恢复数据库，对应的是“导入”操作，具体参考下图 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-import-websoft9.png)

5. 导入文件特别要注意字符集兼容性

#### 常见问题

##### phpMyAdmin on Docker如何修改导入文件大小限制？

1. 使用 SFTP 连接服务器，编辑 */data/apps/phpmyadmin/docker-compose.yml* 文件，在环境变量处增加一个字段 `- UPLOAD_LIMIT=20M`
  ```
  version: "3.7"
  services: 
    phpmyadmin:
        image: phpmyadmin/phpmyadmin
        container_name: "phpmyadmin"
        environment:
         - PMA_HOST=172.17.0.1
         - PMA_PORT=3306
         - UPLOAD_LIMIT=20M
  ```

2. 重新创建 phpMyAdmin 容器后生效
  ```
  cd /data/apps/phpmyadmin && docker-compose up -d
  ```

##### phpMyAdmin 限制特定 IP 访问

把 phpMyAdmin.conf（```/etc/httpd/conf.d/phpmyAdmin.conf```）文件中的：  
     ```Require all granted``` 
改为：  
     ```Require ip xxx.xxx.xxx.xxx```  
这样，只有指定 IP 的主机能访问 phpMyAdmin，IP还可以缩写：192.168.*.* 这样则表示以 192.168 开头的 IP 段都能访问。 修改完成后需要重启 Apache

### 图形化工具：jspMyAdmin

下面介绍常见的JspMyAdmin操作

#### JspMyAdmin 修改密码
1. 在浏览器上输入*http://服务器公网IP/jspmyadmin*，，进入jspMyAdmin管理界面

2. 登录 jspMyAdmin（[不知道账号密码？](/zh/stack-accounts.md)）

3. 点击上方菜单栏“ Users & Privileges ,在下方显示的页面单击“alter user”
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/jspmyadmin-updatepw2-websoft9.png)

4. 输入新的密码，最后点击“run”即可
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/jspmyadmin-updatepw1-websoft9.png)

   >注意，在修改密码的过程中，必须将服务器上所有密码一并重置修改，操作三次密码修改才能保证密码重置成功

#### JspMyAdmin 开启MySQL远程

1. 登录到 jspMyAdmin

2. 点击上方菜单栏“ Users & Privileges” ,在下方显示的页面单击“alter user”，将Host Name文本框中“localhost”更改为“%”
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/jspmyadmin-updatehost-websoft9.png)
    
   >注意，在远程连接的过程中，只需更改原主机名为“localhost”的服务器为“%”即可

#### JspMyAdmin 导出数据

1. 登录到 jspMyAdmin

2. 点击上方菜单栏“ Export”，此时 JspMyAdmin 会自动添加你刚创建的所有数据库，单击“run”导出完成
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/jspadmin-exportmath-websoft9.png)
   
   >说明：如果没有可以导出的数据库，可以在左侧的数据库名上右健`新建--数据库`，进行创建

### 图形化工具：Navicat

如果你已经开启服务器安全组3306端口，并设置完成 MySQL 远程连接，可以参考如下的步骤使用 Navicat：

1. 打开Navicat Premium，点击顶部菜单栏， 【文件】>【新建连接】>【MySQL】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/websoft9-mysql-navcaittest.png)

2. 自定义连接名，将localhost更改为数据库所在的主机公网IP地址

3. 输入账号和密码（[不知道账号密码？](/zh/stack-accounts.md)）

3. 点击“测试连接”，系统提示：连接成功 ! 即表示成功连接
    
### 图形化工具：Workbench

Workbench 是 MySQL 官方提供的图形化客户端工具

### 图形化工具：MySQL-Front

MySQL-Front是一款小巧的管理Mysql的应用程序。下面介绍常见的MySQL-Front操作。

#### 远程连接MySQL

1. 打开MySQL-Front，点击顶部菜单栏， 【文件】>【连接管理】
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/websoft9-mysql-fronttest.png)

2. 自定义连接名，主机为数据库所在的主机ip地址（[不知道账号密码？](/zh/stack-accounts.md)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/websoft9-mysql-frontcome.png)

3. 点击“确定”后，在连接管理窗口上点击“打开”，系统无任何提示及警告即表示连接成功

#### 新增数据库

1. 登录数据库

2. 在连接管理窗口上点击“打开”，一个新的数据库变建立成功

3. 登录成功进入到数据库操作界面，该界面为图形化操作，方便、简洁
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/websoft9-mysql-frontteacher3.png)

> 注意：可以在本地导入数据库，此次操作导入数据库名为mysql。

#### 数据库导入和导出

导入即恢复数据库，导出即备份数据库。这个两个操作对SQL-Front来说比较简单，具体如下：

1. 登录数据库

2. 右击你选择的数据库名，完成：【导入】>【SQL文件】，选择本地已有的*.sql数据库备份文件
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/websoft-mysql-frontcome2.png)

3. 点击上方导航栏的大的绿色按钮即可执行

  >注意：根据实际情况选择默认的字符集，一般选择UTF-8

4. 选择备份的数据库，右击你选择的数据库名，依次完成：【导出】>【SQL文件】，完成数据库备份

#### 运行SQL语句
 
点击工具栏中：【视图】>【SQL编辑器】，手动编写SQL语句并执行

## 异常处理

#### 浏览器无法访问 phpMyAdmin（白屏没有结果）？

您的服务器对应的安全组9090端口没有开启（入规则），导致浏览器无法它

#### phpMyAdmin 是如何安装的？

采用 Docker 安装，保证 MySQL 环境具有良好的隔离性。