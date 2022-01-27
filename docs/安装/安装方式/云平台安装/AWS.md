# AWS

[Websoft9](https://www.websoft9.com) 已经在 AWS Marketplace 上提供了多款镜像（**AWS 称镜像为 AMIs**），覆盖常用的云场景，已经收到用户的良好反馈。

>  是不是想了解有哪些优质的镜像呢？点击 [此处](https://aws.amazon.com/marketplace/seller-profile?id=c639a579-182c-4d30-8578-4d4d89fba658) 查看Websoft9在AWS上发布的所有镜像。

那么如何在AWS上使用这些镜像呢？有两种方法：

## Marketplace部署

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


## EC2部署

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


> 除了镜像订阅部署之外，你还可以通过我们发布到 [Github](https://github.com/websoft9)上的 Ansible 脚本，来实现自动部署。