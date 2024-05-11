---
sidebar_position: 1.2
slug: /guide/appsethttps
---

# 设置应用的 HTTPS 访问

HTTPS 能够加密客户端和服务器之间交换的数据，确保传输过程中的敏感信息不会被窃听者所截获。 

## 前置条件

Websoft9 网关虽然支持便捷的 HTTPS 配置，但配置 HTTPS 还有两个因素需要准备的：

- 开启服务器安全组的 443 端口
- 应用已经完成了[域名配置](./appsetdomain.md)，可以通过 HTTP 访问

具体以上条件后，便可以登录服务器配置 HTTPS。此处提供两种方案，请根据实际情况选择：  

## 控制台配置 HTTPS{#console}

### 自动证书{#auto}

网关默认支持 [Let's Encrypt](https://letsencrypt.org/) 免费的证书部署程序

1. 控制台依次打开：【网关】>【Hosts】>【Proxy Hosts】项

2. 编辑 SSL 项，点击保存即启动证书自动设置
   ![](./assets/websoft9-gateway-setautohttps.png)

   > Email 建议填写为可以收到邮件的常用邮箱，以便于及时了解证书的状态

### 上传证书{#upload}

Websoft9 的网关采用先上传证书，再绑定到 Proxy Host 的这种模式：

1. 控制台依次打开：【网关】>【SSL Certificates】

2. 点击【Add SSL Certificate】子菜单下的【Custom】项，开始增加自上传证书
   ![](./assets/websoft9-gateway-addcustomssl.png)

3. 在 Add Custom Certificate 选项卡中上传已有的证书

4. 转到网关的：【Hosts】>【Proxy Hosts】项，编辑应用的配置文件的 SSL 项，指定上面上传的证书

##  HTTPS 特别指南

#### CDN（全站加速）开启 HTTPS

如果应用需要使用云平台的 CDN 或全栈加速服务，相关的设置如下：

1. CDN/全站加速的控制台需设置 HTTPS
2. Websoft9 网关中为应用启用 HTTPS

需要注意的是，两端 HTTPS 必须使用同一套证书。

#### HTTP 自动跳转 HTTPS

Websoft9 控制台进入【网关】>【Proxy Hosts】，编辑域名的 SSL 设置，勾选**Force SSL** 即可

#### 中文域名配置 HTTPS

中文域名很特殊，它仅在中国被使用。HTTPS 是不支持中文域名的，但如何设置证书呢？

1. 在[中国互联网络信息中心](http://www.cnnic.cn/jczyfw/zwym/zgymzcjsy/201206/t20120612_26523.htm)转码。例如：`网久软件.com` 转码为 `xn--3iQsQ211JuqN.com`

2. 域名解析：将中文域名解析直接解析到服务器 IP 地址

3. 域名绑定：域名设置的 **Domain Names** 绑定 `xn--3iQsQ211JuqN.com`  

4. 启用 HTTPS



## 问题解答

#### 向云平台申请免费证书要注意什么？

全球主流云平台以及 [ZeroSSL](https://zerossl.com/) 都提供了免费证书申请：

*   免费证书只能用于单个域名，例如: buy.example.com 或 next.buy.example.com,
*   example.com 是通配符域名方式，不能用于申请免费证书
*   申请证书的时候，请先解析好域名，有些证书会绑定域名对应的 IP 地址，即一旦申请后，IP 地址不能更换，否则证书不可用


#### Docker 容器内支持 HTTPS？

部分容器支持，但建议通过网关配置 HTTPS

#### IP 地址可以申请 HTTPS 证书吗？

可以通过 openssl 为 IP 创建自签名证书，但在线的证书颁发机构不支持 IP 申请证书。  

#### Android 无法使用HTTPS，而 iOS 可以？

确保 SSLCertificateChainFile 已被采用

#### HTTPS 设置成功，仍显示“与此网站建立的连接并非完全安全”？

首选明确一点即您的HTTPS设置是成功的，只是由于网站中存在包含 http访问的静态文件 或 外部链接等，导致浏览器告警您的网站并非完全安全。

#### 证书上传到哪个目录？

请直接通过【网关】>【SSL】功能上传和管理证书，即不需要考虑存储在哪个目录

