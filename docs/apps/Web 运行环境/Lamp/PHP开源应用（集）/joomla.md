---
slug: /lamp/installation/zh/joomla
---

# Joomla

本文档可供使用了 **Joomla 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Joomla 参考。

Joomla（joomla.org）是全球三大开源内容管理系统之一（CMS），占据全球5%的建站市场。其拥有高度的可定制性和电子商务方面的优势，一旦突破最初的学习瓶颈之后，你可以用它进行广泛的Web应用开发，简直是无所不能。目前是由Open Source Matters（见扩展阅读）这个开放源码组织进行开发与支持，Joomla实际有两个开源的部分：一个是Joomla CMS（Joomla内容管理系统），它是网站的一个基础管理平台。另一个是Joomla Platform（Joomla框架）。

## 准备

在开始 Joomla 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Joomla 安装到服务器

**如果你使用的是 *Joomla 镜像*，本节请忽略，直接阅读下一节 【Joomla 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Joomla 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Joomla 系统增加一个数据库，假如名称为：`joomla`
3. 到 Joomla 官方[下载源码](https://downloads.joomla.org/)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Joomla 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Joomla 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
2. 选择一门语言，并设置后台管理账号信息，牢记之
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/jm01.png)
3. 填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），点击 “Next”;
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/jm02.png)
4. 进入是否需要安装演示数据环节，选择您需要的演示数据示例或不选择，点击“Install”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/jm03.png)
5. 可选项：点击安装语言按钮，按照提示选择你喜欢的网站语言包进行安装。注意：语言包的版本不需要和软件包一样，请选择你需要的语言包名字，如简体中文。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/jm04.png)
6. 恭喜成功Joomla网站，请注意在语言包安装完成之后,点击“Remove installation folder”移除安装脚本目录.
7. Joomla后台地址：http://域名/e/administrator

## 常见问题

#### 在组件中如何加载其他扩展的语言文件?

开发一个Joomla投稿组件的时候，需要调用joomla文章组件的语言文件，因为界面很多字符串都来自系统的文章组件，本来打算直接将系统的文章组件的语言文件直接复制一份的，但感觉那样做不优雅，因此，查了一下源码，发现是Joomla是可以在任何时间，任何地方调用任何组件的语言文件的。

直接上代码了，并不难理解

~~~
`$lang` `= JFactory::getLanguage();`

`$extension` `= ``'com_content'``;`

`$base_dir` `= JPATH_ADMINISTRATOR;`

`$language_tag` `= ``'zh-CN'``;`

`$reload` `= true;`

`$lang``->load(``$extension``, ``$base_dir``, ``$language_tag``, ``$reload``);`
~~~

上面的代码没有什么好解释的。需要什么扩展就将extension变量赋值即可。