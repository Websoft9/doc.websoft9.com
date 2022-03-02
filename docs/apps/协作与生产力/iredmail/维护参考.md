---
sidebar_position: 2
slug: /iredmail/admin
tags:
  - iRedMail
  - 企业邮箱
---


# 维护参考

## 系统参数

镜像采用的是iRedMail开源电子邮件解决方案，这个方案中有多个与电子邮件相关的开源组件，主要包括：

### 路径

邮箱配置完成之后，请使用SFTP到服务器，下载 `/root/iRedMail/iRedMail.tips`文件，它包含了：
- 各个 web 程序的访问地址（URL），用户名和密码。
- 各个组件的配置文件路径
- 以及其它一些重要和敏感信息

下面摘录一部分重要的配置信息：

* SSL cert keys:
    - /etc/pki/tls/certs/iRedMail.crt
    - /etc/pki/tls/private/iRedMail.key

* Mail Storage:
    - Mailboxes: /var/vmail/vmail1
    - Mailbox indexes: 
    - Global sieve filters: /var/vmail/sieve
    - Backup scripts and backup copies: /var/vmail/backup

* Nginx:
    * Configuration files:
        - /etc/nginx/nginx.conf
        - /etc/nginx/sites-available/00-default.conf
        - /etc/nginx/sites-available/00-default-ssl.conf
    * Directories:
        - /etc/nginx
        - /var/www/html
    * See also:
        - /var/www/html/index.html

* MySQL:
    * Config file: /etc/my.cnf
    * RC script: /etc/init.d/mariadb

* Backup MySQL database:
    * Script: /var/vmail/backup/backup_mysql.sh

* Postfix:
    * Configuration files:
        - /etc/postfix
        - /etc/postfix/aliases
        - /etc/postfix/main.cf
        - /etc/postfix/master.cf

    * SQL/LDAP lookup config files:
        - /etc/postfix/mysql

* Dovecot:
    * Configuration files:
        - /etc/dovecot/dovecot.conf
        - /etc/dovecot/dovecot-ldap.conf (For OpenLDAP backend)
        - /etc/dovecot/dovecot-mysql.conf (For MySQL backend)
        - /etc/dovecot/dovecot-pgsql.conf (For PostgreSQL backend)
        - /etc/dovecot/dovecot-used-quota.conf (For real-time quota usage)
        - /etc/dovecot/dovecot-share-folder.conf (For IMAP sharing folder)
    * Syslog config file:
        - /etc/rsyslog.d/1-iredmail-dovecot.conf (present if rsyslog >= 8.x)
    * RC script: /etc/init.d/dovecot
    * Log files:
        - /var/log/dovecot/dovecot.log
        - /var/log/dovecot/sieve.log
        - /var/log/dovecot/lmtp.log
        - /var/log/dovecot/lda.log (present if rsyslog >= 8.x)
        - /var/log/dovecot/imap.log (present if rsyslog >= 8.x)
        - /var/log/dovecot/pop3.log (present if rsyslog >= 8.x)
        - /var/log/dovecot/sieve.log (present if rsyslog >= 8.x)
    * See also:
        - /var/vmail/sieve/dovecot.sieve
        - Logrotate config file: /etc/logrotate.d/dovecot

* ClamAV:
    * Configuration files:
        - /etc/clamd.d/amavisd.conf
        - /etc/freshclam.conf
        - /etc/logrotate.d/clamav
    * RC scripts:
            + /etc/init.d/clamd@amavisd
            + /etc/init.d/freshclamd

* Amavisd-new:
    * Configuration files:
        - /etc/amavisd/amavisd.conf
        - /etc/postfix/master.cf
        - /etc/postfix/main.cf
    * RC script:
        - /etc/init.d/amavisd

* iRedAPD - Postfix Policy Server:
    * Version: 2.2
    * Listen address: 127.0.0.1, port: 7777
    * Configuration file:
        - /opt/iredapd/settings.py
    * Related files:
        - /opt/iRedAPD-2.2
        - /opt/iredapd (symbol link to /opt/iRedAPD-2.2

* iRedAdmin - official web-based admin panel:
    * Version: 0.9.1
    * Root directory: /var/www/iRedAdmin-0.9.1
    * Config file: /var/www/iRedAdmin-0.9.1/settings.py
    * Web access:
        - URL: https://mail.websoft9.cn/iredadmin/
        - Username: postmaster@websoft9.cn
        - Password: ***

* Roundcube webmail: /var/www/roundcubemail-1.3.6
    * Config file: /var/www/roundcubemail-1.3.6/config
    * Web access:
        - URL: http://mail.websoft9.cn/mail/ (will be redirected to https:// site)
        - URL: https://mail.websoft9.cn/mail/ (secure connection)
        - Username: postmaster@websoft9.cn
        - Password: ***
    * Cron job:
        - Command: "crontab -l -u root"

* SOGo Groupware:
    * Web access: httpS://mail.websoft9.cn/SOGo/
    * Main config file: /etc/sogo/sogo.conf
    * Nginx template file: /etc/nginx/templates/sogo.tmpl
    * See also:
        - cron job of system user: sogo

* netdata (monitor):
    - Config files:
        - All config files: /opt/netdata/etc/netdata
        - Main config file: /opt/netdata/etc/netdata/netdata.conf
        - Modified modular config files:
            - /opt/netdata/etc/netdata/python.d/mysql.conf
            - /opt/netdata/etc/netdata/python.d/postgres.conf
    - HTTP auth file (if you need a new account to access netdata, please
      update this file with command like 'htpasswd' or edit manually):
        - /etc/nginx/netdata.users
    - Log directory: /opt/netdata/var/log/netdata

### 端口号

本邮件服务器需要用到的端口包括：

|服务名|端口|
|---|---|
|Postfix|25,587|
|Dovecot|993,995,110,143|
|Nginx|80,443|

> 以上端口需要设置好安全组，并且向云产商申请解封25端口

### 版本号

|软件名称|软件版本|软件简介|
|---|---|---|
|Postfix|2.10.1|Postfix 是一种电子邮件服务器|
|Dovecot|2.2.32|Dovecot 是一个开源的 IMAP 和 POP3|
|Nginx |1.12.2|Nginx是一个高性能的HTTP和反向代理服务，也是一个IMAP/POP3/SMTP服务|
|MariaDB|15.1|MariaDB数据库管理系统|
|mlmmj |1.1|MLMMJ是一个简单而简明的邮件列表管理器|
|Amavisd-new|2.11.1|Amamisd-new是开源中最流行的反垃圾和反病毒软件|
|SpamAssassin|3.4.0|SpamAssassin是一种安装在邮件服务器上的邮件过滤器，用来辨识垃圾信|
|ClamAV |0.100.2/25113|ClamAV是一种用于检测木马、病毒、恶意软件和其他恶意威胁的开源反病毒引擎。|
|Roundcube |1.3.6|RoundCube Webmail是一个基于浏览器，支持多国语言的IMAP客户端|
|SOGo Groupware |4.0.4|群件服务器|
|Fail2ban |0.9.7|lLinux系统防暴力破解工具|
|iRedAPD|2.2|iRedAPD是一个简单的Postfix策略服务器|
|netdata|1.10.0|Linux系统性能实时监控平台|
|iRedAdmin|0.9.1|iRedAdmin是一个邮件用户管理面版|


### 服务

## 备份

### 全局自动备份

所有的云平台都提供了全局自动备份功能，基本原理是基于**磁盘快照**：快照是针对于服务器的磁盘来说的，它可以记录磁盘在指定时间点的数据，将其全部备份起来，并可以实现一键恢复。

```
- 备份范围: 将操作系统、运行环境、数据库和应用程序
- 备份效果: 非常好
- 备份频率: 按小时、天、周备份均可
- 恢复方式: 云平台一键恢复
- 技能要求：非常容易
- 自动化：设置策略后全自动备份
```

不同云平台的自动备份方案有一定的差异，详情参考 [云平台备份方案](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

### 程序手工备份

程序手工本地备份是通过**下载应用程序源码和导出数据库文件**实现最小化的备份方案。

下面以列表的方式介绍这种备份：
```
- 备份范围: 数据库和应用程序
- 备份效果: 一般
- 备份频率: 一周最低1次，备份保留30天
- 恢复方式: 重新导入
- 技能要求：非常容易
- 自动化：无
```


## 恢复

## 升级

### 系统级更新

运行一条更新命令，即可完成系统级更新：

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的 Cron


## 故障处理

此处收集使用 iRedMail 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)
