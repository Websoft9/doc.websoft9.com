---
sidebar_position: 2
slug: /runtime/javaplus
tags:
  - Java
  - 运行环境
---

# Java plus 运行环境

## 初始化向导

Java plus 通过 cockpit 面板集成了一系列可视化工具。

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://服务器公网IP/panel*, 进入登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus1-websoft9.png)

2. 输入操作系统账号密码后登录到后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus2-websoft9.png)

3. 查看密码信息以及使用Nginx和MySQL可视化工具
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus3-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus4-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus5-websoft9.png)

4. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://服务器公网IP*, 查看Java范例Jenkins
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus6-websoft9.png)

> Java应用Jenkins 通过`java -jar jenkins`启动

## 常用操作

### 配置域名

前提：准备好IP对应的域名

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://服务器公网IP/panel*, 进入登录界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus1-websoft9.png)

2. 输入操作系统账号密码后登录到后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus2-websoft9.png)

3. 进入登录界面后选择【Nginx代理】菜单
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus5-websoft9.png)

4. 登陆Nginx Proxy Manager，密码通过【初始账号】查看，登陆根据
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus7-websoft9.png)

5. 点击【Proxy Hosts】-> 【Add Proxy Host】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus8-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus9-websoft9.png)

6. 根据自己的域名配置代理设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus10-websoft9.png)

7. 浏览器输入域名访问Java应用
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/runtime/runtime-javaplus11-websoft9.png)

### 如何启动自己的Java应用



## 维护 Java 环境

参考本文档相关专题章节：

* [Java 指南](../java) 和 [Java 进阶](../java/advanced) 
