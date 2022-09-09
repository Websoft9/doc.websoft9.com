---
sidebar_position: 100
slug: /fastpanel
tags:
  - Web 面板
  - 可视化
  - GUI
---

# 快速入门

FASTPANEL 面板是可视化的服务器管理软件，支持快速安装LAMP/LNMP/网站多项服务器管理功能。可以通过 Web 端轻松管理服务器，提升运维效率。例如：管理网站、管理文件、邮件、防火墙等功能。
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/fastpanel/fastpanel-show-websoft9.png)
   
部署 Websoft9 提供的 FASTPANEL 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:8888** 端口已经开启
3. 在服务器中查看 FASTPANEL 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 FASTPANEL，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## FASTPANEL 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名:8888* 或 *http://服务器公网IP:8888*, 进入初始化页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/fastpanel/fastpanel-init-websoft9.png)

2. 点击申请许可证，通过邮箱在FASTPANEL官网注册后，复制激活码激活
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/fastpanel/fastpanel-active-websoft9.png)
   
3. 输入账号密码后登录（[不知道账号密码？](#账号密码)）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/fastpanel/fastpanel-login-websoft9.png)
   
4. 进入 FASTPANEL 主界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/fastpanel/fastpanel-main-websoft9.png)
   
### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

**进入初始化页面时，页面报警：面临潜在的安全风险？**  

这是因为没有申请Https证书提示的安全警告，请点击【接受风险并继续】继续操作即可。

## FASTPANEL 使用入门{#quickstart}

下面以 **创建网站** 作为一个任务，帮助用户快速入门：

1. 首页选择手动创建一个网站
2. 输入域名后，选择下一步
3. 点击【创建网站】
4. 您的网站可以正常访问了

## FASTPANEL 常用操作{#guide}

### 重置管理员密码{#resetpw}

忘记管理员密码时，请参考如下流程方案重置密码：  

1. 使用 root 密码通过 SSH 连接到您的服务器
   ```
   ssh root@your.server
   ```

2. 修改 fastuser 用户的密码之后，您可以使用设置的新密码登录面板
   ```
   passwd fastuser
   ```

 > FASTPANEL 的管理员用户也是服务器的普通用户fastuser

## 参数{#parameter}

FASTPANEL 应用中包含 PHP, Nginx, MySQL 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

### 路径{#path}

FASTPANEL 安装目录： */usr/local/fastpanel2/fastpanel*    

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 3306   | MySQL 数据库端口 | 可选   |

### 版本{#version}

FASTPANEL 没有特定版本号，都是以日期命名，请参照[发布版本](https://fastpanel.direct/changelog)

### 服务{#service}

```shell
sudo docker start | stop | restart | stats nginx
sudo docker start | stop | restart | stats mysql
```

### 命令行{#cli}

暂无

### API{#api}

暂无
