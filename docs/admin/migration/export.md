---
sidebar_position: 2
slug: /migration-from-websoft9
---

# 从 Websoft9 迁出

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