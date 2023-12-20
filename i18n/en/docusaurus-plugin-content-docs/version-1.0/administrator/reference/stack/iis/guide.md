---
sidebar_position: 1
slug: /iis
---

# Guide

## Tutorial

### Domain binding{#binddomain}

If you want to deploy more than one site on IIS,this step is necessary

1. Remote to Windows Server, open your IIS

2. IIS->Sites->Default Website(right click)->Edit Binding, select one host which is null,then Edit it
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/iis/iis-adddomain001-websoft9.png)

3. Fill in your domain name in Host Name,then click 【OK】 button

4. Add more domain name to this site, please select the 【Add】 button on the step 1


### Change root directory

It is very easy for changing root directory on IIS:  

1. IIS->Default Web Site(right click)->Manage Web Site->Advanced Settings
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/iis/iis-changeroot-websoft9.png)

2. Modify a new the Physical path

3. Restart the IIS,then it’s OK

### Set rewrite{#rewrite} 

1. Make sure you have install **[URL rewrite](https://www.iis.net/downloads/microsoft/url-rewrite)** components at IIS

2. Enter to site settings and edit rewrite rules
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrew-websoft9.png)

3. Restart IIS

### Set SSL/HTTPS on IIS{#https}

#### Solution one: Upload your certs

1. Upload your certs to Server

2. Import your certs at IIS
   ![1523428081837](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX3-websoft9.PNG)
   ![1523428307113](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX4-websoft9.png)

3. Waiting for importing successfully  
   ![1523428321945](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX5-websoft9.png)

4. Open your site setting and set the certs for it  
   ![1523428488886](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX6-websoft9.png)

   ![f1523428617943](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX7-websoft9.png)

5. Test your HTTPS access

#### Solution two: Auto create certs

You can use the free SSL/TLS Certificate Let's Encrypt, Let's Encrypt is a free, automated, and open Certificate Authority.

#####  Configure

1. Download [win-acme](https://github.com/PKISharp/win-acme/releases) to Server, and unzip to directory: `C:\Program Files`

    ![1523429808764](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt3-websoft9.png)

2. Run the `letsencrypt.exe`     

    ![1523429865345](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt4-websoft9.png)

3. Start to configure certs, select `N` for the first selection   

   ![1523430024664](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt5-websoft9.png)

4. Complete the next steps   

   ![1523430136570](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt6-websoft9.png)  
   ![1523430270351](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt7-websoft9.png)  

5. Configure completely   
   ![1523430320474](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt8-websoft9.png)

6. Open IIS to check your HTTPS access   
   ![1523430359697](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt9-websoft9.png)


##### Renewals

win-acme support renewals, below is the steps:  

1. Run the win-acme, input *L** at the first selection  
  ![1523430513122](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt10-websoft9.png)

2. Select your site which want to renewal
   ![1523430937571](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt11-websoft9.png)

3. Automatically renewal successfully
   ![1523431002175](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt12-websoft9.png)


## Troubleshoot{#troubleshoot}

## Parameters

### Service{#service}

IIS 中点击主机名称或 IIS 根目录，右侧的操作就会显示**启动、重启启动，停止**等操作

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-restart-websoft9.png)

