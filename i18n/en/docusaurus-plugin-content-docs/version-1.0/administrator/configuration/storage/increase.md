---
sidebar_position: 5
slug: /administrator/storage_increase
---

# System disk expansion

系统盘容量不足的时候，可通过云控制台给系统盘扩容（增加更多的空间）。  

一般来说，云平台具备**系统盘自动扩容**能力，用户无需任何配置。  

但是，少数情况下，可能需要我们手动操作：

## 检查新增空间

运行 `df -Th` 命令检查新增磁盘空间是否需要手工扩容

## 扩容分区

1. 安装分区扩容软件 growpart

    ```
    yum install -y cloud-utils-growpart
    ```

2. 扩容分区（包含对应的文件系统）
    ```
    #1 扩容分区
    growpart /dev/vda 1

    #2 增大或收缩 ext2/ext3/ext4 文件系统
    resize2fs /dev/vda1  
    ```

