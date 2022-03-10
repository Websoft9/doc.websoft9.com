---
slug: /lamp/installation/zh/ecshop
---

# ECSHOP

本文档可供使用了 **ECSHOP 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 ECSHOP 参考。

ECSHOP（ecshop.com）流行的中文开源商城软件之一。有完善的本地化生态体系，提供了大量仿制模板和功能插件，方便用户快速构建个性化B2C商城、微信商城、多级分销等场景，适合于零售、跨境、母婴、鞋服等网店商业。

## 准备

在开始 ECSHOP 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## ECSHOP 安装到服务器

**如果你使用的是 *ECSHOP 镜像*，本节请忽略，直接阅读下一节 【ECSHOP 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 ECSHOP 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 ECSHOP 系统增加一个数据库，假如名称为：`ecshop`
3. 到 ECSHOP 官方[获取源码](https://www.shopex.cn/products/ecshop)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 ECSHOP 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## ECSHOP 初始化安装向导

1.  本地浏览器访问：*http://域名 或  http://公网IP 进入安装向导（首选域名访问方式安装）
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-startinstall-websoft9.png)
2.  完成许可协议、环境检测之后，进入配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），并设置的管理员帐号密码，然后继续
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-dbconf-websoft9.png)
3.  系统安装成功，系统提示激活系统，可以选择注册云起（云起是ecshop的开发厂商）激活或跳过激活
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-active-websoft9.png)
4.  跳过激活后，系统提示安装成功，可以进入后台登录
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-filishins-websoft9.png)
5.  进入登录界面
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-login-websoft9.png)
6.  开始体验后台
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-backend-websoft9.png)

### ECSHOP 合集版配置

如果您使用的ecshop合集版镜像（ECSHOP合集版是模板堂公司开发，包含ecshop2.7.3+5款简洁版模板+ECTouch手机触屏版+后台美化+Bug修复，多屏合一，更简洁、更稳定），除了完成上章节的“开始安装ecshop”之外，还可以完成如下两个功能：

#### ECSHOP合集版模板切换

合集版有6款免费的模板可以切换，登录之后在左侧的导航找到模板管理-》模板选择

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-mb6-websoft9.png)

现在我们可以看到画的红框的6款模板了，点击之后即可替换了，替换完记得点击右上角的清除缓存后在刷新前台页面

整合的6个简洁版依次是：钻石小鸟，聚美优品，丽子美妆，美丽说，梦芭莎，顺丰优品 


#### ECSHOP合集版ECTOUCH安装

ectouch即ecshop的移动端程序，与ecshop是共用一个数据库的，具体安装如下：

*   在你的域名或ip后面加上 /mobile 即可来到ECTOUCH安装页面
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-ectouchinstall-websoft9.png)
*   输入数据库信息，如果你之前安装好了ECSHOP这里会自动获取到配置信息，如果获取的信息正确可以直接点击同意使用协议并且点击安装
*   装成功之后你现在直接访问你的域名加上 /mobile 即可看到ECTOUCH版页面
*   你也可以进入ECTOUCH的后台管理你的ECTOUCH应用，进入ECTOUCH后台方法 你的域名加上 /mobile/admin，即可访问ECTOUCH后台管理手机版，用户名密码与ecshop一致
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-ectouch-websoft9.png)

## 常见问题

#### ECSHOP 是免费的吗？

ECSHOP 不是免费的商城系统，官方并没有提供任何开源许可协议，更多的是引导用户购买商业授权。


#### 如何设置SMTP发邮件？

ECSHOP可以通过设置SMTP来实现发送邮件的功能，具体设置步骤如下：
1. 进入网站后台，选择邮件服务器设置；  
2. 选择“采用其他的SMTP服务”；  
3. 选择“是”采用SSL加密连接方式；  
4. 输入提供SMTP服务的服务器地址；  
5. 输入SMTP服务器的端口号；  
6. 输入提供SMTP服务的邮箱地址；  
7. 输入该邮箱的SMTP服务密码(有的也叫做授权码)；  
8. 输入邮件回复地址，需要与邮件发送账号一致；  
9. 输入测试接收人邮件地址，若弹出发送成功的窗口即表示SMTP设置正确，最后点击确定保存设置即可。
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/ecshop/ecshop-smtp-websoft9.png)