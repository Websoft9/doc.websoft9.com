---
sidebar_position: 1
slug: /administrator/domain_step
---

# Five steps for Domain

## Five Steps

There five steps for configuring Domain for your application:   

* Login your Domain provider to: Register domain, Verify domain, Record domain and Resolve domain
* Connect your Server to **Binding domain**

### Register domain{#domainreg}

Register a domain name you like and match the characteristics of your website through a domain name service provider.

### Verify domain{#domainauth}

After the domain name registration is completed, it is also necessary to provide personal or company legal person certificates for real-name authentication of the domain name owner. 

### Record domain{#domainbei}

Some special region (e.g  China) need to Record domain for government if you can to resolve domain to your website.  

You can contact your Cloud platform to complete this business process.  

### Resolve domain{#domainresolve}

Make your DNS or sub DNS point to a IP address of Server  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/domain-websoft9.png)


### Binding domain{#domainbind}

Binding your DNS to a special application directory by modify the **vhost configuration file** when their have more than two websites or applications on your Server.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/apache/apache-vhostui-websoft9.png)

You can refer to different Web Server for it:  

* [Binding domain on Apache](../apache#domain)
* [Binding domain on Nginx](../nginx#domain)
* [Binding domain on Caddy](../caddy#template)
* [Binding domain on Traefik](../traefik#binddomain)
* [Binding domain on IIS](../iis#binddomain)


## FAQ

Here are the FAQs you may need:  

#### First-level domain name Second-level domain name?

When you completed one Domain, you owned a first-level Domain Name, e.g abc.com  
When you completed one DNS resolution for your website, e.g www.abc.com, this is a second-level Domain Name  

#### How do domain and servers associate?

The domain name needs to be resolved to the server through the **A record** to establish an association with the server. After the domain name is resolved to the server IP, the server will use the "domain name configuration file (vhost file)" to determine the mapping relationship between multiple domain names and multiple websites

#### How does the server recognize the level of the domain name?

abc.com and www.abc.com are different Domain Name for Cloud Server.

#### Domain resolution has not taken effect?{#effect}

After the resolution takes effect, local access may still not take effect due to cache problems, please clear the browser cache and DNS cache