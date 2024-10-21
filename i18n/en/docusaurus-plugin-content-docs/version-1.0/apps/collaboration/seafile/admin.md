---
sidebar_position: 3
slug: /seafile/admin
tags:
  - Seafile
  - File sync and share
  - knowledge Management
---

# Seafile Maintenance

This chapter is special guide for Seafile maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

## Troubleshoot{#troubleshoot}

In addition to the Jenkins issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### How can I use the logs?

You can find the keywords **Failed** or **error** from the logs directory: `/data/logs`  

You can also use docker command to check error logs: 
```
docker logs seafile
docker logs seafile-mysql
```

#### Seafile upload file error?

You should set the your correct Seafile host after deployment, otherwise you can't upload any files

   - SERVICE_URL：*http://Internet IP of Server*
   - FILE_SERVER_ROOT：*http:/Internet IP of Server/seafhttp*
   
   ![Seafile Host settings](https://libs.websoft9.com/Websoft9/DocsPicture/en/seafile/seafile-seturl-websoft9.png)
   
   
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

## FAQ{#faq}

#### Seafile support multi-language?

Yes, more than just Chinese and English

#### 为什么要推荐使用企业版 Seafile？

企业版用户拥有很多社区版没有的功能，如下：
![Seafile企业版社区版功能对比](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-compare-websoft9.png)

#### 如何购买 Seafile 企业版才有优惠？

通过 Websoft9 购买有优惠，欢迎[联系我们](../helpdesk)客户成功团队

#### 为什么采用 Docker 方式部署 Seafile？

官方推荐

#### How Seafile connect with MariaDB/MySQL?

Container internal connection, container orchestration

#### How can Seafile view & edit file online?

You should complete the [OnlyOffice setting](../owncloud/solution#onlyoffice) on your Nextcloud.

#### Seafile 支持手机客户端吗？

支持，[参考设置](../seafile#client)

#### Seafile 功能分类？

Seafile 是一款开源的企业网盘，作为企业网盘，主要用于网络存储和管理文件，以及文件共享和协同办公：

- 用户和分组管理，用于用户管理，和成员分组统一管理
- 文件和文件库管理，用于文件的管理和分类，并通过查看文件的历史信息了解文件的版本变更
- 共享与写作，用于将文件或文件库共享给个人或群组，实现协同办公

#### Is it possible to modify the source path of Seafile?

Yes, but you must migrate the data to new directory

#### 没有域名是否可以设置 Seafile HTTPS？

不可以，即如果 SEAFILE_SERVER_HOSTNAME 处设置为IP地址，会导致 Seafile 无法启动

#### 是否支持自己上传 ca 证书？

支持，具体参考[官方文档](https://manual-cn-origin.seafile.com/deploy/deploy_with_docker#xiang-lets-encrypt-shen-qing-ssl-zheng-shu)
