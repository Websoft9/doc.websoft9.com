---
sidebar_position: 4
slug: /huaweicloud/image
---

# Image Guide

This document is intended to introduce the usage guidelines for using Websoft9 application images based on cloud servers. Websoft9 Software provides free technical support for the running environment of the application image, and provides introductory guide document support for the use of the application. The content of this document covers three parts:
- Access to application 
- Application Getting Started Guide
- Application operation and maintenance management
## Prepare
Please open the port in the server's security group inbound direction: 80 443 22 9000 9001

## Access to application 
Access URL of application: http://ip:9001

Account information of application image: [View account information](#view-application-information-info)

## Application Getting Started Guide
Application Mirroring Getting Started Guide: https://support.websoft9.com/en/docs/next/apps/

## Operation and maintenance management of application 
Websoft9 provides a convenient and easy-to-use operation and maintenance management panel for application images (based on Cockpit, Portainer, Nginx, etc.), which can help users visually manage Linux, apply for free SSL certificates, configure domain names and other operations:
- Visual management of Linux, including files, FTP, and terminal tools
- Domain configuration, free SSL certificate application, https configuration is convenient and fast
- Software account management, running status monitoring, and flexible management of uninstallation and installation

![myapp](https://libs.websoft9.com/Websoft9/DocsPicture/en/websoft9-panel/w9-myapp-websoft9.png)


### Operation and maintenance management panel access
Access URL of the operation and maintenance panel: http://ip:9000
Account for the operation and maintenance management panel: root account of the server

![login](https://libs.websoft9.com/Websoft9/DocsPicture/en/websoft9-panel/w9-login-websoft9.png)

### View application information {#info}

Use the menu on the left side of the panel [**My Application**] to view application information, including application ID, version information, port, access URL, login account, database information, etc.

- View the application URL and initial account through [**My App**]-[**Access**]
- Check the database account through [**My Application**]-[**Database**]

![myapp](https://libs.websoft9.com/Websoft9/DocsPicture/en/websoft9-panel/w9-myapp-websoft9.png)

### File Management
File management can be done through the left menu [**Navigator**], which is usually used to view and manage server files, and can also be used to upload and download files.

![file](https://libs.websoft9.com/Websoft9/DocsPicture/en/websoft9-panel/w9-file-websoft9.png)

### Terminal tools
You can open the terminal tool through the left menu [**Terminal**] to facilitate the use of commands to interact with Linux

![file](https://libs.websoft9.com/Websoft9/DocsPicture/en/websoft9-panel/w9-teminal-websoft9.png)


### Domain name configuration

Through the left menu [**Gateway**], you can open the built-in Nginx Proxy Manager tool to visually complete domain name binding, certificate application, https configuration and other operations.

1. Domain resolution: The domain  provider controls the resolution of the domain name to the server IP.
2. Obtain application information for domain name binding: Click the application in [**My Apps**], and obtain the app ID and port by applying the [**Container**] option (the ports are the host port and application container port).

![nginx](https://libs.websoft9.com/Websoft9/DocsPicture/en/websoft9-panel/w9-nginx-websoft9.png)

3. Domain binding: click [**Gateway**], click [**Proxy Hosts**], click [**Add Proxy Hosts**]. Fill in the domain name information and application container information to bind the domain name.

![nginx](https://libs.websoft9.com/Websoft9/DocsPicture/en/websoft9-panel/w9-nginx-addproxy-websoft9.png)


![nginx](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-nginx-dns-websoft9.png)

4. SSL certificates management: If you already have a certificate, you can upload it. Click [**Gateway**], click [**SSL Certificates**], click [**Add SSL certificate**]-[**Custom**] to upload the certificate.

5. Certificate configuration: By configuring an SSL certificate for the domain , secure https access to the website is achieved. Click [**Gateway**], select the domain name for which you want to configure the certificate in [**Proxy Hosts**], edit the Proxy Host, and configure the certificate in the SSL option. For the certificate, you can choose an existing certificate or apply for a free certificate through Let's Encrypt.

![nginx](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-nginx-editproxy-websoft9.png)


![nginx](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-nginx-ssl-websoft9.png)




### Database Management

The app store includes phpMyAdmin, pgAdmin, CloudBeaver and other web visual database management tools. Users can customize the installation and manage the database in the app store. The following is how phpMyAdmin manages MySQL for WordPress.
1. Obtain application database information: Click Application in [**My Apps**], and obtain host and account information by applying the [**Database**] option.

![database](https://libs.websoft9.com/Websoft9/DocsPicture/en/websoft9-panel/w9-databseinfo-websoft9.png)


2. Connect to the database: Open phpMyAdmin, enter data information, and connect to the database server.

![phpmyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/en/websoft9-panel/w9-phpmyadmin-websoft9.png)
