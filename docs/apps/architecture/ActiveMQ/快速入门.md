---
sidebar_position: 1
slug: /activemq
tags:
  - ActiveMQ 
  - IT 架构
  - 中间件
---

# 快速入门

[ActiveMQ](https://activemq.apache.org) 是Apache出品，流行的、能力强劲的开源消息总线，完全支持JMS1.1和J2EE 1.4规范（持久化，XA消息，事务)，尽管JMS规范出台已经是很久的事情了，但是JMS在当今的J2EE应用中间仍然扮演着特殊的地位。ActiveMQ支持多种语言和协议编写客户端。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/activemq/activemq-logined-websoft9.png)


在云服务器上部署 ActiveMQ 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:8161** 端口是否开启
3. 若想用域名访问 ActiveMQ，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用ActiveMQ，可能会用到的几组账号密码如下：

### ActiveMQ

管理员账号: `admin`  
管理员密码: `admin` 或 存储在您的服务器中的文件中 */credentials/password.txt*

运行 `cat /credentials/password.txt` 命令，可以查看其中内容

> 本地浏览器访问：http://服务器公网IP:8161 即可打开ActiveMQ 控制台

## ActiveMQ 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名:8161* 或 *http://Internet IP:8161*, 进入初始化页面（[不知道账号密码？](/zh/stack-accounts.md#activemq)）
   ![ActiveMQ初始化页面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/activemq/activemq-login-websoft9.png)

2. 点击【Manage ActiveMQ broker】登录ActiveMQ控制台
   ![ActiveMQ控制台](http://libs.websoft9.com/Websoft9/DocsPicture/zh/activemq/activemq-logined-websoft9.png)

3. 建议通过 */opt/apache-activemq/conf/jetty-realm.properties* 文件修改默认密码

> 需要了解更多ActiveMQ的使用，请参考官方文档：[Using Apache ActiveMQ](https://activemq.apache.org/using-activemq)


## 常用操作

### 配置

参考官方方案：http://activemq.apache.org/configuration.html

## 异常处理

#### 浏览器打开IP地址，无法访问 ActiveMQ（白屏没有结果）？

您的服务器对应的安全组8161端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### ActiveMQ 服务启动失败？

请确保您的服务器主机名中没有包含"."，例如：activemq5.6 这样的主机名就会导致ActiveMQ服务无法启动  

请通过下面的命令修改:  

```
hostnamectl set-hostname activemq
```



