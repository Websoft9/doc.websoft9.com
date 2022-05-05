---
sidebar_position: 1
slug: /iis
---

# 指南

## 场景

### 绑定域名{#binddomain}

IIS 中绑定域名的操作步骤如下：  

1.  打开IIS，右键点击需配置域名的网站，选择【编辑绑定】，选择一个待绑定域名的网站后，点击【编辑】 按钮 
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-adddomain001-websoft9.png)

2.  在主机名处填写域名，然后保存
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-adddomain002-websoft9.png)

3. 需要增加多个域名，请在第一步选择“添加”按钮

> 如果服务器上增加多个应用，本步骤是必要的


### 修改网站根目录

在 IIS 中修改根目录是比较容易的：

1. 打开IIS，邮件点击Default Web Site，依次选择管理网站-高级设置
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-changeroot-websoft9.png)

2. 将物理路径修改为新的路径即可（要提前将wwwroot内容拷贝到新目录）

3. 重启IIS后生效

### 设置伪静态{#rewrite}

IIS 中设置伪静态的主要操作步骤如下：  

1. 确保 IIS 安装了 **[URL重写](https://www.iis.net/downloads/microsoft/url-rewrite)** 组件

2.  进入IIS后选择具体的网站，打开URL重写工具
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrew-websoft9.png)

3.  依次添加规则

4.  重启IIS后生效

### 设置 HTTPS 访问{#https}

#### 方案一：上传证书

1. 上传用户自己的证书文件到服务器

2. 找到 IIS 服务器证书导入功能入口，导入证书
   ![1523428081837](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX3-websoft9.PNG)
   ![1523428307113](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX4-websoft9.png)

3. 等待导入成功
   ![1523428321945](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX5-websoft9.png)

4. 打开网站的【绑定】功能，设置证书
   ![1523428488886](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX6-websoft9.png)

   ![f1523428617943](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX7-websoft9.png)

5. 测试 HTTPS 访问

#### 方案二：自动化证书程序

采用自动化证书程序设置 HTTPS，也是一个非常不错的方案，它节省了证书申请和更新的实践

#####  配置

1. 下载 [win-acme](https://github.com/PKISharp/win-acme/releases) 到服务器，解压至  `C:\Program Files`

    ![1523429808764](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt3-websoft9.png)

2. 双击 `letsencrypt.exe` 程序

    ![1523429865345](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt4-websoft9.png)

3. 开始创建证书，第一个选型输入`N`  

   ![1523430024664](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt5-websoft9.png)

4. 参考下图继续完成后续步骤  

   ![1523430136570](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt6-websoft9.png)  
   ![1523430270351](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt7-websoft9.png)  

5. 配置完成    
   ![1523430320474](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt8-websoft9.png)

6. 打开IIS，查看站点是否已经配置 HTTPS，并测试访问   
   ![1523430359697](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt9-websoft9.png)

浏览器在测试SSL是否配置成功


##### 续订

win-acme 支持证书续订，具体步骤如下：

1. 打开程序，输入 *L**   
  ![1523430513122](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt10-websoft9.png)

2. 选择需要自动续订证书的站点
   ![1523430937571](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt11-websoft9.png)

3. 自动续订成功
   ![1523431002175](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt12-websoft9.png)


### HTTP 跳转 HTTPS

HTTP 自动跳转至 HTTPS 的操作步骤如下：  

> 以下方案适用于通配证书。

1. 确保 IIS 安装了 **[URL重写](https://www.iis.net/downloads/microsoft/url-rewrite)** 组件

2. 在需要跳转的网站上，双击“url 重写”，设置自动跳转规则  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-1-websoft9.png)

3. 选择【空白规则】  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-2-websoft9.png)  

4. 添加 URL 重写规则  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-3-websoft9.png) 

5. 添加 HTTPS 通配规则  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-4-websoft9.png)

6. 添加 URL 重定向规则  
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-5-websoft9.png)

7. 添加完成后，重启 IIS 服务，测试设置是否成功


**注意：**

如果域名 `www.example.com` 用的不是通配证书，还需要如下额外的操作：

1. 在IIS中新建站点时，确保绑定域名 `example.com` 和  `www.example.cm`
2. 进入 URL 重写模块，添加规则时选择**规范域名**
3. 设置 `example.com` 与 `www.example.cm` 的重定向关系


## 参数

### 服务{#service}

IIS 中点击主机名称或 IIS 根目录，右侧的操作就会显示**启动、重启启动，停止**等操作

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-restart-websoft9.png)

