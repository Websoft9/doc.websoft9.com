---
sidebar_position: 2
slug: /migration/app
---

# 应用程序迁移

应用程序迁移是常见的场景，Websoft9 支持各种迁入和迁出场景

## 准备

迁移应用需做好如下准备：

- 稳妥的备份
- 域名变更
- 各种可用的账号

## 场景

应用迁移涉及如下几个不同的场景：  

### 应用在多个 Websoft9 中迁移

**应用复制** 功能解决这个问题，规划中...

### 应用迁入至 Websoft9

参考：[迁移至 Websoft9](./onboard)

### 应用从 Websoft9 中迁出

Websoft9 应用都是 Docker 容器形式存在，因此很方便使用 Docker 的原生迁移方案。  

其原理：将容器备份为镜像 > 镜像转成 tar 包 > tar 包复原成镜像

```
# 创建镜像
sudo docker commit appname image_name

# 导出镜像为 tar 包
sudo docker save image_name > image_name.tar

# 重载 tar 包为镜像
sudo docker load < image-name.tar
```

## 后续

完成应用迁移之后，可能还有一些后续的工作：

* 域名重新解析和绑定
* 文件（文件夹）权限修正

