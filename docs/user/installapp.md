---
sidebar_position: 3
slug: /user/installapp
---

# 安装应用

安装应用是 Websoft9 最吸引用户的功能之一，它与很多同类软件有很多之处：

- 遵循“先安装，再配置”的原则，努力消除了一切困扰用户的安装参数
- 根据已经绑定的泛解析，自动为每个应用应用绑定域名
- 兼容**域名和端口**两种常见的应用访问模式
- 应用的配置文件和数据文件分离
- 基于 GitOps 的技术哲学，让应用可以持续部署


下面是一个安装应用的范例：  

1. 进入应用商店，打开应用详情后点击【安装】

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-appstoredetail.png)

2. 填写或选择所需的参数：

   - 应用名称：建议填写为可识别的英文或拼音
   - 版本：自行选择，其中 latest 版本不是严格每日测试的版本
   - 端口：外网访问端口，设置后需要同时在安全组中放开方可使用
   - 域名：自动产生的域名或自行额外增加域名，也可以禁用自动产生的域名

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-installapp-fill.png)

   > 在使用域名的情况下，外围端口设置后不需要在安全组中设置。  
