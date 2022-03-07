---
sidebar_position: 3
slug: /prestashop/study
tags:
  - Scratch
  - 电子商务
---

# 原理学习

[PrestaShop](https://prestashop.com) 是一款全功能、跨平台的免费开源电子商务解决方案，采用PHP+MySQL开发。始于2008年，发展迅速，全球已超过四万家网店采用Prestashop进行部署。Prestashop基于Smarty引擎编程设计，模块化设计，扩展性强，能轻易实现多种语言，多种货币浏览交易，支持Paypal等几乎所有的支付手段，是外贸网站建站的不错选择。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/pretashopui-websoft9.png)

## 指南

支撑 PrestaShop 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看对应的手册，完成更多配置。

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| PrestaShop(LAMP) | Apache+MySQL+PHP on Linux | [《LAMP管理员手册》](https://support.websoft9.com/docs/lamp/zh) |
| PrestaShop(LNMP)| Nginx+MySQL+PHP on Linux |[《LNMP管理员手册》](https://support.websoft9.com/docs/lnmp/zh)|

## 环境是什么？

除了使用 PrestaShop 部署包的默认设置之外，你可能需要在服务器上完成更多任务：

- 修改PHP配置文件
- 增加更多网站
- 配置HTTPS证书等
- 修改网站路径
- 绑定域名
- ...

完成这些任务，你都需要参考[环境指南](/zh/admin-runtime.md#指南)  

另外，你可能会思考，PrestaShop 是如何在这些环境下运行的呢？ 请参考下图的层次结构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)

## 演示

Prestashop 官网提供了演示环境，您可以直接访问演示地址体验：http://demo.prestashop.com

> 免责说明：此处仅提供Prestashop官方的演示地址，不保证与Websoft9镜像功能完全一致，若演示过程中若需要填写个人资料、获取Cookie、显示广告等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此产生的可能存在的商业纠纷与我们司无关。

## PrestaShop API (Web Service)

PrestaShop 使商家能够通过 CRUD API（也称为 Web 服务）让第三方工具访问其商店的数据库。

参考官方文档：https://doc.prestashop.com/display/PS16/Using+the+PrestaShop+Web+Service