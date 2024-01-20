---
sidebar_position: 2
slug: /starter
---

# 快速入门

一旦用户安装或订阅 Websoft9 之后，就可以参考下面的入门向导，快速上手：

## 登录控制台

以自安装或购买镜像为例，这种方式都是通过服务器的端口访问 Websoft9 控制台。

1. 本地浏览器访问：`http://服务器公网IP:9000`， 进入 Websoft9 登录界面
   ![Websoft9 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-loginpage.png)

2. 输入账号登录   
   - 用户名：服务器的管理员账号，一般为 `root`
   - 密码：服务器的管理员密码

   > Websoft9 与服务器共享账号，故登录账号不限于管理账号，也可以是其他[符合要求的账号](./user/credentials)

3. 登录成功后会看到干净整洁的 Websoft9 控制台界面 
   ![Websoft9 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-console-overview.png)

## 绑定全局域名

虽然 Websoft9 支持在无域名下使用，但仍然建议先为 Websoft9 设置**全局域名**，这样今后安装每个应用都不需额外再配置域名。 

1. 从域名注册服务商的控制台，增加一个**泛域名解析**。假设域名为：abc.com，泛解析的设置为：  

   - 记录类型：A
   - 主机记录：*.websoft9
   - 记录值：服务器公网IP

2. 解析成功后，可以任意使用以 websoft9.abc.com 为后缀的子域名。下面是测试范例：  
   ```
   ping app1.websoft9.abc.com
   ping app2.websoft9.abc.com
   ping app3.websoft9.abc.com
   ```

2. 从 Websoft9 控制台的【设置】栏目，设置全局域名
   ![Websoft9 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-settings-globaldomain.png)

## 使用应用

完成上述设置后，我们开始体验如何快速部署一个应用：

### 安装应用

进入 Websoft9 控制台的【应用商店】，找到所需的应用，开始[安装应用](./user/installapp)

### 访问应用

应用安装完成后，等待 1-5 分钟，便可以进入：【我的应用】界面，打开对应的应用的【访问】标签页，查看访问信息

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-myapps-access.png)

### 编辑应用

Websoft9 控制台编辑应用，也可以成为编排应用。它主要是当标准安装无法满足用户需求之后，用户可以对应用进行个性化的**安装设置**，然后重新部署。详情参考：[管理应用](./user/manageapp) 相关章节。

