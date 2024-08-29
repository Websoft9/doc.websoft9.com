---
sidebar_position: 3
slug: /odoo/admin
tags:
  - Odoo
  - 企业管理
  - ERP
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### 开启 PostgreSQL 远程连接

Odoo 默认安装的 PostgreSQL 并不会启用数据库账号，官方解决方案：https://www.odoo.com/documentation/13.0/setup/deploy.html#postgresql

### 在线升级

Odoo 后台提供了在线升级能力，让升级工作变得非常简单。参考下面的步骤完成升级：

1. 登录 Odoo 后台，[启动开发者模式](../odoo#dev-mode)
2. 通过 【Settings】>【Updates】开始更新 Odoo 主程序
   ![Odoo升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-upgradesui-websoft9.png)
3. 升级成功会有 “Well done...” 的提示
4. 点击 【Update Apps list】，开始更新 Odoo 模块

更多更新方案和注意事项请参考官方文档：[Odoo Update](https://www.odoo.com/documentation/master/setup/update.html)


## 故障排除

除以下列出的 Odoo 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

#### 如何查看 Odoo 错误日志？

最简单的方式是通过 SSH 连接服务器，运行`odoo`这个命令，就会显示错误日志以及 Odoo 的运行情况

#### 恢复数据库、上传附件等操作，出现 “413 Request Entity Too Large” 错误？{#attachment}

这是由于 Nginx 默认安装下，上传文件最大为 1M，因此需要修改 Nginx 这个限制：
1. 使用 WinSCP 远程连接服务器
2. 编辑 [Nginx 虚拟机主机配置文件](../nginx#path)
3. 插入一行 `client_max_body_size 0;` 解除上传文件限制的配置项
   ```
   server {
    listen 80;
    server_name _;
    client_max_body_size 0; #解除上传文件限制
    ...
   ```
4. 保存并[重启 Nginx 服务](../administrator/parameter#service)

#### Odoo 总出现数据库设置提醒？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-setpasswodrem-websoft9.png)

这个提醒的是要求你尽快给数据库设置一个高强度的管理员密码，如果不设置将面临很大的风险。一旦设置后，此界面就不会再弹出了

#### SFTP 无法上传文件到 Odoo 目录？

Linux 普通用户没有 Odoo 程序的源码或目录有操作的权限，需要执行以下命令:

```
sudo chmod o+rw  /usr/lib/python2.x/dist-packages/odoo   # odoo10版本
sudo chmod o+rw  /usr/lib/python3/dist-packages/odoo   # odoo11版本以上
```

#### PDF 无法打印中文

Odoo11 之前的版本，在使用 Odoo 打印功能时，下载的PDF文件只有英文，没有中文，导致打印不完整。

**问题原因**：系统环境里没有下载所需的中文字体

**解决方案**：执行以下命令下载字体

~~~
sudo apt-get install ttf-wqy-zenhei
sudo apt-get install ttf-wqy-microhei
~~~

#### Command pg_dump not found？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-backuperror-websoft9.png)

现象：Odoo 备份数据时，报错：Command pg_dump not found  
原因：PostgreSQL 的备份命令没有找到
方案：需要进一步查看PostgreSQL安装问题，还是Odoo本身的问题


## 问题解答

#### Odoo 支持多语言吗？

支持多语言（包含中文），参考：[语言设置](../odoo#setlang)

#### Odoo 数据库连接配置信息在哪里？

Odoo 采用 [Peer Authentication](https://www.postgresql.org/docs/10/auth-methods.html#AUTH-PEER) 方式连接 PostgreSQL，即以操作系统用户登录数据库，无需密码。

#### Odoo 控制台看不到更新提示？

此功能只能在开发者模式下使用，请确保你的 Odoo 控制台是否已经切换成[开发者管理模式](../odoo#dev-mode)

#### 如何删除 Odoo 演示数据？

没有直接上传的方案。由于 Odoo 支持多企业组织方式，建议新增一个企业组织（不要勾选演示数据）后，再删除带演示的数据库。具体操作方式参考：[ Odoo 数据库管理](../odoo#dbadmin)

#### Odoo 是否可以导出 PDF 文件？

可以。安装 Invoice, Purchase 等模块可以测试 print to PDF 功能
![Odoo 打印PDF](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-printtopdf-websoft9.png)

#### 是否有可视化的数据库管理工具？

请直接通过 [Odoo 自带的数据库管理工具](../odoo#dbadmin)操作

#### Odoo 在中国有哪些实施商？

如果您需要Odoo的配置，咨询、实施和开发服务，请与专业的服务商联系。我们了解到的信息如下：

*   苏州远鼎 http://www.chinamaker.net/
*   开源智造 http://www.oscg.cn/
*   上海寰享网络科技有限公司 https://www.elico-corp.com/zh_CN/
*   北京开远科技有限公司 https://www.kalway.cn/
*   珠海市信莱德软件开发有限公司 http://www.zhsunlight.cn/
*   成都欧督系统科技有限公司 http://www.odoostart.com/
*   山西清水欧度信息技术有限公司  http://www.odooqs.com (54773801@qq.com)

#### 有什么好的Odoo学习资源？

* Odoo爱好者博客：https://alanhou.org/category/odoo/

#### 贵司提供的企业版镜像包含授权吗？

不包含授权，用户需要向Odoo官方订阅授权。  

下面是关于试用、授权和费用的说明：

* 镜像部署后，用户需向官方申请免费试用30天
* 试用期之后，用户需向官方订阅商用授权以继续使用
* 镜像费用不包含 Odoo 授权费用，Odoo 授权费用也不包含镜像费用
* 镜像解决了用户的安装部署，订阅镜像一方面省去了安装麻烦，另外一方面可以在运维过程获得我们的技术支持
* 总体费用 = 云服务器费用 + 镜像费用 + 企业版授权费用

#### Odoo 社区版可以升级到企业版吗？

可以，但需要提前订阅企业版授权
