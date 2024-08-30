---
sidebar_position: 1
slug: /runtime/php
tags:
  - PHP
  - LAMP
  - LNMP
  - Runtime
---

# Deploy PHP app

## Deploy Your PHP application{#phpapps}

To deploy PHP application on LAMP, you need to add **VirtualHost** for it
> VirtualHost is vhost configuration segment. Each application must correspond to a unique VirtualHost in **vhost.conf / default.cong**

* [Apache vhost configuration file](../apache#path): /etc/httpd/conf.d/vhost.conf
* [Nginx vhost configuration file](../nginx#path): /etc/nginx/conf.d/default.conf
  
Overall, just need two steps: 
1. Upload source codes of applicaiton
2. Add new VirtualHost vhost configuration segment

* [Apache VirtualHost](../apache#virtualhost) ：`<VirtualHost *:80>...</VirtualHost>`
* [Nginx VirtualHost](../nginx#wwwtemplate) ：`server{}`


### Deploy fisrt application

There is a example application in LAMP, we sugget you to **replace the example application** for deploy first application:

1. Use WinSCP to connect Cloud Server
2. Delete all files in the folder */data/wwwroot/www.example.com*, but don't delete *www.example.com*
3. Upload your application's codes to the folder: */data/wwwroot/www.example.com* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/winscp-uploadcodestoexample-websoft9.png)

4. Modify the virtual host configuration file to realize operations such as binding domain  and modifying website directory
 * [Apache](../apache#virtualhost) ：`<VirtualHost *:80>...</VirtualHost>`
 * [Nginx](../nginx#wwwtemplate) ：`server{}`


5. Save virtual host configuration file and then restart service
    ~~~
    # restart Apache
    systemctl restart httpd
    
    # restart Nginx
    systemctl restart httpd
    ~~~

6. Using the Chrome or Firefox to visit: *http://domain* or *http://IP/mysite2* to visit your application


### Deploy second application

Start to deploy the second application, you should add new VirtualHost segment to the file *vhost.conf* 

1. Use WinSCP to connect Cloud Server，create a new "mysite2" website directory under /data/wwwroot
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-createmysite2-websoft9.png)

2. Upload your application's codes to the folder:：*/data/wwwroot/mysite2* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-uploadcodes-websoft9.png)

3. Edit the **Virtual machine host configuration file** file to get the code snippet according to the scenario:

    | Web Server | 场景                                          | 获取代码段                    |
    | ---------- | --------------------------------------------- | ----------------------------- |
    | Apache     | **有域名，通过 http://域名 访问网站**         | [获取](../apache#wwwtemplate) |
    |            | **没有域名，通过 http://IP/mysite2 访问网站** | [获取](../apache#aliastemplate) |
    | Nginx      | **有域名，通过 http://域名 访问网站**         | [获取](../apache#wwwtemplate) |
    |            | **没有域名，通过 http://IP/mysite2 访问网站** | [获取](../apache#httpstemplate) |

4. Save virtual host configuration file and then restart service
    ~~~
    # restart Apache
    systemctl restart httpd
    
    # restart Nginx
    systemctl restart httpd
    ~~~

5. Using the Chrome or Firefox to visit: *http://domain* or *http://IP/mysite2* to visit your application


### Deploy more application

**Deploy more application** is the same with **Deploy second application**

Finally, we know the new and summarize the steps of the LAMP deployment site: 

1. Upload the website code 
2. Bind the domain name (not necessary) 
3. Add the site configuration or modify the sample site configuration 
4. Increase the database corresponding to the site (not necessary) 
5. Enter the installation wizard


## Maintain PHP Environment

Refer to：[《PHP Guide》](../php) and [《PHP Advanced》](../php/advanced) 



