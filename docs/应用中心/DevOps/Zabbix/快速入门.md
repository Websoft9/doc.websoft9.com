---
sidebar_position: 1
slug: /zabbix
tags:
  - Zabbix 
  - DevOps
---

# 快速入门

[Zabbix](https://www.zabbix.com/cn) 是一个开源的企业级监控解决方案，支持实时监控数千台服务器，虚拟机和网络设备，采集百万级监控指标。支持分布式架构，通过统一的 Web 界面监控自动监控大型动态环境。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-gui-websoft9.png)


在云服务器上部署 Zabbix 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Zabbix，请先到 **域名控制台** 完成一个域名解析

## 账号密码


通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Zabbix

* 管理员用户名：`Admin`  
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

### MySQL

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

## Zabbix 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登录界面
   ![Zabbix 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-login-websoft9.png)

2. 输入账号密码后登录到后台（[不知道账号密码？](#账号密码)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboard-websoft9.png)

3. 打开用户管理界面，更换所需的语言（如果语言为灰色状态，参考[启用语言方案](/zh/solution-more.md#zabbix-多语言)）
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-changelang-websoft9.png)  
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboardzh-websoft9.png)

## Zabbix 入门向导

下面继续上一节，通过连接一个客户端的实际应用场景，帮助用户快速入门。  

1. 使用SSH连接 Zabbix 服务器

2. 获取服务器上 Zabbix-Agent 容器虚拟机的IP（用于演示并监控服务器自身）
   ```
   docker inspect zabbix-agent | grep IPAddress
   ```
   > 若监控其他服务器，需先[安装Zabbix-Agent](#安装客户端)，然后参数上述步骤

3. 登录到 Zabbix 控制台后， 依次打开：【配置】>【主机】，打开主机列表
   ![Zabbix 添加主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-edithost001-websoft9.png)

4. 输入第二步获取的 IP 地址，保存配置
   ![Zabbix 添加主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-edithost002-websoft9.png)

5. 回到主机列表页，启用主机监控，当主机【可用性】列变成**绿色**即表明监控已成功

> 需要了解更多 Zabbix 的使用，请参考官方文档：[Zabbix Documentation](https://www.zabbix.com/documentation/current/)

## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Zabbix 域名绑定操作步骤：

1. 使用 SFTP 工具登录云服务器

2. 修改 [虚拟机主机配置文件](/zh/stack-components.md#nginx)，将其中的域名相关的值
   ```text
   server_name    localhost; # 改为自定义域名
   ```
   
3. 保存配置文件，[重启 Nginx 服务](/zh/admin-services.md#nginx)


Zabbix 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

### SSL/HTTPS

必须完成[域名绑定](#域名绑定)且可通过 HTTP 访问 Zabbix ，才可以设置 HTTPS。

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

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 Zabbix 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录到 Zabbix 后台，完成 SMTP 参数设置  
  
   - 依次打开：【管理】>【报警媒介类型】，选择【Email】
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-opensmtp-websoft9.png)
   - 准确的填写你的 SMTP 参数
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-smtpsetting-websoft9.png) 

3. 自测是否可以发送邮件
     
> 更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


### 更换数据库

默认部署方案中，采用的是本地安装的 MySQL 数据库。如果您打算更换数据库，请参考如下步骤：

1. 导出 zabbix, zabbix-proxy 数据库

2. 使用 SFTP 连接到服务器，编辑与数据库连接相关的两个文件

   * /data/wwwroot/zabbix/.env_db_mysql_proxy
   * /data/wwwroot/zabbix/.env_db_mysql

3. 分别修改两个文件中的数据库连接信息，保存

4. 重新运行容器后生效
   ```
   cd /data/wwwroot/zabbix
   sudo docker compose up -d
   ```

5. 导入备份数据到新的数据库中

### 多语言

Zabbix 默认已经内置多种语言包，非常方便进行在线切换。

1. 登录到 Zabbix 后台

2. 依次打开：【管理】>【用户】，编辑用户信息管理界面，更换所需的语言
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-changelang-websoft9.png)  
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboardzh-websoft9.png)

> 如果语言为灰色状态,参考官方字符编码安装方案：[How to install locale](https://zabbix.org/wiki/How_to/install_locale)

### 安装客户端

1. 安装 [Zabbix-agent](https://www.zabbix.com/download?zabbix=5.0&os_distribution=centos&os_version=7&db=mysql&ws=apache) 
   ```shell
   rpm -Uvh https://repo.zabbix.com/zabbix/<ZABBIX_VERSION>/rhel/7/x86_64/zabbix-release-<ZABBIX_VERSION>-1.el7.noarch.rpm
   yum install zabbix-agent -y
   ```

2. 配置 /etc/zabbix/zabbix_agentd.conf
   ```
   Server=SERVER_IP   
   ServerActive=SERVER_IP (服务端ip)   
   Hostname=zabbix_web (客户端主机名)   
   ```

### 重置密码

常用的 Zabbix 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 Zabbix 后台，依次打开：【管理】>【用户】，编辑目标用户
  ![Zabbix 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-modifypw-websoft9.png)

2. 点击【修改密码】

#### 找回密码

如果用户忘记了密码，需要通过修改数据库相关字段来重置密码：

1. 登录 [phpMyAdmin](/zh/admin-mysql.md)，进入 Zabbix 数据库

2. 在 SQL 窗口运行重置密码的命令
   ```
   sudo mysql -uroot -p new_password -e "update zabbix.users set passwd=md5(new_password) where alias='Admin';"
   ```


## 异常处理

#### 浏览器无法访问 Zabbix（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 端口已经开启，*http://服务器公网IP* 仍然无法访问 Zabbix？

您使用的非容器部署方案，请参考[此处](/zh/stack-installationold.md)

#### 本部署包采用的哪个数据库来存储 Zabbix 数据？

MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Zabbix 数据？

不建议


