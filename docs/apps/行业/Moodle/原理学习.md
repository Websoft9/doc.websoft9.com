---
sidebar_position: 3
slug: /moodle/study
tags:
  - Moodle
  - 在线学习管理
---

# 原理学习

[Moodle](https://moodle.org) 是一个开源的在线教育系统（慕课）。采用PHP+Mysql开发，界面友好，符合SCORM/AICC标准。以功能强大、而界面简单、精巧而著称。它是eLearning技术先驱，是先进在线教学理念和实践的集大成者，已成为全球大中学院校建立开放式课程系统的首选软件。主要模块：课程管理、作业模块、聊天模块、投票模块、论坛模块、测验模块、资源模块、问卷调查模块、互动评价（workshop）。Moodle具有先进的教学理念，创设的虚拟学习环境中有三个维度：技术管理维度、学习任务维度和社会交往维度，以社会建构主义教学法为其设计的理论基础，它提倡师生或学生彼此间共同思考，合作解决问题。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodlegui-websoft9.jpg)

## 指南

支撑 Moodle 运行的环境组件包括：PHP, MySQL, Apache or Nginx等，请根据不同的部署包分别查看对应的手册，完成更多配置。

| 部署包名称 | 说明| 参考项 |
| --- | --- | --- |
| Moodle(LAMP) | Apache+MySQL+PHP on Linux | [《LAMP管理员手册》](https://support.websoft9.com/docs/lamp/zh) |
| Moodle(LEMP)| Nginx+MySQL+PHP on Linux |[《LNMP管理员手册》](https://support.websoft9.com/docs/lnmp/zh)|

## 环境是什么？

除了使用 Moodle 部署包的默认设置之外，你可能需要在服务器上完成更多任务：

- 修改PHP配置文件
- 增加更多网站
- 配置HTTPS证书等
- 修改网站路径
- 绑定域名
- ...

完成这些任务，你都需要参考[环境指南](/zh/admin-runtime.md#指南)  

另外，你可能会思考，Moodle 是如何在这些环境下运行的呢？ 请参考下图的层次结构图

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/wamp/php-infra-websoft9.png)

## 演示

Moodle官网提供了试用环境，您可以直接试用

* 演示地址：https://moodle.org/demo/

> 免责说明：此处仅提供Moodle官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。