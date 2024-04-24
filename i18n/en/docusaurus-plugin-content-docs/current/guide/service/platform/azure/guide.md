---
sidebar_position: 1
slug: /azure
---

# 指南

## 服务器管理

下面列出服务器管理常见的操作，在 CVM 控制台可以对实例状态进行修改，包括：

- 开机
- 关机
- 重启
- 删除
- 转包周期
- 更新

### 连接 VM

Azure平台中，操作系统的账号和密码是创建虚拟机的时候自行设置的。图示：

![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-vmsetpw-websoft9.png)

其中，身份验证类型包括：密码和SSH公钥（秘钥对）两种方式。

一般使用命令行（Command）连接 Azure，Azure提供了两种网页版SSH工具，无需账号即可登录。

> 如果您不习惯使用云平台的提供的在线SSH命令行工具，下载SSH客户端工具（例如：[putty](https://putty.org/)），配置登录信息之后便可以连接Linux。

* 方法一：登录云控制台，打开虚拟机->操作，点击“运行命令”

![运行命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-runcmd-websoft9.png)

* 方法二：登录云控制台，打开虚拟机->支持与疑难解答，点击“串行控制台“

![运行命令](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-runcmd2-websoft9.png)

通过命令行连接服务器之后，如下两个最常用的操作示例是需要掌握的：

##### 示例1：获取数据库密码

为了安全考虑，用户每一次部署，都会生成唯一的随机数据库密码，存放在服务中。只需如下的一条命令，即可查看

```shell
sudo cat /credentials/password.txt

//运行结果
MySQL username:root
MySQL Password:@qDg1Vq1!V
```

##### 示例2：启用系统root账号{#enableroot}

Azure出于安全和法规要求，默认情况下没有开放Linux的root账号，只给用户提供了普通账号。如果您希望使用root账号，通过下面的步骤启用之：

```shell
sudo su
sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd
sudo passwd root
```

### 创建 VM

下面介绍Azure上虚拟机的创建方式。

创建虚拟机最基本的条件是需要给虚拟机准备一个系统盘的启动模板文件。这个模板文件有两种：一个是我们非常熟悉的镜像，另外一个是VHD（虚拟磁盘）文件。

因此，创建VM也有两种方式：基于镜像创建和基于系统盘创建

#### 镜像创建

1. 登录Azure控制台，打开：虚拟机->添加，开始创建虚拟机

2. 创建虚拟机的时候选择合适的镜像（这是最重要的步骤）
   ![image.png](http://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-createvmbyimage-websoft9.png)

   > 镜像来源有：官方镜像、云市场镜像和自定义镜像三种镜像来源。如果自定义镜像来源，磁盘就只能选择托管模式

3. 依次设置账号密码、网络、安全组等配置

4. 查看 + 创建 通过之后，点击“创建”即可

#### 系统盘创建

1. 登录Azure控制台，打开“所有资源”，找到一个已经被解除绑定的磁盘
   ![image.png](http://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-createvmbydisk-websoft9.png)
2. 点击这个磁盘，对这个磁盘进行“创建VM”操作
3. 依次设置账号密码、网络、安全组等配置
4. 查看 + 创建 通过之后，点击“创建”即可

#### 秘钥对

在创建VM的时候，有些用户喜欢采用秘钥对方式作为登录凭证

![image.png](http://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-createvmsshkey-websoft9.png)

由于Azure需要自行提供SSH public key, 因此需要用户提前准备。

下面以PUTTYGEN(KEY GENERATOR FOR PUTTY ON WINDOWS)为例，说明如何创建SSH public key

1. Download and Install [PUTTYGEN](https://www.ssh.com/ssh/putty/windows/puttygen).

2. Click "Generate"    
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/en/putty/puttygen-generate-websoft9.png)

3. Public key and Private key is OK, you can copy public to Azure(format starting with "ssh-rsa")   
   Save the public key and private key on your local computer for backups  
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/en/putty/puttygen-generatesave-websoft9.png)

4. When connect Linux on your local computer, you can use private key for authentication 

### VM 更新

Azure提供一套完整的[自动更新管理方案](https://aka.ms/updatemanagement)，

1. 登录Azure门户，点击操作下面的“更新管理”。
2. 为此VM启用更新
![启用更新管理](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-enableupdate-websoft9.png)
3. 耐心等待，系统会创建更新解决方案。点击“安全更新部署”开始设置自动更新策略
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-updateset-websoft9.png)

### 调整配置

VM配置是可以调整，登录到控制台，依次打开：设置->大小，点击“调整大小”按钮即可。

![调整配置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-configures-websoft9.png)

### 重置 VM

在一些特殊情况下，用户打算将VM恢复到初始状态，但希望保留所有VM的配置选项和关联资源均保留。这个时候，我们就需要用到“重新部署”的操作。

1. 选择想要重新部署的 VM，然后选择“设置”边栏选项卡中的“重新部署”按钮。 可能需要向下滚动，查看包含“重新部署”按钮的“支持和故障排除” 部分，如以下示例所示：
   ![重新部署](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-resetstart-websoft9.png)
   
2. 若要确认该操作，请选择“重新部署”按钮：

   ![确认重置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-resetbutton-websoft9.png)

3. VM 准备好重新部署时，该 VM 的“状态”会更改为“正在更新” ，如以下示例所示：
   ![正在更新](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-resetupdate-websoft9.png)

4. VM 在新的 Azure 主机上启动时，“状态”将更改为“正在启动”，如以下示例所示：
   ![正在启动](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-resetstarting-websoft9.png)

5. VM 完成启动过程后，“状态”返回到“正在运行” ，这表示 VM 已成功重新部署：
   ![正在运行](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-resetruning-websoft9.png)



### 备份 VM

Azure中，控制台门户->存储->保管库服务就是用于备份VM的专项服务：

![保管库](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-backuprs-websoft9.png)

下面我们针对已有VM和创建VM中如何设置备份，分别作出说明

#### 已有VM设置

对于已经创建的VM，设置自动备份策略请参考下图

![设置备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-backupstart-websoft9.png)

#### 创建VM设置

在创建VM之时，我们便可以设置自动备份方式

1. 创建VM，在管理选项卡下备份项，启用备份![启用备份](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-backupmanage-websoft9.png)
2. 选择已经建立的保管库名称 或 新建一个保管库名称，然后设置备份策略
   ![备份策略](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-backuppolicy-websoft9.png)
3. 在预算允许的情况下，提高备份的频次是不错的选择


## 磁盘、快照与镜像

对于Azure平台来说，磁盘可以是单独的一种计算资源（单独创建、单独计费、单独管理等），同时也可以被集成到虚拟机，作为其中的一个组件。

之所以我们把磁盘、快照和镜像放在一起描述，是因为这三者有一定的关联，甚至说有互生关系。

Azure的磁盘管理中有几个特殊的概念，下面提前解释：

* 托管磁盘：托管由Azure公共存储来管理
* 非托管磁盘：指磁盘只能由账号下的存储账号来管理，不作为一个独立资源对外
* 存储账号：Azure的后台中提供了存储账号功能，所谓存储账号，即一个可以管理磁盘的入口。

### 数据盘

我们知道数据盘是区别于系统盘的一种磁盘，主要用于存放数据。

#### 增加数据盘

1. 登录Azure云控制台，找到所需操作的虚拟机
2. 打开设置->磁盘，点击“添加数据磁盘”
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-addddisk-websoft9.png)
3. 设置数据磁盘规格
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-addddisk2-websoft9.png)
4. 登录到虚拟机，完成初始化磁盘操作
    - Windows, 需要进入磁盘管理，请参考Azure官方文档 [初始化Windows磁盘](https://docs.microsoft.com/zh-cn/azure/virtual-machines/windows/attach-managed-disk-portal#initialize-a-new-data-disk)
    - Linux，需要新磁盘进行分区、格式化和装载等操作，请参考请参考文档 [初始化Linux磁盘](https://docs.microsoft.com/zh-cn/azure/virtual-machines/linux/attach-disk-portal#connect-to-the-linux-vm-to-mount-the-new-disk) 
5. Complete the above configuration to use the disk

#### 分离数据盘

1. 在左侧菜单中，选择“虚拟机” 。
2. 选择具有要分离的数据磁盘的虚拟机，并单击“停止” 以解除分配 VM。
3. 在虚拟机窗格中，选择“磁盘” 。
4. 在“磁盘” 窗格的顶部，选择“编辑” 。
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-ddiskds-websoft9.png)
5. 在“磁盘” 窗格中，转到要分离的数据磁盘最右侧，并单击分离按钮。
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-ddiskds2-websoft9.png)
6. 删除磁盘后，单击窗格顶部的“保存”。
7. 在虚拟机窗格中，单击“概述” ，并单击窗格顶部的“开始” 按钮重启 VM。

> 磁盘分离后，会保留在存储中，不会删除

### 容量增加

仅当未附加磁盘或取消分配所有者 VM 时，才可调整磁盘大小或更改帐户类型。

![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-ddiskin-websoft9.png)

> 大多数情况下，磁盘只能增加大小，而不能降低大小

### 创建快照

1. 登录到 [Azure 门户](https://portal.azure.com/)。
2. 首先在左上角单击“所有服务” ，找到：计算->快照
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-snapshot-websoft9.png)
3. 在“快照”边栏选项卡中，单击“添加” 或点击“创建快照”
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-createsnapshot-websoft9.png)
4. 根据提示，完成从**源磁盘**到快照的创建过程

### 创建镜像

前面讲过，基于快照可以创建镜像，基于虚拟机也可以创建镜像

#### 虚拟机创建镜像

1. 登录到 [Azure 门户](https://portal.azure.com/)。
2. 打开需要创建镜像的虚拟机，点击“捕获”
![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-vmtoimage-websoft9.png)
3. 根据提示完成后续步骤
4. 值得注意的是，捕获操作在创建镜像的同时也会删除虚拟机

#### 快照创建镜像

1. 登录到 [Azure 门户](https://portal.azure.com/)。
2. 首先在左上角单击“所有服务” ，找到：计算->快照
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-snapshot-websoft9.png)
3. 系统会列出所有快照
4. 选择所需的快照，对它进行创建镜像操作


## 网络与安全

### 公网IP{#ip}

**查看**

1. 登录Azure控制台
2. 打开要查看公网IP的虚拟机，我们会看到公网IP地址项
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-publicip-websoft9.png)
3. 如果虚拟机没有公网IP地址项（或为空），就需要参考下一个小节挂载一个公网IP

**挂载**

当创建的虚拟机没有公网IP地址，只要有空闲（或新购）的公网IP地址，Azure控制台是可以给虚拟机挂载上公网IP地址的。具体操作步骤如下：

1. 登录到Azure控制台
2. 打开所需的虚拟机，查看：网络->网络接口
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-networkinterface-websoft9.png)

2. 在网络接口详情操作中，打开设置->IP配置，点击ipconfig1项
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-ipconfig-websoft9.png)

3. 对ipconfig1进行已有公网IP挂载操作
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-ipconfig1-websoft9.png)
4. 如果没有公网IP可选，可以新建一个
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-createip-websoft9.png)

**静态IP**

创建虚拟机默认选项是创建动态IP，你也可以选择创建静态IP  
![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-createstaticip-websoft9.png)

### 安全组{#securitygroup}

安全组是管理VM端口的功能，端口是服务器上应用程序与外部访问出入访问的通道。下面以**开启80端口为例**，为您介绍安全组的使用

1. 打开VM->网络，首先显示的就是安全组配置
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-networkset-websoft9.png)

2. 点击“添加入站端口规则”，源端口范围填写*号，目标端口范围填写80，保存后生效
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-safegroup80-websoft9.png)

3. 点击“保存”按钮即可生效

## 域名{#domain}

这里我们介绍一个Azure比较实用的域名功能：Azure针对于每个虚拟机提供了DNS服务。

当VM配置的是动态IP时，每次重启VM，IP地址都可能会发生变化，导致需要重新解析域名，给运维带来不必要的麻烦。Azure的DNS功能，就是帮我们避免这个问题的。

1. 在Azure门户打卡虚拟机->概述，找到DNS名称，点击“配置”
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-opendns-websoft9.png)
2. 输入DNS标签，例如：mysite，点击保存
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-setdns-websoft9.png)
3. 设置完成之后，通过域名：mysite.centralus.cloudapp.azure.com 就可以访问这台VM