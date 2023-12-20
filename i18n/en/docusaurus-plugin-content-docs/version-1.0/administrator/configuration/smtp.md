---
sidebar_position: 6
slug: /administrator/smtp
---

# SMTP sheets

Sending mail is a common feature for RabbitMQ. With a large number of users' practice and feedback, only one way is recommended, that is, using the **third-party SMTP service** to send the email.

> Do not try to install **Sendmail** or other Mail server software on your Cloud Server for sending mail

## SMTP references

The following is the SMTP service settings of mainstream email providers ([Source](https://www.lifewire.com/search?q=smtp))

### QQ mail

- SMTP host: smtp.qq.com
- SMTP port: 465 or 587 for SSL-encrypted email
- SMTP Authentication: must be checked
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: This is not password of you mail, it is an authorization code you need to apply

> The above is for quick reference only. see the [QQ SMTP settings](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=166)


### 163 mail

- SMTP host: smtp.163.com
- SMTP port: 465 or 994 for SSL-encrypted email
- SMTP Authentication: must be checked
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: This is not password of you mail, it is an authorization code you need to apply

> The above is for quick reference only. see the [163 SMTP settings](https://help.163.com/09/1223/14/5R7P6CJ600753VB8.html?servCode=6010376)


### Aliyun mail

- SMTP host: smtp.mxhichina.com
- SMTP port: 465  for SSL-encrypted email
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: email password

> The above is for quick reference only. see the [Aliyun SMTP settings](https://help.aliyun.com/knowledge_detail/36576.html)

### SendGrid

To configure your application to send email through SendGrid’s SMTP service, use the settings below. Replace USERNAME with your SendGrid account username and PASSWORD with your SendGrid account password.  

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

## SMTP diagnosis

If you use the SMTP service provided by a third party (such as QQ mailbox, NetEase mailbox, etc.), the configuration is no problem, but you still cannot send mail. Please check the following questions:

1. Use the **telnet** to connect SMTP service to check it

> The successful Telnet test on the local computer does not mean that the server Telnet is successful, because your server IP address may be blacklisted by the STMP server for some reasons.

~~~
//Install telnet
yum install telnet -y

//sample one：test QQ mail
telnet smtp.qq.com 465

//sample one：test Gmail mail
telnet smtp.gmail.com 465

~~~

When you see the feedback code `220 smtp.*.com Esmtp *Mail Server ` or  `Escape character is '^]'`, it means connection is OK

2. The security group of Cloud Platform set the external access disabled
3. You iptables or firewall disabled the 465 or 587 port which for mail
4. OpenSSL version is low or CA certification have error