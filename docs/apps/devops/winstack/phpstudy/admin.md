---
sidebar_position: 2
slug: /phpstudy/admin
tags:
  - phpStudy
  - DevOps
---


# 维护指南

## 场景

### 将数据转移到数据盘

默认情况下 C:\websoft9\phpStudy\PHPTutorial\WWW 是在系统盘的，当需要转移到数据盘，步骤如下：

##### 转移网站数据

1. 停止 Apache 服务
2. 将 C:\websoft9\phpStudy\PHPTutorial\WWW 下所有文件拷贝新的目录，假如为：D:\wwwroot
3. 修改 C:\websoft9\phpStudy\PHPTutorial\Apache\conf\extra\httpd-vhosts.conf 文件，将“C:\websoft9\phpStudy\PHPTutorial\WWW”修改为“D:\wwwroot”
4. 重启Apache后生效

##### 转移数据库文件

1. 停止MySQL服务

2. 将 C:\websoft9\phpStudy\PHPTutorial\MySQL\data 下所有文件拷贝到新目录，例如：D:\data

3. 修改 C:\websoft9\phpStudy\PHPTutorial\MySQL\my.ini 文件，将以下语句

   ~~~
   datadir="C:\websoft9\phpStudy\PHPTutorial\MySQL\data"
   log-error="C:\websoft9\phpStudy\PHPTutorial\MySQL\data\mysqld.log"
   ~~~
   修改为：
   ~~~
   datadir="D:\data"
   log-error="D:\data\mysqld.log"
   ~~~

4. 重启MySQL服务




### SSL/HTTPS

在设置https访问之前，请开启安全组的443端口，如果不开启，https访问是不可用的。

如果您已经申请了证书（请保证证书可用），请参考如下的配置方式：

1.  将证书上传到服务器证书目录：C:\wwwrootcert（没有cert目录可以自己新建）
2.  打开配置文件：C:\websoft9\phpStudy\PHPTutorial\Apache\conf\extra\httpd-vhosts.conf
3.  拷贝下面的*https配置文件模板* 到配置文件中，并保存

    ```
    <VirtualHost *:443>
       ServerName www.mydomain.com
       # ServerAlias other.mydomain.com
       DocumentRoot "C:\websoft9\phpStudy\PHPTutorial\WWW"
       ErrorLog " logs\mydomain.com_error_apache.log"
       CustomLog "logs\mydomain.com_error_apache.log" common
       <Directory "C:\websoft9\phpStudy\PHPTutorial\WWW">
       Options Indexes FollowSymlinks
       AllowOverride All
       Require all granted
       </Directory>
        SSLEngine on
        SSLCertificateFile  C:\wwwroot\cert\server.crt
        SSLCertificateKeyFile  C:\wwwroot\cert\server.key
        SSLCertificateChainFile  C:\wwwroot\cert\server-ca.crt
     </VirtualHost>
    ```

4.  修改配置文件中相关项，并保存。
   
 > 注意：证书的后缀一般是：.crt或者 .pem，私钥的后缀是：.key

5. 保存 httpd-vhosts.conf，然后重启Apache服务。



## 故障速查

除以下列出的 phpStudy 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

## 问题解答