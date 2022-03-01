---
sidebar_position: 1
slug: /elk
tags:
  - ELK Stack
  - 日志管理
  - 数据分析
---

# 快速入门

[ELK](https://www.elastic.co/cn/elastic-stack/) 是由 Elastic Stack 的简称（也称为 ELK Stack），由 Elasticsearch、Kibana、Beats 和 Logstash 等开源软件组成。能够安全可靠地获取任何来源、任何格式的数据，然后实时地对数据进行搜索、分析和可视化。ELK 适用于各种各样的用例，从日志开始，到您能想到的任何项目，无一不能胜任。

![ELK Stack](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-gui-websoft9.gif)

在云服务器上部署 ELK 安装环境之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 ELK，请先到 **域名控制台** 完成一个域名解析
4. 登录云服务器，运行下面的命令，拉取 ELK 相关 Docker 镜像并启动容器
   ```
   cd /data/wwwroot/elk && docker-compose pull && docker-compose up -d
   ```

   > Elastic 开源版 License 不允许第三方的分发行为，但允许用户免费使用，故需自行获取镜像。


## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### Kibana

* 管理员账号: `elastic`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

## ELK 安装向导

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入 ELK 登录界面
   ![ELK 登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-login-websoft9.png)

2. 输入账号密码（[不知道账号密码？](/zh/stack-accounts.md#elk)），成功登录到 ELK 后台  
   ![ELK 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-bkreminder-websoft9.png)
   ![ELK 控制台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-dashboard-websoft9.png)

> 需要了解更多 ELK 的使用，请参考官方文档：[ELK Documentation](https://www.elk.com/documentation.html)

## ELK 入门向导

ELK的数据源多种多样，这里用常见的日志文件为Logstash的输入为例，步骤如下：

1. 在Logstash的配置文件/data/wwwroot/elk/src/logstash/pipelinelogstash.conf设置索引"mytest"，并重启容器（[不知道账号密码？](/zh/stack-accounts.md#elk)）
```
input{
    file{
        path => "/var/log/yum.log"
        type => "elasticsearch"
        start_position => "beginning"
    }
}

output {
	elasticsearch {
		hosts => "elasticsearch:9200"
		user => "elastic"
		password => "xxxxx"
                index => "mytest"
	}
}
```

```
  cd /data/wwwroot/elk
  docker-compose down
  docker-compose up -d
```

2. 验证Elasticsearch和Logstash是否成功连接，索引数据是否生效(通过URL验证：http://服务器公网IP:9200/_cat/indices?v)
  
  ![ELK 验证](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizardindex-websoft9.png)
  
3. 登陆Kibana，点击【Manage】，再点击右侧菜单的【Index Patterns】
  
  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard1-websoft9.png)

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard2-websoft9.png)
  
  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard3-websoft9.png)

4. 检索"mytest"，根据提示完成创建

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard4-websoft9.png)
  
  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard5-websoft9.png)
  
5. 索引在Kibana创建成功，可以用时间条件在此检索数据

  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard6-websoft9.png)
  
  ![ELK Index](https://libs.websoft9.com/Websoft9/DocsPicture/zh/elk/elk-wizard7-websoft9.png)

## 常用操作

### 配置

ELK 目录下提供了 ELK Stack 各个组件的配置文件，用户可以修改配置文件，然后重启容器即可

### 域名绑定

绑定域名的前置条件是：已经完成域名解析（登录域名控制台，增加一个A记录指向服务器公网IP）  

完成域名解析后，从服务器安全和后续维护考量，需要完成**域名绑定**：

ELK 域名绑定操作步骤：

1. 确保域名解析已经生效  
2. 使用 SFTP 工具登录云服务器
3. 修改 [Nginx虚拟机主机配置文件](/维护参考.md#nginx)，将其中的 **server_name** 项的值修改为你的域名
   ```text
   server
   {
   listen 80;
   server_name elk.yourdomain.com;  # 此处修改为你的域名
   ...
   }
   ```
4. 保存配置文件，重启 [Nginx 服务](/维护参考.md#nginx-1)

### SSL/HTTPS

必须完成[域名绑定](/zh/solution-more.md)且可通过 HTTP 访问 ELK ，才可以设置 HTTPS。

ELK 预装包，已安装Web服务器 SSL 模块和公共免费证书方案 [Let's Encrypt](https://letsencrypt.org/) ，并完成预配置。因此，除了虚拟主机配置文件之外，HTTPS 设置则不需要修改 Nginx 其他文件。

## 快速指南

### 自动部署

如果没有申请证书，只需在服务器中运行一条命令`sudo certbot`便可以启动免费证书**自动**申请和部署

```
sudo certbot
```

### 手动部署

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
3. 重启[Nginx服务](/维护参考.md#nginx-1)

#### 专题指南

若参考上面的**简易步骤**仍无法成功设置HTTPS访问，请阅读由Websoft9提供的 [《HTTPS 专题指南》](https://support.websoft9.com/docs/faq/zh/tech-https.html#nginx)

HTTPS专题指南方案包括：HTTPS前置条件、HTTPS 配置段模板、注意事项、详细步骤以及故障诊断等具体方案。

### SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿在服务器上安装sendmail等邮件系统，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，非常不稳定，且不易维护、诊断故障很困难。

下面以**网易邮箱**为例，提供设置 ELK 发邮件的步骤：

1. 在网易邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.163.com
   SMTP port: 465 or 994 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9@163.com
   SMTP password: #wwBJ8    //此密码不是邮箱密码，是需要通过163邮箱后台设置去获取的授权码
   ```
2. 登录 ELK 控制台，依次打开：【Stack Management】>【Watcher】，增加一个 [Email Action](https://www.elastic.co/guide/en/elasticsearch/reference/current/actions.html)

3. 编辑 Elasticsearch 的配置文件，增加 [Email 配置](https://www.elastic.co/guide/en/elasticsearch/reference/current/actions-email.html)

更多邮箱设置（QQ邮箱，阿里云邮箱，Gmail，Hotmail等）以及无法发送邮件等故障之诊断，请参考由Websoft9提供的 [SMTP 专题指南](https://support.websoft9.com/docs/faq/zh/tech-smtp.html)

### 重置密码

常用的 ELK 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

登录 Kibana 后，右上角用户图标的【用户配置文件】即可修改密码

#### 找回密码

如果用户忘记了密码，需通过重新运行容器的方式重置密码：

```
cd /data/wwwroot/elk
docker-compose down && docker-compose up -d
```

`.env`文件中的 **DB_ES_PASSWORD** 变量即重置后的密码

### API

后续...

## 异常处理

#### 浏览器打开IP地址，无法访问 ELK（白屏没有结果）？

您的服务器对应的安全组 80 端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署方案采用什么安装方式

Docker
