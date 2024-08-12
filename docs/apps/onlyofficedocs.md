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

### 验证安装{#wizard}

1. Websoft9 控制台安装 ONLYOFFICE Docs 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

2. 正常访问时，会出现 "ONLYOFFICE Docs Community Edition installed" 成功安装的提示页面

3. 运行提示页面的测试命令，测试可用性

### 与网盘系统集成

* [ownCloud 集成  ONLYOFFICE Docs](./owncloud#onlyoffice)
* [Nextcloud 集成  ONLYOFFICE Docs](./nextcloud#onlyoffice)
* [Seafile 集成  ONLYOFFICE Docs](./seafile#onlyoffice)

### 增加字体{#addfonts}

参考官方文档 [Adding fonts to ONLYOFFICE Docs](https://helpcenter.onlyoffice.com/installation/docs-community-install-fonts-linux.aspx)，并注意如下几点：

1. 需清空浏览器缓存或使用隐私模式打开新的浏览器页面，方可看到新增字体
2. Windows 系统上拷贝的 ttf 或 字体网上下载的 ttf 字体可能无法使用，导致增加字体没有效果

### 导出 PDF

集成到云盘软件后，打开文档，通过 ONLYOFFICE Docs  【文件】-【另存为】或【下载为】，将文件保存为 PDF 文件。

### 自签名配置 HTTPS

ONLYOFFICE Docs [自签名的证书](https://helpcenter.onlyoffice.com/installation/docs-community-install-docker.aspx) 配置如下：

1. ONLYOFFICE Docs 编排文件，为容器 443 端口映射到宿主机上（假设为：8089）

2. 进入 ONLYOFFICE Docs 容器，下载并运行创建证书的脚本
   ```
   wget -N -P /var/www/onlyoffice/Data https://websoft9.github.io/docker-library/apps/onlyofficedocs/src/createCA.sh
   bash /var/www/onlyoffice/Data/createCA.sh
   ```
3. 修改容器的配置文件
   ```
   sed -i 's/"rejectUnauthorized": true/"rejectUnauthorized": false/g' /etc/onlyoffice/documentserver/default.json
   supervisorctl restart all
   ```
4. 退出 ONLYOFFICE Docs 容器，重启通过 `http://URL:8089` 访问

## 企业版

### 为什么通过 Websoft9 购买？

Websoft9 是 ONLYOFFICE Docs [全球的合作伙伴](https://www.onlyoffice.com/search.aspx?search=websoft9)，中国的技术支持中心之一。 通过 Websoft9 采购，可以帮助用户：

- 采购收费版本，最少 10% 的折扣
- 更全面的产品支持，协助[提交工单](https://www.onlyoffice.com/support-contact-form.aspx)
- 与网盘、云存储等更多技术的集成技术解决方案 

### 同时连接数规则{#onlyofficedocsmaxconn}

ONLYOFFICE Docs 同时连接数是指：所有用户在同一时间以**编辑模式**下打开文档的中数量，超过此数量的连接以**预览模式**打开文档。

### 激活 License

将 License 文件放入 ONLYOFFICE Docs 卷存 **data** 目录中即可立即生效。  

## 配置选项{#configs}

 - [文件历史版本（多版本）](https://helpcenter.onlyoffice.com/onlyoffice-editors/onlyoffice-document-editor/HelpfulHints/VersionHistory.aspx)（√）："文件" > "版本历史"

 - 支持主流格式：docx、xlsx、pptx、odt、ods、odp、doc、xls、ppt、pdf、txt、rtf、html、epub、csv等

 - OnlyOffice的产品家族主要分为：

    * ENTERPRISE EDITION：企业版（收费）
    * COMMUNITY EDITION：开源版（完全免费）
    * DEVELOPER EDITION：开发者版本（收费）

- 授权访问控制（√）：用于第三方软件与 ONLYOFFICE Docs 的密码验证，确保 ONLYOFFICE Docs 在授权的情况下才可以被调用，支持 JWT 等协议。

## 管理维护{#administrator}

- **启用 JWT Key**：修改 ONLYOFFICE Docs 应用**编排文件**  `.env` 中 JWT_ENABLED=true 即可 

## 故障

#### 包含中文的 csv 文件打开乱码？

ONLYOFFICE 在打开 csv 文件时，会让客户选择字符编码和字段分隔符。下面的组合一般能解决乱码的问题：  

- 【GB2313】+【逗号】  

#### 开启 Debug 日志？ 

1. 进入容器修改 */etc/onlyoffice/documentserver/log4js/production.json* 文件，将  "level": "WARN" 更改为 "level": "DEBUG"
2. 运行 *supervisorctl restart all* 命令后生效。 
