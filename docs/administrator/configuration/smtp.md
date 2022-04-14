---
sidebar_position: 6
slug: /administrator/smtp
---

# SMTP 发送邮件

应用中发送邮件是一个很常见的功能。经过大量用户实践反馈，只推荐一种发邮件的方式，即安装邮件插调用第三方邮件系统的STMP相关账号来进行邮件发送。

> 请忘掉在本机上安装sendmail等邮件服务器的方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不容易维护、不好诊断问题。

## SMTP配置

下面是主流的邮箱提供商之SMTP服务设置（[来源](https://www.lifewire.com/search?q=smtp) ）

### QQ邮箱

- SMTP host: smtp.qq.com
- SMTP port: 465 or 587 for SSL-encrypted email
- SMTP Authentication: must be checked
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: 这个密码不是邮箱密码，是需要通过QQ邮箱SMTP设置去获取的授权码

> The above is for quick reference only. see the [QQ邮箱SMTP设置](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=166)


### 163邮箱（网易）

- SMTP host: smtp.163.com
- SMTP port: 465 or 994 for SSL-encrypted email
- SMTP Authentication: must be checked
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: 这个密码不是邮箱密码，是需要通过163邮箱SMTP设置去获取的授权码

> 以上仅供快速设置参考，更多详情查看官网文档：[163邮箱SMTP设置](https://help.163.com/09/1223/14/5R7P6CJ600753VB8.html?servCode=6010376)


### 阿里云邮箱

- SMTP host: smtp.mxhichina.com
- SMTP port: 465  for SSL-encrypted email
- SMTP 身份认证: 必须勾选
- SMTP 加密: 需启用SSL
- SMTP username: email address
- SMTP password: email password

>以上仅供快速设置参考，更多详情查看官网文档： [阿里云邮箱SMTP设置](https://help.aliyun.com/knowledge_detail/36576.html)

### SendGrid


To configure your application to send email through SendGrid’s SMTP service, use the settings below. Replace USERNAME with your SendGrid account username and PASSWORD with your SendGrid account password.<br />

- SMTP host: smtp.sendgrid.net
- SMTP port: 25 or 587 for unencrypted/TLS email, 465 for SSL-encrypted email
- SMTP username: USERNAME
- SMTP password: PASSWORD

### Gmail

- Gmail SMTP server address: **smtp.gmail.com**
- Gmail SMTP username: **Your Gmail address** (e.g. _example@gmail.com_)
- Gmail SMTP password: **Your Gmail password**
- Gmail SMTP port (TLS): **587**
- Gmail SMTP port (SSL): **465**
- Gmail SMTP TLS/SSL required: **yes**

> Remember that in addition to these email server settings, you need to let the email client receive/download mail from your Gmail account too. There's more information on that at the bottom of this page.


### Outlook.com

- SMTP Server: smtp-mail.outlook.com
- Username: Your full Outlook.com email address
- Password: Your Outlook.com password
- SMTP Port	587
- SMTP TLS/SSL Encryption Required	Yes

### Hotmail

- **Hotmail SMTP Server**: smtp.live.com
- **Hotmail SMTP Username**: Your complete Windows Live Hotmail email address (e.g. _me@hotmail.com_ or _me@live.com_)
- **Hotmail SMTP Password**: Your Windows Live Hotmail password
- **Hotmail SMTP Port**: 587
- **Hotmail SMTP TLS/SSL Required**: yes

### Yahoo Mail

- Yahoo Mail SMTP server address: **smtp.mail.yahoo.com**
- Yahoo Mail SMTP username: Your full [**Yahoo email address**](https://www.lifewire.com/forward-yahoo-mail-to-another-address-1174481) (including **@yahoo.com**)
- Yahoo Mail SMTP password: Your **Yahoo Mail password**
- Yahoo Mail SMTP port: **465 **or** 587**
- Yahoo Mail SMTP TLS/SSL required: **yes**

> These settings work with most desktop, mobile, and web email programs and services. After you set up Yahoo Mail in your preferred email client, the mail and your Yahoo folders appear in both locations: in Yahoo and in your preferred app or web interface, such as Gmail.


### iCloud Mail

- Server name:** smtp.mail.me.com**
- SSL required: **Yes**
- Port: **587**
- SMTP authentication required: **Yes**
- Username: Type your full iCloud email address.
- Password: Type an app-specific iCloud Mail password.

### Zoho Mail

- Zoho Mail SMTP server address: **smtp.zoho.com**
- Zoho Mail SMTP port: **465**
- Zoho Mail SMTP TLS/SSL required: **Yes**
- Zoho Mail SMTP user name: **Your** **Zoho Mail address** (example@zoho.com or your email address if you use Zoho Mail with your own domain)
- Zoho Mail SMTP password: **Your** **Zoho Mail password**

### Directmail

Directmail是阿里云的邮件推送服务，相对于免费邮箱来说，自主性更强，同时更稳定可靠 
下面是Directmail的配置简要流程：
1. 登录阿里云邮件推送控制台，新增一个发信域名
   ![新增发信域名](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-dmailadd-websoft9.png)
2. 根据域名配置要求，在域名控制台完成对应的域名解析，并点击“验证”
   ![验证](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-dmailverify-websoft9.png)
3. 验证通过后，设置发信地址
   ![设置发信地址](https://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-dmailsetsendm-websoft9.png)
4. 如果需要接受用户的邮件回复，可以针对此发件地址配套一个回信地址。
5. 完成所有配置后，您会得到一个如下的SMTP参数

```
SMTP地址：smtpdm.aliyun.com 
SMTP用户名：norelpy@smtp.websoft9.cn
SMTP密码：*******
SMTP端口：465 需要启用ssl加密
SMTP端口：80 无需加密 
```

## SMTP诊断

如果使用第三方提供的SMTP服务（如qq邮箱、网易邮箱等），配置也没有问题，但是仍然无法发送邮件。请检查如下几个问题：

1. 通过服务器的telnet工具，验证服务器是否可以连接SMTP服务

> 注意：本地电脑Telnet测试成功，不代表服务器Telnet成功，因为您的服务器IP地址由于某些原因可能会被STMP服务器列入黑名单。

~~~
//安装telnet
yum install telnet -y

//示例1：测试qq邮箱 端口有465和587
telnet smtp.qq.com 465

//示例2：测试网易邮箱 端口有465和994
telnet smtp.163.com 465

~~~

出现 `220 smtp.*.com Esmtp *Mail Server `或 `Escape character is '^]'` 类似反馈，说明可以连接

2.  服务器安全组（出设置）禁止外部访问
3.  服务器系统iptables，firewall设置关闭了465等端口
4.  OpenSSL版本过低或者没有安装或其CA证书异常
