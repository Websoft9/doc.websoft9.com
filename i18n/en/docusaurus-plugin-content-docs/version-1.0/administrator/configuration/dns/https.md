---
sidebar_position: 3
slug: /administrator/domain_https
---

# Set HTTPS for App

### Basic settings for HTTPS{#https}

#### Prepare

Before you configure HTTPS, make sure that:

* Enable TCP:443 port of your Cloud Console
* Your application can accessed by HTTP

After the above conditions are specified, you can log in to the server to configure HTTPS. Two solutions are provided here, please choose according to the actual situation:

#### Solution one: Automatic deployment

Just run the one command `sudo certbot` on your instance to start the HTTPS deployment.

```
sudo certbot
```
This solution is based on [Let's Encrypt](https://letsencrypt.org/), and certifications stored in the file: `/etc/letsencrypt/live/`.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/certbot-ui-websoft9.png)


#### Solution one: Manual deployment

Manual deployment mean you should upload certs file for HTTPS:  

1. Upload your certs to directory: */data/cert*  

2. Open the **vhost configuration file** and insert **HTTPS template**

   * For Nginx: Insert below **HTTPS template** to *server{  }* in the **vhost configuration file** */etc/nginx/conf.d/default.conf* 
   
        ``` text
        #-----HTTPS template start------------
        listen 443 ssl; 
        ssl_certificate /data/cert/xxx.crt;
        ssl_certificate_key /data/cert/xxx.key;
        ssl_trusted_certificate /data/cert/chain.pem;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
        ssl_prefer_server_ciphers on;
        #-----HTTPS template end------------
        ```
    * For Apache: Insert below **HTTPS template** to **vhost configuration file** */etc/httpd/conf.d/vhost.conf* directly
        ```
        #-----HTTPS template start------------
        <VirtualHost *:443>
        ServerName  www.mydomain.com
        DocumentRoot "/data/wwwroot/default"
        #ErrorLog "logs/www.mydomain.com-error_log"
        #CustomLog "logs/www.mydomain.com-access_log" common
        <Directory "/data/wwwroot/default">
        Options Indexes FollowSymlinks
        AllowOverride All
        Require all granted
        </Directory>
        SSLEngine on
        SSLCertificateFile  /data/cert/www.mydomain.com.crt
        SSLCertificateKeyFile  /data/cert/www.mydomain.com.key
        SSLCertificateChainFile  /data/cert/www.mydomain.com_chain.crt
        </VirtualHost>
        #-----HTTPS template end------------
        ```

4.  Modify the HTTPS item for yourself, then save it
     
5.  Restart Web Server
    ```
    systemctl restart nginx
    systemctl restart apache
    ```

###  Special settings for HTTPS

#### Configure HTTPS when use CDN

If you want to use CDN, there have two HTTPS configurations for you:

1. Enable HTTPS on your CDN
2. Enable HTTPS on your Cloud Server

And make sure use the same Certification files on your Cloud Server and CDN.

#### HTTP redirect to HTTPS on Apache

For Apache, suggest your add the redirect rules in the file **.htacesss** of your application root directory

```
# All redirect
RewriteEngine On
RewriteCond %{SERVER_PORT} 80
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R,L]

# Redirect for one Domain
RewriteEngine On
RewriteCond %{HTTP_HOST} ^yourdomain\.com [NC]
RewriteCond %{SERVER_PORT} 80
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R,L]

# Redirect for on folder
RewriteEngine On
RewriteCond %{SERVER_PORT} 80
RewriteCond %{REQUEST_URI} folder
RewriteRule ^(.*)$ https://www.yourdomain.com/folder/$1 [R,L]

```

#### HTTP redirect to HTTPS on Nginx

Please use add the following rules in the Nginx vhost configuration file `server { }`

```
# HTTP to HTTPS
if ($scheme = http) {
    return 301 https://$host$request_uri;

```


## FAQ

#### How to set HTTPS for Docker app?

It is not recommended to set up HTTPS inside the container, but to configure HTTPS in port forwarding mode through the host's HTTP server (Nginx/Apache, etc.).

#### Android cannot use HTTPS, but IOS can?

Ensure that **SSLCertificateChainFile** has set the corresponding certificate file

#### Can an IP address apply for a certificate?

No

#### Where is the Certbot certifications?

Certbot directory:  */etc/letsencrypt/live*  

#### What Web Servers support HTTPS?

Mainstream Web Server can be easily supported, e.g [Apache](../apache#path), [Nginx](../nginx#path) , [Caddy](../caddy#path)    


