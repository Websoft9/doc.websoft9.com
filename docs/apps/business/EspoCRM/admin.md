---
sidebar_position: 3
slug: /espocrm/admin
tags:
  - EspoCRM
  - CRM
  - 客户成功
---


# 维护指南

## 场景

### 备份与恢复

### 升级

## 故障速查

#### 网站显示重定向错误？

检查网站根目录下的 *.htaccess* 文件，分析其中的重定向规则，找到其中的死循环。

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看 MySQL 状态
sudo systemctl status mysql
sudo journalctl -u mysql
```

#### 数据库日志文件太大，导致磁盘空间不足？

默认安装，mysql会自动开启binlog，binlog是一个二进制格式的文件，用于记录用户对数据库**更新的****SQL语句****信息**，例如更改数据库表和更改内容的SQL语句都会记录到binlog里。

binlog主要用于出现没有备份的情况下，恢复数据库。但binlog会占用较大空间，长期不清理会让剩余磁盘空间为0，从而影响数据库或服务器无法启动

如果对自己的备份有信心，不需要binlog功能，参考如下步骤关闭之：

1. 编辑 [MySQL 配置文件](../mysql#path)，注释掉 binlog 日志
  ~~~
  #log-bin=mysql-bin  
  ~~~
2. 重启mysql
  ~~~
  systemctl restart mysqld
  ~~~

#### 重启 Apache 服务显示 *No spaces...*

出现此信息的时候，重启服务是成功的。

解决方案:

```
echo "fs.inotify.max_user_watches=262144" >> /etc/sysctl.conf 

sysctl -p
```

#### 运行命令 `httpd -t` 报错 [so:warn] [pid 14645] AH01574: module ssl_module is already loaded

问题原因：mod_ssl 重复加载  
解决方案：检查下面两个文件，找到 mod_ssl 字段，注释其中一个

  * /etc/httpd/conf.modules.d/00-base.conf
  * /etc/httpd/conf.modules.d/00-ssl.conf 

## 问题解答

#### 默认字符集是什么？
UTF-8

#### Apache工作模式有event,prefork,worker等，LAMP 默认是哪个？
prefork

#### 网站源码路径如何修改？

通过修改 [Apache 虚拟主机配置文件](../apache#virtualHost) 中相关路径参数

#### 如何删除9Panel?

删除 */data/apps/9panel* 下的所有数据即可，但需要保留文件夹

#### 通过 SFTP 上传网站源码后是否需要修改拥有者权限？

不需要，LAMP 会自动修正

#### 如何重置 php.ini 文件？

[下载 php.ini 模板](https://github.com/Websoft9/ansible-lamp/blob/master/roles/php/templates/php.ini) 后覆盖你服务器上的 */ect/php.ini*

#### 如何取消 Apache Test 页面？

使用 # 号将: */etc/httpd/conf.d/welcome.conf* 中的所有内容全部注释掉，然后重启 Apache 服务

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R apache.apache /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
#### 如何拒绝用户通过IP访问服务器？

参考 ：[HTTP 跳转到 HTTPS](../apache#denyip)

#### 如果设置 HTTP 跳转到 HTTPS？

参考 ：[HTTP 跳转到 HTTPS](../apache#httptohttps)

#### LAMP 是否安装了mod_php模块，Apache服务器怎么解析PHP文件？ 

LAMP 默认安装了mod_php模块，并且已经已经启用。Apache服务器通过php-fpm服务来解析PHP文件，如果想用mod_php解析PHP文件，请参照 [PHP文件解析方式变更](../apache#php)

#### LAMP 默认安装了哪些 Apache模块？ 

运行命令 `apachectl -M` 查看

#### LAMP 默认安装了哪些 PHP 模块？

运行命令 `php -m` 查看

#### 如何启用或禁用 Apache 模块？

以伪静态模块为例。打开 [Apache模块配置文件](../apache/advanced#moudlesconf)，找到 *LoadModule rewrite_module modules/mod_rewrite.so*，通过“#”作为注释来开启或禁用此模块

#### 没有域名是否可以通过 http://公网IP/mysite1 这样的方式访问网站？

可以。具体配置方法参考 [安装网站](../runtime/php#phpapps) 