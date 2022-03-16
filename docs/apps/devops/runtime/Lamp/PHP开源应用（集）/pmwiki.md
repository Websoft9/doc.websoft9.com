---
slug: /lamp/installation/zh/pmwiki
---
# PmWiki

本文档可供使用了 **PmWiki 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 PmWiki 参考。

PmWiki（pmwiki.org）是一个开源维基百科系统（Wiki），程序小巧而功能强大、灵活，使用PHP开发而无需数据库支持， 功能和界面类似DokuWiki。安装简单，易于定制，便于维护，主题和功能都可以通过扩展实现，适合中小团队和个人网站的知识库管理。

## 准备

在开始 PmWiki 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## PmWiki 安装到服务器

**如果你使用的是 *PmWiki 镜像*，本节请忽略，直接阅读下一节 【PmWiki 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 PmWiki 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
3. 到 PmWiki 官方[下载源码](https://www.pmwiki.org/wiki/PmWikiZhCn/Download)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 PmWiki 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## PmWiki 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
2. PmWik无需安装，打开就是已经安装好了的系统
3. PmWiki后台账号和密码：通过配置文件config.php自行设置