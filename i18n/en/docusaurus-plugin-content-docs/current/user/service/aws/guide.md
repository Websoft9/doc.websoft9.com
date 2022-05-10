---
sidebar_position: 1
slug: /aws
---

# Guide

## Manage EC2

### Start, Stop and Terminate

You can change the instance state on EC2 console, including:

- Start
- Stop
- Reboot
- Terminate
- Recover

![aws EC2 state Websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2state-websoft9.png)

If you want to automatically recover the instance when it becomes impaired due to an underlying hardware failure or a problem that requires AWS involvement to repair, you need to enable [CloudWatch alarms](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) previously.




### Connect EC2

#### For Linux{#connectlinux}

Command is the basic operation of the Linux system. AWS supports three ways to connect by Command:

| Tool                                                  | Instructions                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| A standalone SSH client                                  | Download [putty](https://putty.org/) and other SSH clients to local computer to connect to Linux. |
| Hosting SSH client based on my browser (Alpha)               | Connect from AWS console website, the prerequisite is to install [EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html) on your instance. |
| A Java SSH client directly connected from my browser（Java required） | Directly connect from AWS console website, the prerequisite is to **install Java plugin**. |


Taking **Hosting SSH client based on my browser** as an example, steps for how to connect to a Linux server are as follows:

1. Refer to [Set up EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html) to install EC2 Instance Connect module（For Websoft9 image, the module is installed by default, just skip this step.）

2. Login to AWS EC2 console, open 【Instance】> 【Connect】and choose the second way to connect.
   ![command line](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-connectmethods-websoft9.png)

3. Click 【Connect】, a window opens and you are connected to the instance.

After you're connected to the server through command line, the following two most common examples of operations are required.

##### Sample1: Get password

For security reasons, each time a user deploys, a unique random database password is generated and stored in the service. Just require the following command to view:

```shell
sudo cat /credentials/password.txt

//result
MySQL username:root
MySQL Password:@qDg1Vq1!V
```

##### Sample2: Enable root user{#enableroot}

For security and regulatory requirements, AWS does not open the Linux root account by default, and only provides users with a common account. If you wish to use the root account, enable it by following the steps below:

```shell
sudo su
sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd
sudo passwd root
```

#### For Windows

Before you use local computer's Remote client to connect Windows Server, you should complete these steps: 

1. Login to AWS console, choose the instance which you want to connect to, click 【Connect】 and then click 【Get Password】 in the pop-up window.
   ![aws get password](http://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-winconnect-websoft9.png)

2. Upload the key pair stored locally.
   ![aws upload key pairs](http://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-winconnectpw-websoft9.png)

3. Click 【Decrypt Password】, then the password will be displayed on the interface.
   ![aws Decrypt Password](http://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-winconnectgpw-websoft9.png)


### Create EC2

The introduction below is about how to launch instance on AWS.  

The basic condition for launching instance is to prepare a boot disk file for the system disk for the instance. The most common template file is image.  

Steps below are about how to launch instance based on image:  

1. Login to AWS Management Console, and click 【EC2】.
   ![log in](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2-websoft9.png)

2. Enter EC2 Dashboard, and click 【Launch Instance】to create Instance.
   ![launch instance](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-addec2-websoft9.png)

3. When choosing AMIs, click 【View all public and private AMIs】 and search keyword "websoft9" to see the list of images.
   ![choose image of Websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2image-websoft9.png)

4. Select the image you need.

5. Finish the following steps, which require you to choose instance type, VPC, set key pair and more.
   ![create instance](http://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2createpw-websoft9.png)

6. Wait several minutes after completing creating EC2, and the image is started as the system disk of the instance, that is, the image is automatically deployed to the instance.

### Key Pair for EC2{#keypair}

When launching instance, AWS requires key pair to log in. Steps for how to create key Pair are as follows:

1. Login to AWS console, open 【EC2 Dashboard】>【NETWORK & SECURITY】>【Key Pairs】and click 【Create Key Pair】.
   ![create key pair](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-createkeyps-websoft9.png)

2. Name the key pair, such as "myKey".
   ![name](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-keypsname-websoft9.png)
   
3. Store key pair file **myKey.pem** into the local computer.

### Change EC2 Type

Follow the steps below to change instance type：

1. Login to AWS console and stop the instance.

2. Open 【Actions】>【Instance Settings】>【Change Instance Type】.
   ![adjust configuration](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-configures-websoft9.png)

3. Complete new settings, then start the instance.

### Get EC2 logs

You can get system log on EC2 console：

1. Login to AWS console and stop the instance.

2. Open 【Actions】>【Instance Settings】>【Get System Log】.
   ![get system log](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-getsyslogs-websoft9.png)
3. Complete the new settings, then start the instance.
   ![display system log](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-syslogs-websoft9.png)


### Backups EC2{#backup}

We know that no one (organization) can guarantee that the EC2 will always be up and running. If EC2 fails to start or fails to connect, what would happen without backups? Is it worthwhile to try?

If there is a backup, it can be restored, which greatly reduce the loss.

For AWS, to create backup for EC2 is based on automatic snapshot for the volume of EC2.

There are two entries to create backups on AWS console:

#### Snapshot Backup

##### Automatic Backup

1. Login to AWS console.  

2. Open【EC2】>【ELASTIC BLOCK STORE】>【Lifecycle Manager】>【Create Snapshot Lifecycle Policy】.
    ![Snapshot lifecycle policy](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/en/aws/aws-snapshotauto-websoft9.png)  

3. Follow the prompts to complete the settings.

##### Manual Snapshot 

Steps for manual snapshot on demand are as follows:

1. Login to AWS console and open EC2 Dashboard.  

2. Open 【ELASTIC BLOCK STORE】>【Volumes】 and choose volume to 【Create Snapshot】.
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-createsnapshot-websoft9.png)  

3. Name the snapshot before creating.

#### AWS Backup service

AWS Backup is the specific backup service for AWS resources.

1. Login to AWS console, open 【Services】>【Storage】>【AWS Backup】 and create Backup plan.
   ![AWS Backup service](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-backupservices-websoft9.png)
2. Choose to start from an existing plan and begin to create on-demand backup, that is, to choose the protected resources as you need.
   ![AWS Backup service](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-backupres-websoft9.png) 

3. Choose EBS (disk) as the resource type and choose the volume ID.
   ![AWS Backup service](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-backupres2-websoft9.png) 
   
4. Complete the settings.

### Upgrade EC2

AWS offers [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) solution, which can help you automate collecting software inventory, patching applications OS, launching system VMs, and configuring Windows and Linux.

1. Login to AWS Management Console and open 【AWS System Manager】 service.

2. Open 【Instances & Nodes】>【Patch Manager】to enter the manage interface.
![launch system manager](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/en/aws/aws-sysmupdate-websoft9.png)

3. Follow the guide to complete upgrading.

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
