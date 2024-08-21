---
sidebar_position: 2
slug: /install-aws
---


# AWS

For users of the AWS, Websoft9 has a pre-configured offering in the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-5jziwpvx4puq4). This tutorial describes installing Websoft9 Enterprise Edition in a single Virtual Machine (EC2).   

## Prerequisite

You need an account on AWS. Use of the following methods to obtain an account:

- If you or your company already have an account with a subscription, use that account. 
- If not, you can open your own [AWS account for free](https://aws.amazon.com/cn/free). AWS free trial gives you 100+ product trials. 

## Deploy Websoft9

AWS supports various ways to deploy Websoft9, essentially via EC2 image creation.  

Before deployment, you should understand EC2 [requirements](./install-requirements#server) first.     

Regardless of which deployment method you choose, AWS will initiate the deployment of a new EC2.  

### From AWS Marketplace

1. Open Websoft9 offer page at [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-5jziwpvx4puq4)

2. Click **Continue to Subscribe** to start, and accept Terms and Conditions as the system prompts

3. Then click **Continue to Configuration** to go to **Launch** step
   ![Start to buy](./assets/aws-rs-websoft9.png)

4. At **Launch** step, choose the **Choose Action**
   ![Start to load](./assets/aws-imagecreate2-websoft9.png)

   - Launch through EC2 (recommendation)
   - Launch from Website
   - Copy to Service Catalog

5. Complete EC2 creation and Websoft9 image subscription as instructed.

### From AWS Console

1. Login to the AWS Management Console, and start to create EC2 instance

2. When choosing AMIs, click **View all public and private AMIs** and search keyword "websoft9" to see the list of images. 

3. Select one of Websoft9 image, and complete EC2 creation and Websoft9 image subscription as instructed.

### From AWS CloudFormation

Websoft9 product information at AWS:

- **Product ID**: ef170715-3e45-4d1f-b753-bc0dbcf11dcd
- **Product code**: e5khuz6bgm3khfdzxa1q9fs99
- **ARN**: arn:aws:aws-marketplace:us-east-1:797851739507:AWSMarketplace/AmiProduct/ef170715-3e45-4d1f-b753-bc0dbcf11dcd

Then you can follow below steps to deploy Websoft9:  

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

