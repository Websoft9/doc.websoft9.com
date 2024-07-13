---
sidebar_position: 2
slug: /install-aws
---


# AWS

For users of the AWS, Websoft9 has a pre-configured offering in the [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=c639a579-182c-4d30-8578-4d4d89fba658). This tutorial describes installing Websoft9 Enterprise Edition in a single Virtual Machine (EC2).   

## Prerequisite

You need an account on AWS. Use of the following methods to obtain an account:

- If you or your company already have an account with a subscription, use that account. 
- If not, you can open your own [AWS account for free](https://aws.amazon.com/cn/free). AWS free trial gives you 100+ product trials. 

## Deploy Websoft9

AWS supports various ways to deploy Websoft9, essentially via EC2 image creation.  

Before deployment, you should understand EC2 [requirements](./requirements) first.     

Regardless of which deployment method you choose, AWS will initiate the deployment of a new EC2.  

### From AWS Marketplace

1. Login to [AWS Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps), input the key "websoft9" to search image of Websoft9

2. Click **Continue to Subscribe** to start, and accept Terms and Conditions as the system prompts

3. Then click **Continue to Configuration** to go to **Launch** step
   ![开始订阅镜像](./assets/aws-rs-websoft9.png)

4. At **Launch** step, choose the **Choose Action**
   ![开始载入镜像](./assets/aws-imagecreate2-websoft9.png)

   - Launch through EC2 (recommendation)
   - Launch from Website
   - Copy to Service Catalog

5. Complete EC2 creation and Websoft9 image subscription as instructed.

### From AWS Console

1. Login to the AWS Management Console, and start to create EC2 instance

2. When choosing AMIs, click **View all public and private AMIs** and search keyword "websoft9" to see the list of images. 

3. Select one of Websoft9 image, and complete EC2 creation and Websoft9 image subscription as instructed.

### From AWS CloudFormation

1. Prepare [AWS CloudFormation](https://aws.amazon.com/cloudformation) for Websoft9 deployment

2. Run this template

   - Login to AWS Dashboard, load that AWS CloudFormation template and run it
   - Use AWS CLI/API to load that AWS CloudFormation template and run it

## After deployment

The deployment process will take a few minutes to complete. Once finished, you can:

1. View the details of the new VM through the **EC2 Dashboard** of AWS console
2. Run below command to set **root** account password
   ```
   sudo su
   passwd
   ```
3. [Login to Websoft9 Console](./login-console) and refer to [Post-Installation Setup](./install-setup) for next steps

