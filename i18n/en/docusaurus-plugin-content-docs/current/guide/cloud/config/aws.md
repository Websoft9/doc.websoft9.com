---
sidebar_position: 1.2
slug: /iaas-aws
---

# AWS

This chapter provides a quick guide for using Websoft9 on AWS.   

## Quick References

### Create EC2{#create-EC2}

You can create Amazon EC2 by below methods: 

- Amazon EC2 console
- AWS CLI/API
- AWS CloudFormation or Terraform

All the methods is based on AMI for EC2.  

### Default username{#root}

AWS EC2 default system account username is not `root`, you just need to use the [default username](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/connect-to-linux-instance.html)。  


### DNS for EC2{#ip-domain}  

If you create EC2, AWS created a DNS `ec2-52-0-231-176.compute-1.amazonaws.com` for it.

### Security Group{#security-group}

AWS Console can set security group by: **EC2 Dashboard > Network and Security**

### AWS CLI

 [AWS CLI](https://docs.aws.amazon.com/en_us/cli/) commands that may be used when hosting applications with Websoft9.  

- Get Websoft9 image information

    ```
    aws ec2 describe-images --filters "Name=product-code,Values=e5khuz6bgm3khfdzxa1q9fs99"
    ```

## Configure Options

- EC2 update (√): [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

- AWS online connect EC2 (√): **EC2 Dashboard > Connect**

- EC2 backup (√): AWS Backup

- EC2 resize (√): **EC2 Dashboard > Instance > Actions > Instance Settings > Change Instance type**

- EC2 redeploy (×)

- Spot Virtual Machines (√)

- Replace EC2 image (×)


## Related AWS docs

- [Enable root account password](./linux#enable)
- [Deploy Websoft9 at AWS](./install/aws)
- [AWS EC2](https://docs.aws.amazon.com/en_us/ec2/)
- [AWS CLI](https://docs.aws.amazon.com/en_us/cli)


## Troubleshoot

#### 80 port disabled at AWS (China)?

You need to complete the [ICP Beian](https://www.amazonaws.cn/support/icp/) at AWS (China) when you want to use **80** port.
