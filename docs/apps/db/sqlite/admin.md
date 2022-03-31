---
sidebar_position: 3
slug: /sqlite/admin
tags:
  - SQLite
  - DevOps
---

# 维护指南

## 场景

### SQLite 备份

通过 SFTP 将 SQLite 数据库文件（一般以 .db 结尾）下载到本地

### SQLite 升级

如果系统仓库中的 SQLite 版本比较低，又想升级到指定的版本，可以参考如下教程： 

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 找到所需 SQLite 目标版本的[下载地址](https://www.sqlite.org/chronology.html)

2. 分别运行如下的升级命令
   ```
   # 下载 SQLite 源码（自行替换）
   wget https://www.sqlite.org/2019/sqlite-autoconf-3290000.tar.gz

   # 编译
   tar zxvf sqlite-autoconf-3290000.tar.gz 
   cd sqlite-autoconf-3290000/
   ./configure --prefix=/usr/local
   make && make install
   
   # 替换旧版本
   mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
   ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
   echo "/usr/local/lib" > /etc/ld.so.conf.d/sqlite3.conf
   ldconfig
   sqlite3 -version
   ```

## 故障速查

除以下列出的 SQLite 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### CloudBeaver 无法连接 SQLite 数据库？

确保 SQLite 数据库文件存放在： */data/apps/cloudbeaver/volumes* 目录下，如果不在此目录，CloudBeaver 便无法管理。

## 问题解答

#### SQLite 是否支持用户名和密码验证？

不支持

#### 本项目中 SQLite 采用何种安装方式？

采用编译安装

#### CloudBeaver 是如何连接 SQLite 的？

SQLite 数据库文件存放在 */data/apps/cloudbeaver/volumes* 目录下，CloudBeaver 便可管理到它们。

#### SQLite 有系统服务吗？

没有