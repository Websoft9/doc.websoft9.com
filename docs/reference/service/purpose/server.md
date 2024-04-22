---
sidebar_position: 4
slug: /servers
---

import DocCardList from '@theme/DocCardList';
import {useCurrentSidebarCategory} from '@docusaurus/theme-common';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# 云服务器

## 连接服务器（通用）{#connect} 

如果你准备好了服务器的[管理员账号](#osaccount)密码、公网IP地址等信息，可以参考下面的通用教程开始连接服务器。

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




## 云资源选购建议{#howbuy}

镜像基于云资源运行，云资源的选购一方面要考虑能够匹配镜像的要求，另外还要考虑成本和性能最优。

下面分享 Websoft9 的云资源选购经验：  

### 地域

**问题1：选择华北、还是华南，它们有什么区别？**

华北、华南实际上是云平台的机房地域简称。多台云服务器，最好选用同一个机房，以未来多台服务器之间的数据同步和组网。

举例：A 是数据库服务器，B 和 C 是应用服务器，B 和 C 都要调用 A，此时：A B C 在同一个地域比较合适。  

**问题2：我是广州的公司，华南是不是比价合适我？**

区域选择与你的客户集中地有关。如果客户在华南，你选华南稍微合适一点。如果你的客户在全国，那么全国的机房都差不多。

**问题3：我的客户在海外，我在国内，选哪个地域？**

> 地域原则：“网站用户在哪里就选哪里”

### 带宽

带宽的选择需要慎重，云平台提供了两种带宽计费模式：  

* 包年包月：带宽越大成本越高，好处付费是固定的。  

* 按需付费：根据总流量消耗付费，好处是付费与带宽大小无关

### CPU 内存

推荐以下几种配置组合方案，能够满足大部分用户的需求。

*   1 vCPU 1 GB，适用于访问量较小的个人网站初级阶段
*   1 vCPU 2 GB，适用于流量适中的网站、简单开发环境、代码存储库等
*   2 vCPU 4 GB，能满足 90% 云计算用户，适用于企业运营活动、并行计算应用、普通数据处理
*   4 vCPU 8 GB，用于对计算性能要求较高的业务，如企业运营活动、批量处理、分布式分析等

推荐配置仅帮助用户首次使用时快速决断。云平台都提供了灵活、可编辑的配置修改方式。如果在使用过程中，发现配置过高或过低，可以随时修改配置，进行升降配。  

## 异常处理

#### 忘记服务器密码怎么办？

服务器密码在创建服务器的时候自行设置，若不记得密码必须通过云控制台重置。

#### 连接服务是所需的主机名（host）是？

服务器公网 IP 地址

#### 操作系统账号是什么？{#osaccount}

不同的云平台操作系统账号是不一样的，有的云平台可以在创建服务器时自定义用户名称，有的是固定用户名`root`。

具体参考下面的表格：  

<Tabs>
  <TabItem value="linuxaccount" label="Linux" default>

   |  云平台   |  管理员账号   | 其他|
   | --- | --- | --- |
   |  Azure   |  创建服务器的时候自行设置   | [如何开启root账户？](../azure#enableroot) |
   |  AWS   |  AmazonLinux（ec2）  CentOS（centos）  Ubuntu（ubuntu）  Debian（admin）   | [如何开启root账户？](../aws#enableroot)|
   |  阿里云，华为云，腾讯云   |  root | |
   |  腾讯云 Ubuntu 系统   |  ubuntu | |

  </TabItem>
  <TabItem value="windowsaccount" label="Windows">

   |  云平台   |  管理员账号   | 其他|
   | --- | --- | --- |
   |  Azure   |  创建服务器的时候自行设置   |  |
   |  AWS，阿里云，华为云，腾讯云   |   administrator    | |

  </TabItem>
</Tabs>

#### 如何向服务器上传文件？

向服务器上传文件，完全**不需要**额外设置服务器：  

* Windows服务器：直接 [远程桌面](./user/cloud#connectwindows) 登录后，通过拷贝和粘贴的方式管理文件
* Linux服务器：请使用 [SFTP 连接服务器](./user/cloud#connectlinux) 后，通过可视化界面管理文件


