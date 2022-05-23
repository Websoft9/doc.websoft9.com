---
sidebar_position: 3
slug: /seafile/admin
tags:
  - Seafile
  - 网盘
  - 知识管理
  - 团队协作
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

## 故障排除

#### Seafile 无法上传文件？

设置 Seafile 的主机地址（**必选项，否则无法使用文件上传功能**）

   - SERVICE_URL：*http://服务器公网IP*
   - FILE_SERVER_ROOT：*http://服务器公网IP/seafhttp*

   ![Seafile后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)
   
   
#### 完成文档服务器配置，Seafile 仍然无法编辑和预览文件？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-canotaccess-websoft9.png)  

问题原因：SERVICE_URL 与实际不符  
解决方案：需登录控制台的系统设置，修改 SERVICE_URL 为实际值

#### 完成 ONLYOFFICE Docs 配置，Seafile 编辑和预览显示错误 “文档安全令牌未正确形成”？

问题原因：ONLYOFFICE docs 安全设置过高   
解决方案：需修改 ONLYOFFICE docs 编排文件中的环境变量 JWT_ENABLED，设置为 false  

```
  onlyoffice-document-server:
    container_name: onlyoffice-docs
    image: onlyoffice/documentserver:6.0.2
    stdin_open: true
    tty: true
    restart: always
    environment:
     - JWT_ENABLED=flase
```

## 常见问题

#### Seafile 支持多语言吗？

支持多种语言（中文，英文等）

#### 为什么要推荐使用企业版 Seafile？

企业版用户拥有很多社区版没有的功能，如下：
![Seafile企业版社区版功能对比](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-compare-websoft9.png)

#### 如何购买 Seafile 企业版才有优惠？

通过 Websoft9 购买有优惠，欢迎[联系我们](../helpdesk)客户成功团队

#### 为什么采用 Docker 方式部署 Seafile？

官方推荐

#### Seafile 是如何与 MySQL 连接的？

容器内部连接，即容器编排

#### Seafile 默认能否对文档进行预览和编辑？

支持，如果不能预览，请参考[Office设置](../seafile/solution#onlyoffice)

#### Seafile 支持手机客户端吗？

支持，[参考设置](../seafile#client)

#### Seafile 功能分类？

Seafile 是一款开源的企业网盘，作为企业网盘，主要用于网络存储和管理文件，以及文件共享和协同办公：

- 用户和分组管理，用于用户管理，和成员分组统一管理
- 文件和文件库管理，用于文件的管理和分类，并通过查看文件的历史信息了解文件的版本变更
- 共享与写作，用于将文件或文件库共享给个人或群组，实现协同办公

#### 是否可以修改 Seafile 的数据路径？

可以，但需要对历史数据进行迁移

#### 没有域名是否可以设置 Seafile HTTPS？

不可以，即如果 SEAFILE_SERVER_HOSTNAME 处设置为IP地址，会导致 Seafile 无法启动

#### 是否支持自己上传 ca 证书？

支持，具体参考[官方文档](https://manual-cn-origin.seafile.com/deploy/deploy_with_docker#xiang-lets-encrypt-shen-qing-ssl-zheng-shu)
