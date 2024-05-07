---
sidebar_position: 2
slug: /install/aws
---


# AWS


Websoft9 在 AWS 的云市场上提供了丰富的应用和解决方案，用户可以通过购买的方式实现自动化安装部署。

- [Websoft9 on AWS](https://aws.amazon.com/marketplace/seller-profile?id=c639a579-182c-4d30-8578-4d4d89fba658)

> 我们是全球为数不多能够支持中英文产品和服务的云原生技术商。

## 安装

一旦您注册了 AWS 的账号，您可以通过如下多种方式安装我们的产品：

### Marketplace部署

1. 访问 [AWS Marketplace](https://aws.amazon.com/marketplace) 网站

2. 搜索关键字"websoft9"，网站会列出所有相关的镜像
   ![搜索Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-mkss-websoft9.png)  

3. 点击您所需的产品（以 Odoo 为例），进入产品详情页后点击"Continue to Subscribe"开始订阅镜像
   ![开始订阅镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-rs-websoft9.png)

4. 根据系统提示，接受许可协议（Terms and Conditions）

5. 待系统提示订阅成功后，点击“Continue to Configuration” 准备EC2创建前的检查
   ![配置镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-cc-websoft9.png)

5. 检查镜像、版本和地区无误后，点击“Continue to Launch”开始创建EC2
   ![开始载入镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-imagecreate-websoft9.png)

6. 创建EC2过程中，系统会提示您选择三种后续动作
   ![开始载入镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-imagecreate2-websoft9.png)

   - Launch through EC2 （推荐）
   - Launch from Website
   - Copy to Service Catalog

7. 后续动作基本都会要求用户完成：选择实例类型、VPC、Key Pair等设置

8. 等待几分钟，EC2创建完成后，镜像会作为EC2实例的系统盘启动，即镜像自动部署到实例中


### EC2部署

1. 登录到AWS管理控制台，点击“EC2”，
   ![进入ec2控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-ec2-websoft9.png)

2. 进入EC2控制面板，点击“启动实例”，即开始创建一个新的实例
   ![启动实例](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-addec2-websoft9.png)

3. 在映像一栏，点击“浏览所有公用和专用映像”，然后搜索关键件词“websoft9”，列出相关镜像
   ![选择Websoft9镜像](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-ec2image-websoft9.png)

4. 选择一个你所需的镜像，系统提示订阅，点击【Continue】，开始创建EC2实例
   ![同意订阅](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-createdec2-imageselected-websoft9.png)

5. 后续动作基本都会要求用户完成：选择实例类型、增加存储、配置安全组、设置秘钥对等设置
   ![创建EC2](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-createdec2-chooseinstances-websoft9.png)

6. 等待几分钟，EC2创建完成后，镜像会作为EC2实例的系统盘启动，即镜像自动部署到实例中

### 部署非默认版本

每个商品支持多个版本，默认为最新版本，也可以通过下面的步骤修改版本：

1. 选择镜像时，先点击【Previous version】链接
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-subs-odoo-websoft9.png)

2. 通过【Software version】下拉菜单选择你所需的版本
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-subs-odoooldversion-websoft9.png)


## 安装后