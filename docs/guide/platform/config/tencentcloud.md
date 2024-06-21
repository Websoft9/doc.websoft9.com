---
sidebar_position: 1.5
slug: /iaas-tencentcloud
---

# 腾讯云

本章为在 腾讯云 上使用 Websoft9 托管平台的用户提供 腾讯云 操作的快速指南。

## 快速参考

### 创建 ECS{#create-ecs}

腾讯云 支持多种创建 ECS 服务器的方式，包括：

- 腾讯云控制台
- 腾讯云 CLI/API/SDK
- [Terraform](https://www.huaweicloud.com/product/aos.html)

但是，任何一种方式均需要为 ECS 选用或准备所需的镜像

### 管理磁盘{#disk}

腾讯云 ECS 提供了丰富的磁盘类型和磁盘管理功能：  

- 磁盘可以从服务器分离
- 支持在线扩容系统盘和数据盘，即无需重启 ECS 实例便可以完成扩容
- 卷转换成快照，快照转换成镜像
- 支持数据盘


### 管理 IP 与域名{#ip-domain}

- 支持静态 IP 和弹性 IP
- 支持动态弹性 IP 到 ECS
- 提供域名注册与管理产品服务
- 弹性公网 IP 


### 设置安全组{#security-group}

腾讯云 控制台提供了对[安全组](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0030878383.html)的直接设置：**操作 > 网络/安全组 > 安全组规则配置**


### 腾讯云 CLI

使用 Websoft9 托管应用时可能用到的 [腾讯云 CLI](https://support.huaweicloud.com/hcli/index.html) 命令。  

- 查询镜像
    ```
    # 查询公共镜像
    hcloud IMS ListImages --cli-region="ap-southeast-1" --__imagetype="gold"

    # 查询镜像信息
    hcloud IMS ListImages --cli-region="ap-southeast-1" --__imagetype="private" --name="image-name"
    ```

- 创建服务器

  ```
  hcloud ECS CreatePostPaidServers --cli-region="ap-southeast-1" --server.key_name="websoft9_auto" --server.security_groups.1.id="14e9ce31-0378-4785-8e03-a43ec78f12b9" --server.availability_zone="ap-southeast-1b" --server.vpcid="943bc887-3340-4219-bf9d-8265d8cef1d2" --server.name="test-cdl" --server.nics.1.subnet_id="4105cc19-20dd-4be5-b03c-50734cdf9248" --server.root_volume.volumetype="SSD" --server.flavorRef="c3.large.2" --server.publicip.eip.bandwidth.size=300 --server.publicip.eip.bandwidth.sharetype="PER" --server.publicip.eip.iptype="5_bgp" --server.imageRef="5be19e6d-80ef-4e9d-96a2-ec1b8438065d"
  ```

## 配置选项

- 在线连接 ECS（√）：**云服务器控制台> 远程连接**

- 在线生成并存储密钥对（√）

- 鲲鹏服务器部署（√）

- ECS 备份、磁盘备份（√）：[腾讯云 CBR 服务](https://www.huaweicloud.com/product/cbr.html)

- ECS 规格调整（√）：**云服务器控制台> 操作 > 升降配**

- ECS 重置到初始状态（√）**云服务器控制台> 操作 > 重装系统**

- ECS 更换镜像（√）

- ECS 控制台重置密码（√）

- 竞价实例（√）

- 系统盘和数据盘在线扩容（√）


## 相关文档

- [腾讯云 上部署 Websoft9](./install/huaweicloud)
- [腾讯云 ECS 官方文档](https://support.huaweicloud.com/ecs/index.html)
- [腾讯云 CLI](https://support.huaweicloud.com/hcli/index.html)
- [腾讯云地区和终端节点](https://developer.huaweicloud.com/endpoint)
- [域名备案](https://beian.huaweicloud.com/)

## 故障

#### CLI 创建的秘钥控制台不显示？

腾讯云 CLI 创建的密钥对只能被创建者单独使用，故不显示在控制台