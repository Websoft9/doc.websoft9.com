---
slug: /lamp/installation/zh/dedecms
---

# DedeCms（织梦）

本文档可供使用了 **DedeCms 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 DedeCms 参考。

DedeCMS是中国知名的开源建站系统，以简单、健壮、灵活、开源几大特点占领了国内CMS的大部份市场，目前已经有超过35万个站点正在使用DedeCMS或基于DedeCMS核心开发，产品安装量达到95万。

## 准备

在开始 DedeCms 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## DedeCms 安装到服务器

**如果你使用的是 *DedeCms 镜像*，本节请忽略，直接阅读下一节 【DedeCms 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 DedeCms 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 DedeCms 系统增加一个数据库，假如名称为：`dedecms`
3. 到 DedeCms 官方[下载源码](http://www.dedecms.com/products/dedecms/downloads/)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 DedeCms 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## DedeCms 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dedecms/dedecms-installstart-websoft9.png)
2. 完成通过许可协议、环境检测之后，进入配置数据库界面（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），并设置的管理员帐号密码，然后继续 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dedecms/dedecms-installset-websoft9.png)
3. 系统安装成功，系统提示 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dedecms/dedecms-installss-websoft9.png)
4. 进入后台登录 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dedecms/dedecms-login-websoft9.png)
5. 开始体验后台 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/dedecms/dedecms-backend-websoft9.png)


## 常见问题

#### 当勾选了所有模块的时候，安装会报错“Safe Alert：Request Error step 2！”

修改网站根目录下的dedesql.class.php文件，将$this-&gt;safeCheck=FALSE; 其中的=FALSE改成TURE