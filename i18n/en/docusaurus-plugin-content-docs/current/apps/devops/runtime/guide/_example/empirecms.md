---
slug: /lamp/installation/zh/empirecms
---

# EmpireCMS（帝国）

本文档可供使用 **EmpireCMS 镜像** 用户参考，也可供准备在 **LAMP 镜像** 上自行部署 EmpireCMS 参考。

EmpireCMS（帝国）（phome.net）是国内著名的开源建站软件（内容管理系统），简单、易用、好用。通过十多年的不断创新与完善，使系统集安全、稳定、强大、灵活于一身。目前帝国程序已经广泛应用在国内上百万家网站，覆盖国内上千万上网人群，并经过上千家知名网站的严格检测，被称为国内安全稳定的开源CMS系统。

## 准备

在开始 EmpireCMS 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## EmpireCMS 安装到服务器

**如果你使用的是 *EmpireCMS 镜像*，本节请忽略，直接阅读下一节 【EmpireCMS 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 EmpireCMS 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 EmpireCMS 系统增加一个数据库，假如名称为：`empirecms`
3. 到 EmpireCMS 官方[下载源码](http://www.phome.net/download/)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 EmpireCMS 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## EmpireCMS 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
2. 首先点击 “我同意”，然后点击“下一步”完成环境检测，检测通过后方可进入后续步骤 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/empirecms/empirecms-install002-websoft9.png)
3. 进入目录权限检测，检测通过后方可进入后续步骤 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/empirecms/empirecms-install003-websoft9.png)
4. 填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），点击 “下一步”; 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/empirecms/empirecms-install004-websoft9.png)
5. 设置您的管理员账号，点击 “下一步”; 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/empirecms/empirecms-install005-websoft9.png)
6. 恭喜成功安装帝国网站，点击 “进入后台控制面案”（请记住管理地址。为确保服务器安全，可以远程登录后台服务器，将e/install目录删除）; 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/empirecms/empirecms-install006-websoft9.png)
7. 输入管理员账号，进入管理后台： 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/empirecms/empirecms-install007-websoft9.png)
8. 管理后台效果如下： 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/empirecms/empirecms-backend-websoft9.png)
9. 初始化内置数据，依据下图顺序分别操作 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/empirecms/empirecms-cacheclear-websoft9.png)
10. 至此，帝国网站管理系统全部安装完毕。

> 帝国的后台地址：http://域名/e/admin

## 常见问题

下面列出EmpireCMS使用中比较常见的问题以及对应的处理方案

#### 后台密码忘记拉，怎么办？

用phpmyadmin修改phome\_enewsuser表里的记录：把password字段的内容改为：“a024187abaf1c7a6392128a90493e99b”；把salt字段的内容改为：“empire”；把salt2字段的内容改为：“empirecms”. 密码就是：123456

#### 全站域名更换说明

1. 设置好参数设置的选项． 
2. 替换相应的字段值：  方法一：运行＂update phome\_ecms\_news set newstext=REPLACE\(newstext,’原域名’,’新域名’\),titlepic=REPLACE\(titlepic,’原域名’,’新域名’\)＂（说明：news为相应的表）  方法二：后台批量替换字段值即可

#### 数据库配置文件是哪个？

e/config/config.php

#### 用Ecms做英文站需要改什么？

1. 修改e/data/langauge/gb/pub/目录下的q\_message.php与fun.php语言包文件为英文。 
2. 前台调用用ecmsinfo万能标签