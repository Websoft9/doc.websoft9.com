---
sidebar_position: 1
slug: /nopcommerce
tags:
  - nopCommerce
  - 电商平台
  - 客户体验
---

# 快速入门

[nopCommerce]([nopcommerce.com](https://www.nopcommerce.com))是.NET领域最优质的企业级商城平台，适合每个商家的需要：它强大的企业和小型企业网站遍布世界各地的公司销售实体和数字商品。nopCommerce是一个透明且结构良好的解决方案，它结合了开源和商业软件的最佳特性。在全球拥有数万名开发者，为你提供源源不断的插件扩展。

![](https://netmarket.oss.aliyuncs.com/product/f8b1e93e-fba8-4fe3-b349-2a393ac01aa8.png)

## 演示

nopCommerce 官网提供了试用环境，您可以直接试用

* 演示地址：https://www.nopcommerce.com/zh/demo

> 免责说明：此处仅提供 nopCommerce 官方的演示，不保证与 Websoft9 部署包功能完全一致，若演示过程中若需要填写个人资料、获取Cookie等，这些都是官方行为，由此产生的安全问题与我司无关。若您在演示中进行了付费，即表明您愿意接受官方提供的付费服务，由此可能存在的商业纠纷与我司无关。

在云服务器上部署 nopCommerce 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问网站，请先到 **域名控制台** 完成一个域名解析

## 账号密码

应用程序安装、使用和维护中需要用到三种账户：

1. **MySQL默认账号和密码**：*root/123456*  
  管理地址：[http://公网ip/phpmyadmin](http://公网ip/phpmyadmin) 或 MySQLFront客户端管理
2. **SQLServer默认账号和密码**：*sa/websoft9!* 
  使用SQLServer Management Studio管理
3. **Tomcat Virtual Host Manager默认账号和密码**：*tomcat/tomcat* 
  管理地址：[http://127.0.0.1:8080](http://127.0.0.1:8080)
> 密码安全性提示：镜像默认的密码是为了帮助您简化安装和使用的，但默认密码并不安全，因此在完成镜像安装之后，立即通过管理地址修改默认密码。


## nopCommerce 入门向导

1. 本地浏览器访问：**[http://域名](http://域名)** 或 **[http://公网IP](http://公网IP)** 进入安装向导（首选域名访问方式安装） 
2. 选择语言，设置管理员账号信息， 填写数据库信息（默认账号密码是：sa/websoft9!）  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-install-websoft9.png)

3. 点击安装， 进入安装进程![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-intalling-websoft9.png)

4. 安装成功后，您会看到如下界面  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-front-websoft9.png)

5. 进入后台管理： **http://域名/Admin**  或  **http://公网IP/Admin**
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/nopcommerce/nopcommerce-backend-websoft9.png)


## 常用操作

### SQLServer 数据管理

开启SQLServer的远程访问

本镜像默认完成了SQLServer远程访问的配置，但需要立即使用远程连接，还需要完成如下两个步骤：

1.  在Windows服务器防火墙设置中开启远程访问。控制面板-&gt;系统和安全-&gt;Windows防火墙-&gt;打开或关闭Windows防火墙 

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver-firewall001-websoft9.png) ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/sqlserver2014/sqlserver-firewall002-websoft9.png)

2.  在云控制台中，开启服务器安全组的1433端口，即可远程访问。

### 域名绑定

请远程登录到Windows服务器后，修改IIS下对应的网站的域名绑定，具体如下：

1. 打开IIS，右键点击需要配置域名的网站，选择“编辑绑定”，系统弹出网站绑定列表。选择一个没用绑定域名的网站后，点击“编辑” 按钮 

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-adddomain001-websoft9.png)

2. 在主机名处填写域名，然后保存 

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-adddomain002-websoft9.png)

3.  需要增加多个域名，请在第一步选择“添加”按钮

**说明**：如果你计划在服务器上增加多个应用，本步骤是必要的

### SSL/HTTPS

#### IIS SSL 配置 

##### 腾讯申请的免费证书配置


腾讯免费证书申请成功后下载证书为一个压缩包,解压后内容大致如图所示:(test.websoft9.cn为测试域名)

![1523418632922](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX1-websoft9.png)


进入 IIS 文件夹内容如下:

![1523418668438](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX2-websoft9.png)

打开 IIS 开始导入证书 

![1523428081837](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX3-websoft9.PNG)

![1523428307113](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX4-websoft9.png)

导入成功

![1523428321945](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX5-websoft9.png)

给站点配置SSL证书

![1523428488886](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX6-websoft9.png)

![f1523428617943](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX7-websoft9.png)

最后在浏览器上测试 `https://域名` 是否配置成功


##### 阿里云免费证书配置

免费申请阿里云证书成功后,配置可以直接参考阿里提供的方案进行操作

![1523432385204](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-Aliyun-websoft9.png)


#### 使用let's encrypt自动配置证书

前往[github](https://github.com/PKISharp/win-acme/releases)下载程序 

![1523429626325](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt1-websoft9.png)

下载好后解压

![1523429704719](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt2-websoft9.png)

将解压出的文件夹 复制到 `C:\Program Files` (目录可以随意设置,建议存放在这个目录下,配置好证书后程序切勿删除)

![1523429808764](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt3-websoft9.png)

进入程序目录,内容大致如下:

![1523429865345](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt4-websoft9.png)


创建证书,输入`N`

![1523430024664](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt5-websoft9.png)

绑定单个IIS站点

![1523430136570](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt6-websoft9.png)

这里会列出当前IIS上已有的站点根据序号选择需要配置SSL的站点

![1523430270351](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt7-websoft9.png)

配置成功,如图所示:(到这一步后先别关闭这个窗口)

![1523430320474](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt8-websoft9.png)


打开IIS 检测ssl是否配置成功 

![1523430359697](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt9-websoft9.png)

浏览器在测试SSL是否配置成功


设置自动续订(如果之前窗口关闭了,重新打开程序输入`L`)

![1523430513122](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt10-websoft9.png)


选择需要自动续订证书的站点

![1523430937571](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt11-websoft9.png)

自动续订成功

![1523431002175](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt12-websoft9.png)

### 设置HTTP自动跳转HTTPS

1. 安装 URL 重写模块
  
访问[IIS官方下载页面](https://www.iis.net/downloads/microsoft/url-rewrite)，下载对应版本的安装文件进行安装。

2. 设置自动跳转
  2.1 示例一：http://www.example.com 跳转到 https://www.example.com
  a. 在需要跳转的网站上，双击“url 重写”；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-1-websoft9.png)
  b. 添加空白规则；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-2-websoft9.png)
  c. 添加 URL 重写规则；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-3-websoft9.png)
  d. 继续添加；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-4-websoft9.png)
  e. 继续添加 URL 重写规则；
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-5-websoft9.png)
  f. 最后一步，单击右边的“应用”按钮，不需重启 IIS 服务，即可测试是否自动跳转了。
  2.2 示例二：不带 www 的域名跳转至 www 域名
  如果您的 www.example.com 用的不是通配证书，则如示例一设置跳转后，还需按照示例二进行设置。
  a. 在IIS中新建站点时，确保绑定域名 [example.com](example.com) 和 [www.example.cm](www.example.cm)；
  a. 进入 URL 重写模块，添加规则（操作和示例一相同）；
  b. 添加规则时选择**规范域名**，确定进入下一步；
  c. 选择主域名即需要重定向的域名；
  d. 完成后访问 [example.com](example.com) 即可跳转至 [www.example.cm](www.example.cm)，如果 [www.example.cm](www.example.cm) 设置了 https 自动跳转，则访问 [example.cm](example.cm) 会直接跳转到 [https://www.example.com](https://www.example.com)


### 设置伪静态

本镜像默认安装了针对于IIS伪静态设置的“**URL重写**”组件，下面以Wordpress为例描述如何设置伪静态：

1.  进入IIS后选择具体的网站，打开URL重写工具 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrew-websoft9.png)
2.  依次添加规则
3.  重启IIS后生效

## 异常处理

