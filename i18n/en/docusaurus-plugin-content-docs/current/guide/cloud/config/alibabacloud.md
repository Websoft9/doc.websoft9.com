---
sidebar_position: 1.3
slug: /iaas-alibabacloud
---

# Alibaba Cloud

This chapter provides a quick guide for using Websoft9 on Alibaba Cloud.   

## Quick References

### Create ECS{#create-ecs}

You can create Alibaba Cloud ECS by below methods: 

- Alibaba Cloud EC2 console
- Alibaba Cloud CLI/API
- Alibaba Cloud Terraform

All the methods is based on Alibaba Cloud for ECS.  


### Security Group{#security-group}

Alibaba Cloud Console can set security group by: **ECS Dashboard > Network and Security > Security Group**

### Alibaba Cloud CLI

 [Alibaba Cloud CLI](https://www.alibabacloud.com/en/product/openapiexplorer) commands that may be used when hosting applications with Websoft9.  

- Get image details

    ```
    aliyun ecs DescribeImages --Architecture x86_64 --ImageOwnerAlias system --PageSize 100 --output cols=OSName,ImageId,CreationTime rows=Images.Image[]
    ```

## Configure Options

- Online SSH connection(√): [Workbench](https://ecs-workbench.aliyun.com) or VNC at ECS console

- ECS backup(√): Create Snapshot or image for ECS

- ECS resize(√): **ECS Console > Resize**

- ECS redeploy(√):

- ECS replace image(√):

- ECS reset password(√):

  - Reset by ECS console
  - Reset by command：`echo "yourpassword" | passwd --stdin root`

- Spot instance(√)

- Resize system disk or data disy online(√)


## Related Alibaba Cloud docs

- [Deploy Websoft9 at Alibaba Cloud](./install/alibabacloud)
- [ECS docs](https://www.alibabacloud.com/help/en/ecs/)
- [CLI docs](https://www.alibabacloud.com/help/en/cli/)
- [China ICP](https://www.alibabacloud.com/help/en/china-gateway-program)

## Troubleshoot