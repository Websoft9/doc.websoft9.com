---
sidebar_position: 3
slug: /odoo/admin
tags:
  - Odoo
  - 企业管理
  - ERP
---

# Odoo Maintenance

This chapter is special guide for Odoo maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### 开启 PostgreSQL 远程连接

Odoo 默认安装的 PostgreSQL 并不会启用数据库账号，官方解决方案：https://www.odoo.com/documentation/13.0/setup/deploy.html#postgresql

### Odoo Upgrade

Odoo can be upgraded from Console, online follow the steps below to complete the upgrade:

1. Log in Odoo Console, [Enable developer mode](../odoo#dev-mode)
2. Go to **Settings** > **Updates** to start upgrade Odoo
   ![Odoo upgrade reminder](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-upgradesui-websoft9.png)
3. When completed the upgrade, you can get the successful reminder “Well done...”
4. Click the **Update Apps list** to upgrade all Odoo's Modules if you need

More details please refer to official docs [Odoo Update](https://www.odoo.com/documentation/master/setup/update.html)


## Troubleshoot{#troubleshoot}

In addition to the Odoo issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 如何查看 Odoo 错误日志？

最简单的方式是通过 SSH 连接服务器，运行`odoo`这个命令，就会显示错误日志以及 Odoo 的运行情况

#### Nginx “413 Request Entity Too Large” error?{#attachment}

The upload file size is limit 1M by default of Nginx, so you should lift this restrictions

1. Use WinSCP to connect Server
2. Edit [Nginx vhost configuration file](../nginx#virtualHosx)
3. Insert `client_max_body_size 0;` 
   ```
   server {
    listen 80;
    server_name _;
    client_max_body_size 0; #insert here
    ...
   ```
4. Save it and [Restart Nginx Service](../administrator/parameter#service)

#### Odoo 总出现数据库设置提醒？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-setpasswodrem-websoft9.png)

这个提醒的是要求你尽快给数据库设置一个高强度的管理员密码，如果不设置将面临很大的风险。一旦设置后，此界面就不会再弹出了

#### Could not upload file to Odoo program directory problem via SFTP?

Since some Ubuntu systems have created the default user name ubuntu by default, ubuntu does not have the right to operate the source code or directory of the odoo program for ordinary users. you need to execute the command:

```
sudo chmod o+rw  /usr/lib/python2.x/dist-packages/odoo   # odoo10
sudo chmod o+rw  /usr/lib/python3/dist-packages/odoo   # odoo11 or 12
```

#### Odoo can't print Chinese content?

When using the Odoo printing function, the downloaded PDF file is only in English and there is no Chinese part, resulting in incomplete printing. The reason is that the required Chinese font is not downloaded in the system environment. Solution: execute the following command to download fonts

~~~
sudo apt-get install ttf-wqy-zenhei
sudo apt-get install ttf-wqy-microhei
~~~

#### Command pg_dump not found？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-backuperror-websoft9.png)

现象：Odoo 备份数据时，报错：Command pg_dump not found  
原因：PostgreSQL 的备份命令没有找到
方案：需要进一步查看PostgreSQL安装问题，还是Odoo本身的问题


## FAQ{#faq}

#### Odoo support multi-language?

Yes, refer to [Add language](../odoo#setlang)

#### Where is the database connection configuration of Odoo?

Odoo used the [Peer Authentication](https://www.postgresql.org/docs/10/auth-methods.html#AUTH-PEER) to connect PostgreSQL, the peer authentication method works by obtaining the client's operating system user name from the kernel and using it as the allowed database user name (with optional user name mapping). This method is only supported on local connections.

#### Why can't I see the Odoo Updates feature in the Settings panel?

The function is only used in the developer mode, make sure you have change to [Developer Mode](../odoo#dev-mode)

#### How can I delete the Demo data of Odoo?

It is recommended to delete the database directly and then add it again (the Demo data is no longer checked)

#### Can Odoo export PDF files?

Yes, you can test it from the modules: Invoice, Purchase
![Odoo print to PDF](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-printtopdf-websoft9.png)


#### Is there a web-base GUI database management tools?

Yes, Odoo includes the database GUI functions, refer to [Odoo Mange Database function](../odoo#pgadmin) 

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
