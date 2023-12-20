---
slug: /lamp/installation/zh/weengine
---
# WeEngine

本文档可供使用了 **WeEngine 镜像** 用户参考，也可以供准备在 **LAMP 镜像** 上自行部署 WeEngine 参考。

WeEngine（微擎）是一款由宿州涛盛网络科技有限公司研发的免费开源的公众号管理系统，基于目前流行的WEB2.0的架构（php+mysql），拥有成熟、稳定的的技术解决方案。源码透明、开放，一切的数据及资源都架设在自己的服务上，保证独立性、安全性及可控性。活跃的第三方开发者及开发团队，依托微擎的整个开放的生态系统之上，更丰富的扩展功能。良好的开发框架、文档，轻松扩展、定制私有功能。优质的在线更新系统、客服人员、技术工程师解决使用或是开发上的各种疑难问题。
## 准备

在开始 WeEngine 的安装部署之前，建议完成如下事情：

* 浏览器访问：*http://公网ip/9panel* ，快速了解镜像的使用
* 查看镜像环境参数，包括：**目录路径、版本、数据库、虚拟主机配置文件等** （[马上查看](https://support.websoft9.com/docs/lamp/zh/stack-components.html)）

## WeEngine 安装到服务器

**如果你使用的是 *WeEngine 镜像*，本节请忽略，直接阅读下一节 【WeEngine 初始化安装向导】**

如果你使用的是 LAMP 镜像，请先将 WeEngine 安装到服务器，操作步骤如下：

1. 通过域名控制台完成解析域名（增加一个A记录指向服务器IP），并测试是否成功
2. 通过 [phpMyAdmin 登录 MySQL](https://support.websoft9.com/docs/lamp/zh/admin-mysql.html)，为 WeEngine 系统增加一个数据库，假如名称为：`weengine`
3. 到 WeEngine 官方[下载源码](https://s.w7.cc/static/install)
2. 参考[《如何在 LAMP 上增加网站》](https://support.websoft9.com/docs/lamp/zh/solution-deployment.html#安装第二个网站) ，将 WeEngine 安装到服务器的 [LAMP](https://support.websoft9.com/docs/lamp/zh/) 环境中

---

## WeEngine 初始化安装向导

1. 本地浏览器访问：*http://域名* 或 *http://公网IP* 进入安装向导（首选域名访问方式）
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/weengine/weengine-ins001-websoft9.png)
2. 系统进入版权许可步骤，继续下一步
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/weengine/weengine-ins002-websoft9.png)
3. 在通过环境检测后，系统要求填写您的数据库参数（[查看数据库账号密码](https://support.websoft9.com/docs/lamp/zh/stack-accounts.html)），并填写管理员信息，牢记之，点击“继续”进入安装，
  ![](https://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/weengine/weengine-ins003-websoft9.png)
4. 安装成功，系统会给出提示
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/weengine/weengine-ins004-websoft9.png)
5. 进入后台，体验系统的完整功能

## 常见问题

#### 安装微擎后，点“站点注册”后提示：couldn't connect to host传输站点资料至您的站点时发生错误...

问题原因：域名访问下出现此问题，当前官方没有说明原因
解决方案：请使用IP访问，完成绑定操作