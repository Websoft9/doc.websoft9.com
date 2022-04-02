---
sidebar_position: 3
slug: /mattermost/admin
tags:
  - Mattermost
  - 团队协作
  - 团队通讯
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### 备份与恢复

### 升级

## 故障速查

## 常见问题

### Mattermost 与 Slack 有什么区别？

参考官方文档 [Mattermost vs Slack](https://mattermost.com/mattermost-vs-slack/)

#### Mattermost Server, [Mattermost Team Edition](https://docs.mattermost.com/developer/manifesto.html?highlight=mattermost%20team%20edition) 和 Matttermost Enterprise Edition 有什么区别？

Mattermost Server 是它的产品的服务器端（后端）  
Mattermost Team Edition 是它的开源版本    
Matttermost Enterprise Edition 是它的企业版本  

目前官方提供了一致性的软件包下载，安装后默认就是 Enterprise Edition 的程序，但用户界面只有开源版的功能，如果需要企业版的功能，需要通过导入企业版秘钥实现升级。

#### Mattermost提供客户端吗？

提供，[下载地址](https://mattermost.com/download/#mattermostApps)

#### Mattermost提供CLI工具吗？

提供，参考[官网CLI文档](https://docs.mattermost.com/administration/command-line-tools.html#using-the-cli)

#### Mattermost支持多语言吗？

支持，[参考设置](../mattermost#setlang)

#### Mattermost数据库连接配置信息在哪里？

数据库配置信息在Mattermost安装目录下的config/config.json中，[查阅安装目录路径](../mattermost#path)

#### 如果没有域名是否可以部署 Mattermost？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？
密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP:9090

#### 如何禁止phpMyAdmin访问？

关闭服务器安全组的9090端口即可禁止

#### 是否可以修改Mattermost的源码路径？

可以，通过修改 [Nginx 虚拟主机配置文件](../Nginx#template)中相关参数

#### 如何修改上传的文件权限?

```shell
chown -R nginx.nginx /data/wwwroot
find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```
