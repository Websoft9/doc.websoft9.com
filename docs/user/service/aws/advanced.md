---
sidebar_position: 3
slug: /aws/advanced
---

# 进阶

## 核心原理

### API/CLI

AWS 提供了原生 API/CLI 。 

- [AWS CLI 命令](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html)
- [AWS CLI 用户手册](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
- 其他非官方：[入门参考](https://razeencheng.com/post/tool-awscli-overview-1.html)、[常用命令](https://www.studytrails.com/amazon-aws/create-aws-ec2-instance-using-cli/)、[15个常见命令](https://www.thegeekstuff.com/2016/04/aws-ec2-cli-examples/)

#### 配置

提前准备好访问秘钥，然后运行命令 aws configure 即可 

#### 角色管理

如果使用 [aws ssm](https://docs.aws.amazon.com/zh_cn/systems-manager/latest/userguide/ssm-agent.html) 命令，就需要将服务器授权给 AmazonSSMRoleForInstancesQuickSetup 这个角色

```
--iam-instance-profile Arn="arn:aws:iam::797851739507:instance-profile/AmazonSSMRoleForInstancesQuickSetup"
```
#### 常用命令

```
# 安装
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# 版本
aws --version

# 配置
aws configure

# 配置文件使用
aws s3 ls --profile profilename

# 帮助
aws help

# 等待另一个命令完成
aws deploy wait deployment-successful --deployment-id d-A1B2C3111

# 获取镜像ID
aws ec2 describe-images --owners amazon  --filters "Name=architecture,Values=x86_64" "Name=image-type,Values=machine" "Name=root-device-type,Values=ebs" --region us-east-1  --query 'Images[*].[ImageId,Description,Name]' 


# 创建子网
aws ec2 create-default-subnet --availability-zone us-east-2a

# 创建实例
aws ec2 run-instances
--instance-market-options "MarketType=spot,SpotOptions={SpotInstanceType=persistent,InstanceInterruptionBehavior=stop}"     
      --image-id ami-0947d2ba12ee1ff75 --count 1            --instance-type t3a.medium            --key-name websoft9_auto   
	  --security-group-ids sg-1240356f            --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=docker0-AmazonLinux2}]"  
	  --block-device-mappings "DeviceName=/dev/xvda,Ebs={VolumeSize=40}"       
	  --iam-instance-profile Arn="arn:aws:iam::797851739507:instance-profile/AmazonSSMRoleForInstancesQuickSetup"
```

## 问题解答

#### 实例的登录账号密码是什么？ 

Windows实例的账号名称是`Administrator`，Linux实例的账号与发行版相关，具体[参考](../user/cloud#osaccount)   

密码是用户在创建实例的时候，AWS 只支持秘钥对方式

#### root 账号可用吗？

root 账号默认启用的，实际上我们可以想办法启用它。参考：[启用root账号](../aws#connectlinux)

#### 服务器的IP地址重启后发生变化怎么办？

建议更改为静态IP或为服务器设置一个由AWS提供的DNS

#### 如何查看 Websoft9 在 AWS 上所有产品？

* 方式一：通过 [Websoft9 店铺 on AWS](https://aws.amazon.com/marketplace/seller-profile?id=c639a579-182c-4d30-8578-4d4d89fba658) 查看

* 方式二：AWS Marketplace 搜索关键字 **Websoft9** 列出

#### 实例上的镜像是否可以更换？

不可以

#### 实例存储与EBS存储有什么区别？

实例存储是一种理想的临时存储解决方案，非常适合存储需要经常更新的信息，如缓存、缓冲、临时数据和其他临时内容，或者存储从一组实例上复制的数据，如 Web 服务器的负载均衡池。

EBS存储是固定的块级存储，可以单独创建后绑定到EC2，也可以从EC2解绑而不丢失数据

#### 我能创建EC2的操作系统账号吗？

创建EC2的时候只有默认账号名称，但采用默认账号登录到系统后，可以自行创建更多账号

#### EC2 支持密码登录吗？

AWS在创建EC2的时候，只能选择采用秘钥对作为验证方式

![秘钥对设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-ec2createpw-websoft9.png)

#### AWS CLI 创建服务器如何指定机房？

cli创建服务器的时候，只指定到了区域（如us-ease-1），没有指定到具体机房（如us-ease-1a），但是你会发现都是在同一机房创建的服务器，这个具体机房到底是通过什么参数指定的呢？

其实是通过安全组（其参数是--security-group-ids ）之VPC，VPC默认指定了子网，子网会对应具体的机房位置

#### AWS CLI 获取官方镜像 ID vs 控制台获取镜像ID？

目前看起来控制台获取的最精准。具体原因有待调查。

