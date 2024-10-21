---
sidebar_position: 1.5
slug: /iaas-tencentcloud
---

# 腾讯云

本章为在 腾讯云 上使用 Websoft9 托管平台的用户提供 腾讯云 操作的快速指南。

## 快速参考

### 创建 CVM 服务器{#create-cvm}

腾讯云 支持多种创建 CVM 服务器的方式，包括：

- 腾讯云控制台
- 腾讯云 CLI/API/SDK
- [Terraform](https://cloud.tencent.com/product/iatf)

但是，任何一种方式均需要为 CVM 选用或准备所需的镜像

### 管理磁盘{#disk}

腾讯云 CVM 提供了丰富的磁盘类型和磁盘管理功能：  

- 磁盘可以从服务器分离
- 支持在线扩容系统盘和数据盘，即无需重启 CVM 实例便可以完成扩容
- 卷转换成快照，快照转换成镜像

### 管理 IP 与域名{#ip-domain}

- 支持静态 IP 和弹性 IP
- 提供域名注册与管理产品服务

### 设置安全组{#security-group}

腾讯云 控制台提供了对[安全组](https://cloud.tencent.com/document/product/215)的直接设置：**网络与安全 > 安全组**


### 腾讯云 CLI

使用 Websoft9 托管应用时可能用到的 [腾讯云 CLI](https://console.cloud.tencent.com/api/explorer) 命令。  

- 查询镜像
    ```
    tccli cvm DescribeImages  --Filters '[{"Name":"image-type","Values":["PUBLIC_IMAGE"]}]' \
    --filter  'ImageSet[*].{name:ImageDescription, id:ImageId, cloudin: IsSupportCloudinit, at:Architecture}'
    ```

- 创建服务器

  ```
  tccli cvm RunInstances --InstanceChargeType SPOTPAID --InstanceMarketOptions '{"MarketType":"spot","SpotOptions":{"MaxPrice":"5"}}' 
  ```

## 配置选项

- 在线连接 CVM（√）：**云服务器控制台> 登录**

- 在线生成并存储密钥对（√）

- CVM 备份、磁盘备份（√）

- CVM 规格调整（√）：**云服务器控制台> 资源调整 > 调整配置**

- CVM 重置到初始状态（√）**云服务器控制台> 操作 > 重装系统**

- CVM 更换镜像（√）

- CVM 控制台重置密码（√）

- 竞价实例（√）

- 系统盘和数据盘在线扩容（√）


## 相关文档

- [腾讯云 上部署 Websoft9](./install-tencentcloud)
- [腾讯云 CVM 官方文档](https://cloud.tencent.com/document/product/213)
- [腾讯云 CLI](https://cloud.tencent.com/document/product/440)
- [腾讯云地区和终端节点](https://cloud.tencent.com/document/product/213/6091)
- [域名备案](https://cloud.tencent.com/product/ba)

## 故障