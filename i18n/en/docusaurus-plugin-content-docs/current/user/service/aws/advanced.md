---
sidebar_position: 3
slug: /aws/advanced
---

# Advanced

## Concepts

### API/CLI

AWS 提供了原生 API/CLI 。  

## FAQ + Troubleshoot

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