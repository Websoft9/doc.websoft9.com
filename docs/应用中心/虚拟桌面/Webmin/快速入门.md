---
sidebar_position: 1
slug: /webmin
tags:
  - Webmin
  - 虚拟桌面
  - Web 可视化 Linux 管理员工具
---

# 快速入门

[Webmin](https://www.webmin.com) 是基于 Web 的可视化 Linux/Unix 系统管理员工具，它可以管理 Apache, MySQL等基础环境软件，也可以管理 DNS, FTP, 用户, 防火墙等系统级配置。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-dashboard-websoft9.png)


在云服务器上部署 Webmin 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Webmin，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Webmin

#### 密码登陆

* 管理员账号: `root`
* 管理员密码: 服务器的 root 密码

#### 秘钥登陆

服务器未设置root密码，使用秘钥登陆的情况，执行如下脚本：

```
sudo su -
passwd 'your password'
```

* 管理员账号: `root`
* 管理员密码: 'your password'

## Webmin 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://服务器公网IP*, 进入登录页面

   ![Webmin 登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](/zh/stack-accounts.md#webmin)），成功登录到 Webmin 后台  

   ![Webmin 登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-dashboard-websoft9.png)

   > Webmin 默认以服务器的 root 用户作为账号

3. 设置语言：依次打开菜单【Webmin】>【Change Language and Theme】重设所需的语言

   ![Webmin 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-changelangs-websoft9.png)

4. 系统管理：通过【系统】菜单可以进行系统管理，如修改密码及用户及群组、软件包管理等

   ![Webmin 系统管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-system-websoft9.png)

5. 服务器管理：通过【服务器】菜单可以进行服务器管理，如 Apache web服务、SSH服务等

   ![Webmin 服务器管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-server-websoft9.png)

5. 文件管理：通过【Tools】>【File Manage】菜单可以进行目录、文件管理，如新建文件夹、上传文件、修改文件的权限等

   ![Webmin 文件管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-file-websoft9.png)

6. 点击菜单下方的【>_】图标，进入 SSH 命令行模式（ESC 键取消）

   ![Webmin SSH 模式](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-sshcli-websoft9.png)

7. 完成其他所需的配置

> 需要了解更多 Webmin 的使用，请参考官方文档：[Webmin Documentation](http://doxfer.webmin.com/Webmin/Main_Page)

## Webmin 入门向导

现在开始针对于如何使用 Webmin 安装一个 WordPress 网站，做出一个完整的说明：  

### 准备环境

WordPress 基于PHP 和 MySQL 技术栈，web 服务器使用Apache 。本部署方案中默认已经安装 Apache，还缺少 PHP 和 MySQL。  

PHP 和 MySQL 的安装是比较麻烦的，所幸，我们可以使用 Websoft9 提供的自动化脚本完成安装

> 可能会因网络原因，git clone 从 github 站下载时会有异常，可以多尝试几次

1. 运行下面的命令，安装 PHP，本次安装的 WordPress 是 5.8 ，需要 PHP7.4 支持，因此版本选择 7.4 
   ```
   git clone https://github.com/Websoft9/role_php.git
   ansible-playbook role_php/tests/test.yml
   ```

2. 运行下面的命令，安装 MySQL，其中版本选择 5.7
   ```
   git clone https://github.com/Websoft9/role_mysql.git
   ansible-playbook role_mysql/tests/test.yml
   ```
   > 请记住 MySQL 安装时设置的登录密码。如没有设置，默认密码为：123456 ，请及时修改为更为复杂的强密码。

3. 登录到 Webmin 后台，点击左侧菜单下方的【刷新模块】按钮，在【服务器】菜单下可以看到【MySQL数据库服务器】


### 上传源码

先下载 WordPress 到本地，然后上传、解压、修改文件权限。

1. 通过菜单打开【Tools】>【File Manager】 选择进入/data/wwwroot 目录，点击“File”下拉菜单，选择“Upload to current directory”完成wordpress压缩包上传：

   ![Webmin 上传](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb01.png)

1. 选中软件压缩包，鼠标右键中选择【提取】,文件开始解压

   ![Webmin 解压](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb02.png)

2. 文件解压后，多了1个目录

   ![Webmin 解压](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb03.png)

3. 选中目录，鼠标右键【属性】>【更改所有权】，开始授权

   ![Webmin 修改文件权限](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb04.png)

4. 分别将用户和组都设置为 apache 勾选 Recursive，点击“Change”

   ![Webmin 修改文件权限](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb05.png)

### 创建数据库

1. 打开菜单【服务器】 > 【MySQL数据库服务器】，点击“创建新的数据库”

   ![Webmin MySQL数据库服务器](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb06.png)

2. 设置你的数据库名称

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb07.png)


### 配置数据库

为 WordPress 连接数据库。
通过FTP工具（这里是用 WinSCP）连接到服务器，找到 WordPress 的配置文件 /data/wwwroot/wordpress/wp-config.php，修改数据库连接信息（** 密码是上面安装MySQL时设置的密码 **），并保存。

   ![Webmin 连接数据库](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb071.png)


### 配置虚拟主机

配置虚拟主机，需提前将域名解析到服务器。解析成功后，参考下面配置完成虚拟主机设置：

1. 打开菜单【服务器】 > 【Apache服务器】，点击“Create virtual host”。

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb08.png)

2. 点击右上角按钮，使域名设置生效：

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb09.png)

3. 本地浏览器访问：http://域名，测试 WordPress

   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/wb10.png)


## 常用操作

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

Webmin 域名绑定操作步骤：

1. 确保域名解析已经生效  

2. 登录 Webmin 控制台，打开：【Apache 服务器】>【编辑配置文件】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-confapache001-websoft9.png)

3. 修改 [Apache虚拟机主机配置文件](/zh/stack-components.md#apache)，将其中的 **ServerName** 项的值修改为你的域名
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-confapache002-websoft9.png)

4. 保存配置文件，重启 [Apache 服务](/zh/admin-services.md#apache)

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 Webmin ，才可以设置 HTTPS。

Webmin 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了证书，只需三个步骤，即可完成 HTTPS 配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/httpd/conf.d/vhost.conf* ，新增**HTTPS 配置段** 到文件中
 ``` text
   <VirtualHost *:443>
    ServerName  webmin.yourdomain.com
    DocumentRoot "/data/apps/webmin"
    #ErrorLog "logs/webmin.yourdomain.com-error_log"
    #CustomLog "logs/webmin.yourdomain.com-access_log" common
    <Directory "/data/apps/webmin">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/webmin.yourdomain.com.crt
    SSLCertificateKeyFile  /data/cert/webmin.yourdomain.com.key
    SSLCertificateKeyFile  /data/cert/webmin.yourdomain.com.key
    </VirtualHost>
   ```
3. 修改域名信息，保存配置文件

4. 重启[ Apache 服务](/zh/admin-services.md#nginx)后生效
   ```
   sudo systemctl restart apache
   ```

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板及故障诊断等具体方案。

### 修改密码

Webmin 默认使用的是服务器 root 账号，修改服务器密码即修改 Webmin 密码。  

故，用 `passwd` 系统命令即可

### Apache 服务器配置

Webmin Apache 配置虚拟主机的操作如下：

要配置的域名为 test3.websoft9.cn，对应 WordPress 网站的根目录是/data/wwwroot/wordpress，接下来为该站点添加配置文件，设置域名、访问目录等（根据这个方法重复多次，就可以配置不同的网站的域名）:

1. 通过 http://IP地址，登录webmin面板工具。

2. 通过菜单中的“服务器”-》“Apache服务器”打开服务器配置。

3. 通过“Create virtual host”创建新的虚拟主机，填写参数，然后点击“创建”。
   > 配置说明
     服务端口：80
     网站目录: /data/wwwroot/wordpress 
     网站域名：xtrack.cn(测试用域名)
     配置文件：xtrack.conf，放在Apache配置文件目录下 /etc/httpd/conf.d/

   ![Webmin Apache](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-apache-vhost-websoft9.png)

4. 通过SSH模式查看生产配置文件

   ![Webmin Apache](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-apache-vhost-conf-websoft9.png)


### 修改时区

### FTP 管理

通过【Tools】 > 【File Manage】菜单可以进行文件管理，如文件的上传、下载等

选择 Wordpress 文件夹，点击【file】下拉菜单，选择“上传到当前目录”，完成文件上传

   ![Webmin File](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-ftp-websoft9.png)

### 用户管理

通过【系统】 > 【用户与群组】菜单可以进行用户及角色（分组）管理，如新增用户和编辑用户

选择“创建新用户”或点击用户列表中的用户可以实现用户添加和编辑操作。

   ![Webmin File](https://libs.websoft9.com/Websoft9/DocsPicture/zh/webmin/webmin-user-websoft9.png)


## 异常处理

#### 浏览器打开IP地址，无法访问 Webmin（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### Webmin 默认使用的哪个端口？

默认使用 10000 端口，但本部署方案采用 Apache 进行了转发访问
