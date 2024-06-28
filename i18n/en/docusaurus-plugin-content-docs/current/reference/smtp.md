---
sidebar_position: 10.1
slug: /smtps
---

# SMTP Services

Configuring the SMTP mail sending function in the application is a very important setting, which can be used for password recovery and notification of important operations.  

Due to the complexity of building a mail system, its routing configuration is subject to domain names, firewalls, routing and many other factors, making it very difficult to maintain a highly available mail system. Therefore, it is recommended to integrate a third-party SMTP service to complete the mail notification function.  

## SMTP providers

The following are the SMTP service settings of the mainstream mailbox providers


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

### QQ Mail{#qq}

- SMTP host: smtp.qq.com
- SMTP port: 465 or 587 for SSL-encrypted email
- SMTP Authentication: must be checked
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: It is not the email account password, it is an [authorisation code](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=166) obtained from the QQ email console.


### 163 Mail{#163}

- SMTP host: smtp.163.com
- SMTP port: 465 or 994 for SSL-encrypted email
- SMTP Authentication: must be checked
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: It is not the email account password, it is an [authorisation code](https://help.163.com/09/1223/14/5R7P6CJ600753VB8.html?servCode=6010376) obtained from the 163 email console.

### Aliyun Email{#aliyun}

- SMTP host: smtp.mxhichina.com
- SMTP port: 465  for SSL-encrypted email
- SMTP Authentication: must be checked
- SMTP Encryption: must SSL
- SMTP username: email address
- SMTP password: email password


## Test SMTP

However, after applying the SMTP settings, you still cannot send e-mail. In this case, you can test the availability of SMTP using the following suggestions

- Test for availability using [SMTP Test Tool](https://www.gmass.co/smtp-test)

- Use the following diagnostic path if SMTP was successfully authenticated in the previous step but still does not work in the application:

   - Run the `telnet` command on your server to test the SMTP network as follows

      ~~~
      telnet smtp.qq.com 465
      ~~~

      If you see **220 smtp.*.com Esmtp Mail Server** or **escape character is '^]'**, it means SMTP network is good.

   - Check that the server's Security Group does not allow external access.
   - Check if the server's iptables, firewall allow connections to external port 465.
   - Check if the OpenSSL version of the application is compatible with the SMTP service.
