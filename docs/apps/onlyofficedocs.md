---
title: ONLYOFFICE Docs
slug: /onlyofficedocs
tags:
  - Office
  - 文档编辑与预览
  - 在线办公
---

import Meta from './_include/onlyofficedocs.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 ONLYOFFICE Docs 后，通过【我的应用】进入它的编辑窗口，在**访问**标签页中获取登录地址和账号。  

本地浏览器访问成功，会看到 OnlyOffice Docs 运行成功的画面。如果页面打不开或报错，则表示运行异常。  
   ![ONLYOFFICE Document Server is running](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyoffice-dkisrunning-websoft9.png)


### 与网盘系统集成

* [ownCloud 集成  ONLYOFFICE Docs](./owncloud/solution#onlyoffice)
* [Nextcloud 集成  ONLYOFFICE Docs](./nextcloud/solution#onlyoffice)
* [Seafile 集成  ONLYOFFICE Docs](./seafile/solution#onlyoffice)
* [Official ONLYOFFICE Docs connector for Moodle](https://www.onlyoffice.com/blog/2022/03/official-connector-for-moodle/)


### 增加字体{#addfonts}

我们已经验证 ONLYOFFICE Docs 官方文档 [Adding fonts to ONLYOFFICE Docs](https://helpcenter.onlyoffice.com/installation/docs-community-install-fonts-linux.aspx) 是完全可以用的。

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyofficedocs-addfonts-websoft9.png)

同时，我们记录了如下的事项供您参考：

1. 需清空浏览器缓存或使用隐私模式打开新的浏览器页面，方可看到新增字体
2. Windows 系统上拷贝的 ttf 字体是可用的
3. 网上下载的 ttf 字体是可用的

### 多版本

ONLYOFFICE Docs 默认设置是支持[多版本](https://helpcenter.onlyoffice.com/onlyoffice-editors/onlyoffice-document-editor/HelpfulHints/VersionHistory.aspx)的，可以通过：【文件】>【版本历史】进行查看。  

下面是 ownCloud 下打开文档后，ONLYOFFICE Docs 多版本的查看结果：  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/onlyoffice/onlyofficedocs-docsversions-websoft9.png)

### 导出 PDF

集成到云盘软件后，打开文档，通过 ONLYOFFICE Docs  【文件】-【另存为】或【下载为】，将文件保存为 PDF 文件。

## 企业版

### 为什么通过 Websoft9 购买？

Websoft9 是 ONLYOFFICE Docs 全球的合作伙伴，中国的技术支持中心之一。 通过 Websoft9 采购，可以帮助用户：

- 采购收费版本，最少 10% 的折扣
- 更全面的产品支持
- 与网盘、云存储等更多技术的集成技术解决方案 

### 同时连接数规则{#onlyofficedocsmaxconn}

ONLYOFFICE Docs 同时连接数是指用户在编辑模式下打开文档的数量。  
例如，对于具有200个同时连接的许可证，一个用户可以打开200个文档，200个用户每个可以打开一个，50个用户每个可以打开4个文档等。  
以何种方式并不重要，但文档服务器只会根据您购买的许可证处理编辑请求的数量。  
超过此数量的连接以预览模式打开文档。


## 配置选项{#configs}

 - 支持主流格式：docx、xlsx、pptx、odt、ods、odp、doc、xls、ppt、pdf、txt、rtf、html、epub、csv等
 - OnlyOffice的产品家族主要分为：
    * ENTERPRISE EDITION：企业版（收费）
    * COMMUNITY EDITION：开源版（完全免费）
    * DEVELOPER EDITION：开发者版本（收费）
- 授权访问控制（√）

## 管理维护{#administrator}

#### 启用 JWT Key

JWT Key 用于第三方软件与 ONLYOFFICE Docs 的密码验证，确保 ONLYOFFICE Docs 在授权的情况下才可以被调用。

只需修改 ONLYOFFICE Docs  根目录下的 `.env` 中 JWT_ENABLED=true 即可。  

```
# [true, false]
JWT_ENABLED=false
JWT_SECRET=sBPF1mjEbQ2bzj31entX
JWT_HEADER=Authorization
JWT_IN_BODY=false
```

#### 自签名配置 HTTPS

除通过网关转发配置之外，ONLYOFFICE Docs 提供了[自签名的 HTTPS](https://helpcenter.onlyoffice.com/installation/docs-community-install-docker.aspx) 方案：

1. ONLYOFFICE Docs 容器新增 443 端口，映射到宿主机

2. 进入 ONLYOFFICE Docs 容器，下载并运行创建证书的脚本
   ```
   wget -N -P /var/www/onlyoffice/Data https://websoft9.github.io/docker-library/apps/onlyofficedocs/src/createCA.sh
   bash /var/www/onlyoffice/Data/createCA.sh
   ```
3. Modify the container configuration file
   ```
   sed -i 's/"rejectUnauthorized": true/"rejectUnauthorized": false/g' /etc/onlyoffice/documentserver/default.json
   supervisorctl restart all
   ```
4. 退出 ONLYOFFICE Docs 容器，重启后生效

## 故障

#### 包含中文的 csv 文件打开乱码？

ONLYOFFICE 在打开 csv 文件时，会让客户选择字符编码和字段分隔符。下面的组合一般能解决乱码的问题：  

- 【GB2313】+【逗号】  

#### 开启 Debug 日志？ 

1. 进入容器修改 */etc/onlyoffice/documentserver/log4js/production.json* 文件，将  "level": "WARN" 更改为 "level": "DEBUG"
2. 运行 *supervisorctl restart all* 命令后生效。 
