---
sidebar_position: 3
slug: /owncloud/admin
tags:
  - ownCloud
  - 网盘
  - 知识管理
  - 团队协作
---

# 维护指南

## 场景

### 备份与恢复

ownCloud 后台提供在线备份功能

1. 登录 ownCloud 后台，安装 **[OwnBackup](https://en.websoft9.com/xdocs/owncloud-image-guide/#using-apps)** 插件
2. 打开：【Admin】>【OwnBackup】，开始备份
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ownbackup-websoft9.png)
3. 此插件也可以用于恢复
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-restore-websoft9.png)

### 升级

ownCloud提供了非常人性化的升级入口，根据系统的更新提示既可以完成主版本、插件的更新。

> 在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级100%成功。

#### 插件升级

升级步骤参加如下：

1. 登录 OwnCloud 之后查看右上角是否有更新通知，若有，请点击其中的更新条目
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatenotify-websoft9.png)

2. 点击更新条目后 或 访问：*http://域名/index.php/apps/market/#/updates*  进入更新界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatelist-websoft9.png)

3. 点击【更新】按钮，系统进入【UPDATING】，耐心等待更新
4. 所有更新完成后，更新清单会显示“所有应用都是最新的”

> 如果升级过程出现问题，例如：无法下载升级包/没有读写权限，请确保网络是通的/OwnCloud目录具有读写权限

#### 主程序升级

主程序升级与插件升级略有差异，具体参考如下：

1. 当有可用升级的程序时，系统提示“ownCloud is available. Get more information ...”
2. 依次打开：Admin->设置->常规，找到更新管理器，若有更新请点击“打开更新管理器”按钮
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-openupdater-websoft9.png)
3. 进入 Updater（更新管理器）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updater-websoft9.png)
4. 点击【Create a checkpoint】，创建一个核心文件备份
5. 点击【Start】按钮，系统进入自动化升级过程，下载和升级过程比较长，请耐心等待
6. 升级成功提示

> 由于升级过程会下载最新版本，ownCloud的下载服务器在国外，若下载不成功，需要不定期尝试

## 故障速查

#### ownCloud 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的ownCloud商店中文版会出现重定向

处理办法：
1. 分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则
2. 进入后台先删除中文，然后再重新导入中文。重新导入的时候，ownCloud会自动生成伪静态规则，覆盖您网站根目录的 `.htaccess` 文件

####  域名配置后，会出现“页面布局混乱或图片无法显示”？

如果先通过 IP 安装，再绑定域名，就会出现这个问题，请分别打开 ownCloud 的[配置文件](../owncloud#path)，将其中的IP地址改成域名。

#### 安装插件，显示403权限不足，错误"you dont have permession to access /admin/index.php"

修改文件：/etc/httpd/conf.d/mod\_evasive.conf 中  DOSPageCount 2 改为 DOSPageCount 12

#### 修改了数据库密码 ownCloud 不能访问？

若已完成 ownCloud 安装向导，再通过 phpMyAdmin 修改数据库密码，Nextcloud 就会连不上数据库  

需要修改 [ownCloud 配置文件](../owncloud#path) 对应的数据库 password 参数即可。

#### Apache httpd 服务无法启动？

请通过分析日志文件定位原因： */var/log/httpd*

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

## 常见问题

#### ownCloud 支持多语言吗？

支持多语言（包含中文）

#### ownCloud 是否提供客户端？

有。包括：ownCloud Desktop Client, ownCloud Android App, ownCloud iOS App

#### ownCloud 自身能够预览和编辑 Office 文档吗？

不可以，需要连接第三方的文档编辑和服务才可以，[设置参考](../owncloud/solution#onlyoffice)

#### ownCloud 支持集成外部存储吗？

支持多种主流外部存储服务

#### ownCloud(LAMP)ownCloud(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持 ownCloud 运行所对应的基础环境，具体参考[环境说明](../runtime/php)

#### 是否可以使用云平台的 RDS 作为 ownCloud 的数据库？

可以，修改 [ownCloud 配置文件](../owncloud#path) 即可

#### Nextcloud能在Windows服务器上运行吗？

可以，但是我们推荐在运行 ownCloud 效率更高的 Linux 服务器上运行

#### Nextcloud数据库连接配置信息在哪里？

数据库配置信息 [ownCloud 配置文件](../owncloud#path)中

#### 如果没有域名是否可以部署 Nextcloud？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 ownCloud 的源码路径？

可以，通过修改 [虚拟主机配置文件](../apache#virtualhost)中相关参数

#### 如何修改上传的文件权限?

```shell
#ownCloud(LAMP)
chown -R apache.apache /data/wwwroot

#ownCloud(LNMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```
