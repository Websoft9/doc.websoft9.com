---
slug: /lamp/installation/zh/drupal
---
# Drupal

本文档可供使用了 **Drupal 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 Drupal 参考。

Drupal（drupal.org）是全球三大开源内容管理系统之一，约3%的网站使用。Drupal也是一个开发框架，逻辑性强、一块块积木，搭起来以后使页面层层分明，它的内核中的有功能强大的PHP类库、函数库和API，能够通过二次化开发来构建复杂多用的企业级应用。Drupal有良好的商业生态，众多高端优质客户使用进一步推动了开源社区的发展。

## 准备

在开始 Drupal 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## Drupal 安装到服务器

**如果你使用的是 *Drupal 镜像*，本节请忽略，直接阅读下一节 【Drupal 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 Drupal 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 Drupal 系统增加一个数据库，假如名称为：`drupal`
3. 到 Drupal 官方[下载源码](https://www.drupal.org/download)
4. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 Drupal 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## Drupal 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
2.  选择一门语言，进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/dp01.png)
3.  选择一种安装方式，进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/dp02.png)
4.  填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），保存并继续;
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/dp03.png)
5.  分别完成网站安装和翻译安装
6.  设置网站信息。站点维护账号及后台账号，请务必设置好并牢记之。进入下一步
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/dp06.png)
7.  系统完成最后一步安装
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/dp08.png)
8.  进入Drupal后台，体验完整功能
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/dp09.png)

## 常见问题

#### Drupal安装后系统提示如下的安全漏洞
settings.php 中的 trusted_host_patterns 设置未配置。这可能导致安全漏洞。强烈建议您配置此项。
解决方案：更多详情请参见 [防止 HTTP HOST 头攻击。](https://www.drupal.org/node/1992030)

#### 如何设置SMTP发邮件？

1. Drupal安装完成后首先确认是否已经安装SMTP模块，如下图所示，
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-smtp-1-websoft9.png)

2. 若没有该模块可在[立即下载](http://drupal.org/project/smtp)。
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-smtp-2-websoft9.png)

3. 按图中所示上传smtp模块，安装完成后还需在**扩展**选项里勾选安装**SMTP Authentication Support**(有已有则忽略这一步)。
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-smtp-3-websoft9.png)

4. 接下来即可在**配置**--**SMTP Authentication Support**选项中开始配置smtp服务，按如图填写保存配置。
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-smtp-4-websoft9.png)
  ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-smtp-5-websoft9.png)
  
5. 至此，drupal的smtp模块配置完成，您现在可以使用drupal的smtp模块收发功能了。