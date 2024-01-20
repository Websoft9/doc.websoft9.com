---
sidebar_position: 5
slug: /user/gateway
---

# 网关

网关需具备一定的 HTTP 服务应用经验的用户使用，否则很容易破坏已安装应用的访问。  

![应用网关](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-gateway-dashboard.png)

Websoft9 控制台集成了 Nginx Proxy Manager（简称 NPM） 作为**应用程序网关**。[NPM](https://nginxproxymanager.com/guide/) 是一个基于 Nginx 的免费、开源的代理服务器管理面板，它为用户提供了一个友好的 web 界面，用于管理和部署 Nginx 代理服务器的功能，包括：

- 反向代理
- 负载均衡
- TCP/UDP 端口转发
- 404 重定向
- 自动化的 SSL 证书申请与续期
- 访问控制与白名单

通过 Websoft9 应用商店安装的程序，会自动发布为 **域名** 访问。其中就是通过调用网关的接口，自动创建域名绑定到容器端口。  

## 操作

[NPM 官方文档](https://nginxproxymanager.com/guide/) 很全面的介绍了它的使用和配置，下面我结合一些配置场景进行更灵活的运用：

### 配置 HTTPS 证书{#sethttps}

Websoft9 的网关支持自动证书和上传证书两种类型：

#### 前置条件

Websoft9 网关虽然支持便捷的 HTTPS 配置，但配置 HTTPS 还有两个因素需要准备的：

- 开启服务器安全组的 443 端口
- 网站可以通过 HTTP 的方式访问域名

具体以上条件后，便可以登录服务器配置 HTTPS。此处提供两种方案，请根据实际情况选择：  

#### 自动证书

网关默认支持 [Let's Encrypt](https://letsencrypt.org/) 免费的证书部署程序

1. 控制台依次打开：【网关】>【Hosts】>【Proxy Hosts】项

2. 编辑 SSL 项，点击保存即启动证书自动设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-gateway-setautohttps.png)

   > Email 建议填写为可以收到邮件的常用邮箱，以便于及时了解证书的状态

#### 上传证书

Websoft9 的网关采用先上传证书，再绑定到 Proxy Host 的这种模式：

1. 控制台依次打开：【网关】>【SSL Certificates】

2. 点击【Add SSL Certificate】子菜单下的【Custom】项，开始增加自上传证书
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-gateway-addcustomssl.png)

3. 在 Add Custom Certificate 选项卡中上传已有的证书

4. 转到网关的：【Hosts】>【Proxy Hosts】项，编辑应用的配置文件的 SSL 项，指定上面上传的证书

### 为应用设置密码访问

有些应用安装后，并没有密码（例如：Netdata），这样直接暴露给互联网用户是不合理的。  

Websoft9 的网关具备为此类应用设置密码访问，具体步骤如下：

1. 控制台依次打开：【网关】>【Access Lists】

2. 点击【New Access List】，新增一个访问控制项

   - Details: 输入英文名称
   - Authorization：输入账号密码
   - Access：allow 出输入可以访问的[白名单](https://nginx.org/en/docs/http/ngx_http_access_module.html#allow)，0.0.0.0/ 表示允许所有 IP 访问

3. 转到网关的：【Hosts】>【Proxy Hosts】项，编辑应用的配置文件，选择上面配置的 Access
   ![设置 Access](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-gateway-setaccess.png)


### 转发数据库端口

如果数据库容器没有绑定到宿主机端口，也没有关系，只需要通过网关的 **Streams** 功能设置即可：

1. 控制台依次打开：【网关】>【Hosts】>【Streams】项

2. 填写好 Incoming Port 以及被转发的 Forward Host 和 Forward Port

### Proxy Host 的 Advanced 设置

Advanced 是一个 server 级作用域（非 location / 作用域），但可以自定义 location / 覆盖默认值

下面是一个可以覆盖默认 location / 的全局设置：  

```
location / {
        add_header       X-Served-By $host;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Scheme $scheme;
        proxy_set_header X-Forwarded-Proto  $scheme;
        proxy_set_header X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header X-Real-IP          $remote_addr;
        proxy_pass       $forward_scheme://$server:$port$request_uri;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection upgrade;
    }
```

### Proxy Host 增加 Location 指令

直接把指令的内容（参考下面的模板）复制到设置框（通过 location 【齿轮】图标打开）

```
proxy_pass http://$server:8080; 
proxy_http_version 1.1;
proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

### 静态网站支持

把网关当做应用程序服务器，在网关容器中上传静态网站内容这种静态网站发布方式是不建议的。  

推荐的方式是：

1. 先运行一个静态网站容器，并将静态网站源码与容器绑定

2. 通过网关将静态网站端口访问发布出来


## 常见问题

#### 用户可以自行修改网关邮件地址吗？

目前不可以，修改后会导致程序异常

#### IP 地址的 Proxy 是否可以设置 HTTPS？

不可以




