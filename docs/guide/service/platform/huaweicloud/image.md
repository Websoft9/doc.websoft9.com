---
sidebar_position: 4
slug: /huaweicloud/image
---

# 镜像指南

Websoft9 与华为云合作，面向全球推出了一序列精品基于镜像部署的开源应用，并提供免费的技术支持。    

本文档主要针对于使用此类镜像的用户，提供应用访问、应用入门和应用管理三个方面的使用说明。

## 准备

在使用应用之前，需要做好如下准备工作：

- 服务器的安全组入方向开放端口：80 443 22 9000 9001
- 获取服务器 root 账号密码
- 解析一个域名到服务器（建议）

## 应用访问

本地浏览器访问应用 URL：*http://服务器公网 IP:9001*。一旦验证应用可以使用之后，建议尽快为应用 **[绑定域名](#domain)**。  

> 应用初始化过程需要的账号密码等信息，请 [访问管理面板](#panel) 后再 [查看应用信息](#info)

## 应用入门

Websoft9 为每个应用都编写详细的应用入门指南，详情请参考：[所有应用文档](../apps)

## 应用管理

每个应用都内置 Websoft9 可视化运维面板，管理应用的生命周期：

![myapp](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-myapp-websoft9.png)

- 在线 SFTP、SSH 终端等服务器管理工具一应俱全
- 绑定域名，免费 SSL 证书申请，HTTPS 配置等方便快捷
- 初始化账号、应用启停卸载、状态监控等操作灵活

### 访问管理面板{#panel}

本地浏览器访问应用 URL : *http://服务器公网 IP:9000*，账号为服务器的 `root` 账号
![login](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-login-websoft9.png)

### 配置域名{#domain}

在绑定域名之前，务必确保域名已经成功**解析**到应用所在的服务器，然后再参考下面的说明：

1. 打开管理面板：[**我的应用**] > [**访问**] 标签页

2. 点击 "添加域名" 按钮，增加所需绑定的域名
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/adddomain-access-websoft9.png)

3. 保存后生效

4. 绑定的域名，随时都可以**修改或删除**


### 设置 HTTPS

配置域名后，Websoft9 管理面板的 [网关](../function/gateway) 中就新增一条虚拟主机记录，将域名转发到 **容器ID:容器端口** 上（见下图）

![nginx](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-nginx-websoft9.png)

而 HTTPS 设置、访问控制、伪静态等更多设置，都通过 **网关** 进行操作：

1. 打开 Websoft9 管理面板，进入网关功能界面

2. 依次点击："Hosts" > "Proxy Hosts"，编辑应用的 Host 记录
   ![edit host](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-nginx-editproxy-websoft9.png)

3. 在 SSL 选项中配置证书（选择一种方式）
   
   - 无证书，在线申请 Let's Encrypt 免费证书（请填写自己的邮箱）
     ![nginx](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-nginx-ssl-websoft9.png)

   - 有证书，[上传证书](../guide/appsethttps#upload)后再设置

### 查看应用信息{#info}

面板左侧菜单[**我的应用**]查看应用信息，包括应用ID，版本信息、端口、访问 URL、登录账号，数据库信息等。

- 通过：[**我的应用**]-[**访问**] 标签页，查看应用 URL 和初始账号
- 通过：[**我的应用**]-[**数据库**] 标签页，查看数据库账号

![myapp](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-myapp-websoft9.png)

### 文件管理

面板左侧[**文件**]菜单，可以查看和管理服务器的文件

![file](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-file-websoft9.png)

### SSH 终端

面板左侧[**终端**]菜单，可以访问在线的 SSH 终端，直接连接到应用所在的 Linux 服务器

![ssh](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-teminal-websoft9.png)

### 管理数据库

Websoft9 应用商店内置 200+ 个工具，其中包含了 phpMyAdmin，pgAdmin，CloudBeaver 等 Web 数据库管理工具。  

但是，您当前使用的镜像中并没有在应用商店开放这些工具，需通过 SSH 工具，运行下面的命令放开它们：

```
docker exec -i websoft9-apphub apphub setconfig --section initial_apps --key keys --value $(docker exec -i websoft9-apphub apphub getconfig --section initial_apps --key keys),phpmyadmin,cloudbeaver,pgadmin
```

接下来，我们以 phpMyAdmin 为例，介绍如何管理数据库

1. Websoft9 管理面板的 **应用商店** 中安装 phpMyadmin

2. 然后，打开应用的编辑页面，通过 "数据库" 选项卡，查看数据库的主机名、账号密码等连接信息
   ![database](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-databseinfo-websoft9.png)

3. 访问 phpMyAdmin，输入上一步获得的数据库连接信息，即可连接
   ![phpmyadmin](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9-panel/w9-phpmyadmin-websoft9.png)
