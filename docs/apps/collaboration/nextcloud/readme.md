---
sidebar_position: 1
slug: /nextcloud
tags:
  - Nextcloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 快速入门

[Nextcloud](https://nextcloud.com) 是 ownCloud 创始人发起的分支项目，是一款用于自建企业云存储（私有网盘）的开源软件。支持 PC、IOS 和 Android 三个同步客户端，用户可以很方便地与服务器上存储的文件、日程安排、通讯录、书签等重要数据保持同步。它还支持将数据保存到第三方存储中：Amazon S3、Dropbox、FTP、Google Drive、SMB、WebDAV、SFTP等。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 Nextcloud 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:9002**  端口已经开启
3. 在服务器中查看 Nextcloud 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Nextcloud **[域名五步设置](./administrator/domain_step)** 过程


## Nextcloud 初始化向导{#init}

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入引导首页
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-wizard-websoft9.png)
   
2. 设置用户名和密码并牢记，点击【安装】，安装完成后提示可继续安装插件，根据需求选择安装或者跳过    
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-plugin-websoft9.png)

3. 关闭弹窗，开始体验后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-main-websoft9.png)

4. 进入Marketplace，扩展更多的功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/nextcloud/nextcloud-app-websoft9.png)
   
5. 浏览器访问网址：*https://服务器公网IP:9002* 查看是否安装 **OnlyOffice docs**
   ![](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-documentserver-websoft9.png)

6. [设置文档预览与编辑](./nextcloud/solution#onlyoffice)功能（非必要）

> 需要了解更多 Nextcloud 的使用，请参考官方文档：[Nextcloud admin_manual](https://docs.nextcloud.com/server/latest/admin_manual/)


### 出现问题

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**Nextcloud 是否支持采用对象存储作为网盘使用？**

支持，但需要额外配置，[参考配置](#oss)

**Nextcloud 是否支持在线文档编辑与预览？**

镜像预装了 [OnlyOffice docs](./onlyofficedocs)，可以通过配置实现在线文档编辑与预览，[参考配置](./nextcloud/solution#onlyoffice)

## Nextcloud 使用入门

下面以 **Nextcloud 构建企业网盘系统** 作为一个任务，帮助用户快速入门：


## Nextcloud 常用操作

### 使用移动端

Nextcloud 支持移动端，使用步骤如下：

1. [下载](https://nextcloud.com/install)移动端
2. [设置](https://docs.nextcloud.com/android/)移动端到服务器的连接

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 登录 Nextcloud 后，点击齿轮图标，打开【个人】设置页面，填写发件邮箱地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-smtp-2-websoft9.png)

3. 点击【其他设置】>【电子邮件服务器】，依次填写 SMTP 信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-smtp-1-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

4. 点击“发送邮件”即可测试SMTP是否设置正确。

### 域名额外配置（修改 URL）{#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需设置 Nextcloud 的 URL:

1. 修改 [Nextcloud 配置文件](#path) 中的域名值
   ```
   'overwrite.cli.url' => 'nextcloud.yourdomain.com', # 修改为新域名
   ```
2. 重启服务后生效

### 设置语言

登录 Nextcloud，在后台 【个人】>【个人信息】中设置语言

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-mylanguage-websoft9.png)

### 在线安装扩展

Nextcloud 后台集成了 [Marketplace](https://apps.nextcloud.com) 大量的扩展（也叫apps），下面介绍如何安装它们

1. 登录 Nextcloud，在后台 【应用】>【应用软件包】中寻找所需的应用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-backendmk-websoft9.png)

2. 在线安装它

### 手工安装扩展{#minstallplugin}

网络问题可能会导致无法在线安装扩展，此时就需要手工安装（下面以 ONLYOFFICE 为例）：

1. 到 Nextcloud [官方应用商店](https://apps.nextcloud.com/apps/onlyoffice/releases?platform=22#22)下载扩展

2. 下载到本地后，解压，通过FTP上传到服务器 Nextcloud 应用目录：/data/wwwroot/nextcloud/apps

3. 登录 Nextcloud 后台，进入应用中心，启用 ONLYOFFICE 即可进入下一步操作，开启文档在线预览和编辑

### 连接外部存储{#oss}

Nextcloud 支持多种流行的企业存储服务，具体使用步骤如下：

1. 登录 Nextcloud 后台，安装 **External storage support** 扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-enablestorage-websoft9.png)

2. 打开：【Admin】>【Add storage】>【External Storage】，选择一个外部存储服务
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-enablestorage002-websoft9.png)

3. 根据实际情况进行设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-auth_mechanism-websoft9.png)

更多详情参考官方文档：[External Storage](https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/external_storage_configuration_gui.html)


### 数据转移

Nextcloud 的程序和数据文件默认均存在系统盘，你要转移到数据盘（或对象存储），步骤如下：

#### 转移到数据盘

1. 在服务器所在的云平台上购买数据盘，并**挂载**到 Nextcloud 服务器
2. 使用 SFTP 工具连接服务器，停止服务
   ```
   systemctl stop httpd
   ```
3. 新建一个 */data/wwwroot/nextcloud2* 文件夹
4. 初始化数据盘，并将数据盘 **mount** 到新建的 *nextcloud2* 文件夹
5. 将 */data/wwwroot/nextcloud* 下的数据全部拷贝到 */data/wwwroot/nextcloud2*  
6. 修改 Nextcloud [虚拟主机配置文件](./apache#virtualhost) 的路径
7. 启动服务后生效
   ```
   systemctl start httpd
   ```

#### 转移到对象存储

1. 在服务器所在的云平台上购买对象存储，新建一个 **bucket**
2. 使用 SFTP 工具连接服务器，停止服务
   ```
   systemctl stop httpd
   ```
3. 新建一个 */data/wwwroot/nextcloud2* 文件夹
4. 将对象存储的 bucket **mount** 到新建的 *nextcloud2* 文件夹
5. 将 */data/wwwroot/nextcloud* 下的数据全部拷贝到 */data/wwwroot/nextcloud2*  
6. 修改 Nextcloud [虚拟主机配置文件](./apache#virtualhost) 的路径
7. 启动服务后生效
   ```
   systemctl start httpd
   ```
8. 设置对象存储开机自动挂载（不同云平台操作不同）

> 以上两种数据转移方案中，**mount** 操作对新手来说是几乎是不可能独立完成的任务。另外，如果转移的数据超过10G，会存在拷贝失败的风险

### 通过 WebDAV 连接 NextCloud

NextCloud 支持 WebDAV 协议，用户可以通过 WebDAV 来连接并同步文件，比如在 Windows10 系统映射磁盘到 NextCloud，用于本地访问云盘文档。

1. 获取 WebDav 连接 URL： 登录NextCloud，点击【文件】-【设置】获取 URL
  > 注意：每个用户都有自己的 URL，使用对应的 URL 和用户名登录才能正确访问文件

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nextcloud/nextcloud-webdavurl-websoft9.jpg)

2. 配置本地连接：在 Windows10 【运行】regedit 命令，进入注册表，修改注册表项 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters，将 BasicAuthLevel 值设为 2 ，将 FileSizeLimitInBytes 值改成十进制 50000000
3. 重启本地服务：打开 Windows PowerShell(管理员) 工具，输入命令 net start webclient 重启 webclient 服务
4. 映射本地磁盘：右击【我的电脑】，选择【映射网络驱动器】， 复制第1步中的URL，确定。在弹出的登录界面，输入NextCloud 登录账号，完成连接。
5. 完成上述操作，进入【我的电脑】，可以看见新添加的【网络位置盘符】，双击打开即可访问 NextCloud 远程文件。

## OwnCloud 参数{#parameter}

Nextcloud 应用中包含 Nginx, Docker, MySQL, phpMyAdmin, [ONLYOFFICE Docs](./onlyofficedocs) 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。  

通过运行 `docker ps`，可以查看到 Nextcloud 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                              COMMAND                  CREATED             STATUS             PORTS                                                  NAMES
c8a5fae52a35   onlyoffice/documentserver:latest   "/app/ds/run-documen…"   59 minutes ago      Up 59 minutes      443/tcp, 0.0.0.0:9002->80/tcp, :::9002->80/tcp         onlyofficedocs
5523e9c3a9bd   phpmyadmin:latest                  "/docker-entrypoint.…"   59 minutes ago      Up 59 minutes      0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
6ecb1771a868   nextcloud:latest                   "/entrypoint.sh apac…"   About an hour ago   Up About an hour   0.0.0.0:9001->80/tcp, :::9001->80/tcp                  nextcloud
ae358a9bb912   mysql:8.0                          "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   nextcloud-db
```

### 路径{#path}

Nextcloud 安装目录： */data/apps/nextcloud*  
Nextcloud 数据目录： */data/apps/nextcloud/data/nextcloud-data*  
Nextcloud 站点目录： */data/apps/nextcloud/data/nextcloud*  
Nextcloud 配置文件： */data/apps/nextcloud/data/nextcloud/config/config.php*  
Onlyofficedocs 安装目录： */data/apps/onlyofficedocs*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9002 | OnlyOffice docs on Docker | 可选 |


### 版本{#version}

```shell
docker exec -i nextcloud cat version.php |grep OC_VersionString |awk -F "'" '{print $2}'
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats nextcloud
sudo docker start | stop | restart | stats nextcloud-db
sudo docker start | stop | restart | stats phpmyadmin
sudo docker start | stop | restart | stats onlyofficedocs
```

### 命令行{#cli}

occ 命令是 Nextcloud 的命令行界面。 OCC 可安装和升级 Nextcloud，管理用户，加密，密码管理，LDAP设置等。  

```
sudo -u www-data php occ
Nextcloud version 19.0.0

Usage:
 command [options] [arguments]

Options:
 -h, --help            Display this help message
 -q, --quiet           Do not output any message
 -V, --version         Display this application version
     --ansi            Force ANSI output
     --no-ansi         Disable ANSI output
 -n, --no-interaction  Do not ask any interactive question
     --no-warnings     Skip global warnings, show command output only
 -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output,
                       2 for more verbose output and 3 for debug

Available commands:
 check                 check dependencies of the server
                       environment
 help                  Displays help for a command
 list                  Lists commands
 status                show some status information
 upgrade               run upgrade routines after installation of
                       a new release. The release has to be
                       installed before.
```

### API

[Basic APIs](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/WebDAV/basic.html)
