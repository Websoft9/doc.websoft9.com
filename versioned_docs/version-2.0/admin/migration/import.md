---
sidebar_position: 1
slug: /migration-to-websoft9
---

# 迁移至 Websoft9

从传统的 LAMP, Java, Node 原生部署应用环境迁移至 Websoft9，并不会太困难。  

## 准备

1. 停止当前服务器的 HTTP 服务，确保 80,443,9000 [端口](./parameter#port)未被占用

2. 备份现有的 HTTP 虚拟主机配置，供迁移至 Websoft9 后使用

3. [安装](../install) Websoft9 到现有服务器

## 迁移

1. 进入 Websoft9 控制台，安装数据库管理工具和数据同步工具

2. 在 Websoft9 应用商店中安装匹配的应用

3. 使用工具将旧应用的数据库和数据文件迁移至 Websoft9 管理的应用中

4. 优化应用的 Proxy 

## 范例

#### 迁移 WordPress 至 Websoft9

本方案中假设 LAMP 环境运行一个 WordPress 网站，具体的迁移方案如下：

1. 停止并卸载 LAMP 已有的 HTTP 服务
   ```
   # for apt
   apt remove apache
   
   # for yum
   yum erase httpd
   ```

2. [安装](../install) Websoft9 到现有服务器

3. 在 Websoft9 应用商店中安装 WordPress 和 phpMyAdmin 两个应用，确保能正确运行

4. 使用 phpMyAdmin 连接 LAMP 环境中的 MySQL，导出 WordPress 的数据库

5. 在 Websoft9 控制台【我的应用】找到 WordPress

   - 在它的【数据库】标签页中获取数据库连接信息，然后使用 phpMyAdmin 导入上一步备份的数据
   - 在它的【卷存】标签页获取 WordPress 的数据路径，删除已有的 wp-content 文件夹
   - 在它的【访问】标签页绑定域名

6. 将 LAMP 环境中 WordPress 的 wp-content 文件夹整体拷贝新 WordPress 的卷存路径

7. 更改 wp-content 的文件夹权限至 0755

8. 迁移成功

#### 迁移数据库至 Websoft9

## 后续

完成应用迁移之后，可能还有一些后续的工作：

* 域名重新解析和绑定
* 文件（文件夹）权限修正




