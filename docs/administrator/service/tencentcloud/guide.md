---
sidebar_position: 1
slug: /tencentcloud
---

# 指南

## 服务器管理

下面列出服务器管理常见的操作，在 CVM 控制台可以对实例状态进行修改，包括：

- 开机
- 关机
- 重启
- 删除
- 转包周期

删除适用于按量购买的服务器   
转包周期，即按量付费模式转换成包年包月付费模式

### 创建服务器

1. 登录腾讯[云服务器控制台](https://console.cloud.tencent.com/cvm)，点击“新建”，
   ![进入CVM控制台购买服务器](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-buyecs-websoft9.png)

2. 首先，选择地域与机型
   ![选择CVM规格](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-guige-websoft9.png)
   - 包年包月：一口价对所选的时间区间的包干预付费制
   - 按量计费：按小时后付费，用一小时给一小时的钱

3. 接下来，选择一个你所需的镜像
   ![进入ecs控制台购买服务器](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-selectmkimage-websoft9.png)

   - 公共镜像：腾讯云官方提供的操作系统镜像
   - 自定义镜像：用户自己的镜像
   - 共享镜像：其他人共享给用户的镜像
   - 镜像市场：提供预装操作系统、应用环境和各类软件的优质第三方镜像。无需配置，可一键部署，满足建站、应用开发、可视化管理等个性化需求。

4. 如果选择镜像市场，可以通过搜索关键件词“websoft9”，列出我们相关镜像
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-selectimage-websoft9.png)

5. 后续动作基本都会要求用户完成：存储、安全组、密码、公网带宽等设置，带宽建议按流量计费
![选择带宽](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-netwithpayasgo-websoft9.png)
6. 等待几分钟，弹性云服务器创建完成后，镜像会作为服务器的系统盘启动，即镜像自动部署到实例中

### 创建秘钥对

在创建弹性云服务器时，如果采用秘钥对作为登录凭证，需要提前创建秘钥对

1. 登录腾讯[云服务器控制台](https://console.cloud.tencent.com/cvm)
2. 单击左侧导航窗格中的【SSH 密钥】，然后点击【创建秘钥】按钮
   ![创建秘钥对](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-createkeys-websoft9.png)
3. 选择方式
   * 若创建方式选择 "创建新密钥对" ，输入密钥名称，单击【确定】；
   * 若创建方式选择 "使用已有公钥" ，输入密钥名称，并输入原有的公钥信息，然后单击【确定】。
3. 弹出提示框，单击【下载】（用户需要在 10 分钟内下载私钥）。

### 重置密码

如果您遗忘了密码，您可以在控制台上重新设置实例的登录密码。

> 只有处于关机状态的实例才允许执行重置密码操作。为了避免数据丢失，请提前规划好操作时间，建议在业务低谷时操作，将影响降到最低。

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 在实例的管理页面，选择需要重置密码的云服务器行，单击【更多】>【密码/密钥】>【重置密码】。如下图所示：
   ![调整配置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-resetpw-websoft9.png)
3. 重新开机，方可生效

### 调整配置

CVM的配置可以[调整](https://cloud.tencent.com/document/product/213/2178)，具体操作如下：

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 在需要调整的实例右侧操作栏，单击【更多】>【资源调整】>【调整配置】。如下图所示：
   ![调整配置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-changeecsconfigure-websoft9.png)
3. 依据操作向导完成调整

### 重装系统

如果你想将服务器恢复至刚启动的初始状态，就需要用到[**重装系统**](https://cloud.tencent.com/document/product/213/4933)操作。  

重装系统之前务必进行完成[服务器备份](/zh/server-backup.md)，然后关闭服务器后方可开始重装：

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 在需要重装系统的实例行中，单击【更多】>【重装系统】。如下图所示：
3. 依次打开：更多->重装系统  
   ![重装系统](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-iniecs-websoft9.png)
4. 在弹出的 “重装系统” 窗口中，选择使用当前机器使用镜像或其他镜像，调整磁盘大小，输入密码，单击【开始重装】。
   ![重装系统详情](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-iniecsdetail-websoft9.png)

### 查看日志
1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 云服务器的操作日志可以在 控制台 右上角查看。
   ![查看日志](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-viewlogscvm-websoft9.png)

## 备份{#backup}

我们知道任何人（组织）都无法保证**云服务器**永远正常运行状态。假如云服务器出现无法启动或无法连接的故障，若没有备份会是什么样的后果？这样的教训是否值得尝试？

如果有备份，就能够恢复到备份之时的状态，大大降低损失。

腾讯云上有**基于快照的自动备份**和**基于镜像的手动备份**两种云端备份方案


### 快照备份

腾讯云可以基于云硬盘直接创建快照 或 设置自动快照策略

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 在左侧栏中，单击【快照】>【自定义快照策略】，然后【创建】策略
    ![创建快照策略](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-snapshotpl-websoft9.png)
3. 在已创建的策略上，【关联云硬盘】
    ![创建快照](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-snapshotpldisk-websoft9.png)
4. 根据提示完成后续操作

> 如果你使用的不是云硬盘，是无法创建快照的

### 镜像备份

腾讯云可以基于服务器直接创建自定义镜像，创建新的自定义镜像后，您可以使用该镜像启动更多与原实例具有相同自定义项的新实例。

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 找到所需操作的服务器，关机
3. 待实例关机后，在该台实例行中，单击【更多】>【制作镜像】。如下图所示：
   ![创建自定义镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-createimage-websoft9.png)
4. 根据提示完成后续操作

> 创建自定义镜像的同时系统默认会创建相关快照，删除此快照之前需要先删除关联的镜像。


## 磁盘、快照与镜像

对于腾讯云平台来说，云硬盘（磁盘）可以是单独的一种计算资源（单独创建、单独计费、单独管理等），同时也可以被集成到服务器实例，作为其中的一个组件。

之所以我们把快照和镜像放在一起描述，是因为这两者有一定的关联，甚至说有互生关系。

> 腾讯云目前不支持快照创建镜像，也不支持磁盘创建服务器

### 增加云硬盘

1. 登录到[云硬盘控制台](https://console.cloud.tencent.com/cvm/cbs)
2. 点击【创建】按钮
   ![购买磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-createdisk-websoft9.png)
3. 设置磁盘类型，大小等，确认无误后开始创建
4. 在云硬盘列表页，单击云硬盘所在行的【更多】>【挂载】。
   ![挂载磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-attachdisk-websoft9.png)
5. “磁盘挂载”执行成功后，需登录本实例对挂载的磁盘进行“初始化数据盘”的操作：
    - Windows, 请参考腾讯云官方文档 [Windows初始化数据盘](https://cloud.tencent.com/document/product/213/3857)
    - Linux，请参考腾讯云官方文档 [Linux初始化数据盘](https://cloud.tencent.com/document/product/213/17487) 
6. 以上所有设置后方可使用磁盘

### 卸载云硬盘

将磁盘从云服务器中解除绑定关系(卸载)，操作如下

1. 登录到[云硬盘控制台](https://console.cloud.tencent.com/cvm/cbs)
2. 找到所需卸载的磁盘，依次打开：更多->卸载
   ![卸载磁盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-ditachdisk-websoft9.png)
3. 根据提示完成后续操作

> 磁盘卸载后，会保留，不会被删除，可以被其他服务器挂载

### 数据盘扩容

腾讯云支持在线扩容***数据盘**，即无需重启CVM实例便可以完成扩容。

1. 登录 [云硬盘控制台](https://console.cloud.tencent.com/cvm/cbs)。
2. 选择目标云硬盘的【更多】>【扩容】。
   ![扩容](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-changedisks-websoft9.png)
3. 选择需要的新容量大小（必须大于或等于当前大小）。
4. 完成支付。
5. 根据目标云服务的操作系统类型，您需要执行 [扩展分区及文件系统（Windows）](https://cloud.tencent.com/document/product/362/6737)或 [扩展分区及文件系统（Linux）](https://cloud.tencent.com/document/product/362/6738)将扩容部分的容量划分至已有分区内，或者将扩容部分的容量格式化成新的独立分区。

> 磁盘只支持扩容，不支持减容。

### 系统盘扩容

系统盘类型为云硬盘时，支持扩容系统盘，但仅允许通过对云服务器执行 [重装系统](/zh/stack-deployment.html#重装系统部署) 操作来实现。

### 创建快照

对于腾讯云来说，可以基于云硬盘来创建快照

1. 登录到[云硬盘控制台](https://console.cloud.tencent.com/cvm/cbs)
2. 单击目标云硬盘所在行的【创建快照】。
3. 在【创建快照】对话框中，输入快照名称，单击【确定】。

> 只有云硬盘方可创建快照，本地硬盘不支持创建快照

### 创建镜像

腾讯云目前不支持快照创建镜像，仅支持服务器创建镜像

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 找到所需操作的服务器，关机
3. 待实例关机后，在该台实例行中，单击【更多】>【制作镜像】。如下图所示：
   ![创建自定义镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-createimage-websoft9.png)
4. 根据提示完成后续操作


## 网络与安全

### 查看公网IP{#ip}

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 在列出的所有服务器实例中，我们会看到 **主IP地址（公）** 
   ![查看公网IP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-getpublicip-websoft9.png)
3. 若实例没有公网IP地址项（或为空），需挂载一个公网IP（[参考文档](https://help.aliyun.com/document_detail/72125.html)）

### 绑定公网IP

如果云服务器没有公网IP，需要绑定弹性IP，具体操作步骤如下：

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 点击服务器名称，进入服务器详情页面。
3. 找到【弹性网卡】标签，找到“绑定”操作
   ![绑定操作](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-bindeip-websoft9.png)
4. 根据提示完成后续操作

> 如果没有可用的弹性公网IP，需要实现购买弹性公网IP

### 更换公网IP

公网IP地址是可以更换的，更换后原公网 IP 将被释放

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
2. 在实例的管理页面，选择待转换 IP 的云服务器行，单击【更多】>【IP/网卡】>【更换公网IP】，如下图所示：
   ![更换操作](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-changepip-websoft9.png)

### 安全组{#security}

安全组是管理云服务器端口的功能，端口是服务器上应用程序与外部访问出入访问的通道。下面以**开启80端口为例**，为您介绍安全组的使用

1. 登录到[云服务器控制台](https://console.cloud.tencent.com/cvm/index)
3. 在实例的管理页面，选择需要一台重新分配至新的安全组的云服务器，单击【更多】>【安全组】>【配置安全组】。如下图所示：
   ![CVM更改安全组](http://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-safegroup001-websoft9.png)
3. 在入站规则中，点击【添加规则】按钮
   ![CVM更改安全组入](http://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-safegroup002-websoft9.png)
4. 以增加80和8888端口为范例
5. 80端口可以通过下拉箭头直接软件，8888端口可以通过自定义增加
   ![CVM更改安全组入](http://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-safegroup003-websoft9.png)

> 以上设置方法是最为简单的一种，更多请参考[腾讯云官方安全组教程](https://cloud.tencent.com/document/product/213/16564)进行更为安全、精准的设置。

## 域名{#domain}

### 域名解析

1. 购买域名(也称之为注册域名)，并完成实名制认证
   ![域名购买](http://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-buydomain-websoft9.png)
2. 登录腾讯[域名控制台](https://console.cloud.tencent.com/cns)
3. 在 “域名解析列表” 中，选择需要进行 A 记录转发的域名，进入域名详情页面。
4. 增加一个A记录：将域名（或子域名）指向IP的操作(下图示例)
   ![A记录解析](http://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-dnsreva-websoft9.png)
5. 保存并等待生效

### 域名备案

腾讯云的备案政策简述：

- 购买服务器满足腾讯云的免费备案要求，就可以由腾讯云供备案服务。  
- 备案过程请通过[腾讯云备案系统](https://cloud.tencent.com/product/ba)全程操作
- 备案是纯粹的商务流程活动，没有任何技术门槛，建议用户自行完成
- 服务器地区在中国大陆的对应的域名需要备案
- 腾讯云提供 7*24域名备案[咨询服务](https://console.cloud.tencent.com/smarty?from=beian-offical)

