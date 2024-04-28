---
sidebar_position: 6
slug: /smtps
---

# SMTP 服务

应用中配置 SMTP 邮件发送功能是非常重要的设置，它可以用于密码找回和重要操作的通知。  

由于邮件系统的搭建非常复杂，其路由配置受制域名、防火墙、路由等多种因素制约，导致维护一个高可用的邮件系统非常困难。所以应用都建议集成第三方的 SMTP 服务来完成邮件通知功能。  

## SMTP 配置

下面是主流的邮箱提供商之 SMTP 服务设置（[来源](https://www.lifewire.com/search?q=smtp) ）

### QQ邮箱{#qq}

- SMTP host: smtp.qq.com
- SMTP port: 465 or 587 for SSL-encrypted email
- SMTP Authentication: must be checked
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: 这个密码不是邮箱密码，是需要通过QQ邮箱SMTP设置去获取的授权码

> The above is for quick reference only. see the [QQ邮箱SMTP设置](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=166)


### 163邮箱（网易）{#163}

- SMTP host: smtp.163.com
- SMTP port: 465 or 994 for SSL-encrypted email
- SMTP Authentication: must be checked
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: 这个密码不是邮箱密码，是需要通过163邮箱SMTP设置去获取的授权码

> 以上仅供快速设置参考，更多详情查看官网文档：[163邮箱SMTP设置](https://help.163.com/09/1223/14/5R7P6CJ600753VB8.html?servCode=6010376)


### 阿里云邮箱{#aliyun}

- SMTP host: smtp.mxhichina.com
- SMTP port: 465  for SSL-encrypted email
- SMTP 身份认证: 必须勾选
- SMTP 加密: 需启用SSL
- SMTP username: email address
- SMTP password: email password

>以上仅供快速设置参考，更多详情查看官网文档： [阿里云邮箱SMTP设置](https://help.aliyun.com/knowledge_detail/36576.html)

### SendGrid{#sendgrid}


To configure your application to send email through SendGrid’s SMTP service, use the settings below. Replace USERNAME with your SendGrid account username and PASSWORD with your SendGrid account password.<br />

- SMTP host: smtp.sendgrid.net
- SMTP port: 25 or 587 for unencrypted/TLS email, 465 for SSL-encrypted email
- SMTP username: USERNAME
- SMTP password: PASSWORD

### Gmail{#gmail}

- Gmail SMTP server address: **smtp.gmail.com**
- Gmail SMTP username: **Your Gmail address** (e.g. _example@gmail.com_)
- Gmail SMTP password: **Your Gmail password**
- Gmail SMTP port (TLS): **587**
- Gmail SMTP port (SSL): **465**
- Gmail SMTP TLS/SSL required: **yes**

> Remember that in addition to these email server settings, you need to let the email client receive/download mail from your Gmail account too. There's more information on that at the bottom of this page.


### Outlook.com{#outlook}

- SMTP Server: smtp-mail.outlook.com
- Username: Your full Outlook.com email address
- Password: Your Outlook.com password
- SMTP Port	587
- SMTP TLS/SSL Encryption Required	Yes

### Hotmail{#hotmail}

- **Hotmail SMTP Server**: smtp.live.com
- **Hotmail SMTP Username**: Your complete Windows Live Hotmail email address (e.g. _me@hotmail.com_ or _me@live.com_)
- **Hotmail SMTP Password**: Your Windows Live Hotmail password
- **Hotmail SMTP Port**: 587
- **Hotmail SMTP TLS/SSL Required**: yes

### Yahoo Mail{#yahoo}

- Yahoo Mail SMTP server address: **smtp.mail.yahoo.com**
- Yahoo Mail SMTP username: Your full [**Yahoo email address**](https://www.lifewire.com/forward-yahoo-mail-to-another-address-1174481) (including **@yahoo.com**)
- Yahoo Mail SMTP password: Your **Yahoo Mail password**
- Yahoo Mail SMTP port: **465 **or** 587**
- Yahoo Mail SMTP TLS/SSL required: **yes**

> These settings work with most desktop, mobile, and web email programs and services. After you set up Yahoo Mail in your preferred email client, the mail and your Yahoo folders appear in both locations: in Yahoo and in your preferred app or web interface, such as Gmail.


### iCloud Mail{#icloud}

- Server name:** smtp.mail.me.com**
- SSL required: **Yes**
- Port: **587**
- SMTP authentication required: **Yes**
- Username: Type your full iCloud email address.
- Password: Type an app-specific iCloud Mail password.

### Zoho Mail{#zoho}

- Zoho Mail SMTP server address: **smtp.zoho.com**
- Zoho Mail SMTP port: **465**
- Zoho Mail SMTP TLS/SSL required: **Yes**
- Zoho Mail SMTP user name: **Your** **Zoho Mail address** (example@zoho.com or your email address if you use Zoho Mail with your own domain)
- Zoho Mail SMTP password: **Your** **Zoho Mail password**

### Directmail{#derectmail}

Directmail 是阿里云的邮件推送服务，相对于免费邮箱来说，自主性更强，同时更稳定可靠。   

下面是 Directmail 的配置简要流程：

1. 登录阿里云 Directmail 控制台，新增一个发信域名  

2. 根据 Directmail 要求，在域名控制台完成域名解析，并“验证”  

3. 验证通过后，Directmail 控制台设置发信地址（一个发信域名支持多个发信地址）

4. 完成所有配置后，您会得到一个如下的 SMTP 服务信息
   ```
   Host：smtpdm.aliyun.com 
   User：norelpy@smtp.websoft9.cn
   Password：*******
   SSL Port：465
   ```

## SMTP 诊断

如果已经确认 SMTP 服务本身可用（[SMTP Test Tool](https://www.gmass.co/smtp-test)），但应用仍然无法发送邮件，从几个方面开始诊断：

- 应用所在的服务器运行 `telnet` 命令 ，检查 SMTP 服务的连通性。下面是一个范例：

   ~~~
   telnet smtp.qq.com 465
   ~~~

   出现 **220 smtp.*.com Esmtp Mail Server** 或 **Escape character is '^]'** ，说明连接成功

- 检查服务器安全组（出设置）是否禁止外部访问
- 检查服务器 iptables，firewall 是否允许发起向外部 465 端口的连接
- 检查应用程序的 OpenSSL 版本是否过低或 CA 证书与 SMTP 服务兼容性
