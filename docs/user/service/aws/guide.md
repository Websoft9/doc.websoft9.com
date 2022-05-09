---
sidebar_position: 1
slug: /aws
---

# 指南

## 服务器管理

### 用户名{#username}

AWS[官方表示](https://docs.aws.amazon.com/zh_cn/AWSEC2/latest/UserGuide/connection-prereqs.html)，AWS 针对于不同的操作系统（甚至发行版）其用户名是不一样的：

- 对于 Amazon Linux 2 或 Amazon Linux AMI，用户名称是 ec2-user。
- 对于 CentOS AMI，用户名称是 centos。
- 对于 Debian AMI，用户名称是 admin 或 root。
- 对于 Fedora AMI，用户名为 ec2-user 或 fedora。
- 对于 RHEL AMI，用户名称是 ec2-user 或 root。
- 对于 SUSE AMI，用户名称是 ec2-user 或 root。
- 对于 Ubuntu AMI，用户名称是 ubuntu。
- 对于Windows，用户名称是 Administrator。

如果 ec2-user 和 root 无法使用，请与 AMI 供应商核实。


### 启动、停止和终止

在EC2控制台可以对实例状态进行修改，包括：

- 启动
- 停止
- 重启
- 终止
- 自动恢复

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-ec2state-websoft9.png)

> 终止=删除EC2

自动恢复的前提，必须启用[CloudWatch功能](https://docs.aws.amazon.com/zh_cn/AWSEC2/latest/UserGuide/ec2-instance-recover.html)，在实例受损（由于发生基础硬件故障或需要 AWS 参与才能修复的问题）时自动恢复实例。

### 连接 EC2

#### 连接 Linux{#connectlinux}

AWS 支持多种 Linux 的连接方式：

| 方式                                                   | 操作说明                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| 一个独立的SSH客户端                                    | 需要下载 [putty](https://putty.org/) 等客户端到本地电脑来连接服务器 |
| 托管SSH客户端直接来自我的浏览器（Alpha）               | 从AWS控制台网页直接连接服务器，前置条件是服务器需要安装[EC2 Instance Connect](https://docs.aws.amazon.com/zh_cn/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html) |
| 直接从我的浏览器连接的 Java SSH 客户端（需要安装Java） | 从AWS控制台网页直接连接服务器，前置条件是浏览器需要**安装Java插件** |


我们以 “**托管SSH客户端直接来自我们的浏览器**” 为例描述如何连接Linux

1. 参考[此处文档](https://docs.aws.amazon.com/zh_cn/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html)，安装EC2 Instance Connect组件（Websoft9镜像默认已安装，忽略此步骤）

2. 登录AWS云控制台，打开：实例->连接，选择第二种连接方式后，点击“Connect”按钮
   ![命令行连接](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-connectmethods-websoft9.png)

3. 将打开一个窗口，并且您连接到实例。

通过命令行连接服务器之后，如下两个最常用的操作示例是需要掌握的：

##### 获取数据库密码

为了安全考虑，用户每一次部署，都会生成唯一的随机数据库密码，存放在服务中。只需如下的一条命令，即可查看

```shell
sudo cat /credentials/password.txt

//运行结果
MySQL username:root
MySQL Password:@qDg1Vq1!V
```

##### 启用系统root账号{#enableroot}

AWS出于安全和法规要求，默认情况下没有开放Linux的root账号，只给用户提供了普通账号。如果您希望使用root账号，通过下面的步骤启用之：

```shell
sudo su
sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd
sudo passwd root
```

#### 连接 Windows

在远程连接 Windows 服务器之前需要上传秘钥对获取密码，然后在使用 Windows 远程桌面工具连接：

1. 登录AWS控制台，找到需要登录的服务器，点击“连接”在弹出的窗口中点击【Get Password】
   ![AWS Get Password](http://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-winconnect-websoft9.png)

2. 上传创建服务器的时候保存的**私钥**
   ![AWS upload key pair](http://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-winconnectpw-websoft9.png)

3. 点击【Decrypt Password】之后，密码解锁成功，并显示在界面上
   ![AWS Descypt Password](http://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-winconnectgpw-websoft9.png)

4.打开本地电脑的**远程桌面**工具连接 Windows



### 创建 EC2

下面介绍 AWS 上服务器实例的创建方式（ AWS 称之为**启动实例**）。

创建实例最基本的条件是需要给服务器准备一个系统盘的启动模板文件，这个模板最常见的表现形式就是镜像文件

下面介绍基于镜像创建云服务器的操作步骤：


1. 登录到AWS管理控制台，点击“EC2”，
   ![进入ec2控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-ec2-websoft9.png)

2. 进入EC2控制面板，点击“启动实例”，即开始创建一个新的实例
   ![启动实例](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-addec2-websoft9.png)

3. 在映像一栏，点击“浏览所有公用和专用映像”，然后搜索关键件词“websoft9”，列出相关镜像
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-ec2image-websoft9.png)

4. 选择一个你所需的镜像（以Odoo为例），开始创建EC2实例 

5. 后续动作基本都会要求用户完成：选择实例类型、VPC、Key Pair等设置
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-ec2createpw-websoft9.png)

6. 等待几分钟，EC2创建完成后，镜像会作为EC2实例的系统盘启动，即镜像自动部署到实例中

### 创建秘钥对{#keypair}

在创建EC2时，AWS要求使用秘钥对登录，下面是创建秘钥对步骤

1. 登录AWS控制台，打开：EC2 Dashboard->网络与安全->秘钥对，点击“**创建秘钥对**”按钮
   ![创建秘钥对](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-createkeyps-websoft9.png)

2. 为秘钥对命名，例如“myKey”
   ![秘钥对名称](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-keypsname-websoft9.png)
   
3. 将秘钥对文件 myKey.pem 保存到本地电脑

### 调整配置

EC2的配置可以随时调整，具体操作如下：

1. 登录到AWS控制台，停止实例
2. 依次打开：操作->实例设置->更改实例类型
   ![调整配置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-configures-websoft9.png)
3. 选择一个新的配置，启动实例

### 获取日志

EC2控制台可以方便的获取系统日志：

1. 登录到AWS控制台，停止实例
2. 依次打开：操作->实例设置->获取系统日志
   ![获取系统日志](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-getsyslogs-websoft9.png)
3. 选择一个新的配置，启动实例
   ![显示系统日志](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-syslogs-websoft9.png)


## 备份{#backup}

AWS中，AWS Backup 就是用于备份AWS设施的专项服务

1. 登录AWS控制台，打开：服务->存储->AWS Backup，创建一个备份计划 
   ![AWS Backup服务](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-backupservices-websoft9.png)
2. 在已有备份计划下，创建按需备份（即选择需要备份的云资源）
   ![AWS Backup服务](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-backupres-websoft9.png)
3. 资源类型为：EBS（磁盘），再选择一个列出的卷ID
   ![AWS Backup服务](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-backupres2-websoft9.png)
4. 完成其他备份设置

同时，也可以使用快照备份的方式。  

## 磁盘、快照与镜像

之所以我们把磁盘、快照和镜像放在一起描述，是因为这三者有一定的关联，甚至说他们是一个事物的多种形态。  

AWS中对EC2实现备份的基本原理就是对EC2所属的磁盘做自动快照。

### 卷（磁盘）

对于AWS平台来说，卷（磁盘）可以是单独的一种计算资源（单独创建、单独计费、单独管理等），同时也可以被集成到服务器实例，作为其中的一个组件。

#### 增加卷

1. 登录AWS云控制台，打开EC2 Dashboard
2. 点开ELASTIC BLOCK STORE下的“卷”操作，点击“创建卷”
   ![创建卷](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-createvolume-websoft9.png)
3. 设置卷类型，大小等，确认无误后开始创建
   ![设置卷规格](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-createvolume2-websoft9.png)
4. 将创建好的卷，挂载到EC2实例
   ![挂载卷](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-volumeaddec2-websoft9.png)
5. 登录到EC2实例，完成初始化磁盘操作，使卷可用：
    - Windows, 请参考AWS官方文档 [使 Amazon EBS 卷可在 Windows 上使用](https://docs.aws.amazon.com/zh_cn/AWSEC2/latest/WindowsGuide/ebs-using-volumes.html)
    - Linux，请参考请参考文档 [使 Amazon EBS 卷可在 Linux 上使用](https://docs.aws.amazon.com/zh_cn/AWSEC2/latest/UserGuide/ebs-using-volumes.html) 
5. 完成所有设置后方可使用磁盘

#### 分离卷

将卷从EC2中解除绑定关系，操作如下

1. 登录AWS云控制台，打开EC2 Dashboard
2. 在左侧菜单中，选择“实例” ，选择具有要分离的数据磁盘的实例，并单击“停止” 
3. 点开ELASTIC BLOCK STORE下的“卷”操作，对所要解绑的卷进行“Detach Volume”操作
   ![创建卷](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-detachvolume-websoft9.png)

> 磁盘分离后，会保留在存储中，不会被删除

#### 容量修改

当卷没有附加到EC2时，可以调整卷的容量

1. 登录AWS控制台，依次打开：EC2->ELASTIC BLOCK STORE->卷
2. 选择所需修改的卷，依次打开：操作->修改
   ![修改卷](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-ddiskin-websoft9.png)
3. 设置新的大小

> 大多数情况下，卷只能增加大小，而不能降低大小

### 创建快照

对于AWS来说，基于卷来创建快照

1. 登录到AWS控制台，打开EC2 Dashboard
2. 打开ELASTIC BLOCK STORE下的卷功能，选择一个卷后，实现“创建”快照操作
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-createsnapshot-websoft9.png)
3. 给快照命名后，开始创建

### 创建镜像

前面讲过，基于快照可以创建镜像，基于实例也可以创建镜像

#### 实例创建镜像

1. 登录到AWS控制台
2. 打开需要创建镜像的实例，打开：操作->映像->创建镜像
![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-ec2toimage-websoft9.png)
3. 根据提示完成后续步骤

#### 快照创建镜像

1. 登录到AWS控制台，进入EC2 Dashboard
2. 找到ELASTIC BLOCK STORE下的快照功能，列出所有快照
3. 选择所需的快照，对它进行创建镜像操作
   ![打开快照](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-snapshot-websoft9.png)

### 自动快照策略

1. 登录AWS控制台
2. 打开：EC2->ELASTIC BLOCK STORE->生命周期管理器，创建快照生命周期策略
    ![创建快照生命周期策略](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-snapshotauto-websoft9.png)
2. 根据提示完成快照策略设置


## 网络与安全

### 公网 IP{#ip}

**查看 IP**

1. 登录AWS控制台
2. 打开要查看公网IP的实例，我们会看到 **公有IP** 和 **公有DNS**
   ![查看公网IP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-getip-websoft9.png)
3. 如果实例没有公网IP地址项（或为空），就需要参考下一个小节挂载一个公网IP

**挂载 IP**

当创建的实例没有公网IP地址，只要有空闲（或新购）的公网IP地址，AWS控制台是可以给实例挂载上公网IP地址的。具体操作步骤如下：

1. 登录到AWS控制台
2. 打开所需的实例，查看：操作->联网->管理IP地址
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-manageip-websoft9.png)

3. 在管理IP地址操作栏中，点击“分配弹性IP”
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-assignip-websoft9.png)

4. 根据提示完成后续操作

### 安全组{#securitygroup}

安全组是管理EC2端口的功能，端口是服务器上应用程序与外部访问出入访问的通道。下面以**开启80端口为例**，为您介绍安全组的使用

1. 登录AWS控制台，打开EC2->实例
2. 打开实例下的“描述”标签，然后点击安全组名称
   ![ec2更改安全组](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-changesg-websoft9.png)
3. 进入所属安全组的设置后，打开“入站”标签页，点击编辑
   ![ec2更改安全组入](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-sfin-websoft9.png)
4. 编辑入站规则，增加一个新的规则（下图以80为例）
   ![ec2更改安全组入](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-set80sg-websoft9.png)
3. 点击“保存”按钮即可生效

### AWS 更新服务

AWS提供一套完整的[AWS Systems Manager](https://www.amazonaws.cn/systems-manager/)解决方案，可以帮助您自动收集软件清单、应用操作系统补丁、创建系统映像以及配置 Windows 和 Linux 操作系统。

1. 登录AWS门户，打开 **System Manager** 服务

2. 找到【Instances & Nodes】>【Patch Manager】进入如下的相关管理界面
![启用更新管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-sysmupdate-websoft9.png)

3. 根据向导开始更新


## 域名{#domain}

这里我们介绍一个AWS比较实用的域名功能：AWS针对于每个实例提供了DNS服务。

### EC2之DNS

AWS给每台EC2实例都配置了一个公有DNS

当EC2配置的是动态IP时，每次重启实例，IP地址都可能会发生变化，导致需要重新解析域名，给运维带来不必要的麻烦。AWS的DNS功能，就是帮我们避免这个问题的。

1. 在AWS门户，打开实例->描述
   ![查看DNS](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-getip-websoft9.png)
2. 找到公有DNS，复制下来

### Route 53

Route 53就是AWS的域名购买、解析与管理平台，通过使用 Amazon Route 53，您可以注册新域、转移现有域、将域流量路由到 AWS 和外部资源，还可以监控您的资源的运行状况。

1. 在AWS门户，在联网与内容分发类别找到Route 53服务
   ![打开Route 53](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-route53-websoft9.png)
2. 开始域名相关操作
   ![Route 53界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-route53start-websoft9.png)
