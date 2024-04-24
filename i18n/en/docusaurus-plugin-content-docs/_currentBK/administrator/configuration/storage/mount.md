---
sidebar_position: 4
slug: /administrator/storage_mount
---

# Mount data disk

用户在云平台购买数据盘并将其附加到指定的服务器之后，还需要下面的工作方可使用：

## 检查数据盘

运行 `lsblk -f` 命令检查数据盘是否已经被附件到服务器

```
$ lsblk -f

NAME    FSTYPE    LABEL        UUID                                    MOUNTPOINT
vda                                                                       
└─vda1 ext4     /     13843fcc-f592-4868-b87f-3784967cd0c4    1.8G    93% /
vdb
```

vdb 表示这是一个全新的磁盘，它还没有创建分区。  

## 创建分区

分区的有 GPT 和 MBR 等几种标准，推荐使用 GPT 分区方式：

1. 安装创建 GPT 类型分区所需的工具
    ```
    yum install -y parted e2fsprogs
    ```

2. 运行 `parted /dev/vdb` 命令进入工作状态，然后分别执行分区工作命令：

    - `mklabel gpt` 
    - `mkpart primary 1 100% ` 
    - `align-check optimal 1 `
    - `print `

    ```
    $ parted /dev/vdb
    GNU Parted 3.3
    Using /dev/vdb
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted) mklabel gpt                                                      
    (parted) mkpart primary 1 100%                                            
    (parted) align-check optimal 1                                            
    1 aligned
    (parted) print                                                            
    Model: Virtio Block Device (virtblk)
    Disk /dev/vdb: 21.5GB
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags: 

    Number  Start   End     Size    File system  Name     Flags
    1      1049kB  21.5GB  21.5GB               primary
    ```

3. 再次运行 `lsblk -f`，你会发现已经创建了一个 vdb1 的分区
    ```
    $ lsblk -f

    NAME    FSTYPE    LABEL        UUID                                    MOUNTPOINT
    vda                                                                       
    └─vda1 ext4     /     13843fcc-f592-4868-b87f-3784967cd0c4    1.8G    93% /
    vdb
    └─vdb1
    ```

## 创建文件系统（格式化）

给上面新建的分区创建文件系统，也就是格式化分区：

```
# 创建 ext4 分区（推荐）
mkfs -t ext4 /dev/vdb1

# 创建 xfs 分区
mkfs -t xfs /dev/vdb1
```

## 挂载点处理

经过上面的几个步骤之后，磁盘已经可用，但它还没有被挂载到 Linux 系统的文件管理体系中。

下面我们介绍持久化挂载方案（区别于 mount 命令的临时挂载）： 

1. Linux 上创建一个新文件夹
   ```
   mkdir /data2
   ```

1. 获取数据盘分区的 UUID

    ```
    $ blkid /dev/vdb1

    /dev/sda1: UUID="0935df16-40b0-4850-9d47-47cd2daf6e59" TYPE="ext4" PARTUUID="7125fcc698a-01"
    ```

2. 打开 */etc/fstab* 文件并为新的分区添加一行，注意 `<mount point>` 的值
    ```
    # <file system>           <mount point>     <type>  <options>   <dump>  <pass>
    UUID=0935df16-40b0-48      /data2           ext4    defaults    0       0    
    ```

3. 重启服务器后生效