---
sidebar_position: 3
slug: /canvas/admin
tags:
  - Canvas
  - 在线学习管理
---

# 维护指南

## 场景

### 备份与恢复

### 升级

Canvas升级有点小复杂，详情参考官方升级文档：[Upgrading Canvas](https://github.com/instructure/canvas-lms/wiki/Upgrading)

## 故障速查

#### 如何查看错误日志？

通过如下两种日志检索关键词 **Failed** 或者 **error** 查看错误

* Canvas 日志：`/data/wwwroot/canvas/log/production.log`
* Apache 日志：`/data/logs/apache`

#### Canvas服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
  df -lh

# 查看内存使用
  free -lh

# 查看服务状态和日志
  systemctl status apache
  journalctl -u apache
```

#### 403 访问权限错误？

需要确保 Canvas 根目录具有 canvas 和 www-data 两个用户的权限


#### 文件上传，不能下载

文件上传后，下载出现"无法访问网站 找不到canvas.example.com服务器IP地址 "
解决办法：
1. 找到apache配置文件/etc/apache2/conf.d/vhost.conf，将默认的ServerName canvas.example.com更改为 ServerName 实际部署站点域名

2. 找到域名配置文件/data/wwwroot/canvas/config/domain.yml，将 production 配置节点的 **domain** 项的值修改为你的域名


## 问题解答

#### Canvas 开源版是否提供移动端？

支持手机浏览器、Android 和 IOS 移动端。 详情参考：[mobile-guide](https://community.canvaslms.com/community/answers/guides/mobile-guide)

#### Canvas 支持中文吗

支持包括中文、英文等二十多种语言

#### Canvas 怎么安装插件？

参考: [安装插件](../canvas#plugin)

#### 是否可以通过命令行修改或重置 Canvas 管理员密码？

Canvas 官方没有提供。

#### 如果没有域名是否可以部署 Canvas？

可以，部署完成后通过：*http://公网IP* 访问即可

#### Canvas 官方云版本与 OpenSource 版本有区别吗？

有。具体参考 [code differences between the open source and hosted offerings](https://github.com/instructure/canvas-lms/wiki/FAQ#does-canvas-support-any-extensions)

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，参考[PostgreSQL管理](../postgresql)

#### 是否可以修改Canvas的源码路径？

可以，通过修改 Apache 虚拟主机[配置文件](../apache#virtualHost)实现

#### Canvas 根目录同时需要赋予用户 canvas 和 www-data （Apache用户）权限，是如何做到的？

拥有者是 canvas，同时通过 setfacl 额外给 www-data 赋予权限

```
  setfacl -m u:www-data:rx -R /data/wwwroot/canvas
```
#### 推荐一个国内学习 Canvas 的网站

小编认为[上海交通大学教育技术中心](https://v.sjtu.edu.cn/guide/)还不错
