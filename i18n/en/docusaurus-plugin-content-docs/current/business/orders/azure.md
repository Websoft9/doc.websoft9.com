---
sidebar_position: 1
slug: /order/azure
---

# Azure 订单

在Azure平台中，镜像部署完成后，就产生了相关的订单

## 费用预估

订阅=购买，Azure平台中，由于虚拟机采用的是按小时计费，故镜像产品采用的是也是按小时计费模式，除此之外没有其他模式。

Azure 上的产品计费有如下几个维度：

* 镜像部署到虚拟机后，虚拟机用多长时间=镜像订阅了多长时间
* 需要取消镜像订阅，就需要删除对应的虚拟机
* 虚拟机停止运行，镜像仍然计费
* 虚拟机CPU核数来灵活定价，一般来说核数越大，价格越高。

以我们发布的Gitlab商品为例，通过商品页面的 Plans+Pricing，列出的Software Cost就是镜像定价

![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-fee-websoft9.png)


## 查看订阅

1. 登录Azure控制台，打开：所有服务->常规->市场，进入门户中云市场频道
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-mkbackend-websoft9.png)
2. 点击“最近创建的内容”，查看已经安装的镜像

## 获取发票

镜像类发票，可以在Azure平台上下载：

1. 登录Azure控制台门户
2. 打开成本管理+计费栏目->发票，选择“Azure市场和预留”选项卡，并选择一种需要发票的订阅号
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-getinvoice0-websoft9.png)

3. 系统会根据选择自动生成发票，点击“下载发票”即可
    ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/azure/azure-getinvoice-websoft9.png)

## 评价产品

对于使用过的镜像商品，您可以给与评价，千万记得给我们好评哦

![img](https://libs.websoft9.com/Websoft9/DocsPicture/en/azure/azure-review-websoft9.png)