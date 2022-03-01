---
sidebar_position: 1
slug: /scratch
tags:
  - Scratch
  - 少儿编程
---

# 快速入门

[Scratch](https://scratch.mit.edu/) 是一款由麻省理工学院(MIT) 设计开发的一款面向少年的简易编程工具，scratch已经是少儿编程行业的基础软件。使用 Scratch，你可以编写属于你的互动媒体，像是故事、游戏、动画，然后你可以将你的创意分享给全世界。Scratch3.0是一个部署在服务器上的Web版本，有浏览器就可以使用Scratch。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/scratch/scratch-gui-websoft9.png)


在云服务器上部署 Scratch 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 Scratch，请先到 **域名控制台** 完成一个域名解析

## 账号密码

使用Scratch，可能会用到的几组账号密码如下：

### Scratch

当前版本无需登录

## Scratch 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://Internet IP*, 就进入了Scratch
![Scratch初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/scratch/scratch-gui-websoft9.png)

2. Scratch首次加载数据超过20M，如果您的网络带宽不足的话，加载会很慢，耐心等待

> 需要了解更多Scratch的使用，请参考官方文档：[Scratch Documentation](https://en.scratch-wiki.info)


## 常用操作

### 域名绑定

绑定域名的前置条件是：Scratch已经可以通过解析后的域名访问。  

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

Scratch 域名绑定操作步骤：

1. 登录云服务器
2. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的**server_name**的值 *_* 修改为你的域名
   ```text
    server {
    listen 80;
    server_name _;   # _改为自定义域名
    root /data/wwwroot/scratch-gui/build;
    }
   ```
3. 保存配置文件，重启[Nginx服务](/维护参考.md#nginx-1)

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

Scratch 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。

> 除了虚拟主机配置文件之外，HTTPS设置无需修改Nginx任何文件

## 快速指南

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

#### 手动部署

如果你已经申请了证书，只需三个步骤，即可完成 HTTPS 配置

1. 将申请的证书、 证书链文件和秘钥文件上传到 */data/cert* 目录
2. 打开虚拟主机配置文件：*/etc/nginx/conf.d/default.conf* ，插入**HTTPS 配置段** 到 *server{ }* 中
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
3. 重启Nginx服务

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿尝试在服务器上安装sendmail等发邮件方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不易维护、诊断故障困难。

下面以**网易邮箱**为例，提供设置 Scratch 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. Scratch没有后台，暂不需要SMTP

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


### 迁移

暂无


## 异常处理

#### 浏览器打开IP地址，无法访问 Scratch（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### Scratch打开很慢？

Scratch首次加载数据超过20M。例如：您使用的是2M带宽，那么理想情况下的加载时间为：20000k/(128k/s×2)=78s。显然，如果带宽不足，速度会非常慢。
