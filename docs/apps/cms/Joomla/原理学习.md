---
sidebar_position: 3
slug: /joomla/study
tags:
  - Joomla
  - CMS
  - 建站系统
---

# 原理学习

[Joomla](https://joomla.org) 是全球三大开源内容管理系统之一（CMS），占据全球5%的建站市场。其拥有高度的可定制性和电子商务方面的优势，一旦突破最初的学习瓶颈之后，你可以用它进行广泛的Web应用开发，简直是无所不能。目前是由Open Source Matters（见扩展阅读）这个开放源码组织进行开发与支持，Joomla实际有两个开源的部分：一个是Joomla CMS（Joomla内容管理系统），它是网站的一个基础管理平台；另一个是Joomla Platform（Joomla框架）。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-gui-websoft9.jpg)


## 指南

支撑 Joomla 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看对应的手册，完成更多配置。

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| Joomla(LAMP) | Apache+MySQL+PHP on Linux | [《LAMP管理员手册》](https://support.websoft9.com/docs/lamp/zh) |
| Joomla(LNMP)| Nginx+MySQL+PHP on Linux |[《LNMP管理员手册》](https://support.websoft9.com/docs/lnmp/zh)|

## 环境是什么？

除了使用 Joomla 部署包的默认设置之外，你可能需要在服务器上完成更多任务：

- 修改PHP配置文件
- 增加更多网站
- 配置HTTPS证书等
- 修改网站路径
- 绑定域名
- ...

完成这些任务，你都需要参考[环境指南](/zh/admin-runtime.md#指南)  

另外，你可能会思考，Joomla 是如何在这些环境下运行的呢？ 请参考下图的层次结构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)

## 演示

Joomla 官网提供了试用环境，您可以直接试用

* 演示地址：https://launch.joomla.org

> 免责说明：此处仅提供 Joomla 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。