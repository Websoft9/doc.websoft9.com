---
sidebar_position: 3
slug: /azure/advanced
---

# 进阶

## 核心原理

### API/CLI

Azure 提供了原生 [API/CLI](https://docs.azure.cn/zh-cn/cli/reference-index?view=azure-cli-latest) 。[安装](https://docs.azure.cn/zh-cn/cli/install-azure-cli-linux?view=azure-cli-latest)完成后即可使用。  

#### 验证

azure cli 运行时需服务器登录到 Azure 作为一种额外的账号验证。具体如下：

1. 运行验证命令
   ```
   az account clear
   az login --use-device-code
   ```
2. 本地浏览器打开：https://microsoft.com/devicelogin，输入上一步骤的授权码，开始验证

#### 导入存储账号

连接CLI所在的服务器，编辑操作系统的 /etc/profile 文件，加入如下两行代码，key vualue 为秘钥字符串

```
export AZURE_STORAGE_ACCOUNT="websoft9imagedisks"
export AZURE_STORAGE_KEY="key value"
```

`source /etc/profile` 后生效。  

#### 常用命令

```
# 列出常用镜像，这个列表与Azure控制台购买VM列出的镜像有一定差异
# Azure没有官方镜像的说法，只有自定义镜像和云市场镜像两种类型，即使是Azure自己发布的镜像，也存放在云市场汇总。
az vm image list --output table

Offer          Publisher               Sku                 Urn                                                             UrnAlias             Version
-------------  ----------------------  ------------------  --------------------------------------------------------------  -------------------  ---------
CentOS         OpenLogic               7.5                 OpenLogic:CentOS:7.5:latest                                     CentOS               latest
CoreOS         CoreOS                  Stable              CoreOS:CoreOS:Stable:latest                                     CoreOS               latest
debian-10      Debian                  10                  Debian:debian-10:10:latest                                      Debian               latest
openSUSE-Leap  SUSE                    42.3                SUSE:openSUSE-Leap:42.3:latest                                  openSUSE-Leap        latest
RHEL           RedHat                  7-LVM               RedHat:RHEL:7-LVM:latest                                        RHEL                 latest
SLES           SUSE                    15                  SUSE:SLES:15:latest                                             SLES                 latest
UbuntuServer   Canonical               18.04-LTS           Canonical:UbuntuServer:18.04-LTS:latest                         UbuntuLTS            latest
WindowsServer  MicrosoftWindowsServer  2019-Datacenter     MicrosoftWindowsServer:WindowsServer:2019-Datacenter:latest     Win2019Datacenter    latest
WindowsServer  MicrosoftWindowsServer  2016-Datacenter     MicrosoftWindowsServer:WindowsServer:2016-Datacenter:latest     Win2016Datacenter    latest
WindowsServer  MicrosoftWindowsServer  2012-R2-Datacenter  MicrosoftWindowsServer:WindowsServer:2012-R2-Datacenter:latest  Win2012R2Datacenter  latest
WindowsServer  MicrosoftWindowsServer  2012-Datacenter     MicrosoftWindowsServer:WindowsServer:2012-Datacenter:latest     Win2012Datacenter    latest
WindowsServer  MicrosoftWindowsServer  2008-R2-SP1         MicrosoftWindowsServer:WindowsServer:2008-R2-SP1:latest         Win2008R2SP1         latest

# 下面列出OpenLogic发布的所有Centos镜像，这个公司就是为Azure用户提供CentOS。
az vm image list --all -p OpenLogic -f centos --output table
Offer         Publisher    Sku         Urn                                            Version
------------  -----------  ----------  ---------------------------------------------  --------------
CentOS        OpenLogic    6.10        OpenLogic:CentOS:6.10:6.10.20180709            6.10.20180709
CentOS        OpenLogic    6.10        OpenLogic:CentOS:6.10:6.10.20180803            6.10.20180803
CentOS        OpenLogic    6.10        OpenLogic:CentOS:6.10:6.10.20180822            6.10.20180822

az vm image list --all -p Canonical -f ubuntu --output table
az vm image list --all -p Debian -f debian --output table
az vm image list --all -p MicrosoftWindowsServer -f WindowsServer --output table

# 列出自定义VHD
az storage fs file list -f vhds --query '[*].name'

# 列出市场镜像
az vm image list --location westus --publisher vmlabinc1613642184700 --output table

Offer                       Publisher              Sku                                       Urn                                                                          Version
--------------------------  ---------------------  ----------------------------------------  ---------------------------------------------------------------------------  -------------
activemq                    vmlabinc1613642184700  activemq-centos                           vmlabinc1613642184700:activemq:activemq-centos:5.16.1                        5.16.1
activemq                    vmlabinc1613642184700  activemq-ubuntu                           vmlabinc1613642184700:activemq:activemq-ubuntu:5.16.1                        5.16.1
ansible                     vmlabinc1613642184700  ansible-ubuntu                            vmlabinc1613642184700:ansible:ansible-ubuntu:2.11.1                          2.11.1
awx                         vmlabinc1613642184700  ansible-awx-centos                        vmlabinc1613642184700:awx:ansible-awx-centos:17.1.0                          17.1.0
awx                         vmlabinc1613642184700  ansible-awx-ubuntu                        vmlabinc1613642184700:awx:ansible-awx-ubuntu:17.1.0                          17.1.0
canvas                      vmlabinc1613642184700  canvas-ubuntu                             vmlabinc1613642184700:canvas:canvas-ubuntu:2021.05.2623                      2021.05.2623
codeserver                  vmlabinc1613642184700  codeserver-centos                         vmlabinc1613642184700:codeserver:codeserver-centos:3.10.2                    3.10.2
docker                      vmlabinc1613642184700  docker-portainer-ubuntu                   vmlabinc1613642184700:docker:docker-portainer-ubuntu:2.1.1                   2.1.1

# 基于订阅的 VHD 创建服务器
# docs: https://docs.microsoft.com/en-us/powershell/module/azurerm.compute/set-azurermvmplan?view=azurermps-6.13.0&viewFallbackFrom=azurermps-6.6.0
az vm create -n akeneo-test -g networkwatcherrg --attach-os-disk akeneo-test_OsDisk_1_8a98e493bc144ffd8d68a62b8da35532  --os-type linux --location centralus  --plan-publisher Bitnami --plan-name '1-4' --plan-product Akeneo --image Bitnami:akeneo:1-4:3.2.1910031550

# Blob 更名
az storage fs file move -p metabase0.39.4-CentOS7.9-bug.vhd -f vhds --new-path vhds/metabase0.39.4-CentOS7.9.vhd  

# 上传到web容器下docs目录(web容器多了一个$)
az storage blob upload-batch -d '$web'/docs -s /root/docs --account-key 1KIIE --account-name w9support

# 上传到vhds容器下docs目录
az storage blob upload-batch -d vhds/docs -s /root/docs --account-key 1KIIE --account-name w9support

# 下载
az storage blob download-batch -d /data/wwwroot/backup/support-azure -s $web --account-key 1KIa --account-name w9support

# 查询扩展命令
az extension list-available --output table

# 安装，例如：azure-iot
az extension add --name azure-iot
```


## 问题解答

#### 虚拟机的登录账号是什么？

虚拟机账号和密码是用户在创建虚拟机的时候，自行设置的。  

#### 如何给存储配置CDN？

创建CDN，然后再CDN中绑定存储账号即可

#### 如何启用Linux系统的root账号？

Azure默认情况下，root账号是没有启用的，实际上我们参考：[启用root账号](../azure#enableroot)

#### 服务器的IP地址重启后发生变化怎么办？

建议更改为静态IP或为服务器设置一个由Azure提供的DNS

#### 查看 Websoft9 在 Azure 上的所有产品？

通过 [Websoft9镜像库](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?page=1&search=websoft9) 查看我们在Azure上的所有镜像，也可以通过搜索关键字“websoft9”列出

#### 虚拟机上的镜像是否可以更换？

不可以

#### 可否使用临时磁盘 (/dev/sdb1) 存储数据？

不要使用临时磁盘 (/dev/sdb1) 存储数据。 它只是用于临时存储。 有丢失无法恢复的数据的风险。

#### 托管磁盘与非托管磁盘有什么区别？

托管磁盘即用户的磁盘属于Azure磁盘集群中的一部分，非托管磁盘是用户存储账号下的磁盘。

#### 创建 VM 时，用户名和密码有格式要求吗？

Azure有较为明确的要求，具体参考[Azure用户名和密码要求](https://docs.microsoft.com/zh-cn/azure/virtual-machines/linux/faq#what-are-the-username-requirements-when-creating-a-vm)

#### 如何批量恢复误删的 blob?

下载[Microsoft Azure Storage Explorer](https://azure.microsoft.com/zh-cn/features/storage-explorer/)，安装连接登录后，参考下图恢复已删除的文件

![Azure 批量恢复文件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-storageexplorer-canceldel-websoft9.png)

> 恢复过程中可能会报错，需反复重试多次

#### 如何基于云市场来源的VHD磁盘创建VM？

问题描述：基于云市场的 VHD 创建 VM 时，会出现报错。错误信息大意是没有包含云市场的plan。  

解决方案：需要在编排模板的虚拟机属性中加入云市场镜像的计划，例如：

```
"plan": {
                "name": "wordpress52-lemp72-centos76",
                "publisher": "websoft9inc",
                "product": "w9wordpress2"}
```

设置 Plan 之前，需通过 PowerShell 命令获取 plan

```
PS Azure:\> az vm image list --offer w9wordpress2 --all --output table
Offer         Publisher    Sku                          Urn                                                             Version
------------  -----------  ---------------------------  --------------------------------------------------------------  ---------
w9wordpress2  websoft9inc  wordpress52-lemp72-centos76  websoft9inc:w9wordpress2:wordpress52-lemp72-centos76:5.2.20000  5.2.20000
```

#### 如何创建子账号？

1. 登录到Azure后台，在 Auzre Default Directory 中找到 AD 的域名
2. 在这个 AD 下创建一个账号
3. 在成本管理中，找到Pay-As-You-Go的订阅项，点击这个订阅项，为 AD 中的子账号分配权限

#### 资源配额不足？

可以在线申请资源，部分资源申请之后会自动创建一个支持工单，等待人工审批后配合才会增加。

#### Azure-cli 安装完成后，显示没有acs模块？

需额外安装：  
```
python3 -m pip install azure-cli-acs
```

#### Azure CLI 运行报错 NoRegisteredProviderFound？
错误信息：BadRequestError: (NoRegisteredProviderFound) No registered resource provider found for location 'all' and API version '2020-06-01' for type 'locations/publishers'. The supported api-versions are '2015-05-01-preview, 2015-06-15, 2016-03-30, 2016-04-30-preview, 2016-08-30, 2017-03-30, 2017-12-01, 2018-04-01, 2018-06-01, 2018-10-01, 2019-03-01, 2019-07-01, 2019-12-01, 2020-06-01, 2020-09-30, 2020-12-01, 2021-03-01'. The supported locations are 'eastus, eastus2, westus, centralus, northcentralus, southcentralus, northeurope, westeurope, eastasia, southeastasia, japaneast, japanwest, australiaeast, australiasoutheast, australiacentral, brazilsouth, southindia, centralindia, westindia, canadacentral, canadaeast, westus2, westcentralus, uksouth, ukwest, koreacentral, koreasouth, francecentral, southafricanorth, uaenorth, switzerlandnorth, germanywestcentral, norwayeast, jioindiawest'.  

问题原因：当前程序无法支持所有地区的API类型  
解决方案：设置默认区域  

```
python3 -m pip install azure-cli-acs
```

