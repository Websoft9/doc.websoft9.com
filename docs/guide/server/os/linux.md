---
sidebar_position: 1
slug: /linux
---

# Linux Server

Websoft9 面向企业用户，提供个性化的操作系统以及托管技术支持服务，目前支持个性化的操作系统包括：

- 纯净版的操作系统，例如：Oracle Linux, Rocky Linux, CentOS7.x
- 含桌面的操作系统，例如：Oracle Linux with Gnome
- 含软件包的操作系统，例如：Ubuntu with Docker, Ubuntu with AI 大模型

下面是管理和维护操作系统中相关的操作指南。  

## 发行版

### Oracle Linux

[Oracle Linux](https://www.oracle.com/linux/) 是一个完全免费、开源并可以自由分发的 Linux 发行版。 

#### 为什么选 Oracle Linux？

它与 CentOS 或 Ubuntu 等其他免费 Linux 相比，有几个特别之处：

1. 更兼容 Oracle 的其他产品线，例如：[Why Oracle Database Runs Best on Oracle Linux](https://www.oracle.com/a/ocom/docs/linux/oracle-database-runs-best-on-oracle-linux.pdf)

2. 修复补丁后无需重启（零停机）

3. Oracle Linux 官方提供了比较完善的配套支持：
   * [Oracle Linux 认证应用程序](https://apexapps.oracle.com/pls/apex/f?p=10263:17::::::)
   * [Oracle Linux 硬件兼容商](https://linux.oracle.com/ords/f?p=117:1)
   * [Oracle Linux CVE](https://linux.oracle.com/ords/f?p=130:21:)
   * [Oracle Linux 升级包](https://linux.oracle.com/ords/f?p=105:21:117077190823888:pg_R_1213672130548773998:NO&pg_min_row=1&pg_max_rows=50&pg_rows_fetched=50)
   * [Oracle Linux 勘误表](https://oss.oracle.com/mailman/listinfo/el-errata)

4. Oracle 官方提供了可选的[技术支持订阅](https://shop.oracle.com/apex/f?p=dstore:2:0::NO:RIR,RP,2:PROD_HIER_ID:4510272175861805728468)

5. Oracle 在云上提供了一个 Oracle Autonomous Linux 系统，具备自主更新升级的能力（零停机）

6. Oracle Linux 内核 [Unbreakable Enterprise Kernel](https://github.com/oracle/linux-uek)，兼容 RHCK

#### 系统升级{#oracle-upgrade}  

Oracle Linux 在一个维护周期内会发布多个安全漏洞和 Bug 补丁，所以升级的流程包含： 

1. 订阅 Oracle 官方的[补丁通知邮件](https://www.oracle.com/cn/security-alerts/)：注册免费 Oracle 账号 > 用户控制面板 > 订阅管理 > Oracle 安全通知

2. 选择一种升级方案：
    - 普通升级方案：[Linux 标准的软件包升级方案](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/sfw-mgmt-UpdateSoftwareonOracleLinux.html#update-software)  
    - 不停机升级方案：Oracle 官方提供的升级工具[Ksplice](https://ksplice.oracle.com/try/trial) 


### CentOS7

### Rocky Linux


## 设置编码与字体

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


## 管理磁盘与文件系统

- 运行 `lsblk` 查看外设和磁盘分区，Linux 支持的外设：IDE, SATA, USB, SCSI 等
- 运行 `fdisk -l`查看分区容量
- 运行 `df -T` 查看文件系统，Linux 支持的文件系统类型：Btrfs、JFS、ReiserFS、ext、ext2、ext3、ext4、ISO9660、XFS、Minx、MSDOS、UMSDOS、VFAT、NTFS、HPFS、NFS、SMB、SysV、PROC 等。
- 常见的分区工具：fdisk, lvm, gdisk, lsblk, parted


## 设置时间

使用 `timedatectl`，您可以设置系统时间、日期和时区

```
# 设置时间
sudo timedatectl set-time '2024-04-22 15:30:00'

# 查询时间
timedatectl status
```

## 增加用户

- adduser 用于创建 Linux 系统账号，创建过程中会提示：用户名/密码，同时会创建用户家目录
- useradd 仅创建无法登陆 Linux 系统的应用账号



阅读：[系统托管--Linux 桌面](./desktop)




## 故障排除{#troubleshoot}

#### CPU 100% 导致系统重启？

如果 CPU 100% 负荷持续一段时间，系统可能会自动重启，其实这是 Linux 的一种设计。原因是 Linux 系统中有一个叫 [WatchDog](https://linux.die.net/man/8/watchdog) 的程序在起作用。但监测到系统异常且预计无法自愈，则只能触发重启机制以解决问题。  

```
The Linux kernel can reset the system if serious problems are detected. This can be implemented via special watchdog hardware, or via a slightly less reliable software-only watchdog inside the kernel.
```

重启是果，CPU 100% 是根本原因。当然，也可以修改 WatchDog 的配置以降低它通过重启解决问题的权重。  

#### IO 密集型计算下服务器重启？

问题描述：数据库建索引等 IO 密集型计算负载下或资源耗尽 CPU 100%，服务器出现重启的情况？  
解决方案：Oracle 官方建议及时升级补丁

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
