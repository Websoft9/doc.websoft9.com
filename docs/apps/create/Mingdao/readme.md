---
sidebar_position: 1
slug: /mingdao
tags:
  - 明道云
  - IT 架构
  - 无代码平台
---

# 快速入门

[明道云](https://www.mingdao.com/) 是一个无代码开发平台，它可以让企业的业务部门在**不需要编程序**的情况下，自行创作出完全符合实际需求的软件系统。

![](https://alifile.mingdaocloud.com/wwwhome/dist/pack/static/src-common-mdfeature-img-2x-yy02.jpg)

Websoft9 提供的是明道云私有部署的**免费版**。它相对于**标准版**和**专业版**等收费版本来说，其有如下限制：  

- 用户数不超过 30 个
- 单个工作表最大行数 10 万行

> 当本文档无法完全找到所需的参考时，请务必阅读：[明道云官方文档](https://docs.pd.mingdao.com/)



## 准备

在云服务器上部署本软件之后，请参考下面的步骤快速入门。

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:38881** 和 **TCP:8880** 端口是否开启
3. 若想用域名访问，请先到 **域名控制台** 完成一个域名解析


## 明道云安装向导

明道云安装向导包含三个过程：初始化、安装数据、设置管理员：

1. 使用本地电脑的浏览器访问网址：*http://服务器公网IP:38881* 进入初始化页面

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-initial1-websoft9.png)

   > 上图中访问地址的默认端口 8880 可自行设置为其他端口号

2. 设置访问地址后，进入【下一步】，开始初始化（过程持续约 3~5 分钟）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-initial2-websoft9.png)

3. 初始化完成后，开始**安装数据** （此过程中会引导至明道云官网申请密钥）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-install1-websoft9.png)
   

4. 完成**注册系统管理员**信息（务必牢记账号密码）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-set-admin-websoft9.png)

5. 访问第1步设置的访问地址（例如：**http://服务器公网IP:8880**），登陆明道云后台

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-login-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-main-app-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-main-lib-websoft9.png)


> 需要了解更多 明道云 的使用，请参考：[明道云官方文档](https://help.mingdao.com/)

## 明道云入门向导

明道云官方提供了非常贴心的教程和视频指南，赶快[学习](https://help.mingdao.com/)去吧

## 明道云定制服务

Websoft9 作为明道的合作伙伴，具备基于明道云的软件快速构建能力。我们可以为客户提供如下的服务：

* 基于实际业务，快速建立基础数据模型
* 提炼管理流程，将业务融合到软件操作中
* 将明道云与其他系统的连接集成，打破企业数据孤岛

![](https://alifile.mingdaocloud.com/wwwhome/dist/pack/static/src-common-partnerIntroduction-img-jj2.png)

欢迎广大的客户朋友和行业合作[联系我们](./helpdesk#contact)。

## 常用操作

### 维护

请参考官方提供的：[《私有版维护文档》](https://docs.pd.mingdao.com/)，包括：短信设置、对象存储设置、网络访问、环境变量、服务管理等

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

明道云 域名绑定操作步骤：

1. 确保域名解析已经生效  

2. 使用 SFTP 工具登录云服务器

3. 修改 [Nginx虚拟机主机配置文件](/zh/stack-components.md#nginx)，根据需要修改 **server_name** 和 **proxy_pass** 的值
   ```text
   server
   {
   listen 80;
   server_name mingdao.yourdomain.com;  # 此处修改为你的域名
       location / {
        proxy_pass  http://127.0.0.1:8880; # 此处修改为你的端口
   ...
   }
   ```

4. 保存配置文件，重启 [Nginx 服务](/zh/admin-services.md#nginx)

### 重置密码

常用的 明道云 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 明道云 后台，依次打开：【系统设置】>【用户管理】，找到所需修改密码的账号对象

2. 开始修改密码

#### 找回密码

方案有待完善

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 明道云 ，才可以设置 HTTPS。

明道云 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

#### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

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
3. 重启[Nginx服务](/zh/admin-services.md#nginx)

#### 专题指南

若参考上面的**快速指南**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

《HTTPS 专题专题》方案包括：HTTPS前置条件、HTTPS 配置段模板及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 明道云 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录明道云，打开右上角用户图标下的【系统配置】，点击【邮件服务设置】开始配置
   ![明道云 SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-smtp-websoft9.png)

3. 完成设置

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)


## 异常处理

#### 浏览器打开IP地址，无法访问 明道云（白屏没有结果）？

您的服务器对应的安全组 38881 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 为什么采用单机部署？

私有部署版虽然是一个单机部署方式，单其内部依然是一个微服务集合，所以为了保证容器内各服务进程的可用性，在容器内部预置了健康检查线程，当某服务出现故障时能自动恢复。

#### 访问地址的端口号可以不用 **8880** 吗？

可以，但需要在云控制台安全组中，检查 **Inbound（入）规则** 下您所使用的端口确保开启


#### 服务器重启后，服务器IP地址变化，导致工作流等一些服务无法使用

服务器IP变化后，需要修改 docker-compose 配置：
打开 /data/mingdao/script/docker-compose.yaml，修改 ENV_MINGDAO_HOST 为新的IP，再用重启服务

```
version: '3'

services:
  app:
    image: registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-community:2.10.1
    environment:
      ENV_MINGDAO_PROTO: "http"
      ENV_MINGDAO_HOST: "123.57.218.118"  
      ENV_MINGDAO_PORT: "8880"
      COMPlus_ThreadPool_ForceMinWorkerThreads: 100
      COMPlus_ThreadPool_ForceMaxWorkerThreads: 500
    ports:
      - 8880:8880
    volumes:
      - ./volume/data/:/data/
      - ./volume/tmp/:/usr/local/MDPrivateDeployment/wwwapi/tmp/
      - /usr/share/zoneinfo/Etc/GMT-8:/etc/localtime
      - ../data:/data/mingdao/data

  doc:
    image: registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-doc:1.2.0
```


