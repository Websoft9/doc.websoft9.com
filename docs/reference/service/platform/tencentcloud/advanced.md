---
sidebar_position: 3
slug: /tencentcloud/advanced
---

# 进阶

## 核心原理

### API/CLI

腾讯云的[命令行工具](https://cloud.tencent.com/document/product/440)与其 API 调用的参数是一致的，这一点做得非常好。

* 在线的API调试工具：[API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer)
* 地域分布[查看](https://cloud.tencent.com/document/product/213/6091)

#### 配置

一条交互式命令即可配置
```
$ tccli configure
TencentCloud API secretId [*afcQ]:AKIDwLw1234xxxxxxe2g9nR2OTI787aBCDP
TencentCloud API secretKey [*ArFd]:OxXj7khcV1234xxxxxxABcdCc1LiArFd
region: ap-guangzhou
output[json]:
```

#### 常见命令
```
# 查询当前区域的zones
tccli cvm DescribeZones

# 查询镜像
tccli cvm DescribeImages  --Filters '[{"Name":"image-type","Values":["PUBLIC_IMAGE"]}]' \
    --filter  'ImageSet[*].{name:ImageDescription, id:ImageId, cloudin: IsSupportCloudinit, at:Architecture}'

# 使用SPOTPAID（竞价实例）类型创建服务器
        'vm_createVM_template':'tccli cvm RunInstances \
            --InstanceChargeType SPOTPAID \
            --InstanceMarketOptions \'{"MarketType":"spot","SpotOptions":{"MaxPrice":"5"}}\' \
```


## 常见问题

#### 如何启用Linux系统的root账号？

腾讯云默认已经开启root账号

#### 如何列出Websoft9在腾讯云云市场上的所有产品？

通过 [Websoft9腾讯云店铺](https://market.cloud.tencent.com/stores/1252192180) 查看我们在腾讯云上的所有镜像，也可以通过搜索关键字“websoft9”列出

#### 如何通过腾讯云控制台获取镜像文档？

登录[云市场控制台](https://console.cloud.tencent.com/servicemarket/services)，找到订单，通过订单详情页面进入镜像的前台商品页面。文档链接在商品页面详情第一行。

#### 腾讯云磁盘支持扩容吗？

腾讯云支持在线扩容***数据盘**，即无需重启CVM实例便可以完成扩容。系统只能通过重装系统的时候扩容。

#### 本地磁盘和云硬盘的区别？
云硬盘是一种弹性、高可用、可定制化的网络块设备，可以作为云服务器的独立可扩展硬盘使用。 

本地盘来自 CVM 实例所在物理机的本地存储，是从 CVM 实例所在的物理机上划分的一块存储区域。  

两者的主要区别[参考](https://cloud.tencent.com/document/product/213/4952)

#### 如何在无需付出高成本的情况下享受服务器的高带宽（>100M）?

只要服务器的带宽付费方式为**按流量计费**即可享受最大100M的带宽，付费方式是后付费

#### 重装系统有什么要注意的？

重装系统提供以用户选择的镜像进行重装系统的功能，换操作系统会清除系统盘数据，包括系统盘上的系统分区和所有其它分区，请做好数据备份。

#### 购买云市场的商品后如何开票？

云市场商品的发票由各服务商开具，如您需要申请开票，请在发票管理 > [云市场](https://console.cloud.tencent.com/expense/invoice?tab=CloudMarket) 页面申请，开取云市场发票，详情请参见 发票申请流程

发票相关问题可以参考 [发票相关问题](../order)。

#### 重装系统很慢或者失败怎么办？

重装系统一般需要的时间是：操作后10 ~ 30 分钟。

- 若系统重装时间较久但未超过 30 分钟，请您耐心等待；
- 若重装系统时间过长甚至失败了，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系腾讯云。

#### 重装系统是否会丢失数据？

重装系统后，服务器系统盘内的所有数据将被清除，恢复到初始状态；服务器数据盘的数据不会丢失，但需要手动挂载才能使用。

#### 云服务器系统盘默认空间多大？

目前，新购的云服务器系统盘默认空间50GB。

#### 能否将云服务器的系统盘由本地硬盘换成云硬盘？
当您购买的云服务器所在可用区有可用的云硬盘时，您可以使用 [调整硬盘介质](https://cloud.tencent.com/document/product/213/31978) 功能将系统盘由本地硬盘转换为云硬盘。

#### 重装系统时，云服务器系统盘是否支持扩容？

分为以下两种情况，请根据您的实际情况参考：

- **系统盘为云硬盘：**
重装系统时，支持扩容（调高系统盘大小），不支持缩容（降低系统盘大小）。
- **系统盘为本地硬盘：**
重装系统时，根据当前系统盘的大小，分为两种情况：
   - 购买时系统盘默认空间为50GB的实例，不支持扩容。
   - 该情况适用于早期购买的实例：系统盘空间小于或等于20GB，将默认重装至20GB；系统盘空间大于20GB，将默认重装至50GB。

#### 如何让我保存云服务器实例当前的数据并扩容系统盘？

可以选择先制作镜像，再通过镜像重装系统，从而达到扩容系统盘的目的。

#### 如何搭建FTP？

具体 FTP 部署方式您可以参考：

- Windows ： [搭建 FTP 服务](https://cloud.tencent.com/document/product/213/10414)
- Linux： [搭建 FTP 服务](https://cloud.tencent.com/document/product/213/10912)

#### 使用 SSH 密钥登录还可以同时使用密码登录吗？

用户使用 SSH 密钥对登录 Linux 实例，默认禁用密码登录，以提高安全性，所以密钥登录后用户将不能再使用密码登录。

#### 云服务器常用端口有哪些？

请参考 [服务器常用端口](https://cloud.tencent.com/document/product/213/34601)。