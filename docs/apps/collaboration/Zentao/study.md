---
sidebar_position: 3
slug: /zentao/study
tags:
  - ZenTao（禅道）
  - 项目管理
---

# 原理学习

[ZenTao（禅道）](https://www.zentao.net) 由青岛易软天创网络科技有限公司（用心做开源的杰出公司）开发，是一款优秀的开源项目管理软件。它集产品管理、项目管理、质量管理、文档管理、组织管理和事务管理于一体，是一款专业的研发项目管理软件，完整覆盖了研发项目管理的核心流程。禅道管理思想注重实效，功能完备丰富，操作简洁高效，界面美观大方，搜索功能强大，统计报表丰富多样，软件架构合理，扩展灵活，有完善的API可以调用。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zentao/zentao-gui-websoft9.png)

## 指南

支撑 ZenTao 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看对应的手册，完成更多配置。

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| ZenTao(LAMP) | Apache+MySQL+PHP on Linux | [《LAMP管理员手册》](https://support.websoft9.com/docs/lamp/zh) |
| ZenTao(LNMP)| Nginx+MySQL+PHP on Linux |[《LNMP管理员手册》](https://support.websoft9.com/docs/lnmp/zh)|

## 环境是什么？

除了使用 ZenTao 部署包的默认设置之外，你可能需要在服务器上完成更多任务：

- 修改PHP配置文件
- 增加更多网站
- 配置HTTPS证书等
- 修改网站路径
- 绑定域名
- ...

完成这些任务，你都需要参考[环境指南](/zh/admin-runtime.md#指南)  

另外，你可能会思考，ZenTao 是如何在这些环境下运行的呢？ 请参考下图的层次结构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)


## 演示

快速了解 ZenTao，请查看[官方演示](http://demo.zentao.net/)