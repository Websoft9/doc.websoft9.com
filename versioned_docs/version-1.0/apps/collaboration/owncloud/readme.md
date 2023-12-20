---
sidebar_position: 1
slug: /owncloud
tags:
  - ownCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 快速入门

[ownCloud](https://owncloud.org) 是一款用于自建内容协作（私有网盘）的开源软件，使团队能够轻松地共享和处理文件，而无需考虑设备或位置。全球已有超过 1 亿用户使用 ownCloud 作为公共云盘的替代方案，从而选择更多的数字主权、安全性和数据保护。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 ownCloud 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:9002**  端口已经开启
3. 在服务器中查看 ownCloud 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  ownCloud **[域名五步设置](./administrator/domain_step)** 过程


## ownCloud 初始化向导{#init}

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 就进入引导首页
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-init1-websoft9.png)

2. 填写登陆信息（[不知道账号密码？](./user/credentials)）  

5. 点击【login】，开始体验后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-installcomplete-websoft9.png)

6. [设置文档预览与编辑](./owncloud/solution#onlyoffice)功能（非必要）

> 需要了解更多 ownCloud 的使用，请参考官方文档：[ownCloud admin_manual](https://doc.owncloud.org/server/admin_manual/)



### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**ownCloud 是否支持采用对象存储作为网盘使用**

支持，但需要额外配置，[参考](#oss)

**ownCloud 是否支持在线文档编辑与预览**

镜像预装了 OnlyOffice Docs，可以通过配置实现在线文档编辑与预览，[参考](./owncloud/solution#onlyoffice)


## ownCloud 使用入门

下面以 **ownCloud 构建企业网盘系统** 作为一个任务，帮助用户快速入门：


## ownCloud 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 登录OwnCloud后，打开【admin】>【设置】>【个人】>【常规】，填写发件邮箱地址
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-smtp-1-websoft9.png)

3. 打开【设置】>【管理】>【常规】，依次填写 SMTP 信息
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-smtp-2-websoft9.png)

    * 发送模式选择“SMTP”，加密方式选择“SSL/TLS”;
    * 输入发送方邮箱地址；
    * 认证方式选择“登录”，并勾选“需要认证”选项；
    * 输入SMTP服务器地址和SMTP服务器的端口号；
    * 输入和发件人邮箱一致的邮箱地址；
    * 输入该邮箱地址的SMTP服务的授权码或密码；
    * 存储凭据；

4. 点击“发送邮件”即可测试SMTP是否设置正确。


### 域名额外配置（修改 URL）{#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需设置 ownCloud 的 URL:

1. 修改 [Owncloud 配置文件](#path) 中的域名值
   ```
   'overwrite.cli.url' => 'owncloud.yourdomain.com', # 修改为新域名
   ```
2. 重启服务后生效

### 设置语言

登录 ownCloud，在后台 【Personal】>【General】中设置语言

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-zh-websoft9.png)

### 安装扩展

ownCloud [Marketplace](https://marketplace.owncloud.com/) 包含大量的扩展（也叫apps），下面介绍如何安装它们

1. 访问 [Marketplace](https://marketplace.owncloud.com/) ，搜索所需的应用（以 OwnBackup 为例）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-searchapps-websoft9.jpg)

2. 下载并解压  

3. 上传到 ownCloud 应用目录：/var/lib/docker/volumes/owncloud_owncloud/_data/apps，并通过chown 命令，改变扩展目录（如 ownbackup）的拥有者和关联组用户为 www-data
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ftp-websoft9.png)

4. 启用 OwnBackup  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enableapps-websoft9.png)

> 除了下载安装之外，也可以通过 ownCloud 后台在线安装 Marketplace 应用

### 连接外部存储{#oss}

ownCloud 支持多种流行的企业存储服务，具体使用步骤如下：

1. 登录 ownCloud 后台，安装 **External storage support** 扩展
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enablestorage-websoft9.png)

2. 打开：【Admin】>【Add storage】>【External Storage】，选择一个外部存储服务
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-enablestorage002-websoft9.png)

3. 根据实际情况进行设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-auth_mechanism-websoft9.png)

更多详情参考官方文档：[External Storage](https://doc.owncloud.org/server/admin_manual/configuration/files/external_storage/index.html)


### 数据转移

ownCloud 的程序和数据文件默认均存在系统盘，你要转移到数据盘（或对象存储），步骤如下：


#### 转移到对象存储

1. 将 ownCloud 数据目录复制一份到目录：*/data/backup/owncloud*  
2. 在服务器所在的云平台上购买对象存储，新建一个 **bucket**
3. 将对象存储的 bucket **mount** 到 ownCloud 数据目录，并设置开机自动挂载（具体参考对象存储文档）
4. 将 ownCloud 备份文件拷贝到 ownCloud 数据目录
5. 连接到 ownCloud 容器，重建 ownCloud 索引 
   ```
   occ files:scan --all
   ```

#### 转移到数据盘

转移到数据盘的操作与转移到对象存储非常类似，只是 2-3 步骤操作略有差异


> 以上两种数据转移方案中，**mount** 操作对新手来说是几乎是不可能独立完成的任务。另外，如果转移的数据超过10G，会存在拷贝失败的风险


## ownCloud 参数{#parameter}

ownCloud 应用中包含 PHP, Apache, Nginx, Docker, Redis, MySQL, phpMyAdmin, [ONLYOFFICE Docs](./onlyofficedocs) 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行`docker ps`，可以查看到 ownCloud 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                              COMMAND                  CREATED             STATUS                       PORTS                                                  NAMES
47ea9a709b5d   onlyoffice/documentserver:latest   "/app/ds/run-documen…"   About an hour ago   Up About an hour             443/tcp, 0.0.0.0:9002->80/tcp, :::9002->80/tcp         onlyofficedocs
cd2792a962d0   phpmyadmin:latest                  "/docker-entrypoint.…"   About an hour ago   Up About an hour             0.0.0.0:9090->80/tcp, :::9090->80/tcp                  phpmyadmin
c2cce00268eb   ownCloud/server:latest             "/usr/bin/entrypoint…"   About an hour ago   Up About an hour (healthy)   0.0.0.0:9001->8080/tcp, :::9001->8080/tcp              ownCloud
bdfde6911911   mysql:5.7                          "docker-entrypoint.s…"   About an hour ago   Up About an hour (healthy)   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   ownCloud-db
59fa97a29571   redis:6                            "docker-entrypoint.s…"   About an hour ago   Up About an hour (healthy)   6379/tcp                                               ownCloud-redis
```

### 路径{#path}

ownCloud 安装目录： */data/apps/ownCloud*  
ownCloud 数据目录： */data/apps/ownCloud/data/ownCloud*  
ownCloud 配置文件： */data/apps/ownCloud/data/ownCloud/config/config.php*  
Onlyofficedocs 安装目录：*/data/apps/onlyofficedocs*

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 9002 | OnlyOffice Docs on Docker | 可选 |


### 版本{#version}

```shell
docker exec -i ownCloud occ -Version
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats ownCloud
sudo docker start | stop | restart | stats ownCloud-db
sudo docker start | stop | restart | stats ownCloud-redis
sudo docker start | stop | restart | stats onlyofficedocs
```

### 命令行{#cli}

[ownCloudcmd](https://doc.ownCloud.com/desktop/next/advanced_usage/command_line_client.html) 命令是 ownCloud 的命令行工具

```
ownCloudcmd -h
```

### API

[Provisioning API](https://doc.ownCloud.com/server/next/developer_manual/core/apis/provisioning-api.html)

