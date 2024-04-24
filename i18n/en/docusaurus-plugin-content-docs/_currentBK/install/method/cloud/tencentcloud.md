---
sidebar_position: 5
slug: /install/tencentcloud
---

# Tencent Cloud

Websoft9 is Partner of Tencent Cloud Marketplace, you can install [Websoft9 product on Tencent Cloud](https://market.cloud.tencent.com/stores/1252192180) very conveniently.  

## Installation

一旦您注册了腾讯云的账号，您可以通过如下多种方式安装我们的产品：

### 云市场部署

1. 访问 [腾讯云云市场](https://market.cloud.tencent.com/search/websoft9) 网站 或 [Websoft9店铺地址](https://market.cloud.tencent.com/stores/1252192180)

2. 搜索关键字"websoft9"，网站会列出所有相关的镜像
   ![搜索Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-simagefrommk-websoft9.png) 

3. 进入产品详情页后点击"立即购买"按钮，镜像就选好了
   ![立即购买](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-buyimage-websoft9.png) 

4. 接下来系统会自动要求购买一台新服务器：选择计费模式、地域、规格、网络和安全组等设置
   ![立即购买](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-buyimagebuycvm-websoft9.png) 

   > 购买服务器过程中请勿再次选择镜像

5. 等待几分钟，CVM创建完成后，镜像会作为CVM实例的系统盘启动，即镜像自动部署到实例中




### 购买服务器部署

购买CVM或控制台创建实例过程中，可以选择Websoft9的镜像作为系统启动盘

1. 登录腾讯云控制台->云服务器，点击“新建”，
   ![进入ecs控制台购买服务器](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-buyecs-websoft9.png)
2. 购买的第二步，选择镜像选择“镜像市场”
   ![进入ecs控制台购买服务器](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-selectmkimage-websoft9.png)
3. 然后搜索关键件词“**websoft9**”，列出相关镜像
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-selectimage-websoft9.png)

4. 选择一个你所需的镜像，开始创建CVM实例
6. 等待几分钟，CVM创建完成后，镜像会作为CVM实例的系统盘启动，即镜像自动部署到实例中

### 重装系统部署

镜像除了可以在创建新服务器之时购买，针对已有了服务器，也可以通过**重装系统**的方式使用镜像。

> 需要注意的是，重装系统意味着系统数据全部会格式化，所以请注意做好数据的备份。

1. 登录到腾讯云控制台，在“实例”中关机，然后选择：更多->重装系统 
   ![重装系统](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-changesysdisk-websoft9.png)

2. 确认更换后，镜像选择“服务市场”，搜索关键字“**websoft9**”，列出相关镜像
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/qcloud/qcloud-changeimage-websoft9.png)

3. 确认好所选镜像，重设操作系统密码

4. 请耐心等待几分钟，直至更换完成

## After installation

Here are a few resources you might want to check out after completing the installation on Cloud.

* [Get the Internet IP of VM](../tencentcloud#ip)
* [View purchased orders](../order/tencentcloud#listorders)