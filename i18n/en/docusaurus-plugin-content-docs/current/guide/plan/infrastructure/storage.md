---
sidebar_position: 1.2
slug: /storage
---

# 扩充或优化存储

在本章中，你可以了解到与应用存储空间有关的各种配置：  

## 扩容系统盘{#system-disk}

大多少公有云都具备**购买即自动扩容**能力，用户无需任何多余配置。  

而私有云下，可能需要手动操作：

1. 运行 `df -Th` 命令检查磁盘状态
2. 使用 growpart, GParted, fdisk, lvm, gdisk, lsblk, parted 等软件调整分区
3. 使用 resize2fs 增大或收缩 ext2/ext3/ext4 文件系统

## 附加数据磁盘{#data-disk}

Websoft9 多应用托管平台由于运行的应用较多，用户可能需要增加数据盘以扩展存储。

增加数据磁盘的主要步骤：

* 购买数据磁盘
* 磁盘分区与初始化
* 磁盘设置为系统的挂载点

下面是一个附件数据盘的完整范例：  

1. 在物理层面将数据盘附件到指定的服务器，运行 `lsblk -f` 命令检查是否附加成功（体现为 vdb 磁盘）

2. 使用 parted 等工具为磁盘创建分区（GPT 或 MBR），运行 `lsblk -f` 命令检查

   ```
   #1 Install tools
   yum install -y parted e2fsprogs

   #2 Start parting
   parted /dev/vdb
   ```

3. 为分区创建文件系统（格式化）
    ```
    # 创建 ext4 分区（推荐）
    mkfs -t ext4 /dev/vdb1

    # 创建 xfs 分区
    mkfs -t xfs /dev/vdb1
    ```
4. 为文件系统创建挂载点，使它纳入 Linux 文件系统的管辖中

   ```
   #1 Create directory
   mkdir /data2

   #2 Get the UUID
   blkid /dev/vdb1

   #3 Add a permanent mount point
   echo '/dev/sda1: UUID="uuid_value" TYPE="ext4" PARTUUID="7125fcc698a-01"' > /etc/fstab

   #3 Or add a temp mount point
   mount /dev/sda1 /data2
   ```

## 附加网络磁盘{#outer-disk}

网络磁盘也称为外部存储，它位于服务器之外，是区别于服务器磁盘的一种第三方存储服务（例如：对象存储）。    

Websoft9 建议您使用 [Rclone](https://rclone.org/commands/rclone_mount/) 将外部云存储挂载为网络磁盘。  

## 优化容器数据卷{#volume}

Docker [Volume](https://docs.docker.com/storage/volumes/) 是容器生成和使用的数据的首选机制，优化的场景：

- [Named Volumes](https://docs.docker.com/storage/volumes/) vs [Bind Mounts](https://docs.docker.com/storage/bind-mounts/) 
- [更改默认存储卷位置](./docker-server#changepath)

Websoft9 考虑数据权限和双向同步，使用 Named Volumes 作为应用的默认存储方式。  
