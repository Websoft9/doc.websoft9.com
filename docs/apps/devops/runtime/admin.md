---
sidebar_position: 2
slug: /runtime/admin
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 常见问题

#### 默认字符集是什么？

UTF-8

#### Nginx 虚拟主机配置文件是什么？

虚拟主机配置文件是 Nginx 用于管理多个网站的**配置段集合**，路径为：*/etc/nginx/conf.d/default.conf*。  
每个配置段的形式为： `server{ }`，有多少个网站就有多少个配置段

#### 如何修改示例网站根目录？

修改 Nginx 虚拟主机配置文件 path 

#### 如果没有域名是否可以部署 Web 应用？

可以，访问`http://服务器公网IP:端口号` 即可

#### 数据库对应的账号密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 phpMyAdmin 和 adminMongo

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```

#### Web 应用环境是否支持部署多个网站？

支持。每增加一个网站，只需在**虚拟主机配置文件**中增加对应配置端。

#### 9Panel 是什么？

[9Panel](https://github.com/Websoft9/9panel)是 Websoft9 公司镜像的开源组件之一，支持中英文显示，部分镜像内置了9Panel. 它是集合数据库管理、文档和支持服务的引导页面，是镜像快速入门的向导工具。基于Bootstrap+vue.js开发，几乎不会占用系统资源，也不会对系统文件进行任何修改。

#### 如何删除9Panel?

删除 */data/apps/9panel* 下的所有数据即可，但需要保留文件夹

#### LEMP 与 LNMP 有何不同？

LEMP 就是 LNMP，是不同的用户采用的不同名称而已

#### LNMP 环境中默认有伪静态模板吗？

已经内置了部分常用网站的伪静态规则文件，进入目录可以查看
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/lnmp-multi/lnmp-rewrite-1-websoft9.png)

#### Python 应用环境中的框架安装方式？

采用虚拟环境安装


## 故障速查

#### 访问网站，页面显示 “没有权限...” ？

运行一条修改文件权限的命令
~~~
chown -R nginx.nginx /data/wwwroot
~~~

#### 修改 default.conf 后，Nginx 无法启动？

一般是 server{ } 中虚拟主机的目录位置不正确导致

#### 新增网站访问异常，且导致其他网站异常？

一般是 server{ } 中虚拟主机的目录位置不正确导致 Nginx 无法启动

#### 打开新增的网站，显示404错误？

一般是网站目录下没有 index.php 或 index.html 等默认首页导致

#### 新增网站 500 Internal Server Error？

程序代码错误，需要查看程序的日志文件

#### 打开新增的网站，显示404错误？

一般是网站目录下没有 index.php 或 index.html 等默认首页导致