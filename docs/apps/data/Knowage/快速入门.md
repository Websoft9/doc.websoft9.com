---
sidebar_position: 1
slug: /knowage
tags:
  - Knowage
  - 大数据分析
  - BI
---

# 快速入门

[Knowage](https://www.knowage-suite.com) 源自SpagoBI，是使用Java语言写的开放源码的商业智能分析工具,是一套适合现代商业分析的开源工具套装。Knowage提供了高级的自助服务功能，为最终用户提供了自主权，可以构建自己的分析、探索和组织自己的数据空间。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-gui-websoft9.png)

在云服务器上部署 Knowage 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 和 **TCP:8080** 端口是否开启
3. 若想用域名访问 Knowage，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Knowage

* 管理员账号: `biadmin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

### MariaDB

* 管理员账号：*`root`*
* 管理员密码：存储在您的服务器中的文件中 */credentials/password.txt*  

> 需要登录MariaDBL，请参考 [MySQL可视化管理](#mariadb-数据管理)

## Knowage 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 进入登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-login-websoft9.png)

   > 也可以通过 http://公网IP:8080/knowage 访问本应用

2. 输入账号密码（[不知道账号密码？](#账号密码)），成功登录到 Knowage 后台  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-backend-websoft9.png)

3. 打开【Profile Management】>【Users Management】 修改密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-changepw-websoft9.png)

4. 打开【Server Settings】>【Configuration Management】 配置 Knowage
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-confmanagement-websoft9.png)

> 需要了解更多 Knowage 的使用，请参考官方文档：[Knowage Documentation](https://knowage-suite.readthedocs.io/)

## Knowage 入门向导

下面我们以一个完整的示例（**可视化呈现订单中不同国家的订单总额**），介绍如何使用 Knowage 快速分析数据。

基本步骤分为 4 步：连接数据源，数据建模，配置数据集，数据可视化呈现。
前2步为IT人员的数据准备，后2步为业务人员的自助分析。

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-websoft9.png)

1. 连接数据源：连接 MySQL 数据库服务器；

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-datasource-websoft9.png)

2. 数据建模：根据业务场景从数据源中选取数据，建模；

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-model-websoft9.png)

3. 配置数据集：业务人员从模型中二次筛选数据，分析和呈现；

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-dataset1-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-dataset2-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-dataset3-websoft9.png)

4. 数据呈现，设置可视化呈现方式（CHART）。根据场景也可以将数据以其他的可视化业务报表（仪表盘）呈现，供决策、分析使用。

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis1-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis2-websoft9.png)

选择数据集
![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis3-websoft9.png)

配置数据项
![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis4-websoft9.png)

![knowage](https://libs.websoft9.com/Websoft9/blog/tmp/knowage/zh/knowage-analysis5-websoft9.png)


## 常用操作

### 域名绑定

当服务器上只有一个网站时，不做域名绑定也可以访问网站。但从安全和维护考量，**域名绑定**不可省却。

以示例网站为例，域名绑定操作步骤如下：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name www.example.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### SSL/HTTPS

须完成[域名绑定](#域名绑定)且可通过 HTTP 访问 Knowage ，才可以设置 HTTPS。

Knowage 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

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
3. 重启[Nginx服务](/维护参考.md#nginx-1)

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### MariaDB 数据管理

Knowage 预装包中内置 MariaDB 及可视化数据库管理工具 `phpMyadmin` ，使用请参考如下步骤：

1. 登录云控制台，[开启服务器安全组9090端口](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

2. 本地浏览器 Chrome 或 Firefox 访问：*http://服务器公网IP:9090*，进入phpMyAdmin
  ![登录phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-logincn-websoft9.png)

3. 输入数据库用户名和密码([不知道密码？](#账号密码))

4. 开始管理数据库
  ![phpMyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mysql/phpmyadmin-adddb-websoft9.png)

> 阅读Websoft9提供的 [《MariaDB教程》](https://support.websoft9.com/docs/mariadb/zh/admin-phpmyadmin.html) ，掌握更多的 MariaDB 实用技能：修改密码、导入/导出数据、创建用户、开启或关闭远程访问、日志配置等

### 密码管理

修改密码即通过已有的密码正常登录系统后，再重新设置一个新密码；  
重置密码即忘记了登录密码，需要通过特殊的手段重新设置一个密码。

#### 修改密码

以管理员用户 biadmin 为例，介绍如何修改密码

1. 登录 Knowage 后台
2. 依次打开：【Profile Management】>【Users Management】 修改密码
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-changepw-websoft9.png)

#### 重置密码

以管理员用户 biadmin 为例，介绍如何重置密码

1. 使用 phpMyAdmin 登录数据库，找到`knowage_ce`库下的 `SBI_USER`表，删除其中的【biadmin】整行
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/knowage/knowage-deletedbbiadmin-websoft9.png)

2. 重启容器服务
   ```
   sudo docker restart knowage-server
   ```

3. 进入到 knowage-server容器，查看密码
   ```
   docker exec -it knowage-server bash
   cat /home/knowage/apache-tomcat/webapps/knowage/WEB-INF/conf/config/internal_profiling.xml | grep "password"
   ```

### 多语言

Knowage 支持多语言（不包含中文），下面介绍如何切换语言：

1. 登录 Knowage 后台

2. 打开左侧菜单的：【KNOWAGE ADMINISTRATOR】>【Languages】，设置你所需的语言

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/knowage/knowage-setlanguages-websoft9.png)


## 异常处理

#### 浏览器打开IP地址，无法访问 Knowage（白屏没有结果）？

您的服务器对应的安全组**80端口**没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### Knowage 服务启动失败？

请确保数据库连接信息准确无误

#### 为什么通过IP地址直接可以访问 Knowage？

本项目已经通过 Nginx 设置了端口转发



