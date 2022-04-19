---
sidebar_position: 2
slug: /administrator/migration_app
---

# 应用程序迁移


被迁移对象和目的地位置的组合，形成了多种多样的迁移场景。下面详细说明最常见的迁移场景：


### 数据库变更（容器环境）

如果用户不喜欢使用服务器上安装的 MariaDB/MySQL，而希望迁移到云数据库中（RDS），大致流程：

1. 备份已有数据库，并导入到 RDS 中

2. 修改 [应用容器配置文件:/data/wwwroot/appname/.env](#path) 中的数据库相关信息
   ```
   DB_MRAIADB_USER=root
   DB_MARIADB_PASSWORD=yourpassword
   DB_MARIADB_HOST=mariadb
   DB_MARIADB_PORT=3306
   DB_MARIADB_VERSION=10.6
   ```

   > DB_MARIADB_HOST 设置为外部数据库地址

3. 重新运行容器
   ```
   cd /data/wwwroot/erpnext
   docker-compose up -d
   ```

4. 测试更改数据库后的连接可用性

### 迁移网站源码（本地）

以将原目录 */data/wwwroot* 下的 **mysite1** 迁移到 */data2/wwwroot* 目标目录下为例，具体步骤如下：

1. 使用 WinSCP 连接服务器
2. 将 ***mysite1*** 文件夹整体拷贝到目标位置 */data2/wwwroot*
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-copysite1todata2-websoft9.png)
3. 修改vhost.conf 中 mysite1 这个网站对应的 VirtualHost 配置段 DocumentRoot, Directory 项的值
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-modifyvhostdata2-websoft9.png)

   原地址：/data/wwwroot/mysite1  
   目标地址：/data2/wwwroot/mysite1

4. 保存vhost.conf，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
      ~~~
      # 重启Apache服务命令
      systemctl restart httpd
      ~~~
5. 测试迁移后的结果，成功后可以删除原来的 *mysite1* 文件夹

### 迁移数据库文件（本地）

没有特殊情况，我们不建议迁移数据库文件到服务器上另外一个目录，毕竟主流的云厂商磁盘均可扩容。

如果要更改 [MySQL 数据库文件目录](/zh/stack-components.md#mysql)，请参考此处[ MySQL 专题文档](https://support.websoft9.com/docs/mysql/zh/solution-modifydatadir.html)

### 将/data目录迁移到数据盘（本地）

默认情况下 /data 是在系统盘的，当需要转移到数据盘，步骤如下:

1. 开始操作之前，**请务必做好数据备份**；
2. 提前购买数据盘，然后到云控制台将数据盘关联到云服务器
3. 连接服务器，将数据盘分区格式化
4. 在云服务器根目录下创建一个临时目录 temp 
5. 将数据盘挂载（mount）到:*/temp* 目录
4. 停止云服务器上的 Apache 和 MySQL 服务
    ~~~
    sudo systemctl stop httpd mysqld
    ~~~

5. 将当前 */data* 下所有文件拷贝到服务器临时文件夹 */temp*  中
    > 数据较大的话，拷贝可能会失败，此步骤具体问题需具体对待
6. 等待数据转移完成
7. 连接服务器，将数据盘再次挂载（mount）到:*/data* 目录 
8. 运行以下命令重新启动 Apache 和 MySQL:
   ```
   sudo systemctl start httpd mysqld
   ``` 
9. 测试迁移结果

> 数据盘格式化以及挂载（mount）操作非常复杂，需要有熟练的相关技能


### 迁移到外部服务器

网站从一台服务器（原服务器）迁移到另外一台服务器（目的服务器）是一个系统工程，基本步骤如下：

1. 通过云控制台，在目的服务器上[部署](/zh/stack-deployment.md)参数一致的 LAMP 镜像。
2. 通过 WinSCP 将原服务器上的网站源文件**下载**到本地电脑，然后再**上传**到目的服务器。
3. 通过 phpMyAdmin **导出**原服务器上的数据库，然后在目的服务器上**导入**数据库。
4. 把原服务器上的 vhost.conf 配置文件内容，完整拷贝到目的服务器的 vhost.conf 中，保存之。
5. 重启 Apache 服务。
5. 解析域名到目的服务器，等待域名解析生效。
5. 通过域名访问网站，测试可用性。
6. 正式发布。

如果一台服务器上有多个网站需要迁移，建议逐个迁移