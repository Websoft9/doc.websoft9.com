---
sidebar_position: 1
slug: /install/azure
---

# Azure

Websoft9 在 Azure 的提供了预制[云市场镜像](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=vmlab&page=1)，用户可以通过购买的方式实现自动化安装部署 Websoft9 多应用托管平台。

下面的教程介绍如何在 Azure 上部署 Websoft9。

## 先决条件

必须拥有 Azure 的账号：

- 如果你或你的公司已经有一个订阅帐户，请使用该帐户
- 如果没有，可以免费[开设自己的 Azure 帐户](https://azure.microsoft.com/en-us/free/)，Azure 的免费试用版提供 200 美元的信用额度

## 规划虚拟机配置

先阅读 [Websoft9 安装要求](./requirements)，了解所需的服务器规格、存储和带宽要求。 

另外，在 Azure 上部署 Websoft9 时，需要填写重要的配置参数，下面先提前说明：

- 操作系统磁盘类型，请选择 **SSD** 相关类型
- 安全组端口开启：80, 443, 9000
- 身份验证：密钥对或密码均可

## 安装 Websoft9

一旦您注册了 Azure 的账号，您可以通过如下多种方式安装 Websoft9：

### 基于界面向导安装

Azure 提供了三种部署虚拟机镜像的入口界面：

- [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps)
  ![搜索Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-mkss-websoft9.png)

- Azure 后台门户（Portal）

  - Portal > "创建资源"，检索 Websoft9 镜像
    ![Azure Portal 搜索镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-portalmk-websoft9.png)

  - Portal > "创建虚拟机" > "浏览所有镜像"，检索 Websoft9 镜像
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-vmimage-websoft9.png)

不管哪种入口，最终的操作都是一致的：**基于预制的 Websoft9 镜像创建虚拟机**

### 基于 API/CLI 安装

即将推出

### 基于编排模板安装

1. 提前准备部署模板

2. 登录 Azure 门户，将部署模板导入运行

### 基于 VHD 安装

如果用户已有一个包含 Websoft9 的 VHD，那么也可以基于此 VHD 创建新建，重新部署 Websoft9

1. 在 Azure 上运行 PowerShell 命令获取 Websoft9 镜像的 plan
   ```
   PS Azure:\> az vm image list --offer w9wordpress2 --all --output table
   Offer         Publisher    Sku                          Urn                                                             Version
   ------------  -----------  ---------------------------  --------------------------------------------------------------  ---------
   w9wordpress2  websoft9inc  wordpress52-lemp72-centos76  websoft9inc:w9wordpress2:wordpress52-lemp72-centos76:5.2.20000  5.2.20000
   ```

2. 在编排模板的虚拟机属性中加入云市场镜像的计划
   ```
   "plan": {
                  "name": "wordpress52-lemp72-centos76",
                  "publisher": "websoft9inc",
                  "product": "w9wordpress2"}
   ```

3. 基于编排模板重新部署 Websoft9

## 完成虚拟机部署

选用以上任意安装方式，Azure 都会开始部署新的 VM。  

部署过程需要几分钟才能完成。完成后，通过 Azure 的仪表板查看新的 VM 的信息。  

## 后续配置 Websoft9

VM 可用之后，还需要[完成配置域名等后续操作](./setup)，方可使用更好的使用 Websoft9