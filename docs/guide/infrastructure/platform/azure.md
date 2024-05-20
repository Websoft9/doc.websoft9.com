---
sidebar_position: 1.1
slug: /iaas-azure
---

# Azure

Websoft9 与 Azure 进行了深度集成，便于用户以多种方式使用 Websoft9：

- 
- 将 Azure 上已有的虚拟机集成到 Websoft9 控制台，以方便在 Azure 虚拟机上运行更多的应用

不管使用哪一种方式使用 Websoft9，用户都需要

## 在 Azure 上安装 Websoft9

- 最简单的方式是在 Azure 平台上以**购买即使用**的方式[快速使用 Websoft9](./install/azure)
- 也可以在 Azure 上购买虚拟机，然后[安装](./install)并自托管 Websoft9 

## 附加 Azure 虚拟机到 Websoft9

## 备份

## Azure 操作参考

- SSH 登录方式：密码或密钥对
- 在线 Web 终端连接到虚拟机（√）：
- 竞价实例（√）
- 

## 问题与故障

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

