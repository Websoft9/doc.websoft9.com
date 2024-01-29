---
sidebar_position: 1
slug: /huaweicloud
---

# 指南

## 服务器管理

下面列出服务器管理常见的操作，在ECS控制台可以对实例状态进行修改，包括：

- 开机
- 关机
- 重启
- 删除
- 转包周期

删除适用于按量购买的服务器   
转包周期，即按量付费模式转换成包年包月付费模式

### 创建服务器

1. 登录到华为云管理控制台->弹性云服务器ECS，点击“购买弹性云服务器”，
   ![进入ecs控制台购买服务器](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-buyecs-websoft9.png)
2. 选择计费模式、区域、规格等
   ![选择ECS规格](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-guige-websoft9.png)

   - 包年/包月：一口价包干付费制
   - 按需付费：按小时付费，用一小时给一小时的钱

3. 在镜像一栏，有多种选择。
   - 公共镜像：华为云官方提供的操作系统镜像
   - 私有镜像：用户自己的镜像
   - 共享镜像：其他人共享给用户的镜像
   - 市场镜像：提供预装操作系统、应用环境和各类软件的优质第三方镜像。无需配置，可一键部署，满足建站、应用开发、可视化管理等个性化需求。

4. 如果选择镜像市场，可以通过搜索关键件词“网久”，列出我们相关镜像
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-selectimage-websoft9.png)

4. 选择一个你所需的镜像，开始创建弹性云服务器
5. 后续动作基本都会要求用户完成：网络和安全组、密码、公网带宽等设置，带宽建议按流量计费
![选择带宽](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huawei-netwithpayasgo-websoft9.png)
6. 等待几分钟，弹性云服务器创建完成后，镜像会作为服务器的系统盘启动，即镜像自动部署到实例中

### 创建秘钥对

在创建弹性云服务器时，如下采用秘钥对作为登录凭证，需要提前创建秘钥对

1. 登录华为云控制台，打开：弹性云服务器->秘钥对，点击“**创建秘钥对**”按钮
   ![创建秘钥对](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-createkeys-websoft9.png)
2. 为秘钥对命名，例如“myKey”
3. 点击确认后系统会自动将秘钥对文件 myKey.pem 保存到本地电脑
4. 私钥只能下载一次，请妥善保管

### 连接服务器

华为云支持三种命令行连接方式：

| 方式                                                   | 操作说明                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| 一个独立的 SSH 客户端                                    | 需要下载 [putty](https://putty.org/) 等客户端到本地电脑来连接服务器 |
| 华为云管理控制台远程连接                                           | 在线连接工具，直接登录即可使用|


我们以 “**管理控制台远程登录**” 为例描述如何连接Linux

1. 登录华为云控制台，找到需连接的弹性云服务器，点击“远程登录”
   ![命令行连接](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-remoteconnectweb-websoft9.png)
2. 进入管理终端
   ![命令行连接](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-remoteconnectwebui-websoft9.png)
3. 输入账号和密码，便可以使用管理控制台运行命令

华为云 Windows 服务器支持[多种连接来源](ttps://support.huaweicloud.com/qs-ecs/zh-cn_topic_0092494193.html)，甚至移动端。


### 更改配置

ECS的配置可以调整，具体操作如下：

1. 登录到华为云控制台，找到所需操作的云服务器
2. 点击右侧的“升降配”，选择一种变更方案
   ![调整配置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-changeecsconfigure-websoft9.png)
3. 依据相关的操作向导完成变更

### 重装系统{#reinstallos}

如果你想将服务器恢复到刚安装之时的状态，就需要用到**重装系统**操作。  
重装操作系统提供以原镜像进行系统重装的功能

1. 登录到华为云控制台，找到所需操作的云服务器
2. 关机
2. 依次打开：更多->重装系统  
   ![重装系统](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-iniecs-websoft9.png)
3. 根据系统提示完成后续步骤
   ![重装系统详情](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-iniecsdetail-websoft9.png)

> 建议仔细理解**切换操作系统**和**重装系统**的差异 


## 备份

华为云上有提供自动 [**云备份服务**](https://www.huaweicloud.com/product/cbr.html)（Cloud Backup and Recovery，以下简称"CBR"）的自动备份方案。

> 自动备份区别于手动制作一个镜像实现备份。

![云备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-cbr-websoft9.png)

华为云备份的基本原理是基于快照技术的数据保护，华为云备份针对业务场景，包含云服务器备份、云硬盘备份、应用备份、存储备份、VMware备份功能。

下面介绍云硬盘备份和云服务器备份两种方案：

### 云硬盘备份

云硬盘备份提供对云硬盘的基于快照技术的数据保护。

1. 登录到华为云备份服务控制台
2. 购买云硬盘备份存储库
   > 存储库是存放服务器和磁盘产生的备份副本的容器，您可以将服务器和磁盘绑定至存储库并绑定备份策略，为您的数据提供保障。

   ![云硬盘备份存储库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-cbrbuydisks-websoft9.png)

3. 购买过程中可以立即选择所需备份的硬盘、设置备份策略，也可以跳过以后再设置
   ![云硬盘备份存储库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-cbrbuydiskss-websoft9.png)

2. 备份策略设置
   ![云硬盘备份策略](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-cbrdiskpl-websoft9.png)

### 云服务器备份

云服务器备份提供对弹性云服务器和裸金属服务器的基于多云硬盘一致性快照技术的数据保护。

1. 登录到华为云备份服务控制台

2. 购买云服务器备份存储库
   ![云服务器备份存储库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-cbrbuyecsbk-websoft9.png)

3. 购买过程中可以立即选择所需备份的服务器、设置备份策略，也可以跳过以后再设置
   ![云服务器备份存储库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-cbrbuyecsbks-websoft9.png)

2. 备份策略设置
    ![云服务器备份策略](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-cbrecspl-websoft9.png)

## 磁盘、快照与镜像

对于华为云平台来说，云硬盘（磁盘）可以是单独的一种计算资源（单独创建、单独计费、单独管理等），同时也可以被集成到服务器实例，作为其中的一个组件。

之所以我们把磁盘、快照和镜像放在一起描述，是因为这三者有一定的关联，甚至说有互生关系。

> 华为云目前不支持快照创建镜像，也不支持磁盘创建服务器


### 创建快照

对于华为云来说，可以基于磁盘来创建快照

1. 登录到华为云服务器控制台
2. 在云硬盘列出所有磁盘，对需要操作的磁盘进行“创建快照”操作
    ![创建快照](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-dkcreatesnapshot-websoft9.png)
3. 根据提示完成后续操作

### 创建镜像

华为云目前不支持快照创建镜像，仅支持服务器创建镜像

1. 登录到华为云控制台->弹性云服务器，找到需要操作的目标服务器
2. 依次打开：更多->创建镜像
   ![创建自定义镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-createimage-websoft9.png)
3. 根据提示完成后续操作

### 增加硬盘

1. 登录到云服务器控制台，点击**云硬盘**下的**磁盘**
2. 点击“购买磁盘”按钮
   ![购买磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-createdisk-websoft9.png)
3. 设置磁盘类型，大小等，确认无误后开始创建
4. 将创建好的磁盘，挂载到ECS实例
   ![挂载磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-attachdisk-websoft9.png)
5. “磁盘挂载”执行成功后，需登录本实例对挂载的磁盘进行“初始化数据盘”的操作：
    - Windows, 请参考华为云官方文档 [Windows初始化数据盘](https://support.huaweicloud.com/qs-ecs/zh-cn_topic_0030831989.html)
    - Linux，请参考华为云官方文档 [Linux初始化数据盘](https://support.huaweicloud.com/qs-ecs/zh-cn_topic_0030831989.html) 
5. 以上所有设置后方可使用磁盘

### 卸载硬盘

将磁盘从ECS中解除绑定关系(卸载)，操作如下

1. 登录到云服务器控制台，点击**云硬盘**下的**磁盘**
2. 找到所需卸载的磁盘，依次打开：更多->卸载
   ![卸载磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-ditachdisk-websoft9.png)
3. 根据提示完成后续操作

> 磁盘卸载后，会保留，不会被删除，可以被其他服务器挂载

### 磁盘扩容

华为云支持在线扩容**系统盘**和**数据盘**，即无需重启ECS实例便可以完成扩容。

1. 登录到服务器控制台，点击**云硬盘**下的**磁盘**
2. 找到所需卸载的磁盘，点击“扩容”
   ![修改卷](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-changedisks-websoft9.png)
3. 根据提示完成后续操作

> 磁盘只支持扩容，不支持减容。

## 网络与安全

### 查看公网 IP{#ip}

1. 登录到华为云控制台->ECS
2. 打开要查看公网IP的实例，我们会看到 **IP地址（公）** 
   ![查看公网IP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-getpublicip-websoft9.png)
3. 如果实例没有公网IP地址项（或为空），需挂载一个弹性公网IP（[参考文档](https://help.aliyun.com/document_detail/72125.html)）

### 绑定弹性 IP

如果云服务器没有弹性IP，具体操作步骤如下：

1. 登录云服务器管理控制台。
2. 点击服务器名称，进入服务器详情页面。
3. 找到“弹性公网IP”标签，找到“绑定弹性公网IP”按钮
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-bindeip-websoft9.png)
4. 根据提示完成后续操作

> 如果没有可用的弹性公网IP，需要实现购买弹性公网IP

### 安全组{#securitygroup}

安全组是管理云服务器端口的功能，端口是服务器上应用程序与外部访问出入访问的通道。下面以**开启80端口为例**，为您介绍安全组的使用

1. 登录到华为云控制台->云服务器
2. 华为云控制台-云服务器-点击主机ID链接，打开服务器详细信息页面
3. 依次点击：安全组->更改安全组->管理安全组
   ![ec2更改安全组](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-safegroup001-websoft9.png)
3. 进入管理安全组页面->快速添加规则
   ![ec2更改安全组入](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-safegroup002-websoft9.png)
4. 选择 HTTP(80) 端口，点击确认完成设置

> 以上设置方法是最为简单的一种，更多请参考[华为云官方安全组教程](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0030878383.html)进行更为安全、精准的设置。

## 域名{#domain}

域名的目的是通过一段容易识别的文字段来指向服务器上的网站。如果没有域名，网站就只能通过IP地址访问，这样不便于记忆和识别。

为了使网站可以通过域名访问，有三个工作：

### 域名解析

1. 购买域名(也称之为注册域名)，并完成实名制认证
   ![域名购买](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-buydomain-websoft9.png)
2. 登录华为云控制台，打开域名列表，在所需操作的域名上点击“解析”
   ![解析域名](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-dns-websoft9.png)
3. 增加一个A记录：将域名（或子域名）指向IP的操作(下图示例)
   ![A记录解析](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-dnsrev-websoft9.png)
2. 保存并等待生效

### 域名备案

华为云的备案政策简述：

- 购买服务器满足华为云的免费备案要求，就可以由华为云供备案服务。  
- 备案过程请通过[华为云备案系统](https://beian.huaweicloud.com/)全程操作
   ![A记录解析](https://libs.websoft9.com/Websoft9/DocsPicture/zh/huaweicloud/huaweicloud-dnsbeians-websoft9.png)
- 备案是纯粹的商务流程活动，没有任何技术门槛，建议用户自行完成
- 服务器地区在中国大陆的对应的域名需要备案

> 华为云 7*24小时备案专线：4000 955 988 确保您的备案咨询能够得到及时回复


