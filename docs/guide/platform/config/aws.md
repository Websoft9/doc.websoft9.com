---
sidebar_position: 1.2
slug: /iaas-aws
---

# AWS

本章为在 AWS 上使用 Websoft9 托管平台的用户提供 AWS 操作的快速指南。

## 快速参考

### 创建 EC2 服务器{#create-EC2}

AWS 支持多种创建 EC2 的方式，包括：

- Amazon EC2 控制台
- AWS CLI
- AWS CloudFormation
- Terraform

但是，任何一种方式均需要为 EC2 选用或准备所需的镜像（AMI）

### 系统账号

AWS EC2 的默认系统账号并不是 `root`，也无法在创建 EC2 时自行设置，而是由 [AWS 预定设置](https://docs.aws.amazon.com/zh_cn/AWSEC2/latest/UserGuide/connect-to-linux-instance.html)。  

### 管理卷{#disk}

AWS EC2 磁盘被称之为卷，它可以：

- 支持分离
- 分离后的卷支持扩容
- 卷转换成快照

### 管理 IP 与域名{#ip-domain}

- 支持静态 IP 和弹性 IP
- 支持动态弹性 IP 到 EC2
- 默认为 EC2 分配 `ec2-52-0-231-176.compute-1.amazonaws.com` 类似的免费域名
- 专业的域名产品 [Route 53](https://aws.amazon.com/cn/route53/) 

### 设置安全组{#security-group}

AWS 控制台提供了对网络安全的直接设置：**EC2 Dashboard > 网络与安全 > 网络组**。

### AWS CLI

使用 Websoft9 托管应用时可能用到的 [AWS CLI](https://docs.aws.amazon.com/zh_cn/cli/) 命令。  

- 查询镜像

    ```
    aws ec2 describe-images --owners amazon  --filters "Name=architecture,Values=x86_64" "Name=image-type,Values=machine" "Name=root-device-type,Values=ebs" --region us-east-1  --query 'Images[*].[ImageId,Description,Name]' 
    ```

- 基于镜像创建 EC2
  ```
  aws ec2 run-instances
  --instance-market-options "MarketType=spot,SpotOptions={SpotInstanceType=persistent,InstanceInterruptionBehavior=stop}"     
        --image-id ami-0947d2ba12ee1ff75 --count 1            --instance-type t3a.medium            --key-name websoft9_auto   
      --security-group-ids sg-1240356f            --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=docker0-AmazonLinux2}]"  
      --block-device-mappings "DeviceName=/dev/xvda,Ebs={VolumeSize=40}"       
      --iam-instance-profile Arn="arn:aws:iam::797851739507:instance-profile/AmazonSSMRoleForInstancesQuickSetup"
  ```


## 配置选项

- EC2 自动更新（√）：[AWS Systems Manager](https://www.amazonaws.cn/systems-manager/)

- AWS 控制台连接 EC2（√）：**EC2 Dashboard > 连接**

- EC2 备份（√）：AWS Backup

- EC2 规格调整（√）：**EC2 Dashboard > 实例 > 操作 > 实例设置 > 更改实例类型**

- EC2 重置到初始状态（×）

- 竞价实例（√）

- EC2 更换镜像（×）


## 相关文档

- [启用服务器 root 账号密码](./linux#enable)
- [AWS 上部署 Websoft9](./install/aws)
- [AWS EC2 官方文档](https://docs.aws.amazon.com/zh_cn/ec2/)
- [AWS CLI](https://docs.aws.amazon.com/zh_cn/cli)


## 故障

#### AWS（中国）EC2 的 80 端口不能用？

AWS（中国）的云服务器的 **80** 端口默认已被云平台封闭，需用户完成 [ICP 备案](https://www.amazonaws.cn/support/icp/)后，通过工单申请解封。    
