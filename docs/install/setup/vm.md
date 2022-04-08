---
sidebar_position: 2
slug: /setup/vm
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# 操作云服务器

部署和使用开源软件，需要掌握一些基本的云服务器相关操作。

## 云平台指南

针对云服务器我们有数十种操作技能需要掌握，而不同云平台有一定的差异，请参考下表：

| 云平台                 | 常见操作            | 更多操作       |
| ---------------------- | --------------------------- | --------------------------- |
| Azure | <br />- 连接VM、管理文件、运行命令<br />- 修改安全组入方向<br /> - 云服务器自动备份<br />- 添加数据盘<br /> | [《Azure 云平台指南》](../azure) |
| AWS | <br />- 连接EC2实例、管理文件、运行命令<br />- 修改安全组入方向<br /> - 云服务器自动备份<br />- 增加卷<br /> | [《AWS 云平台指南》](../aws) |
| 阿里云 | <br />- 连接ECS云服务器、管理文件、运行命令<br />- 修改安全组入方向<br /> - 云服务器自动备份<br />- 增加数据盘<br /> | [《阿里云 云平台指南》](../alibabacloud) |
| 华为云 | <br />- 连接ECS云服务器、管理文件、运行命令<br />- 修改安全组入方向<br /> - 云服务器自动备份<br />- 增加数据盘<br /> | [《华为云 云平台指南》](../huaweicloud) |
| 腾讯云 | <br />- 连接云服务器、管理文件、运行命令<br />- 修改安全组入方向<br /> - 云服务器自动备份<br />- 增加数据盘<br /> | [《腾讯云 云平台指南》](../tencentcloud) |


## 操作系统账号{#osacount}

不同的云平台操作系统账号是不一样的，有的云平台可以在创建服务器时自定义用户名称，有的是固定用户名`root`。

具体参考下面的表格：  

<Tabs>
  <TabItem value="linuxaccount" label="Linux" default>

   |  云平台   |  管理员账号   | 其他|
   | --- | --- | --- |
   |  Azure   |  创建服务器的时候自行设置   | [如何开启root账户？](https://support.websoft9.com/docs/azure/zh/server-login.html#示例2：启用系统root账号) |
   |  AWS   |  AmazonLinux:ec2  CentOS:centos  Ubuntu:ubuntu  Debian:admin   | [如何开启root账户？](https://support.websoft9.com/docs/aws/zh/server-login.html#示例2：启用系统root账号) |
   |  阿里云，华为云，腾讯云   |  root   | |

  </TabItem>
  <TabItem value="windowsaccount" label="Windows">

   |  云平台   |  管理员账号   | 其他|
   | --- | --- | --- |
   |  Azure   |  创建服务器的时候自行设置   |  |
   |  AWS，阿里云，华为云，腾讯云   |   administrator    | |

  </TabItem>
</Tabs>


## 连接服务器（通用）

如果你准备好了服务器的管理员账号密码、公网IP地址等信息，可以参考下面的通用教程开始连接服务器。

### 连接 Linux{#connectlinux}

推荐使用 SFTP 工具去连接 Linux。SFTP 是使用 SSH 协议的 FTP 模式，也称之为安全增强型的 FTP。

下面以 WinSCP（它具备**可视化管理文件**以及运行命令的能力） 这款 SFTP 工具为例，详细说明SFTP的使用。

##### 配置 WinSCP

1. 下载 [WinSCP](https://winscp.net/) 并安装。启动后，新建一个连接
2. 设置验证密码：针对 **密码验证和秘钥对** 两种验证方式分别说明：
   - 密码验证方式设置（最常见的方式）
     ![密码验证方式](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-newsite.png)
   - 秘钥对验证方式设置
     ![秘钥对验证方式](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-secrets-websoft9.png)
3. 验证方式设置好之后，点击"登录"。登录中过程中，系统提示您是否保存登录信息，选择"是"
4. 成功连接后的界面
   ![WinSCP管理界面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-success.png)

##### 管理文件

WinSCP 通过拖拽，就可以方便上传下载文件，可以对文件（夹）可以对进行多种设置与操作

1. 一般来说网站的文件都放在 */data/wwwroot* 目录下夹  
   ![upload files](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/winscp-dragfile-websoft9.png)

2. 右键单击服务器上一个文件或文件夹，可以对云服务器进行多种操作  
   ![管理文件](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-youjian.png)

3. 以修改文件权限为例的相关界面如下  

   ![管理文件](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-quanxian.png)

##### 运行命令

WinSCP 自带命令运行的终端，对于初学者来说简单实用：  

1. WinSCP登录到服务器，点击菜单来的命令窗口图标（快捷键Ctrl+T也可以）
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-ucmd-websoft9.png)

2. 在弹出的命令运行窗口执行命令（每次一条命令），以查询内存使用为例，运行命令 `free -m`
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/wincp-showmemory-websoft9.png)

##### 集成 Putty

由于 WinSCP 自带命令仅能够运行非交互式命名（即命令执行过程中无需反馈和过程中的输入），所以高级用户会给  WinSCP 增加一个更好的命令行工具：Putty

Putty 虽然可以单独运行，但把 Putty 集成到 WinSCP 上使用更加方便。  

1. 依次打开：WinSCP-选项-集成-应用程序，定位到本地 Putty 路径后保存即成功集成  
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-putty.png)

2. 测试集成：通过 WinSCP 的窗口快捷方式打开 Putty  
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/WinSCP/websoft9-WinSCP-puttyopen.png)

### 连接 Windows{#connectwindows}

可以通过本地电脑的远程桌面工具 (MSTSC) 连接 Window 服务器。具体步骤如下：

1. 登录Azure Portal，找到需要登录的服务器的**公网IP地址**
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-publicip-websoft9.png)

2. 选择一种打开本地电脑远程桌面的方式（三选一）:

   - 打开 **开始菜单** -> **远程桌面连接**
   - 打开 **开始菜单**，输入”mstsc“ ，系统会搜索远程桌面连接工具
   - 通过 **Windows Logo** + **R** 打开系统的命令窗口，输入”mstsc“来启动远程桌面连接工具

3. 打开远程桌面连接，输入公网IP地址

   ![img](http://libs.websoft9.com/Websoft9/DocsPicture/zh/windows/windows-remote.png)

4. 通过更多选项，设置默认用户名，例如”Administrator“，并勾选”允许我保存凭据“

   ![img](http://libs.websoft9.com/Websoft9/DocsPicture/zh/windows/windows-remote-login.png)

5. 点击连接，成功后会看到Windows界面
   ![image.png](http://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-windows2019desktop-websoft9.png)

6. 远程登录后，就可以直接从本地**拷贝**文件，然后**粘贴**文件到服务器上。
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-copyfilewin-websoft9.png)

7. 如果需要使用FTP，需要自行安装FTP软件（推荐使用FileZilla Server）

## 异常处理

#### 忘记服务器密码怎么办？

服务器密码在创建服务器的时候自行设置，若不记得密码必须通过云控制台重置。

#### 连接服务是所需的主机名（host）是？

服务器公网 IP 地址
