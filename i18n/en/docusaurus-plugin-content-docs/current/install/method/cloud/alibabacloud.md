---
sidebar_position: 3
slug: /install-alibabacloud
---

# Alibaba Cloud

For users of the Alibaba Cloud, Websoft9 has a pre-configured offering in the [Alibaba Cloud Marketplace](https://marketplace.alibabacloud.com/products/201072001/sgcmjj00034378.html). This tutorial describes installing Websoft9 Enterprise Edition in a single Virtual Machine (ECS).   

## Prerequisite

You need an account on Alibaba Cloud. Use of the following methods to obtain an account:

- If you or your company already have an account with a subscription, use that account. 
- If not, you can open your own [Alibaba Cloud account for free](https://free.aliyun.com) that gives you 100+ product trials. 

## Deploy Websoft9

Alibaba Cloud supports various ways to deploy Websoft9, essentially via ECS image creation. 

Before deployment, you should understand ECS [requirements](./install-requirements#server) first.   

### From Alibaba Cloud Marketplace

1. Open the product [Websoft9 applications hosting platform](https://marketplace.alibabacloud.com/products/201072001/sgcmjj00034378.html) at [Alibaba Cloud Marketplace](https://shop658hlt17.market.aliyun.com)

2. Click **Choose Your Plan** to start deploy Websoft9
   ![](./assets/alibabacloud-websoft9-choose.png)

3. Complete ECS creation and Websoft9 image subscription as instructed.

### From Alibaba Cloud Console

1. Login to Alibaba Cloud Console and enter to ECS console page

2. Select one of action to deploy Websoft9

   - Create new ECS
   - **Replace system disk** for already existing ECS

3. Start to deploying, at the **Image** configuration, select the **Marketplace Image**
   ![](./assets/aliyun-images-1-websoft9.png)

4. Input the key "websoft9 hosting" to search image of Websoft9

5. Complete ECS creation and Websoft9 image subscription as instructed.

### From ROS templates

1. Prepare [ROS template](https://www.alibabacloud.com/en/product/ros) for Websoft9 deployment

2. Run this template

   - Login to Alibaba Cloud Console, load that ROS template and run it
   - Use Alibaba Cloud CLI/API to load that ROS template and run it

## After deployment

The deployment process will take a few minutes to complete. Once finished, you can:

1. View the details of the new ECS through the Alibaba Cloud Console
2. [Login to Websoft9 Console](./login-console) and refer to [Post-Installation Setup](./install-setup) for next steps