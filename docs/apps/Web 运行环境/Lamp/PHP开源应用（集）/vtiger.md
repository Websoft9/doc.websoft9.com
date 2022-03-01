---
slug: /lamp/installation/zh/vtiger
---

# VtigerCRM

本文档可供使用了 **VtigerCRM 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 VtigerCRM 参考。

[VtigerCRM](https://vtiger.com)一套开源的客户关系管理系统(CRM)。基于SugarCRM开发的一个衍生版本。适合帮助中小企业从业务，从市场、销售、采购、库存、客服等全程跟踪客户，实现销售自动化，获取更多订单。  

[官方演示](https://www.vtiger.com/begin-free-trial/?plan=&email=)


## 准备

在开始 VtigerCRM 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## VtigerCRM 安装到服务器

**如果你使用的是 *VtigerCRM 镜像*，本节请忽略，直接阅读下一节 【VtigerCRM 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 VtigerCRM 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 VtigerCRM 系统增加一个数据库，假如名称为：`vtigercrm`
3. 到 VtigerCRM 官方[下载源码](https://www.vtiger.com/open-source-crm)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 VtigerCRM 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## VtigerCRM 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install001-websoft9.png)

2. 系统进入环境检测步骤，通过后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install002-websoft9.png)

3. 填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install003-websoft9.png)

4. 数据库连接正确，点击“Next”进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install004-websoft9.png)

5. 选择一个匹配的行业，然后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install005-websoft9.png)

6. 选择需要安装的模块，建议全部勾选上，然后进入下一步
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install006-websoft9.png)

7. 系统提示选择货币、时区等
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-install007-websoft9.png)

8. 点击“Get Started”，进入后台，体验系统的完整功能
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-backend-websoft9.png)


> 需要了解更多 VtigerCRM 的使用，请参考官方文档：[Vtiger Help](https://www.vtiger.com/help/)

## 常见问题

#### 浏览器打开IP地址，无法访问 VtigerCRM（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 VtigerCRM 数据？

部署包内置 MySQL

#### 是否可以采用云厂商提供的 RDS 来存储 VtigerCRM 数据？

可以

#### VtigerCRM如何安装中文包？

VtigerCRM支持多国语言，中文包安装方法如下：

1.  到官方[MarketPlace](https://marketplace.vtiger.com/app/listings)-Language Pack下载Chinese 简体中文语言包。官方下载不了，请到中文语言包作者发布的[下载地址](https://maie.name/789.html)下载
2.  通过主菜单【Setting – CRM Setting – Module Management – Modules 】进入模块管理界面，点击右上角 “Import Module from Zip”按钮，进入导入模块管理界面，选择语言包进行导入。注意：导入页面这里有个 bug，导入时请直接选择语言包进行导入，不要勾选“ I accept with disclaimer and would like to proceed”否则无法导入。
3.  右上角点击你的登录用户名->My Preferences-> Edit，点击 Language 后面的下拉框选择语言，然后保存
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/change-language-websoft9.jpg)

注意：语言包也可以通过官方扩展应用市场安装。在 Vtiger CRM 右上角点齿轮图标进入后台设置界面，左侧菜单栏点击 Extension Store 进入官方扩展应用市场。点击应用市场右上角的 Login to Marketplace 登录或者注册应用市场。搜索 Chinese 找到简体中文语言包进行安装。

#### VtigerCRM如何发送邮件？

VtigerCRM支持第三方的SMTP发送邮件模式，具体如下：

1. 打开VtigerCRM->设置按钮 > CRM Settings > Outgoing Server

2. 根据下图的设置，完成SMTP参数的设置
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-smtp-websoft9.png)
	* Server Name 处请填写 SMTP 服务器的地址（前面要加上 ssl:// , 后面要加端口号） ；
	* UseName 处请输入自己的邮箱地址 ；
	* Password 处请输入SMTP密码或授权码（不同于邮箱密码）
	* From Email 处请填写发送邮件地址（请保证与管理员一致）
	* Require Authentication 处勾选表示需要账号验证；

3. 设置完成后，请点击“Send Test Email”测试设置是否成功

> 以上参数设置以163邮箱为例，不同SMTP提供商的设置略有差异，请务必明确您所使用的SMTP所要求的设置方式。

#### VtigerCRM 如何升级

当镜像版本不是官方发布的最新版本的时候，有些用户朋友就有升级需求（虽然升级不是必要的）。VtigerCRM自身提供了升级功能，具体操作如下：

1. 到 VtigerCRM 官网[下载升级包](https://www.vtiger.com/open-source-crm/download-open-source/)（注意：是升级包，不是最新的软件包）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-dlupgradepack-websoft9.png)
   
   > 如果下载不到匹配的升级包，升级就无法进行。
  
2. 将下载包解压后，通过 SFTP 上传到 VtigerCRM 根目录（*data/wwwroot/defualt/vtigercrm*）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-unzippatch-websoft9.png)

3. 运行一条修改文件权限的命令：
    ~~~
    chown -R apache.apache /data/wwwroot
    ~~~
4.  浏览器访问：http://域名或IP地址/migrate 开始升级流程

> 升级之前请备份好网站代码和数据库，这是常识哦

以上方案是Websoft9对[VtigerCRM官方升级文档](http://community.vtiger.com/help/vtigercrm/administrators/migration.html)的解读，建议同时阅读官方提供的升级文档

## 故障

#### 更换服务器IP，VtigerCRM 无法访问？错误信息：*Invalid compiled template for 'modules/Install/Header.tpl'*

问题原因：VtigerCRM 启动后会生成一个记录服务器IP地址的缓存文件  
解决方案：使用下面的命令删除缓存文件

```
- rm -rf /data/wwwroot/vtigercrm/test/templates_c/v7
- rm -rf /data/wwwroot/vtigercrm/cache/*
```
#### VtigerCRM 在添加【任务】或【事件】时，速度慢，并有 DataTime 格式转换错误

![{~CR_VD4S$O 7 LQ@2R4H2](https://user-images.githubusercontent.com/62225175/149732380-42ad5683-d5f3-4ceb-9244-f7a27740153f.png)

问题原因：VtigerCRM 的日期格式设置导致格式转换错误（在中文包环境下出现）
解决方案：将日期格式更改为：yyyy-mm-dd
