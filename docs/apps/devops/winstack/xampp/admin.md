---
sidebar_position: 2
slug: /xampp/admin
tags:
  - XAMPP
  - DevOps
---


# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### SSL/HTTPS

如果您已经申请了证书（请保证证书可用），请参考如下的配置方式：

1.  将证书上传到服务器证书目录：conf/ssl.*（*为目录后缀名）
2.  打开C:\xampp\apache\conf\extra\httpd-ssl.conf配置文件
3.  找到httpd-ssl.conf中的https配置内容模板（下面是去掉注释后的效果）

    ```
    <VirtualHost _default_:443>
    DocumentRoot "C:/xampp/htdocs"
    ServerName www.example.com:443
    ServerAdmin admin@example.com
    ErrorLog "C:/xampp/apache/logs/error.log"
    TransferLog "C:/xampp/apache/logs/access.log"

    SSLEngine on
    SSLCertificateFile "conf/ssl.crt/server.crt"
    SSLCertificateFile "conf/ssl.crt/server.crt"
    SSLCertificateFile "conf/ssl.crt/server.crt"

    #<Location />
    #SSLRequire (    %{SSL_CIPHER} !~ m/^(EXP|NULL)/ \
    #            and %{SSL_CLIENT_S_DN_O} eq "Snake Oil, Ltd." \
    #            and %{SSL_CLIENT_S_DN_OU} in {"Staff", "CA", "Dev"} \
    #            and %{TIME_WDAY} >= 1 and %{TIME_WDAY} <= 5 \
    #            and %{TIME_HOUR} >= 8 and %{TIME_HOUR} <= 20       ) \
    #           or %{REMOTE_ADDR} =~ m/^192\.76\.162\.[0-9]+$/
    #</Location>

    <FilesMatch "\.(cgi|shtml|phtml|php)$">
        SSLOptions +StdEnvVars
    </FilesMatch>
    <Directory "C:/xampp/apache/cgi-bin">
        SSLOptions +StdEnvVars
    </Directory>

    BrowserMatch "MSIE [2-5]" \
             nokeepalive ssl-unclean-shutdown \
             downgrade-1.0 force-response-1.0

    CustomLog "C:/xampp/apache/logs/ssl_request.log" \
              "%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x \"%r\" %b"

    </VirtualHost>     
    ```

4.  修改配置文件中相关项，并保存 ServerName  #主域名，务必修改 DocumentRoot #网站路径，务必填写网站实际路径，例如:C:/xampp/htdocs/wordpress SSLCertificateFile #证书File，务必填写网站实际路径 SSLCertificateKeyFile #证书KeyFile，务必填写网站实际路径 SSLCertificateChainFile #证书ChainFile，务必填写网站实际路径 注意：证书的后缀一般是：.crt或者 .pem，私钥的后缀是：.key
5.  重启Apache服务 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/xampp/xampp-ss-websoft9.png)



### 将数据转移到数据盘

1. 转移网站数据
默认情况下 C:\xampp\htdocs 是在系统盘的，当需要转移到数据盘，步骤如下：
	1. 停止 Apache 服务
	2. 将 C:\xampp\htdocs 下所有文件拷贝新的目录，假如为：D:\wwwroot
	3. 修改 C:\xampp\apache\conf\extra\httpd-vhosts.conf 文件，	将“C:\xampp\htdocs”修改为“D:\wwwroot”
	4. 重启Apache后生效

2. 转移数据库文件
	1. 停止MySQL服务
	2. 将 C:\xampp\mysql\data 下所有文件拷贝到新目录，例如：D:\data
	3. 修改 C:\xampp\mysql\my.ini 文件，将以下语句
		~~~
        datadir="C:\xampp\mysql\data"
        log-error="C:\xampp\mysql\data\mysqld.log"
        ~~~
        修改为：
        ~~~
        datadir="D:/data"
        log-error="D:/data/mysqld.log"
        ~~~
     4. 重启MySQL服务


## 故障处理

除以下列出的 XAMPP 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

## 常见问题