---
slug: /lamp/installation/zh/typo3
---
# Typo3

本文档可供使用了 **Typo3 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Typo3 参考。

[Typo3](https://typo3.org/) 是一个具有大型全球社区的开源企业内容管理系统，由TYPO3协会的大约900名成员支持,TYPO3被许多知名公司和组织使用。

## 准备

在开始 Typo3 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Typo3 安装到服务器

**如果你使用的是 *Typo3 镜像*，本节请忽略，直接阅读下一节 【Typo3 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Typo3 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Typo3 系统增加一个数据库，假如名称为：`typo3`
3. 到 Typo3 官方[下载源码](https://get.typo3.org/)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Typo3 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Typo3 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-installstart-websoft9.png)

   在 Typo3 的根目录下，新建一个名称为 **FIRST_INSTALL** 的空白文件

2. 系统进入环境检测步骤，通过后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty02.png)

3. 填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty03.png)

4. 选择一个数据库 或 新建一个
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty04.png)

5. 设置管理员账号  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty05.png)

6. 安装完成，根据提示进入后台  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty06.png)

7. 登录后台   
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-login-websoft9.png)

8. Typo3 后台界面  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/ty08.png)


> 需要了解更多 Typo3 的使用，请参考官方文档：[Typo3 Documentation](https://typo3.org/help/documentation/)

### 升级

Typo3 后台提供了在线升级功能，升级非常容易：

1. 登录 Typo3后台，打开【ADMIN TOOLS】> 【Upgrade】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-upgrade-websoft9.png)
   
2. 根据升级向导开始升级

### 扩展管理

TYPO3 CMS 提供大量扩展，以增强系统功能。

1. 登录 Typo3后台，打开【ADMIN TOOLS】> 【Extensions】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManager-websoft9.png)

2. 顶部下拉菜单中选择【Get extensions】查看扩展
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerInstall-websoft9.png)

3. 安装、更新扩展  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-BackendExtensionManagerExtensionVersions-websoft9.png)

### 模板管理

TYPO3 CMS 的模板管理非常细致，能够对模板最小元素进行细微的设置

1. 登录 Typo3后台，打开【WEB】>【Template】
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/typo3/typo3-template-websoft9.png)

2. 配置模板

## 常见问题

#### 浏览器打开IP地址，无法访问 Typo3（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Typo3 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 Typo3 数据？

可以
