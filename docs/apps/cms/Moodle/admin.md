---
sidebar_position: 3
slug: /moodle/admin
tags:
  - Moodle
  - 在线学习管理
---

# 维护指南

## 场景

### 备份与恢复

课程是 Moodle 最重要的资源，Moodle 后台提供了自动备份课程的功能

1. 以管理员身份登录 Moodle 后台

2. 依次打开：【网站管理】>【课程】>【备份】，开始进行备份设置
  ![Moodle 课程备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-coursebk-websoft9.png)

3. 详细设置请自行研究

4. 依次打开：【网站管理】>【报表】>【备份】，查看备份执行情况
  ![Moodle 查看备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-coursebkrp-websoft9.png)

### 升级

Moodle 官方提供了多种升级方式（[Moodle Upgrading](https://docs.moodle.org/37/en/Upgrading)），包括上传代码升级和命令升级等方式。  

下面我们以命令行升级方式为例，介绍升级的大致方案：

1. 提前做好代码和数据库备份

2. 使用 SSH 远程登录到 Moodle 服务器，运行如下的命令开始升级：
   ```
   cd /data/wwwroot/moodle/admin/cli
   php upgrade.php
   ```

3. 等待升级完成

## 故障速查

除以下列出的 Moodle 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 


## 问题解答

#### Moodle 支持多语言吗？

支持多语言（包含中文），后台可以设置语言

#### Moodle 支持在线安装插件吗？

支持，类似 Wordpress 在线安装插件，不过 Moodle 需要提前到官方注册一个账号

#### Moodle 能上传多媒体文件吗？

可以

#### Moodle(LAMP)，Moodle(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持Moodle运行所对应的基础环境，具体参考[环境说明](../moodle#ref)

#### 是否可以使用云平台的 RDS 作为 Moodle 的数据库？

可以，修改 Moodle 根目录下的配置文件 `config.php` 即可

#### Moodle能在Windows服务器上运行吗？

可以，但是我们推荐在运行 Moodle 效率更高的 Linux 服务器上运行

#### Moodle数据库连接配置信息在哪里？

数据库配置信息在Moodle安装目录下的 *config.php* 中，[查阅安装目录路径](../moodle#path)

#### 如果没有域名是否可以部署 Moodle？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP/phpmyadmin

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 是否可以修改Moodle的源码路径？

可以，通过修改 [虚拟主机配置文件](../apache#virtualHost)中相关参数