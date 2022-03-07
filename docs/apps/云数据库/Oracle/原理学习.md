---
sidebar_position: 3
slug: /oracle/study
tags:
  - Oracle Database
  - Cloude Native Database
---

# 原理学习

Oracle Database 11*g* 快捷版 ([Oracle Database XE](http://www.oracle.com/technetwork/cn/database/database-technologies/express-edition/index.html)) 是一款基于 Oracle Database 11*g* 第 2 版代码库的小型入门级数据库，它具备以下优点：免费开发、部署和分发；下载速度快；并且管理简单。Oracle Database XE 是一款优秀的入门级数据库，可供以下用户使用:

*   致力于 PHP、Java、.NET、XML 和开源应用程序的开发人员
*   需要免费的入门级数据库进行培训和部署的 DBA
*   需要入门级数据库进行免费分发的独立软件供应商 (ISV) 和硬件供应商
*   需要在课程中使用免费数据库的教育机构和学生
* 
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/oracle_database/oracle-database-1024x410.jpg)

现在，利用 Oracle Database XE，您可以使用强大的、公认的、行业领先的基础架构来开发和部署应用程序，然后在必要时进行升级而不必进行昂贵和复杂的迁移。Oracle Database XE 对安装主机的规模和 CPU 数量不作限制（每台计算机一个数据库），但 XE 将最多存储 11GB 的用户数据，最多使用 1GB 内存，使用主机上的一个 CPU。版权说明：在使用软件之前，建议阅读[ Oracle Database 快捷版 11*g* 第 2 版的 OTN 许可协议](http://www.oracle.com/technetwork/licenses/database-11g-express-license-459621.html)


## Oracle Database 11g EX官方资源

*   [产品官方首页](http://www.oracle.com/technetwork/cn/database/database-technologies/express-edition/index.html)
*   [联机文档](http://download.oracle.com/docs/cd/E17781_01/index.htm)
*   [快捷版论坛](https://forums.oracle.com/forums/forum.jspa?forumID=251&start=0)

## Oracle常见命令

>启动数据库服务
service start oracle
>查看监听状态
在Oracle用户下执行：lsnrctl status
然后使用Oracle工具连接数据库。
>关闭数据库和监听
service stop oracle