---
sidebar_position: 1
slug: /iredmail
tags:
  - iRedMail
  - 企业邮箱
---

# 快速入门

[iRedMail](https://www.iredmail.org/) 是一个基于Linux/BSD 系统的开源的、功能完备、成熟的邮件服务器解决方案。只需几分钟，iRedMail 即可为您部署一台完全基于开源软件、功能完善的邮件服务器。

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/roudcube-admin-websoft9.png)


部署 Websoft9 提供的 iRedMail 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80 25,993,995,587,110,143,80,443** 端口已经开启
3. 向云务器厂商申请解已经安装镜像的服务器的 25 端口
4. 下载一个用于运行命令的终端程序 MobaXterm （iredmail不支持在putty下运行，因此需要使用MobaXterm）
5. 下载 `/root/iRedMail/iRedMail.tips`文件，查看所有相关的账号：邮箱管理员、MySQL等
6. 若想用域名访问  iRedMail **[域名五步设置](./dns#domain)** 过程


## iRedMail 初始化向导{#init}

### 详细步骤

1. 登录到云服务器，运行安装命令
   ```
   cd /root/iRedMail/
   ./iRedMail.sh
   ```

2. 安装过程重要步骤说明

   - 欢迎和感谢使用

     ![img](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/welcome-websoft9.png)

   - 指定用于存储用户邮箱的路径。默认是 `/var/vmail/`

     ![img](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/mail_storage-websoft9.png)

   - 选择Web 服务器 (请保持默认选择:nginx)

     ![1542015525589](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/nginx-websoft9.png)

   - 选择MariaDB数据库(先用鼠标上下箭头选择，然后空格键选定，回车键下一步)

     ![1542015568871](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/mariadb-websoft9.png)

   - 设置数据库root密码

     ![1542015591052](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/set-mysql-pass-websoft9.png)

   - 添加第一个邮件域名

     ![1542015688287](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/mail-domain-websoft9.png)

   - 设置邮件管理员密码（请牢记之）

     ![1542015745211](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/set-mail-passwd-websoft9.png)

   - 选择组件(建议全选)

     ![1542015797799](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/optioal-components-websoft9.png)

   - 以上选择完成之后，安装向导会进行 Yes/No的询问，请全部选择“Y”
   - 等待安装结束
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/iredmail-ss-websoft9.png)
   - 重启服务器（必须做）



**解析域名，并设置主机名**

1. 登录域名控制台，分别增加A、MX记录和TXT，其中TXT记录值为 *v=spf1 mx mx:mail.websoft9.cn -all*

![1542080447085](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/dns-websoft9.png)

2. 远程登录到服务器，通过命令，将主机名称改成 mail.websoft9.cn，然后运行“hostname”命令查看是否绑定成功。
   
  ```
     hostnamectl  set-hostname mail.websoft9.cn
     hostname
  ```

**安全设置**

1. 设置DKIM记录(防垃圾邮件)
DKIM是一种防范电子邮件欺诈的验证技术，通过消息加密认证的方式对邮件发送域名进行验证。下面的步骤为邮件系统的DKIM配置步骤：
   - 查看DKIM密钥
       -  执行命令 ` amavisd-new showkeys`
       -  查看 `/root/iredmail/iRedMail.tips` 文件
   
   > 如何 `amavisd-new ` 命令不存在,请尝试使用 `amavisd`,某些Linux发行版本或者软件更新导致命令存在差异

  ![1542016520413](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/get-dkim-websoft9.png)

   - 在域名控制台-域名解析中再加一个TXT记录，主机记录为`dkim._domainkey` ,记录值为上图 3600 TXT 之后的“()”中的值，但要记得去掉双引号

   ![1542077542483](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/dns-dkim-websoft9.png)

   - 测试DKIM解析：服务器上执行下面命令，若显示 pass 则说明解析成功

   ```
   amavisd-new testkeys
   ```
   ![1542077698815](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/amavisd-testkey-websoft9.png)

>经测试在配置了SPF/DKIM的情况下，QQ邮箱仍然会将您的企业邮件依然会误报为垃圾邮件,，QQ邮件设置中添加域名白名单

2. 设置常见邮箱域名白名单
    - 添加常用邮件域名白名单,服务器执行命令:
         `python /opt/iredapd/tools/spf_to_greylist_whitelists.py`
    - 添加国内常用邮箱域名白名单,服务器执行命令:
       `python /opt/iredapd/tools/spf_to_greylist_whitelists.py qq.com 163.com 126.com sina.com sina.cn aliyun.com`

**访问地址**

安装配置完成之后，系统会自动生成一个默认的账号：postmaster@mydomain.com，可以用于登录：
*  邮箱用户Web端（推荐）： https://mail.mydomain.com/mail/
*  邮箱用户Web端： https://mail.mydomain.con/SOGo/
*  邮件服务器监控： https://mail.mydomain.com/netdata/
*  邮箱管理员Web端 :https://mail.mydomain.com/iredadmin/

> 安装设置完成,系统会自己发送几封系统设置相关邮件到你设置的第一个邮箱里(postmaster@xxx.com)
 
[更多参考](https://docs.iredmail.org/index-zh_CN.html)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**postmaster@xxx.com 有什么用**

镜像包含了系统监控/邮件病毒扫描/垃圾邮件处理等组件, postmaster@xxx.com 邮箱为管理员邮箱,会经常收到系统发来的监控/病毒扫描/病毒库升级/垃圾邮件处理/数据库备份等邮件,请作为管理邮件使用.

## iRedMail 使用入门

下面以 **iRedMail 构建邮件系统** 作为一个任务，帮助用户快速入门：


## iRedMail 常用操作

### 域名绑定

1. 登录域名控制台，分别增加A、MX记录和TXT，其中TXT记录值为 *v=spf1 mx mx:mail.websoft9.cn -all*

![1542080447085](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/dns-websoft9.png)

2. 远程登录到服务器，通过命令，将主机名称改成 mail.websoft9.cn，然后运行“hostname”命令查看是否绑定成功。
   
  ```
     hostnamectl  set-hostname mail.websoft9.cn
     hostname
  ```

### SSL/HTTPS

邮件系统默认提供了证书，在配置完成之后，已经可以通过HTTPS访问。但是由于iRedMail提供的证书只是系统生成的，并没有经过认证，因此浏览器会提示不安全。

建议自行申请Symantec等证书（收费或免费均可），然后覆盖默认的证书

```
     /etc/pki/tls/certs/iRedMail.crt
     /etc/pki/tls/private/iRedMail.key
```
1. 将申请的证书重命名为 iRedMail.crt ，上传到 /etc/pki/tls/certs/ 目录覆盖原有系统证书
2. 将申请的证书的key重命名为 iRedMail.key， 上传到/etc/pki/tls/private/目录覆盖原有系统证书
3. 重启服务器

### 邮箱用户Web端

在邮件服务器的配置完成之后，就可以通过浏览器访问邮箱了。系统默认生成了一个账号：postmaster@域名
> 以安装时候的域名 websoft9.cn 为例，故账号就是：postmaster@websoft9.cn

1. 本地浏览器访问：https://邮箱域名/mail ，进入邮箱用户Web登录页面
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/roudcube-login-websoft9.png)
2. 输入账号之后，登录进入后台
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/roudcube-admin-websoft9.png)
3. 邮箱中默认存在系统设置相关邮件的三封邮件
4. 如果需要个性化设置，请点击右上角的“设置”链接
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/roudcube-setting-websoft9.png)


本镜像中还有另外一个更为简洁的Web端，访问方式：https://邮箱域名/SOGo
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/sogo-adminui-websoft9.png)


### 邮箱管理员Web端

在邮件服务器的配置完成之后，就可以通过浏览器访问邮箱管理端了。系统默认生成了一个账号：postmaster@域名
> 以安装时候的域名 websoft9.cn 为例，故账号就是：postmaster@websoft9.cn

1. 本地浏览器访问：https://邮箱域名/iredadmin ，进入邮箱管理员Web登录页面
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/iredadmin-login-websoft9.png)
2. 输入账号之后，登录进入管理后台
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/iredadmin-bk-websoft9.png)

### 新增邮箱用户

1. 添加->用户，进入新增用户界面
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iredmail/iredadmin-adduser-websoft9.png)
2. 可以设置用户名、密码和邮箱容量限额等，然后点击“添加”

### IAMP/POP3/SMTP

邮件服务器提供的主要收发协议以及对应的端口号如：

|   协议  |  地址   |   端口&加密端口 | 
| --- | --- | --- |
|  IAMP   |   邮箱域名  | 143,993 |
|  POP3 |   邮箱域名  | 110,995 |
|  SMTP |  邮箱域名  | 25,587 |

这里的 【邮箱域名】 是您的MX记录，例如：mail.websoft9.cn
如果您希望采用 iamp.websoft9.cn 或 smtp.websoft9.cn 这种地址形式，请在域名控制台增加响应的CNAME记录

## 参数{#parameter}

**[通用参数表](./setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 iRedMail 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 iRedMail 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 iRedMail 本身的参数：

### 路径{#path}

邮箱配置完成之后，请使用SFTP到服务器，下载 `/root/iRedMail/iRedMail.tips`文件，它包含了：

- 各个 web 程序的访问地址（URL），用户名和密码。
- 各个组件的配置文件路径
- 以及其它一些重要和敏感信息

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
|25,587|Postfix|必选|
|993,995,110,143|Dovecot|必选|
|80,443|Nginx 服务器|必选|

> 以上端口需要设置好安全组，并且向云产商申请解封25端口

### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

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

### 服务{#service}

```shell


```

### 命令行{#cli}

### API

### 参考{#ref}

