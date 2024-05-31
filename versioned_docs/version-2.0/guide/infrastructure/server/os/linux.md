---
sidebar_position: 1
slug: /linux
---

# Linux

本章介绍使用 Websoft9 托管应用过程中，可能需要的 Linux 相关操作。   

## 指南

### 系统账号{#osaccount}

不同的云平台操作系统账号是不一样的，有的云平台可以在创建服务器时自定义用户名称，有的是固定用户名`root`。

具体参考下面的表格：  

   |  云平台   |  管理员账号   | 其他|
   | --- | --- | --- |
   |  Azure   |  创建服务器的时候自行设置   | [如何开启root账户？](./azure#enableroot) |
   |  AWS   |  AmazonLinux:ec2  CentOS:centos  Ubuntu:ubuntu  Debian:admin   | [如何开启root账户？](./aws#enableroot)|
   |  阿里云，华为云，腾讯云   |  除腾讯云 Ubuntu 之外(ubuntu)，其他平台任何系统默认账号都是 root  | |

### 连接 Linux{#connect}

常见 Linux 连接方式包括：

* SSH 和 SFTP 连接系统
* RDP和 VNC 连接桌面

连接的工具有两种类型：

- 本地电脑客户端，例如：Terminus, WinSCP, Putty, Xshell, Tabby, MobaXterm 等
- 在线 Web 客户端：云平台和 Websoft9 控制台均提供的 Web 版在线连接工具  


### 增设数据磁盘

Websoft9 多应用托管平台由于运行的应用较多，用户可能需要增加数据盘以扩展存储。

增加数据磁盘的主要步骤：

* 购买数据磁盘
* 磁盘分区与初始化
* 磁盘设置为系统的挂载点


### 使用 Linux 桌面

阅读：[系统托管--Linux 桌面](./desktop)

### 编码与字体设置

编码与字符虽然看似与语言文字有关系，但它们的本质是不一样的：

- 编码是计算机存储各种文字的格式（UTF8，Unicode等），是面向机器的设计形式
- 字体是计算机将字符显示出来的格式（中文黑体、 Google Fonts），是面向人类的设计形式

查看与设置编码的方法如下：

1. 在系统中运行 `locale` 命令，查看当前已支持的字符编码

2. 运行下面的命令之一，临时切换默认字符编码
   ```
   LANG="zh_CN.UTF-8"
   ```
3. 或修改 /etc/locale.conf 文件，永久性修改字符编码

安装与查看字体的方法如下：

1. 在系统中运行 `fc-list` 命令，查询已安装的字体

2. 运行 `yum groupinstall "fonts"`，装“fonts”这个包含大量字体的软件包组

### 磁盘与文件系统

- 运行 `lsblk` 查看外设和磁盘分区，Linux 支持的外设：IDE, SATA, USB, SCSI 等
- 运行 `fdisk -l`查看分区容量
- 运行 `df -T` 查看文件系统，Linux 支持的文件系统类型：Btrfs、JFS、ReiserFS、ext、ext2、ext3、ext4、ISO9660、XFS、Minx、MSDOS、UMSDOS、VFAT、NTFS、HPFS、NFS、SMB、SysV、PROC 等。
- 常见的分区工具：fdisk, lvm, gdisk, lsblk, parted

### 软件仓库

Linux 操作系统都提供了一个集中的软件包管理机制--软件仓库。 

Linux 软件包由：共享库、应用程序（二进制）、服务和文档组成及其所需的依赖列表。

![](./assets/linux-rpms-websoft9.png)

下面我们列出全球比较流行的仓库：

- [Linux Packages](https://linux-packages.com)：软件包的汇聚仓库，包括 Ubuntu、Centos、Arch、Debian
- [Software Collections - scl](https://www.softwarecollections.org/en/)：软件包的汇聚仓库，包括 Ubuntu、Centos、Arch、Debian
- [Ubuntu Packages](https://packages.ubuntu.com)：Ubuntu 官方仓库
- [RPM Fusion](https://rpmfusion.org)：Fedora Project or Red Hat 额外的包
- [EPEL](https://fedoraproject.org/wiki/EPEL)：由 Fedora Special Interest Group 维护的 Enterprise Linux（RHEL、CentOS）中经常用到的包
- [RepoForge](http://repoforge.org)：RHEL 系统下的软件仓库
- [PackMan](http://packman.links2linux.org)：OpenSUSE 最大的第三方软件源
- [Remi](https://www.remi.com)：PHP 仓库
- [Gentoo portage](https://www.gentoo.org)：Gentoo Portage 软件源
- [Fedora copr](https://copr.fedorainfracloud.org/)：Fedora 软件源
- [Ubuntu Ports](http://ports.ubuntu.com)：Arm64/Armhf 等平台的 Ubuntu 软件仓库
- [Centos altarch](http://mirror.centos.org/altarch)： CentOS 额外的包
- [IUS](https://ius.io)： RPM 上游软件包
- [ATOMIC](http://www.atomicorp.com/channels/atomic)： CentOS 额外的包
- [Centos altarch](http://mirror.centos.org/altarch)： Atomic RPM 包

### 时间设置

使用 `timedatectl`，您可以设置系统时间、日期和时区

```
# 设置时间
sudo timedatectl set-time '2024-04-22 15:30:00'

# 查询时间
timedatectl status
```

### 增加用户

- adduser 用于创建 Linux 系统账号，创建过程中会提示：用户名/密码，同时会创建用户家目录
- useradd 仅创建无法登陆 Linux 系统的应用账号

## 故障排除{#troubleshoot}

#### CPU 100% 导致系统重启？

如果 CPU 100% 负荷持续一段时间，系统可能会自动重启，其实这是 Linux 的一种设计。原因是 Linux 系统中有一个叫 [WatchDog](https://linux.die.net/man/8/watchdog) 的程序在起作用。但监测到系统异常且预计无法自愈，则只能触发重启机制以解决问题。  

```
The Linux kernel can reset the system if serious problems are detected. This can be implemented via special watchdog hardware, or via a slightly less reliable software-only watchdog inside the kernel.
```

重启是果，CPU 100% 是根本原因。当然，也可以修改 WatchDog 的配置以降低它通过重启解决问题的权重。  


#### 磁盘已满，需要清理？

1. 查看文件的占用大小情况
   ```
   # 查看当前目录下各文件、文件夹的大小
   du -h –max-depth=1 *

   # 查询当前目录总大小
   du -sh

   # 显示直接子目录文件及文件夹大小统计值
   du -h –max-depth=0 *
   ```

2. 根据查询结果进行对应的删除

#### 服务器连不上？

下图显示了无法连接云服务器的主要原因分类及出现概率，按照对应的原因进行排查：  

![](./assets/ecs-cannotconnect.jpeg)
