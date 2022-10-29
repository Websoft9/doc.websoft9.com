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

### Enable PostgreSQL remote connection

Odoo default installed PostgreSQL does not enable the database account, the official solution:https://www.odoo.com/documentation/13.0/setup/deploy.html#postgresql

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

#### How to view Odoo error log?

The easiest way is to connect to the server via SSH, run the command `odoo`, it will display the error log and the operation of Odoo

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

#### Odoo always appears database setting reminder?

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-setpasswodrem-websoft9.png)

This reminder is that you are required to set a strong administrator password for the database as soon as possible. If you do not set it, you will face great risks. Once set, this interface will no longer pop up

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

Phenomenon: When Odoo backs up data, an error is reported: Command pg_dump not found
Reason: PostgreSQL backup command not found
Solution: Need to further check the PostgreSQL installation problem, or the problem of Odoo itself


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

#### Which implementers does Odoo have in China?

If you need Odoo configuration, consulting, implementation and development services, please contact a professional service provider. What we learned is as follows:

* Suzhou Yuanding http://www.chinamaker.net/
* Open source intelligent manufacturing http://www.oscg.cn/
* Shanghai Huanxiang Network Technology Co., Ltd. https://www.elico-corp.com/zh_CN/
* Beijing Kaiyuan Technology Co., Ltd. https://www.kalway.cn/
* Zhuhai Xinlaide Software Development Co., Ltd. http://www.zhsunlight.cn/
* Chengdu Oodoo System Technology Co., Ltd. http://www.odoostart.com/
* Shanxi Qingshui Odu Information Technology Co., Ltd. http://www.odooqs.com (54773801@qq.com)

#### What are some good Odoo learning resources?

* Odoo fan blog: https://alanhou.org/category/odoo/

#### Does the enterprise image provided by your company include license?

Authorization is not included, and users need to authorize the official subscription of Odoo.

Below is a description of trials, licenses and fees:

* After the image is deployed, users need to apply to the official for a 30-day free trial
* After the trial period, users need to subscribe to the official commercial license to continue to use
*Mirroring fees do not include Odoo licensing fees, and Odoo licensing fees do not include mirroring fees
* Mirroring solves the installation and deployment of users. On the one hand, subscribing to mirroring saves the trouble of installation. On the other hand, you can get our technical support during the operation and maintenance process.
* Overall fee = cloud server fee + image fee + enterprise license fee

#### Can Odoo Community Edition be upgraded to Enterprise Edition?

Yes, but you need to subscribe to the Enterprise Edition license in advance
