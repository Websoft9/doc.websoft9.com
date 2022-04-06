---
sidebar_position: 3
slug: /metabase/admin
tags:
  - Metabase
  - 大数据分析
  - BI
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### Metabase 升级

Metabase 有升级包的时候，后台会及时给出提示。参考下面的步骤完成升级：

1. Metabase 后台->设置->升级，如果有新的升级包，系统会给与提示
   ![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereminder-websoft9.png)

2. 点击“更新”按钮后，系统会跳转到 Metabase 官方的安装页面。
3. 我们提供的部署包采用的是 jar 包安装模式，因此在安装页面我们选择“Custom install”模式，
   ![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatedl-websoft9.png)

4. 下载 Metabase.jar 包后，上传到服务器 `/data/wwwroot/metabase`, 覆盖已有的同名文件
   ![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereplace-websoft9.png)

5. 重新加载 Metabase，升级成功

## 故障速查

除以下列出的 Metabase 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。

## 问题解答

#### Metabase 支持多语言吗？

支持多语言（包含中文），系统默认根据浏览器自动选择语言