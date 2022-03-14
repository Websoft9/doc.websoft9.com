---
sidebar_position: 1
slug: /alibabacloud
---

# 指南

最常用的阿里云操作指引

## 服务器

下面介绍阿里云上服务器实例相关的操作说明。

### 创建服务器

创建实例最基本的条件是需要给服务器准备一个系统盘的启动模板文件，这个模板最常见的表现形式就是镜像文件

下面介绍基于镜像创建云服务器的操作步骤：


1. 登录到阿里云管理控制台，以此打开：【云服务器 ECS】>【实例】>【创建实例】，
   ![进入ecs控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-createecs-websoft9.png)

2. 选择计费方式、实例类型等
   ![选择ECS规格](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-guige-websoft9.png)

   - 包年包月：一口价包干付费制
   - 按量付费：按小时付费，用一小时给一小时的钱
   - 抢占式实例：按小时付费，但每个小时价格会发生变化，例如：0.07--0.8之间波动，最高价0.8是自行设置，当阿里云价格超过0.8这个最高值之时，ECS将自动释放

3. 在镜像一栏，有多种选择。
   - 公共镜像：阿里云官方提供的操作系统镜像
   - 自定义镜像：用户自己的镜像
   - 共享镜像：其他人共享给用户的镜像
   - 镜像市场：由阿里云云市场伙伴提供的镜像（Websoft9 是这种镜像市场的主要供应商之一）

4. 如果选择镜像市场，可以通过搜索关键件词“websoft9”，列出我们相关镜像
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-searchw9image-websoft9.png)

4. 选择一个你所需的镜像，开始创建ECS实例

5. 后续动作基本都会要求用户完成：网络和安全组、密码、公网带宽等设置

6. 等待几分钟，ECS创建完成后，镜像会作为ECS实例的系统盘启动，即镜像自动部署到实例中

### 创建秘钥对

在创建ECS时，如下采用秘钥对作为登录凭证，需要提前创建秘钥对

1. 登录控制台，打开：【云服务器 ECS】>【实例】>【创建实例】>【秘钥对】，点击“**创建秘钥对**”按钮
   ![创建秘钥对](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-createkeys-websoft9.png)

2. 为秘钥对命名，例如“myKey”

3. 点击确认后系统会自动将秘钥对文件 myKey.pem 保存到本地电脑

### 连接服务器

阿里云支持四种连接方式：

| 方式                                                   | 操作说明                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| 本地电脑上的远程连接软件                                   | 需要下载 [putty](https://putty.org/) 等客户端到本地电脑来连接服务器 |
| [Workbench](https://ecs-workbench.aliyun.com/) 远程连接 | 阿里云提供的网页版的在线连接工具，支持命令和可视化操作 |
| VNC 远程连接                                           | 阿里云提供的在线 VNC 工具，在无法使用 Workbench 和 本地电脑连接软件的时候使用|
| 发送远程命令（云助手）                                           | 不需要登陆连接的一种命令执行工具，需 ECS 中提前安装云助手客户端|

我们以 “**Workbench**” 为例描述如何连接Linux

1. 登录阿里云控制台，找到需连接的 ECS，点击【远程连接】
   ![命令行连接](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-remoteconnectweb-websoft9.png)

2. 点击【Workbench远程连接】下的【立即登陆】按钮

3. 等待加载完成后，输入账号和密码（支持密钥对）后登陆连接

2. 通过阿里云 **WorkBench** 远程连接 Windows（可选）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-remoteconnectweb-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-rdpremote-websoft9.png)


### 重置密码

忘记密码，在阿里云控制台有两种方式可以重置密码：

**直接重置**

1. 登录到阿里云控制台，找到所需操作的ECS
2. 点击下面的“重置实例密码”，输入新密码
   ![调整配置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-resetpw-websoft9.png)
3. 重启ECS实例，方可生效

**命令重置**

1. 登录到阿里云控制台，找到所需操作的ECS
2. 点击右侧【远程连接】>【发送命令】，打开相关窗口
3. 输入的命令如下，点击【执行】按钮
   ```
   echo "yourpassword" | passwd --stdin root  
   ```
4. 提示如下的信息即表示执行成功
   ```
   Changing password for user root.
   passwd: all authentication tokens updated successfully.
   ```

### 升降配

ECS的配置可以调整，具体操作如下：

1. 登录到阿里云控制台，找到所需操作的ECS
2. 点击右侧的“升降配”，选择一种变更方案
   ![调整配置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-changeecsconfigure-websoft9.png)
3. 依据相关的操作向导完成变更

### 重新初始化磁盘

如果你想将服务器恢复到刚安装之时的状态，就需要用到**重新初始化镜像**操作。

1. 登录到阿里云控制台，找到所需操作的ECS
2. 停止ECS示例
2. 依次打开：更多->磁盘和镜像->重新初始化镜像
   ![获取系统日志](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-iniecs-websoft9.png)
3. 根据系统提示完成后续步骤

> 建议仔细理解**更换系统盘**和**重新初始化镜像**的差异

### 备份服务器

阿里云控制台提供了两种快照备份入口：

#### 快照备份

1. 登录到阿里云控制台->存储和快照->快照
2. 打开“自动快照策略”标签 或 自己创建策略
    ![创建快照生命周期策略](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-snapshotstart-websoft9.png)
3. 在已有的快照策略下，设置磁盘（即将磁盘加入到所属的快照策略中）
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-snapshotconf-websoft9.png)
4. 下面是一个已经被设置的磁盘示例
    ![设置磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-snapshotsetdisk-websoft9.png)

#### 镜像备份

如果不做自动备份，而是手动根据需要备份，创建自定义镜像即可：

1. 登录到阿里云控制台->ECS，找到需要操作的目标实例
2. 依次打开：更多->磁盘和镜像->创建自定义镜像
   ![创建自定义镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-createimage-websoft9.png)
3. 根据提示完成后续操作

## 存储

存储、磁盘快照和镜像在服务器管理中，它们本质上是“一类”事物。  

另外，这里把常用的两种存储进行说明：  

* **云盘（磁盘）** 可以是单独的一种计算资源（单独创建、单独计费、单独管理等），同时也可以被集成到服务器实例，作为其中的一个组件。
* **对象存储（OSS）** 是一种无需绑定服务器就能使用的云储存方案，它非常类似企业网盘。

下面我们介绍常见的操作场景： 

### 创建快照

对于阿里云来说，基于磁盘来创建快照

1. 登录到阿里云控制台->ECS，点击**存储与快照**下的**云盘**

2. 点击“创建快照”操作
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-disktosnapshot-websoft9.png)
   
3. 根据提示完成后续步骤

### 创建镜像

前面讲过，基于快照可以创建镜像，基于实例也可以创建镜像

**实例创建镜像**

1. 登录到阿里云控制台->ECS，找到需要操作的目标实例

2. 依次打开：更多->磁盘和镜像->创建自定义镜像
   ![创建自定义镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-createimage-websoft9.png)

3. 根据提示完成后续操作

**快照创建镜像**

1. 登录到阿里云控制台->ECS，点击**存储与快照**下的**快照**

2. 选择所需的快照，对它进行“创建自定义镜像”操作
   ![打开快照](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-snapshottoimage-websoft9.png)

3. 根据提示完成后续操作

**文件创建镜像**

阿里云支持将本地镜像文件上传到 OSS 存储之后，再基于这个已上传的文件创建镜像。

1. 登陆到阿里云控制台，依次打开：【实例与镜像】>【镜像】

2. 选择右侧的【导入镜像】功能
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/alibabacloud-importimage001-websoft9.png)

3. 根据实际情况填写。**操作系统/平台**的选择需特别慎重，它决定控制台是否会通过 Cloud-init 对云服务器初始化工作，以及初始化工作的程度。

   > 【Others Linux】和【Customized Linux】区别阅读：（[非标准平台Linux镜像](https://help.aliyun.com/document_detail/48226.html)）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/alibabacloud-importimage002-websoft9.png)

> **操作系统/平台** 尽量避免选择 Others Linux 或 Customized Linux。例如： OracleLinux 建议选择 CentOS 更为合适 
 

### 增加云盘

1. 登录到阿里云控制台->ECS，点击**存储与快照**下的**云盘**

2. 点击“创建云盘”按钮
   ![创建云盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-createdisk-websoft9.png)

3. 设置磁盘类型，大小等，确认无误后开始创建
   ![设置磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-createdisk2-websoft9.png)

4. 将创建好的磁盘，挂载到ECS实例
   ![挂载磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-attachdisk-websoft9.png)

5. “磁盘挂载”执行成功后，需登录本实例对挂载的磁盘进行“分区格式化和挂载新分区”的操作：
    - Windows, 请参考阿里云官方文档 [Windows格式化数据盘](https://help.aliyun.com/document_detail/25418.html)
    - Linux，请参考阿里云官方文档 [Linux格式化数据盘](https://help.aliyun.com/document_detail/25426.html) 

5. 以上所有设置后方可使用磁盘

### 卸载云盘

将磁盘从ECS中解除绑定关系(卸载)，操作如下

1. 登录到阿里云控制台->ECS，点击**存储与快照**下的**云盘**

2. 找到所需卸载的磁盘，依次打开：更多->卸载
   ![卸载磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-ditachdisk-websoft9.png)

3. 根据提示完成后续操作

> 磁盘卸载后，会保留，不会被删除，可以被其他ECS挂载

### 磁盘扩容

阿里云支持在线扩容**系统盘**和**数据盘**，即无需重启ECS实例便可以完成扩容。

> 大多数情况下，磁盘只能增加大小，而不能降低大小

1. 登录到阿里云控制台->ECS，点击**存储与快照**下的**云盘**

2. 找到所需卸载的磁盘，依次打开：更多->磁盘扩容
   ![修改卷](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-changedisks-websoft9.png)

3. 选择【[在线扩容](https://help.aliyun.com/document_detail/111738.html)】方式

4. 等待扩容后的反馈


### 磁盘挂载

某些磁盘扩容后，文件系统的容量并没有增加。这个时候，就需要进行手工的磁盘挂载操作。  

1. 连接服务器，安装 `growpart` 磁盘挂载软件
   ```
   yum install -y cloud-utils-growpart
   growpart /dev/vda 1
   ```
2. 将磁盘挂载到指定磁盘的第一个分区
   ```
   # 挂载到系统盘的第一个分区
   growpart /dev/vda 1

   # 挂载到数据盘的第一个分区
   growpart /dev/vdb 1
   ```
3. 处理扩容后文件系统，以符合 Linux 要求
   ```
   # 适用于 ext 文件系统
   resize2fs /dev/vda1 

   # 适用于 xfs 文件系统
   xfs_growfs /dev/vda1 
   ```

### OSS 挂载

方案繁琐，参考[官方文档](https://help.aliyun.com/document_detail/134092.html)。  

## 网络与安全

### 查看  IP

1. 登录到阿里云控制台->ECS
2. 打开要查看公网IP的实例，我们会看到 **IP地址（公）** 
   ![查看公网IP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-getpublicip-websoft9.png)
3. 如果实例没有公网IP地址项（或为空），需挂载一个弹性公网IP（[参考文档](https://help.aliyun.com/document_detail/72125.html)）

### 更换 IP

在创建后六小时内的ECS可以更换公网IP。具体操作步骤如下：

1. 登录ECS管理控制台。
2. 在左侧导航栏，选择实例与镜像 > 实例。
3. 找到更换公网IP地址的实例，停止
4. 然后选择：更多-> 网络和安全组 -> 更换公网IP
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-changeip-websoft9.jpg)
5. 根据提示完成后续操作

### 安全组

安全组是管理ECS端口的功能，端口是服务器上应用程序与外部访问出入访问的通道。下面以**开启80端口为例**，为您介绍安全组的使用

1. 登录到阿里云控制台->ECS
2. 打开实例下：网络和安全组->安全组配置
   ![ecs更改安全组](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-modifysg-websoft9.png)
3. 编辑安全组规则，选择“入方向”标签，然后点击“快速创建规则”
   ![ecs更改安全组入](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-modifysg80-websoft9.png)
4. 授权对象一般为`0.0.0.0/0`较为合适
3. 点击“确认”按钮即可生效

## 域名

域名的目的是通过一段容易识别的文字段来指向服务器上的网站。如果没有域名，网站就只能通过IP地址访问，这样不便于记忆和识别。

为了使网站可以通过域名访问，有三个工作：

### 域名解析

阿里云给每台ECS实例都配置了一个公有DNS

当ECS配置的是动态IP时，每次重启实例，IP地址都可能会发生变化，导致需要重新解析域名，给运维带来不必要的麻烦。阿里云的DNS功能，就是帮我们避免这个问题的。

1. 购买域名(也称之为注册域名)，并完成实名制认证

2. 登录阿里云控制台，打开域名列表，在所需操作的域名上点击“解析”
   ![A记录解析](http://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-dns-websoft9.png)

3. 增加一个A记录：将域名（或子域名）指向IP的操作(下图示例)
   ![A记录解析](http://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-dnsrev-websoft9.png)

2. 保存并等待生效

### 域名备案

阿里云的备案政策简述：

- 购买服务器2个月或以上，就可以由阿里云免费提供备案服务。  
- 备案过程请通过[阿里云备案系统](https://beian.aliyun.com/order/index.htm)全程操作
- 备案是纯粹的商务流程活动，没有任何技术门槛，建议用户自行完成
   ![阿里云备案](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-beian-websoft9.png)
- 服务器地区在中国大陆的对应的域名需要备案

> 阿里云 7*24小时备案专线：95187转3 确保您的备案咨询能够得到及时回复

