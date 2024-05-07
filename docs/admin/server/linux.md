---
sidebar_position: 1
slug: /linux
---

# Linux

本章介绍使用 Websoft9 托管应用过程中，可能需要的 Linux 相关操作。   

## 指南

### Linux 系统账号{#osaccount}

不同的云平台操作系统账号是不一样的，有的云平台可以在创建服务器时自定义用户名称，有的是固定用户名`root`。

具体参考下面的表格：  

   |  云平台   |  管理员账号   | 其他|
   | --- | --- | --- |
   |  Azure   |  创建服务器的时候自行设置   | [如何开启root账户？](./azure#enableroot) |
   |  AWS   |  AmazonLinux:ec2  CentOS:centos  Ubuntu:ubuntu  Debian:admin   | [如何开启root账户？](./aws#enableroot)|
   |  阿里云，华为云，腾讯云   |  除腾讯云 Ubuntu 之外(ubuntu)，其他平台任何系统默认账号都是 root  | |

### 连接 Linux{#connect}

常见 Linux 连接方式包括：

* SSH 连接
* SFTP 连接
* RDP 连接
* VNC 连接
* Telnet 连接

而连接的工具类型主要是两种：

- 本地电脑客户端，例如：WinSCP, Putty, Xshell, Tabby, MobaXterm 等
- 在线 Web 客户端：各大云平台均提供的 Web 版在线连接工具  

下面以本地客户端 WinSCP（它具备**可视化管理文件**以及运行命令的能力） 这款 SFTP 工具为例，详细说明 SFTP 和 SSH 的使用。

#### 配置 WinSCP

1. 下载 [WinSCP](https://winscp.net/) 并安装。启动后，新建一个连接
2. 设置验证密码：针对 **密码验证和秘钥对** 两种验证方式分别说明：
   - 密码验证方式设置（最常见的方式）
     ![密码验证方式](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-newsite.png)
   - 秘钥对验证方式设置
     ![秘钥对验证方式](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-secrets-websoft9.png)
3. 验证方式设置好之后，点击"登录"。登录中过程中，系统提示您是否保存登录信息，选择"是"
4. 成功连接后的界面
   ![WinSCP管理界面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-success.png)

#### 管理文件

WinSCP 通过拖拽，就可以方便上传下载文件，可以对文件（夹）可以对进行多种设置与操作

1. 右键单击服务器上一个文件或文件夹，可以对云服务器进行多种操作  
   ![管理文件](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-youjian.png)

2. 以修改文件权限为例的相关界面如下  

   ![管理文件](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-quanxian.png)

#### 运行命令

WinSCP 自带命令运行的终端，对于初学者来说简单实用：  

1. WinSCP登录到服务器，点击菜单来的命令窗口图标（快捷键Ctrl+T也可以）
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-ucmd-websoft9.png)

2. 在弹出的命令运行窗口执行命令（每次一条命令），以查询内存使用为例，运行命令 `free -m`
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/wincp-showmemory-websoft9.png)

#### 集成 Putty

专业的 SSH 工具 Putty 虽然可以单独运行，但把 Putty 集成到 WinSCP 上使用更加方便。  

1. 依次打开：WinSCP-选项-集成-应用程序，定位到本地 Putty 路径后保存即成功集成  
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-putty.png)

2. 测试集成：通过 WinSCP 的窗口快捷方式打开 Putty  


### 初始化数据磁盘

初始化数据磁盘主要分为三个步骤：

* 磁盘分区
* 磁盘初始化
* 磁盘挂载

### 自动关机设置

需求：每天晚上20:00服务器自动关机

```
[Unit]
Description=shutdown linux service

[Service]
Type=oneshot
ExecStart=/usr/sbin/shutdown -h 20:00

[Install]
WantedBy=multi-user.target
```


### 编写 Systemd 系统服务 

服务(service) 本质就是进程，运行在后台，通常都会监听某个端口，等待其它程序的请求，比如(mysql , sshd 防火墙等)，因此我们又称为守护进程，是 Linux 中非常重要的知识点。

一般通过下面的格式来管理服务：
```
systemctl    服务名 [start | stop | restart | reload | status]
```

那服务是如何创建的呢？在Linux技术里面编写这种服务也被称之为编写Systemd 的 Unit 文件  

以 Websoft9 提供的 Redmine 自动化项目为例，下面描述完整的服务创建过程：

1. 编辑好[redmine.service](https://github.com/Websoft9/ansible-redmine/blob/master/roles/redmine/files/redmine.service)文件
   ```
   [Unit]
   Description=Redmine
   After=nginx.service
   [Service]
   Environment=RAILS_ENV=production
   Type=simple
   WorkingDirectory=/data/wwwroot/redmine
   ExecStart=/usr/local/bin/puma -b tcp://127.0.0.1:9292 -e production 
   User=redmine
   [Install]
   WantedBy=multi-user.target
   ```
   
2. 将服务文件放入路径：*/etc/systemd/system* 下

3. 启动并设置开机启动

4. 测试服务的可用性
   ···
   systemctl restart redmine
   systemctl stop redmine
   ···

附：通配符含义

| 替换符 | 含义                                                         |
| ------ | ------------------------------------------------------------ |
| "`%b`" | 系统的"Boot ID"字符串。参见 [random(4)](http://man7.org/linux/man-pages/man4/random.4.html) 手册。 |
| "`%H`" | 系统的主机名(hostname)                                       |
| "`%m`" | 系统的"Machine ID"字符串。参见 [machine-id(5)](http://www.jinbuguo.com/systemd/machine-id.html#) 手册。 |
| "`%T`" | 临时文件目录。也就是 `/tmp` 或 "`$TMPDIR`", "`$TEMP`", "`$TMP`" 之一(若已设置) |
| "`%v`" | 内核版本(**uname -r** 的输出)                                |
| "`%V`" | 存放大体积临时文件以及持久临时文件的目录。也就是 `/var/tmp` 或 "`$TMPDIR`", "`$TEMP`", "`$TMP`" 之一(若已设置) |
| "`%%`" | 百分号自身(%)。使用"%%"表示一个真正的"%"字符。               |

### 设置一次性任务

Systemd 可以用于处理开机一次性运行脚本。只需将 Tpye=oneshot 即可

```
[Unit]
Description=Switch-off Touchpad

[Service]
Type=oneshot
ExecStart=/usr/bin/touchpad-off

[Install]
WantedBy=multi-user.target
```


### 设置计划任务

Cron是一个Linux下的定时执行工具，可以在无需人工干预的情况下定时地运行任务task。

1. 安装Crontab
   ```
   yum install vixie-cron
   yum install crontabs
   ```
2. 编写计划任务脚本：可通过[在线 Crontab 生成器](https://crontab-generator.org/)，简化脚本的编写
   ```
   4 * * * * echo "hello" >/dev/null 2>&1
   ```
3. 将脚本插入Cron配置文件：*/etc/crontab*

### 临时目录清理策略

以 CentOS 为例，为  /tmp, /var/tmp 临时目录清理策略，只需修改 */usr/lib/tmpfiles.d/tmp.conf* 


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

Linux 操作系统都提供了一个集中的软件包管理机制，即搜索、安装和管理软件包。 Linux 软件包的基本组成部分通常有：共享库、应用程序（二进制）、服务和文档。从另外一个角度看，包文件通常包含编译好的二进制文件和其它资源组成的：软件、安装脚本、元数据及其所需的依赖列表。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-rpms-websoft9.png)

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

因此，解决重启的问题，主要还是要找到 CPU 100% 的原因。当然，也可以修改 WatchDog 的配置以降低它通过重启解决问题的权重。  


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

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/ecs-cannotconnect.jpeg)

#### 连接 SFTP，出现 Disconnected...publickey{#sftpnokey}

错误原因：服务器初始化的适合，启用的是密钥对登录方式（密码登录会不开启）    
解决方案：设置 WinSCP 为秘钥对登录 或 云控制台更改登录凭证方式
