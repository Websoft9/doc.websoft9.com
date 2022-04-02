---
sidebar_position: 3
slug: /rocketchat/admin
tags:
  - Rocket.Chat
  - 团队协作
  - 团队通讯
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### 备份与恢复

### 升级

[参考官方文档](https://docs.rocket.chat/quick-start/upgrading-rocket.chat)

## 故障速查

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Rocket.Chat服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
sudo systemctl status rocketchat
sudo journalctl -u rocketchat
```

## 常见问题

#### 如何以调试模式启动Rocket.Chat服务？

```
systemctl stop rocketchat
rocketchat-server console
```

#### 是否可以通过命令行修改Rocket.Chat后台密码？

可以，`rocketchatctl change_password  admin newpassword`

#### 如果没有域名是否可以部署 Rocket.Chat？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置adminMongo，访问地址：*http://服务器公网IP/9091*

#### 如何禁止外界访问adminMongo？

连接服务器，编辑 [adminMongo 配置文件](/zh/stack-components.md#adminMongo)，将其中的 `Require all granted` 更改为 `Require ip 192.160.1.0`，然后重启 Apache 服务

#### 是否可以修改Rocket.Chat的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R apache.apache /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```