---
sidebar_position: 2
slug: /install/aws
---


# AWS

Websoft9 is Partner of AWS Marketplace, you can install [Websoft9 product on AWS](https://aws.amazon.com/marketplace/seller-profile?id=c639a579-182c-4d30-8578-4d4d89fba658) very conveniently.  

## Installation

How to deploy Websoft9 on AWS? There are three methods:

### By AWS Marketplace

1. Log in [AWS Marketplace](https://aws.amazon.com/marketplace).

2. Search "Websoft9" and view the list of images of Websoft9.
   ![Search image of Websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-mkss-websoft9.png)  

3. Click the image you want, then click 【Continue to Subscribe】 after jump to the product page.
   ![Subscribe image](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-rs-websoft9.png)

4. Accept Terms and Conditions as the system prompts.

5. After the system prompts you've finished the subscribing, click the button 【Continue to Configuration】 for preparation before creating EC2.
   ![Configuration](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-cc-websoft9.png)

5. Check the information required, then click 【Continue to Launch】 to start launching.
   ![Continue to Launch](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-imagecreate-websoft9.png)

6. Choose from three actions in the process of creating EC2.
   ![Start to Launch](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aws/aws-imagecreate2-websoft9.png)

   - Launch through EC2 （the recommended way ）
   - Launch from Website
   - Copy to Service Catalog

7. Complete the following steps, including choosing an instance type, setting VPC, Key Pair and so on.

8. Wait several minutes after completing creating EC2, and the image is started as the system disk of the instance, that is, the image is automatically deployed to the instance.


### By AWS EC2

1. Login to the AWS Management Console, and click 【EC2】.
   ![Log in console](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2-websoft9.png)

2. Enter EC2 Dashboard, and click 【Launch Instance】to create Instance.
   ![Launch Instance](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-addec2-websoft9.png)

3. When choosing AMIs, click 【View all public and private AMIs】 and search keyword "websoft9" to see the list of images.
   ![Choose image of Websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-ec2image-websoft9.png)

4. Select the image you need and click【Continue】to subscribe.
   ![Continue to subscribe](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-createdec2-imageselected-websoft9.png)

5. Finish the following steps, which require you to choose instance type, add storage, configure security group, set key pair and more.
   ![Create Instance](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-createdec2-chooseinstances-websoft9.png)

6. Wait several minutes after completing creating EC2, and the image is started as the system disk of the instance, that is, the image is automatically deployed to the instance.


## After installation

Here are a few resources you might want to check out after completing the installation on Cloud.

* [Get the Internet IP of VM](../aws#ip)
* [View purchased orders](../order/aws#listorders)

## FAQ

#### Deploy a non-default version?

Each AWS product supports multiple versions, you can modify the version by following the steps below:

1. List the product and click the 【Previous version】link
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-subs-odoo-websoft9.png)

2. Then you can select【Software version】for yourself
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/aws/aws-subs-odoooldversion-websoft9.png)
