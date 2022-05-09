---
sidebar_position: 1
slug: /administrator/migration_server
---

# Server Migration

The overall server migration is a migration requirement that remains unchanged from the entire virtual machine level. Generally, there are two situations as follows:  

## Migrate to another Region in same Cloud

Just need to create image for your Server and copy image to new region, then create new Server for it.  

## Migrate to another Cloud

Migrate to another Cloud need these steps:  

1. 针对目标云平台的要求，在待迁移的虚拟机上安装一系列所需的软件：Cloud-Init, virtio 驱动等
2. 基于虚拟机创建镜像
3. 将镜像导出为一个文件（格式：vhd, RAW 等）
2. 将导出的文件上传到目标云平台的对象存储空间中
3. 基于对象存储已上传的文件，创建云上的镜像
4. 基于云上的镜像创建虚拟机