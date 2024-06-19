---
sidebar_position: 1.1
slug: /iaas-azure
---

# Azure

本章为在 Azure 上使用 Websoft9 托管平台的用户提供 Azure 操作的快速指南。

## 快速参考

### 创建 VM{#create-vm}

Azure 支持多种创建 VM 的来源：

- 基于创建创建 VM
- 基于系统盘创建，包括磁盘和 VHD

### 启用 root 账号{#enable-root}

Azure 默认没有开放 Linux 系统的 `root` 账号。如果您希望使用 root 账号，通过下面的步骤启用之：

1. 登录 Azure 控制台，在控制台在线连接 VM

2. 分别运行下面的命令
    ```
    sudo su
    sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
    sudo systemctl restart sshd
    sudo passwd root
    ```

### 管理磁盘{#disk}

Azure VM 提供方便的磁盘管理项：

- 支持动态扩容系统盘和数据盘
- 支持[附加数据盘](https://learn.microsoft.com/zh-cn/azure/virtual-machines/linux/attach-disk-portal#connect-to-the-linux-vm-to-mount-the-new-disk)
- 支持分离数据盘
- 支持托管磁盘与非托管磁盘之间的转换
- 支持磁盘转成快照
- 支持磁盘（VHD）下载

### 管理 Azure 存储

Azure 存储是 Microsoft 托管的一项关键服务，它提供高度可用、安全、持久、可缩放且冗余的云存储。    

Azure 存储包括 Azure Blob (对象)、Azure Data Lake Storage Gen2、Azure 文件存储、Azure 队列和 Azure 表   

### 管理 IP 与域名{#ip-domain}

- 支持静态 IP 和动态 IP
- 支持动态绑定 IP 到 VM
- 支持为 VM 设置[子域名](https://learn.microsoft.com/en-us/azure/dns/dns-alias)访问 `your_alias.centralus.cloudapp.azure.com`

### 设置安全组{#security-group}

Azure 控制台提供了对网络安全的直接设置：**虚拟机控制台 > 网络 > 网络设置**。

同时，也支持**应用程序安全组（Application Security Groups，ASG）** 这种分组的安全策略。  

### Azure CLI

使用 Websoft9 托管应用时可能用到的 [Azure CLI](https://learn.microsoft.com/zh-cn/cli/azure/what-is-azure-cli) 命令。  

- 查询 Websoft9 镜像

    ```
    az vm image list --location westus -p vmlabinc1613642184700 --output table
    ```

- 查询基于操作系统镜像
   ```
    az vm image list --all -p Canonical -f ubuntu --output table
    az vm image list --all -p Debian -f debian --output table
    az vm image list --all -p MicrosoftWindowsServer -f WindowsServer --output table
   ```

- 基于镜像创建 VM
  ```
  # docs: https://docs.microsoft.com/en-us/powershell/module/azurerm.compute/set-azurermvmplan?view=azurermps-6.13.0&viewFallbackFrom=azurermps-6.6.0
    az vm create -n akeneo-test -g networkwatcherrg --attach-os-disk akeneo-test_OsDisk_1_8a98e493bc144ffd8d68a62b8da35532  --os-type linux --location centralus  --plan-publisher Bitnami --plan-name '1-4' --plan-product Akeneo --image Bitnami:akeneo:1-4:3.2.1910031550
  ```


## 配置选项

- Azure 控制台连接 VM（√）：**虚拟机控制台 > 连接**

- VM 备份（√）：[Azure Backup](https://azure.microsoft.com/en-us/products/backup/)

- VM 规格调整（√）：**虚拟机控制台 > 可用性 + 缩放 > 大小**

- VM 重置到初始状态（√）：**虚拟机控制台 > 支持与疑难解答 > 重新部署**

- 默认账号：创建 VM 时，需自行填写用户名和密码（密钥对）

- 竞价实例（√）

- VM 更换镜像（×）

- VM 用户名和密码[规范](https://learn.microsoft.com/zh-cn/azure/virtual-machines/linux/faq#what-are-the-username-requirements-when-creating-a-vm)


## 相关文档

- [Azure 上部署 Websoft9](./install/azure)
- [Azure 虚拟机官方文档](https://learn.microsoft.com/zh-cn/azure/virtual-machines/)
- [Azure Blob 存储官方文档](https://learn.microsoft.com/zh-cn/azure/storage/blobs/)
- [Azure 存储账号](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal)
- [Azure CLI](https://learn.microsoft.com/zh-cn/cli/azure/what-is-azure-cli)


## 故障
