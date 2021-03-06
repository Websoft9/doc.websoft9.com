---
sidebar_position: 3
slug: /install/alibabacloud
---

# 阿里云

Websoft9 在阿里云的云市场上提供了丰富的应用和解决方案，用户可以通过购买的方式实现自动化安装部署。

- [Websoft9 on 阿里云](https://shop658hlt17.market.aliyun.com)
- [Websoft9 on AlibabaCloud](https://marketplace.alibabacloud.com/store/2116499.html)

> 我们是全球为数不多能够支持中英文产品和服务的云原生技术商。

## 安装

一旦您注册了阿里云的账号，您可以通过如下多种方式安装我们的产品：

### 云市场安装

1. 访问 [阿里云云市场](https://shop658hlt17.market.aliyun.com/) 网站 或 [Websoft9店铺地址](https://shop658hlt17.market.aliyun.com/)

2. 搜索关键字"websoft9"，网站会列出所有相关的镜像
   ![搜索Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-buywebsoft9.gif) 

3. 点击您所需的产品，进入产品详情页后点击"立即购买"按钮，镜像已经购买完成
7. 接下来系统会自动要求购买一台新服务器：选择计费方式、实例类型、网络和安全组等设置
8. 等待几分钟，ECS创建完成后，镜像会作为ECS实例的系统盘启动，即镜像自动部署到实例中


### 创建实例安装

购买ECS或控制台创建实例过程中，可以选择Websoft9的镜像作为系统启动盘

1. 登录到阿里云管理控制台->ECS，点击“创建实例”，
   ![进入ecs控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-createecs-websoft9.png)
2. 在镜像一栏，选择镜像市场->从镜像市场获取更多选择（含操作系统）。
3. 然后搜索关键件词“websoft9”，列出相关镜像
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-searchw9image-websoft9.png)

4. 选择一个你所需的镜像，开始创建ECS实例
5. 后续动作基本都会要求用户完成：选择计费方式、实例类型、网络和安全组等设置
6. 等待几分钟，ECS创建完成后，镜像会作为ECS实例的系统盘启动，即镜像自动部署到实例中

### 更换系统盘安装

镜像除了可以在创建新服务器之时购买，针对已有服务器，也可以通过更换系统盘的方式使用镜像。

> 需要注意的是，重装系统意味着系统数据全部会格式化，所以请注意做好数据的备份。

1. 登录到阿里云管理控制台，在”实例“中先停止服务器，依次选择：更多->磁盘和镜像->更换系统盘 
   ![更换系统盘](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-changesysdisk-websoft9.png)

2. 确认更换后，镜像类型选择“镜像市场”，然后输入搜索关键字”websoft9“，根据提示设置新密码
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-searchw9image-websoft9.png)

3. 请耐心等待几分钟，直至更换完成

除了镜像订阅部署之外，你还可以通过我们发布到 [Github](https://github.com/websoft9)上的 Ansible 脚本，来实现自动部署。

## 安装后

以上安装完成后，软件就自动化部署到您的服务器中。获取服务网公网 IP 之后，您便可以访问软件。

### 获取服务器公网 IP

参考...

### 查看已购买

1. 登录阿里云控制台，找到云市场频道
2. 默认列出“已购买的服务”
   ![img](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-mkservices-websoft9.png)
2. 每个服务可以看到：付费方式，服务商，联系方式，使用指南等信息
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-getdocfromorder-websoft9.png)


## 常见问题

#### 中国地区用户可以使用 AlibabaCloud Marketplace 吗？

可以，参考如下流程：

1. 注册账号流程中，有一个增加付款账号，建议选择美国地区
2. 然后绑定非中国大陆地区信用卡

#### 支持哪些计费模型？

我们在阿里云上支持按量（按小时）付费、包年包月付费、按次付费等多种模式。
