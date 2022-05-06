---
sidebar_position: 3
slug: /opencart/admin
tags:
  - OpenCart
  - 电子商务
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### 备份

OpenCart 后台提供了数据库备份功能

1. 登录 OpenCart 后台
2. 打开：【System】>【Maintenance】>【Backup/Restore】，开始备份数据库
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-backupdb-websoft9.png)

### 升级

OpenCart 只能通过手动的方式升级。下面是对 OpenCart [官方升级文档](https://docs.opencart.com/en-gb/upgrading/)的简化描述：

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


## 故障排除

除以下列出的 OpenCart 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

####  域名配置后，页面布局混乱？

**原因分析**：先通过 IP 安装，再绑定域名，导致默认 URL 发生变化   

**解决方案**：[修改 URL](../opencart#dns)

#### 安装插件，显示403权限不足？

**现象描述**：错误信息 "you dont have permession to access /admin/index.php"   
**解决方案**：修改文件：/etc/httpd/conf.d/mod\_evasive.conf 中  DOSPageCount 2 改为 DOSPageCount 12

## 问题解答

#### OpenCart 支持多语言吗？

支持多语言（包含中文），通过[后台设置](../opencart#setlanguage)即可

#### 安装 Extension 需要[设置 FTP 账号](http://docs.opencart.com/en-gb/extension/installer/)吗？

自 OpenCart3.0 开始已经不需要了