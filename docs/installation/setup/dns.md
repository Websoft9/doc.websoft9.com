---
slug: /setup/dns
---

# 配置域名

域名的目的是通过一段容易识别的文字段来指向服务器上的网站。如果没有域名，网站就只能通过IP地址访问，这样不便于记忆和识别。

## 域名配置步骤

为了使网站可以通过域名访问，配置域名分为两个步骤：

*   **域名解析**：在域名的控制台上做一个将域名（或子域名）指向IP的操作(下图示例)
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/domain-websoft9.png)

*   **域名绑定**：域名绑定指一台服务器在多网站部署的时候，通过**虚拟主机配置文件**，将每个域名绑定到其对应的网站目录，从而达到每个网站都可以通过域名访问且相会不会干扰的效果。

下面是一个虚拟配置文件范例（LAMP环境）：

   ~~~ 
<VirtualHost *:80>
ServerName www.mydomain.com
ServerAlias other.mydomain.com
DocumentRoot "/data/wwwroot/default/mysite2"
ErrorLog "/var/log/httpd/www.mydomain.com_error_apache.log"
CustomLog "/var/log/httpd/www.mydomain.com_apache.log" common
<Directory "/data/wwwroot/default/mysite1">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
</VirtualHost>
   ~~~

通过修改配置文件中域名相关的值（ServerName,ServerAlias等）实现绑定域名

> 配置文件主要包括域名与网站的对应的关系，即某个域名应该对应访问哪个目录。如果服务器上有多个网站，就必须对应多个配置文件。

## 域名杂谈

我们在实践中，发现大家对域名的理解和描述有一些偏差，下面来个“正本清源”：

#### 什么是一级域名？二级域名？

当您成功注册了一个域名，就是拥有了一个一级域名，类似： abc.com ，
通过一级域名，可以设置出无数个二级域名，类似：www.abc.com 或 help.abc.com

> 如何设置二级域名？进入域名厂商提供的域名控制台设置。

#### 域名与服务器如何建立关联？

域名需要通过A记录的方式解析到服务器才能与服务器建立关联，域名解析到服务器IP之后，服务器会通过“域名配置文件（虚拟主机文件）”来判断多个域名与多个网站之间的映射关系

#### 服务器如何识别域名的级别？

不管是一级域名还是二级域名，对服务器来说都是不同的域名，abc.com 和 www.abc.com 对服务器来说两个独立的域名，即服务器不识别域名的级别。

#### 域名如何备案？

备案是中国大陆的一项法规，使用大陆节点服务器开办网站的用户，需要在服务器提供商处提交备案申请。

域名备案是纯粹的商务流程，需要登录到云平台的备案系统中完成备案。