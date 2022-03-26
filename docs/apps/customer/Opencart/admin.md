---
sidebar_position: 3
slug: /opencart/admin
tags:
  - OpenCart
  - 电子商务
---

# 维护指南

## 场景

### 备份与恢复

OpenCart 后台提供了数据库备份功能

1. 登录 OpenCart 后台
2. 打开：【System】>【Maintenance】>【Backup/Restore】，开始备份数据库
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-backupdb-websoft9.png)

### 升级

以下升级步骤是官方升级文档的简化：

1. 备份 OpenCart 程序和数据库文件，下载到本地
2. [下载](https://www.opencart.com/index.php?route=cms/download)最新的 OpenCart 程序
3. 使用 SFTP 登录服务器，上传新的代码，覆盖原来的文件
4. 将本地备份的 OpenCart 根目录下的 `config.php` 文件和 `admin/config.php` 重新上传到服务器
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/Opencart-update001-websoft9.png)  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/Opencart-update002-websoft9.png) 
5. 浏览器访问：*http://域名/install* 开始升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/Opencart-update003-websoft9.png)  
6. 升级成功提示 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/Opencart-update004-websoft9.png)  

参考官方升级文档：[Upgrading](https://docs.opencart.com/en-gb/upgrading/)



## 故障速查

除以下列出的 OpenCart 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### OpenCart 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的OpenCart商店中文版会出现重定向

处理办法：
1. 分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则
2. 进入后台先删除中文，然后再重新导入中文。重新导入的时候，OpenCart会自动生成伪静态规则，覆盖您网站根目录的 `.htaccess` 文件

####  域名配置后，会出现“页面布局混乱或图片无法显示”？

如果先通过 IP 安装，再绑定域名，就会出现这个问题，请分别打开 OpenCart 的[配置文件](../opencart#dns)，将其中的IP地址改成域名。

#### 安装插件，显示403权限不足，错误"you dont have permession to access /admin/index.php"

修改文件：/etc/httpd/conf.d/mod\_evasive.conf 中  DOSPageCount 2 改为 DOSPageCount 12

#### 修改了数据库密码 OpenCart 不能访问？

若已完成 OpenCart 安装向导，再通过 phpMyAdmin 修改数据库密码，OpenCart 就会连不上数据库  

需要修改 [OpenCart 配置文件](../opencart#path) 对应的数据库 password 参数即可。

#### Apache httpd 服务无法启动？

请通过分析日志文件定位原因： */var/log/httpd*



## 问题解答


#### OpenCart 支持多语言吗？

支持多语言（包含中文），通过[后台设置](../opencart#setlanguage)即可

#### OpenCart(LAMP)，OpenCart(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持 OpenCart 运行所对应的基础环境，具体参考[环境说明](../opencart#ref)

#### 是否可以使用云平台的 RDS 作为 OpenCart 的数据库？

可以，修改 [OpenCart 配置文件](/zh/stack-components.html#opencart) 即可

#### OpenCart能在Windows服务器上运行吗？

可以，但是我们推荐在运行 OpenCart 效率更高的 Linux 服务器上运行

#### OpenCart数据库连接配置信息在哪里？

数据库配置信息 [OpenCart 配置文件](../opencart#path)中

#### 安装 OpenCart Extension 需要[设置 FTP 账号](http://docs.opencart.com/en-gb/extension/installer/)吗？

自 OpenCart3.0 开始已经不需要了

#### 如果没有域名是否可以部署 OpenCart？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 OpenCart 的源码路径？

可以，通过修改 [虚拟主机配置文件](../apache#virtualHost)中相关参数