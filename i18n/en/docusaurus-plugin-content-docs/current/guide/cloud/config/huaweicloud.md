---
sidebar_position: 1.4
slug: /iaas-huaweicloud
---

# HUAWEICLOUD

This chapter provides a quick guide for using Websoft9 on HUAWEICLOUD.   

## Quick References

### Create ECS{#create-ecs}

You can create HUAWEICLOUD ECS by below methods: 

- HUAWEICLOUD EC2 console
- HUAWEICLOUD CLI/API
- HUAWEICLOUD [Terraform](https://www.huaweicloud.com/product/aos.html)

All the methods is based on HUAWEICLOUD for ECS.  


### Security Group{#security-group}

HUAWEICLOUD Console can set [security group](https://www.tencentcloud.com/document/product/213/16564) by: **ECS Dashboard > Manage Network > Configure Security Group Rule**

### HUAWEICLOUD CLI

 [HUAWEICLOUD CLI](https://support.huaweicloud.com/intl/en-us/hcli/index.html) commands that may be used when hosting applications with Websoft9.  


## Huawei Cloud Flexus{#flexus}

Flexus is ready out-of-the-box and beginner-friendly with abundant built-in solutions and images that provided by Websoft9.  

### Deploy Websoft9

When you buy **Flexus** from HUAWEICLOUD, you can select [images](https://support.huaweicloud.com/intl/en-us/bestpractice-hecs/practice_wp_0001.html) from Websoft9.   

### Show more applications{#open-apps}

Websoft9 image for Flexus is not display all applications at **App Store**.

Below commands is the example for you to enable applications **phpMyAdmin，pgAdmin，CloudBeaver** to display at Websoft9 App Store.  
```
docker exec -i websoft9-apphub apphub setconfig --section initial_apps --key keys --value $(docker exec -i websoft9-apphub apphub getconfig --section initial_apps --key keys),phpmyadmin,cloudbeaver,pgadmin
```

Then, you can install them by one-click


## Configure Options

- Connect ECS online (√): **ECS Dashboard > Remote connection**

- ECS Backup (√): [CBR](https://www.huaweicloud.com/intl/en-us/product/cbr.html)

- ECS resize (√)

- ECS redeploy (√)

- ECS replace image (√)

- ECS reset password at console (√)

- Spot Virtual Machines (√)

- System disk online resize (√)


## Related HUAWEICLOUD docs

- [Deploy Websoft9 at HUAWEICLOUD](./install-huaweicloud)
- [HUAWEICLOUD ECS](https://support.huaweicloud.com/intl/en-us/ecs/index.html)
- [HUAWEICLOUD CLI](https://support.huaweicloud.com/intl/en-us/hcli/index.html)
- [HUAWEICLOUD endpoint](https://developer.huaweicloud.com/endpoint)
- [Global Products and Services](https://www.huaweicloud.com/intl/en-us/global/)
- [ICP Filing](https://support.huaweicloud.com/intl/en-us/icp/index.html)

## Troubleshoot