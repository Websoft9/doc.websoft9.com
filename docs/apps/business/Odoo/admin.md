---
sidebar_position: 3
slug: /odoo/admin
tags:
  - Odoo
  - 企业管理
  - ERP
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### 备份与恢复

### 升级

Odoo 后台提供了在线升级能力，让升级工作变得非常简单。参考下面的步骤完成升级：

1. 登录 Odoo 后台，[启动开发者模式](../odoo#dev-mode)
2. 通过 【Settings】>【Updates】开始更新 Odoo 主程序
   ![Odoo升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-upgradesui-websoft9.png)
3. 升级成功会有 “Well done...” 的提示
4. 点击 【Update Apps list】，开始更新 Odoo 模块

更多更新方案和注意事项请参考官方文档：[Odoo Update](https://www.odoo.com/documentation/master/setup/update.html)


## 故障速查

#### 如何查看错误日志？

最简单的方式是通过SSH连接服务器，运行`odoo`这个命令，就会显示错误日志以及Odoo的运行情况

#### 恢复数据库、上传附件等操作，出现 “413 Request Entity Too Large” 错误？{#attachment}

这是由于 Nginx 默认安装下，上传文件最大为 1M，因此需要修改 Nginx 这个限制：
1. 使用 WinSCP 远程连接服务器
2. 编辑 [Nginx 虚拟机主机配置文件](../nginx#virtualHosx)
3. 插入一行 `client_max_body_size 0;` 解除上传文件限制的配置项
   ```
   server {
    listen 80;
    server_name _;
    client_max_body_size 0; #解除上传文件限制
    ...
   ```
4. 保存并[重启 Nginx 服务](../setup/parameter#service)

#### 访问Odoo总是出现数据库设置提醒？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-setpasswodrem-websoft9.png)

这个提醒的是要求你尽快给数据库设置一个高强度的管理员密码，如果不设置将面临很大的风险。一旦设置后，此界面就不会再弹出了

#### 无法通过 SFTP 上传文件到Odoo程序目录问题

由于部分 Ubuntu系统 默认创建了默认用户名 ubuntu ,ubuntu为普通用户没有对odoo程序的源码或目录有操作的权限,需要执行一下命令:

```
sudo chmod o+rw  /usr/lib/python2.x/dist-packages/odoo   # odoo10版本
sudo chmod o+rw  /usr/lib/python3/dist-packages/odoo   # odoo11版本以上
```

#### PDF无法打印中文

Odoo11之前的版本，在使用Odoo打印功能时，下载的PDF文件只有英文，没有中文，导致打印不完整。

**问题原因**：系统环境里没有下载所需的中文字体

**解决方案**：执行以下命令下载字体

~~~
sudo apt-get install ttf-wqy-zenhei
sudo apt-get install ttf-wqy-microhei
~~~

#### Odoo 备份出现 Command pg_dump not found

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-backuperror-websoft9.png)

原因：PostgreSQL的备份命令没有找到
解决方案：需要进一步查看PostgreSQL安装问题，还是Odoo本身的问题

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```



## 问题解答

#### Odoo支持多语言吗？

支持多语言（包含中文），参考：[语言设置](../odoo#setlang)

#### Odoo数据库连接配置信息在哪里？

Odoo 采用 [Peer Authentication](https://www.postgresql.org/docs/10/auth-methods.html#AUTH-PEER) 方式连接 PostgreSQL，即以操作系统用户登录数据库，无需密码。

#### 为什么在设置面板看不到 Odoo 更新（Updates）操作功能？

此功能只能在开发者模式下使用，请确保你的 Odoo 控制台是否已经切换成[开发者管理模式](../odoo#dev-mode)

#### 如何删除 Odoo 演示数据？

由于 Odoo 支持多企业组织方式，建议新增一个企业组织（不要勾选演示数据）后，再删除带演示的数据库。具体操作方式参考：[ Odoo 数据库管理](../odoo#dbadmin)

#### Odoo 是否可以导出 PDF 文件？

可以。安装 Invoice, Purchase 等模块可以测试 print to PDF 功能
![Odoo 打印PDF](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-printtopdf-websoft9.png)

#### 如果没有域名是否可以部署 Odoo？

可以，访问`http://服务器公网IP` 即可

#### Windows 版的 Odoo 的 PostgreSQL 用户对应的密码是多少？

请在[账号密码](/zh/stack-components.md#postgresql)章节查看

#### 是否有可视化的数据库管理工具？

请直接通过 [Odoo 自带的数据库管理工具](../odoo#pgadmin)操作

#### 是否可以修改Odoo的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
chown -R nginx.nginx /data/wwwroot/
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
