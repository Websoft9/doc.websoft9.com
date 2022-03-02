---
sidebar_position: 3
slug: /opencart/study
tags:
  - OpenCart
  - 电子商务
---

# 原理学习

[OpenCart](https://opencart.com) 是近年来国内外非常流行的 PHP 开源电子商务网站系统。该电商网站系统安装方便，功能强大，操作简单。支持多语言、多货币和多店铺。OpenCart 外围开发生态圈发达，更有上万款免费和收费的模块插件和模板主题可供选择。代码完全开源，功能持续更新，代码结构清晰易懂，二次开发容易上手，入门门槛低。基于这些特点使得 OpenCart 快速成为了世界上广泛应用的电子商务建站系统。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-gui-websoft9.png)

## 指南

支撑 OpenCart 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看对应的手册，完成更多配置。

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| OpenCart(LAMP) | Apache+MySQL+PHP on Linux | [《LAMP管理员手册》](https://support.websoft9.com/docs/lamp/zh) |
| OpenCart(LNMP)| Nginx+MySQL+PHP on Linux |[《LNMP管理员手册》](https://support.websoft9.com/docs/lnmp/zh)|

## 环境是什么？

除了使用 OpenCart 部署包的默认设置之外，你可能需要在服务器上完成更多任务：

- 修改PHP配置文件
- 增加更多网站
- 配置HTTPS证书等
- 修改网站路径
- 绑定域名
- ...

完成这些任务，你都需要参考[环境指南](/zh/admin-runtime.md#指南)  

另外，你可能会思考，OpenCart 是如何在这些环境下运行的呢？ 请参考下图的层次结构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)

## 演示

OpenCart 官网提供了演示环境，您可以直接访问演示地址体验：[https://demo.opencart.com](https://demo.opencart.com)

> 免责说明：此处仅提供OpenCart官方的演示地址，不保证与Websoft9镜像功能完全一致，若演示过程中若需要填写个人资料、获取Cookie、显示广告等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此产生的可能存在的商业纠纷与我们司无关。