---
sidebar_position: 1
slug: /parseserver
tags:
  - Node
  - 平台即服务
  - Serverless
---

# 快速入门

[Parse Server ](https://parseplatform.org/) 基于 Node 的后端即服务平台。它通过对象和文件存储、用户身份验证、推送通知、仪表板等， 更快地构建应用程序。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/dashboard.png)

部署 Websoft9 提供的 Parse Server 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Parse Server 的 **[默认账号和密码](./user/credentials)**  


## Parse Server 初始化向导


### 详细步骤


1. 由于 Parse 不可通过 IP 访问，故务完成 **[域名解析](./administrator/domain_step)** 和 **[域名绑定](#binddomain)**

2. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名*  就进入 Parse Dashboard 登录页面
![Parse Dashboard 登录](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/ParseServer-loginpage-websoft9.png)

3. 输入账号和密码，登录后的界面如下
![Parse Dashboard 后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/parseserver/parse-backend-websoft9.png)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## Parse Server 使用入门

> 需要了解更多 Parse 的使用，请参考官方文档：[Parse Server Documentation](https://docs.parseplatform.org/)


## Parse Server 常用操作

### 域名绑定{#binddomain}

Parse 需绑定不同的子域名，例如：*parseserver.yourdomain.com* 和 *parsedashboard.yourdomain.com* 

Parse Server 域名绑定操作步骤：

1. 使用 SSH 连接云服务器，运行如下一条命令：
   ``` shell
   wget https://raw.githubusercontent.com/Websoft9/ansible-Parse-Server/master/script/parse-set-domain.sh && chmod +x parse-set-domain.sh &&./parse-set-domain.sh
   ```
2. 根据提示输入两个不同的域名，回车
   ```   
   Input Parse Server Domain: parseserver.websoft9.com
   Input Parse Dashboard Domain: parsedashboard.websoft9.com
   ```
3. 如果域名格式没有问题，会得到成功提示"Configure Done!"
4. 绑定完成

### 域名修改

修改域名不同于绑定域名，请严格参考下面的步骤：

1. 使用 SFTP 工具连接云服务器
2. 修改 */etc/nginx/conf.d/default.conf* 文件中两个域名信息
3. 修改 */etc/parse-server/parse-dashboard.json* 文件中的域名信息
4. 重启服务后生效
   ```
   sudo systemctl restart parse-dashboard
   sudo systemctl restart parse-server
   sudo systemctl restart nginx
   ```

### 修改 Parse Dashboard 账号密码

Parse Dashboard的账号密码存在它的配置文件中，修改步骤如下： 

1. 通过 SSH 工具连接到云服务器
2. 编辑 * /etc/parse-server/parse-server.json*，修改其中的 **users** 项
   ```
    "users": [
    {
      "user":"admin",
      "pass":"admin"
    } ]
   ```
3. 重启 Parse Dashboard 服务后生效
   ```
   systemctl restart parse-dashboard
   ```

## 参数

Parse Server 应用中包含 Nginx, Docker, MongoDB, adminMongo 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行 `docker ps`，可以查看到 Parse Server 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Parse Server 本身的参数：

### 路径{#path}

#### Parse Server 

Parse Server  程序目录： */usr/lib/node_modules/parse-server*  
Parse Server  配置文件： */etc/parse-server/parse-server.json*  
Parse Server  日志目录： */var/log/parse-server*  

> Parse Server 配置文件中包含数据库连接信息，更改了 MongoDB 账号密码，此处也需要对应修改

#### Parse Dashboard

Parse Dashboard  程序目录： */usr/lib/node_modules/parse-server*  
Parse Dashboard  配置文件： */etc/parse-server/parse-server.json*  
Parse Dashboard  日志文件： *直接在 Parse Dashboard 面板中查看*  


### 版本

控制台界面中查看

### 服务

```shell
sudo systemctl start | stop | restart | status parse-server
sudo systemctl start | stop | restart | status parse-dashboard
```
### 命令行

无

### API

[Parse API](https://docs.parseplatform.org/parse-server/guide/#using-parse-sdks-with-parse-server)

