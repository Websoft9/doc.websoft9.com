---
sidebar_position: 3
slug: /lnmp/study
tags:
  - LNMP
  - PHP
  - Nginx
  - 运行环境
---


# 原理学习

LNMP（Linux-Nginx-MySQL-PHP）是流行的Web运行环境组合，基于免费、开源软件构建。包括：Linux系统，Nginx Web服务器软件，MySQL数据库，PHP语言等四种核心组件以及其他相关辅助组件。Websoft9通过组合、优化和兼容性处理，将所有组件打包成一个高性能、易维护的PHP运行环境解决方案包，保证能够兼容运行绝大部分PHP应用程序。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)

## 高级：PHP&Java 双能环境

LNMP+Java 这样的组合环境，常常被称之为 **PHP&JAVA双能环境**。如果你使用的是我们在云平台上 **PHP&Java 双能运行环境**，那么意味着你的环境已经支持 Java&Tomcat

对于使用 LNMP 环境的用户可能会考虑，能否在 LNMP 的基础上运行 Java 程序呢？经过实践的研究，我们发现只要在 LNMP 基础上再安装 Tomcat 和 JDK （[如何安装](/zh/solution-java.md#补充说明：安装-java-tomcat)），便可以让 LNMP 同时支持 PHP 和 Java 应用程序。

### 路径参数

对于 **PHP&Java 双能运行环境**来说，主要路径信息如下：

#### php

[参考](/zh/stack-components.html#php)

#### Nginx

[参考](/zh/stack-components.html#nginx)

#### MySQL

[参考](/zh/stack-components.html#mysql)

#### Java
Java Edition：*OpenJDK*  
JVM Directory：	*/usr/lib/jvm*

#### Tomcat
Tomcat 安装目录： */usr/local/tomcat*    
Tomcat 配置文件： */usr/local/tomcat/conf/server.xml*     
Tomcat 建议网站目录： */data/wwwroot/*    
Tomcat 日志目录： */var/log/tomcat*  

### 部署 PHP 应用程序

全局上看，部署 PHP 程序，只需两个步骤：**上传网站代码** + [**虚拟机主机配置文件**](/zh/stack-components.md#nginx) **中增加 server{} 配置段**

> server{} 又称之为虚拟主机配置段，每个网站必定在 default.conf 中对应唯一的 server{}。

#### 准备

安装网站之前，请了解如下几个要点，做好准备工作

*  虚拟机主机配置文件：*/etc/nginx/conf.d/default.conf* 
*  连接工具：使用 WinSCP 连接服务器，它包含文件管理、运行命令两方面功能
*  域名：若需要使用域名，请确保备案后的域名成功解析到服务器IP
*  数据库：网站安装向导过程中可能需要使用数据库，请使用 [phpMyAdmin 管理数据库](/zh/admin-mysql.md)

有一个全局认知并完成准备工作之后，我们开始部署网站

#### 安装第一个PHP网站

下面通过**替换示例网站**（LNMP 默认存在一个示例网站）的方式来教你安装你的第一个网站：

1. 使用 WinSCP 连接服务器
2. 删除示例网站 */data/wwwroot/default* 下的所有文件（保留目录）
3. 将本地电脑上的网站源码上传到示例目录下
4. 修改 *default.conf* 中已有 server{} 配置段（[修改参考](/zh/solution-deployment.md#server)），实现绑定域名、修改网站目录名称等操作。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/lnmp-editvhostconf-websoft9.png)
   ::: warning
   如果不绑定域名、不修改网站目录名称，请跳过步骤4和5
   :::
5. 保存 default.conf，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
      ~~~
      # 重启 Nginx 服务命令
      sudo systemctl restart nginx
      ~~~
6. 本地浏览器访问：*http://域名* 或 *http://服务器公网IP* 即可访问您的网站

#### 安装第二个PHP网站

从安装第二个网站开始，需要在 *default.conf* 中增加对应的虚拟主机配置段，具体如下

1. 使用 WinSCP 连接服务器，在 /data/wwwroot 下新建一个网站目录，假设命令为“mysite2”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-createmysite2-websoft9.png)
2. 将本地网站源文件上传到：*/data/wwwroot/mysite2* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-uploadcodes-websoft9.png)
3. 编辑 *default.conf* 文件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-editvhostconf-websoft9.png)

4. 将下面 server{} 模板拷贝到 *default.conf* 中，并修改其中的 server_name, root, error_log, access_log等（[修改参考](/zh/solution-deployment.md#server)）
    ```
    # server segment template
    server
    {
        listen 80;
        server_name mysite2.yourdomain.com;
        index index.html index.htm index.jsp index.do index.php;
        root  /data/wwwroot/mysite2;
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
    
        include php.conf;
        #include jsp.conf;
    }
    ```

4. 保存 *default.conf*，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
      ~~~
      # 重启Nginx服务命令
      sudo systemctl restart nginx
      ~~~
5. 本地浏览器访问：http://mysite2.yourdomain.com/  访问你的网站。


#### 安装第N个PHP网站

安装第n个网站与安装第二个网站的操作步骤一模一样

最后我们温故而知新，总结 PHP&Java 双能环境 安装 PHP 网站步骤：

1. 上传网站代码
2. 绑定域名（非必要）
3. 新增站点配置或修改示例站点配置
4. 增加网站对应的数据库（非必要）
5. 进入安装向导

### 部署 Java 应用程序

部署 Java 程序，从全局的角度看，主要包括：**上传网站代码 + 修改 Tomcat配置文件 和 Nginx 配置文件** 两个主要操作。对 Java 项目来说，Tomcat 是应用服务器的作用，是运行Java程序的入口，而 Nginx 是 Web服务器的作用，负责处理 HTTP 请求，并将Java运行的请求转发给 Tomcat。

#### 安装第一个Java应用

系统中默认有示例网站，可以通过替换示例网站代码的方式安装第一个网站。

> 如果不考虑修改示例网站，请阅读[安装第二个Java网站](/zh/solution-java.md#安装第二个java应用)。

1. 使用 WinSCP 连接服务器
2. 删除示例目录下的所有文件，只保留目录（*/data/wwwroot/default*）
3. 上传代码到默认的示例目录，并修正所属用户和组权限，保证上传的代码具有访问权限
   ```
   chown www: -R /data/wwwroot
   ```
4. 编辑 Tomcat 配置文件 *server.xml* 文件，修改默认 `<host>...</host>` 配置段中 name 等（[参数说明](/zh/solution-java.md#host-参数含义)）
   ```
   <Host name="mysite2.yourdomain.com" appBase="/data/wwwroot/default" unpackWARs="true" autoDeploy="true">
  		<Context path="" docBase="/data/wwwroot/default" reloadable="false" crossContext="true"/>
  		<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
    	prefix="localhost_access_log" suffix=".txt" pattern="%h %l %u %t &quot;%r&quot; %s %b" />
  		<Valve className="org.apache.catalina.valves.RemoteIpValve" remoteIpHeader="X-Forwarded-For"
    	protocolHeader="X-Forwarded-Proto" protocolHeaderHttpsValue="https"/>
	 </Host>
   ```
5. 编辑 Nginx 配置文件 *default.conf* 文件，启用 `include jsp.conf`，注释掉 `#include php.conf`，然后修改 server_name, root 等参数（[参数含义](/zh/solution-deployment.md#server)）
   ```
   server
    {
        listen 80;
        server_name mysite2.yourdomain.com; # 修自己的域名
        index index.html index.htm index.jsp index.do index.php;
        root  /data/wwwroot/mysite2; # 修改为自己的路径
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
        
        #include php.conf; # 注释掉
        include jsp.conf; # 启用
    }
    ```
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/java/lnmp-modifynginx001-websoft9.jpg)
6. 保存配置文件，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
    ~~~
    sudo systemctl restart tomcat
    sudo systemctl restart nginx
    ~~~
7. 通过：*http://域名* 或 *http://服务器公网IP* 访问网站


#### 安装第二个Java应用

我们现在介绍新增一个网站的详细步骤：

1. 使用 WinSCP 连接服务器，在 /data/wwwroot 下新建一个网站目录，假设命令为“mysite2”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-createmysite2-websoft9.png)
2. 将本地网站源文件上传到：*/data/wwwroot/mysite2* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-uploadcodes-websoft9.png)
3. 使用命令修正所属用户和组权限，保证上传的代码具有访问权限
   ```
   chown www: -R /data/wwwroot
   ```
4. 编辑 Tomcat 配置文件 *server.xml* 文件   
   新增 `<Host></Host>` 配置段，**插入**到 server.xml 中，并修改其中的 name, appBase, docBase, prefix等（[参数说明](/zh/solution-java.md#host-参数含义)）
    ```
    # host segment template
    <Host name="mysite2.yourdomain.com" appBase="/data/wwwroot" unpackWARs="true" autoDeploy="true">
    <Context path="" docBase="/data/wwwroot/mysite2" reloadable="false" crossContext="true"/>
    <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" prefix="mysite2.yourdomain.com_access_log" suffix=".txt" pattern="%h %l %u %t &quot;%r&quot; %s %b" />
    <Valve className="org.apache.catalina.valves.RemoteIpValve" remoteIpHeader="X-Forwarded-For" protocolHeader="X-Forwarded-Proto" protocolHeaderHttpsValue="https"/>
    </Host>
    ```
4. 编辑 Nginx 配置文件 *default.conf* 文件    
   将下面 **server{ } **配置段，插入到 default.conf 中，并修改其中的 server_name, root, error_log, access_log等（[参数含义](/zh/solution-deployment.md#server)）
 
    ```
       # server segment template
       server
       {
        listen 80;
        server_name mysite2.yourdomain.com;
        index index.html index.htm index.jsp index.do index.php;
        root  /data/wwwroot/mysite2;
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
        
        #include php.conf;
        include jsp.conf;
        }
    ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/java/lnmp-modifynginx001-websoft9.jpg)

4. 保存配置文件，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
    ~~~
    sudo systemctl restart tomcat
    sudo systemctl restart nginx
    ~~~
5. 本地浏览器访问：http://域名 访问你的网站。

#### 安装第N个Java应用

安装第 N 个网站与安装第二个网站的操作步骤一模一样

最后我们温故而知新，总结 PHP&Java 双能环境 安装 Java 网站步骤： 

1. 上传网站代码
2. 解析域名（非必要）
3. Tomcat 配置文件中增加 host 配置段
4. Nginx 配置文件中增加 server 配置段
5. 进入应用的安装向导

### Host 参数含义

针对 Tomcat 下的 server.xml 文件中的 host 配置段，需要修改的参数说明如下：  

|  host 项  |  作用说明  |  必要性 |
| --- | --- | --- |
|  name  |  域名   |  必须填写 |
|  appBase |  war 包解压路径，例如：在 */data/wwwroot* 下解压 mysite2.war，系统就会自动产生 */data/wwwroot/mysite2* 网站目录  | 务必准确无误 |
|  docBase |  网站存放目录，如果是war包，需带上后缀名，例如:`/data/wwwroot/mysite.war`  | 务必准确无误 |
|  path |  访问路径，一般请保持默认为空  | 建议保持默认 |

### 补充说明：安装 Java&Tomcat

在 LNMP 的基础上安装 Java 以及 Tomcat 的主要步骤如下：  

1. 参考 [Tomcat 官方文档](https://tomcat.apache.org/)，安装 Tomcat
2. 安装JDK
  ```
  #搜索JDK版本
  yum search jdk
  #以1.8.0为例，安装JDK
  yum install java-1.8.0-openjdk* -y
  ```
3. 设置环境变量

##  高级：Apache&Nginx动静分离

## # 路径

## # 应用程序
应用程序目录: /data/wwwroot/default  
default是应用程序的默认目录，其中的index.html是引导文件，可以删除

####  运行环境（PHP 7.0,Apache 2.4.8） 

- PHP配置文件目录: /usr/local/php/etc  
- PHP 扩展配置文件目录: /usr/local/php/etc/php.d  
- Apache目录：/usr/local/apache  
- Apache虚拟主机目录: /usr/local/apache/conf/vhost  
- 日志文件目录：/usr/local/apache/logs  

### # 数据库（MySQL5.6.3）
- Database目录: /usr/local/mysql or /usr/local/mariadb
- Database 数据目录: /data/mysql or /data/mariadb
- Database 配置文件: /etc/my.cnf
- 数据库面板访问路径：*http://公网ip/phpmyadmin*

### # 运维面板（9panel）

9Panel是Websoft9根据镜像用户的习惯和技术能力而研制的轻量级面板，以帮助用户快速掌握程序安装和运维工作  
访问路径：http://ip/9panel


###  主要特点

* 基于系统源码编译安装，细节安全优化，纯命令行，占用系统资源低
* Jemalloc优化MySQL内存管理
* 交互添加Apache虚拟主机，方便快捷，支持Let’s Encrypt一键设置
* 菜单式FTP账号管理脚本，轻松建立ftp虚拟用户
* 提供在线MySQL、PHP、Redis、Memcached、phpMyAdmin升级脚本
* 提供本地备份和远程备份（服务器之间rsync）、内网阿里云OSS备份功能

###  使用手册

请下载后阅读：http://libs.websoft9.com/Websoft9/documents/zh/lanmp/lanmp.zip