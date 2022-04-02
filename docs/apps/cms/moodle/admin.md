---
sidebar_position: 3
slug: /moodle/admin
tags:
  - Moodle
  - 在线学习管理
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### 在线备份

课程是 Moodle 最重要的资源，Moodle 后台提供了自动备份课程的功能

1. 以管理员身份登录 Moodle 后台

2. 依次打开：【网站管理】>【课程】>【备份】，开始进行备份设置
  ![Moodle 课程备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-coursebk-websoft9.png)

3. 详细设置请自行研究

4. 依次打开：【网站管理】>【报表】>【备份】，查看备份执行情况
  ![Moodle 查看备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-coursebkrp-websoft9.png)

### 命令行升级

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


#### Moodle 开源版提供 APP？

有待进一步调查

#### Moodle 能上传多媒体文件吗？

可以

#### Moodle 旗下有哪些产品？

* Moodle LMS：开源的在线学习系统
* Moodle Workplace：Moodle LMS + 高级功能，不开源
* MoodleCloud：Moodle LMS 托管服务，即 SaaS 版
* Moodle App：移动端
* MoodleNet：共享和管理开放教育资源