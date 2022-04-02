---
sidebar_position: 3
slug: /zentao/admin
tags:
  - ZenTao（禅道）
  - 项目管理
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### 备份与恢复

ZenTao 后台提供了非常简单实用的在线备份功能，使用方法如下：

1. 登录 ZenTao 后台，打开：【管理】>【数据】，进入备份页面，设置备份策略。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backupstr-websoft9.png)

2. 点击备份操作
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-backup-websoft9.png)

3. 在线实现的备份可以在线恢复（还原）

4. ZenTao 提供的回收站功能，也可以恢复手工删除的数据
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-recycle-websoft9.png)

### 升级

ZenTao 通过手工上传代码的方式进行升级。在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级 100% 成功。

1. [下载](https://www.zentao.net/download.html)最新源码，解压
2. 上传并覆盖服务器上的 ZenTao 源码
3. 本地浏览器访问: _http://服务器公网 IP/upgrade.php_ 开始升级
4. 如果升级过程报错" Uncaught Error: Call to a member function query() on null in li..."，请给 `zentao/www` 和 `zentao/tmp` 目录递归加下 777 权限后再试

> 更多升级详情，请参考官方升级文档 [ZenTao 通过源代码方式升级(通用)](https://www.zentao.net/book/zentaopmshelp/67.html)

## 故障速查

除以下列出的 Superset 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案：

#### ZenTao 重定向错误？

重定向错误比较常见。处理办法：分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### 密码输入错误多次被锁，怎么解决？

1. 10 分钟后会自动解锁。
2. 管理员登录，组织 → 用户 操作栏里有解锁按钮。

#### 修改了数据库密码 ZenTao 不能访问？

若已完成 ZenTao 安装向导，再通过 phpMyAdmin 修改数据库密码，ZenTao 就会连不上数据库

需要修改 [ZenTao 配置文件](././#path) 对应的数据库 password 参数即可。

## 常见问题

#### ZenTao 支持多语言吗？

支持中英文

#### ZenTao 开源版是免费的吗？

基于 ZPL 协议发布，源代码开放，不限商用。当然您也可以购买官方的[企业版、集团办](https://www.zentao.net/page/professional.html)等

#### 为什么要注册 ZenTao 官网账号？

[注册](https://www.zentao.net/user-register.html)官网账号，你可以将 ZenTao 系统与官网连接，在线安装插件。

#### ZenTao 提供客户端吗？

禅道手机客户端 IOS 版本和安卓版本， 专为禅道专业版和企业版用户提供。

#### ZenTao 商品中的 LAMP,LNMP 有何含义？

LAMP 和 LNMP 代表支持 ZenTao 运行所对应的基础环境，具体参考[环境说明](../php)

#### 可否用云平台 RDS 作为 ZenTao 的数据库？

可以，修改 [ZenTao 配置文件](././#path) 即可

#### ZenTao 能在 Windows 服务器上运行吗？

可以，但是我们推荐在运行 ZenTao 效率更高的 Linux 服务器上运行

#### ZenTao 数据库连接配置信息在哪里？

数据库配置信息 [ZenTao 配置文件](././#path)中

#### 如果没有域名是否可以部署 ZenTao？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 phpMyAdmin，访问地址：http://服务器公网 IP:9090

#### 如何禁止 phpMyAdmin 访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改 ZenTao 的源码路径？

可以，通过修改 虚拟主机配置文件中相关参数

#### 如何修改上传的文件权限?

```shell
#ZenTao(LAMP)
chown -R apache.apache /data/wwwroot

#ZenTao(LNMP)
chown -R nginx.nginx /data/wwwroot

find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```
