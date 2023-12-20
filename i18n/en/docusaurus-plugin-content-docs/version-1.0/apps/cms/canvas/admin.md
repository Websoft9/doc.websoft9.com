---
sidebar_position: 3
slug: /canvas/admin
tags:
  - Canvas
  - elearning
---

# Canvas Maintenance

This chapter is special guide for Canvas maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore
   
### Upgrade

Refer to the official docs: [Upgrading Canvas](https://github.com/instructure/canvas-lms/wiki/Upgrading)


## Troubleshoot{#troubleshoot}

In addition to the Canvas issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more. 

#### How can I use the logs?

You can find the keywords **Failed** or **error** from the these logs

* Canvas log: `/data/wwwroot/canvas/log/production.log`
* Apache log: `/data/logs/apache`

#### 403 error?

You should make sure user **canvas** and **www-data** haver permission of DIR */data/wwwroot/canvas*

#### 文件上传，不能下载

现象描述：文件上传后，下载出现"无法访问网站 找不到canvas.example.com服务器IP地址 "
解决办法：

1. 找到 [Apache 虚拟主机配置文件](../administrator/parameter)，将 ServerName 值修改为实际域名
2. 找到 [Canvas 域名配置文件](../canvas#path)，将 production 配置节点的 **domain** 值修改为实际域名

## FAQ{#faq}

#### Can Canvas open source support mobile?

Yes, refer to: [mobile-guide](https://community.canvaslms.com/community/answers/guides/mobile-guide)

#### Canvas multi-languages?

Yes

#### Canvas 怎么安装插件？

参考: [安装插件](../canvas#plugin)

#### Can I reset administrator password of Canvas by command?

No

#### Canvas hosted offering vs OpenSource?

Refer to: [code differences between the open source and hosted offerings](https://github.com/instructure/canvas-lms/wiki/FAQ#does-canvas-support-any-extensions)

#### Canvas 根目录需 canvas 和 apache 权限？

是的。拥有者是 canvas，同时通过 setfacl 额外给 www-data 赋予权限

```
setfacl -m u:www-data:rx -R /data/wwwroot/canvas
```
