---
sidebar_position: 1
slug: /security
---

# 指南

## 场景 

### 代码植入问题处理{#insertcode}

代码植入是一种通过将【病毒代码】插入到应用程序正常代码中间的一种伪装方式

* 源码中植入非常明显的代码
* 源码中植入难以察觉的代码
* 数据库中被植入

它具备难以被**一锅端**的特征，所以被黑客广泛采用。  

下面以 WordPress 为例，介绍系统被代码植入后的处理方案。  

1. 通过在线安全检查网站[sitecheck.sucuri.net](https://sitecheck.sucuri.net)进行排查，初步定义被植入的内容
2. 登录WordPress后台，安装安全插件[Wordfence Scan Enabled](https://wordpress.org/plugins/wordfence/)
3. 运行Wordfence Scan Enabled，启动网站健康检查
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/wordpress/wordpress-wordfence-websoft9.png)
4. 对于“Critical”标记的结果，手工一一处理

> 其他扫描工具：
> 1. Quttera Web Malware Scanner 
> 2. Anti-Malware Security and Brute-Force Firewall  

### HTTPS 设置{#https}

参考：[域名 HTTPS 设置](./dns#https)

## 参数
