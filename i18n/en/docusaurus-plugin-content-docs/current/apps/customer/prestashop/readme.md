---
sidebar_position: 1
slug: /prestashop
tags:
  - PrestaShop
  - 电子商务
---

# 快速入门

[PrestaShop](https://prestashop.com) 是一个 100% 开源的电子商务平台。基于 Symfony 框架，功能非常全面。它包括 600 多个功能，5,000 多个模块和主题在市场上可用或已内置。更具特点的是，PrestaShop 官方构建了一个非常完善、健康的商业化服务生态。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/pretashopui-websoft9.png)

## 准备

部署 Websoft9 提供的 PrestaShop 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 PrestaShop 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  PrestaShop **[域名五步设置](./administrator/domain_step)** 过程


## PrestaShop 初始化向导

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 就进入引导首页  

   若有升级提醒，请点击【yes,please!】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-installupdate-websoft9.png)
   
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-language-websoft9.png)

2. 选择语言，接受许可协议，继续下一步

3. 安装进入管理员账号设置界面，牢记之，点击“下一步”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-adminconf-websoft9.png)

4. 安装进入数据库配置界面（[不知道数据库密码？](./user/credentials)）然后点击”保存”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dbconfig-websoft9.png)

5. 系统安装成功，分别进入后台和前台体验
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-installss-websoft9.png)

6. 登录后台，系统提示删除intall文件夹
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-delinstall-websoft9.png)

7. SSH 连接服务器，进入 [PrestaShop 根目录](#path)后，删除 **install** 文件夹
   ```
   rm -rf install
   ```

8. 删除完成后，点击第六步的后台链接，开始体验后台（请牢记后台地址）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-login-websoft9.png)

9.  登录成功，体验后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-backend-websoft9.png)

> 需要了解更多 PrestaShop 的使用，请参考官方文档：[PrestaShop Docs](https://www.prestashop.com/en/resources/documentations)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## PrestaShop 使用入门

下面以 **使用 PrestaShop 构建在线商城** 作为一个任务，帮助用户快速入门：


## PrestaShop 常用操作

### 安装扩展（Modules）{#module}

Modules 是 PrestaShop 功能扩展，Modules 可以即插即用

1. 登录 PrestaShop 后台，依次打开：【Modules】>【Module Catalog】，找到所需的插件，点击【Install】开始安装
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-installmd-websoft9.png)

3. 依次打开：【Modules】>【Module Manager】，找到所需的插件，点击【Upgrade】即可在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-upgrademodules-websoft9.png)

### 连接 Marketplace{#marketplace}

安装 PrestaShop 后，建议把你安装的 PrestaShop 系统与 PrestaShop 官方的 Marketplace 资源进行在线连接，这样便可以在线使用 Marketplace 上的大量资源

1. 登录 PrestaShop 后台

2. 依次打开：【Modules】>【Module Manager】，点击【Connect to Addons marketplace】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-connectmk-websoft9.png) 

3. 开始注册账号
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-registeraccount-websoft9.png)  

4. 注册完成后，登录连接

5. 连接后，就可以很方便的使用 Marketplace 上的资源
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/prestashop/prestashop-marketplace-websoft9.png)

### 语言包管理{#setlanguage}

Prestashop的多语言支持非常的成熟，系统在后台内置一套多语言体系，只需要选择对应的语言，在线导入到您的 PrestaShop 系统即可。

##### 导入语言

1. 登录Prestashop后台，依次打开：【国际】>【本地化】，进入设置界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-setlanguage-websoft9.png)

2. 选择一个语言包，点击本项之右下角【上传】图标，完成在线导入

3. 选择【语言】选项卡，我们就可以看到成功导入的语言包
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-alllanguage-websoft9.png) 

> 每次导入一个新的语言包，系统会自动为此语言生成一个伪静态规则。如果您的某个语言的伪静态设置出现问题导致了 Redirect（重定向），可以删除这个语言，然后重新导入一次即可。

##### 删除语言

1. 登录Prestashop后台，依次打开：【国际】>【本地化】>【语言】，编辑您需要的语言
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dellanguage001-websoft9.png)

2. 将语言的状态修改为“否”，然后保存

3. 回到【语言】选项开，找到已经打叉的语言，删除之即可
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-dellanguage002-websoft9.png)

### 设置维护模式{#maintenance}

登录 PrestaShop 后台，打开：【Shop Parameters】>【General】>【Maintenance】，设置维护模式
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-mantmode-websoft9.png)

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数

2. 登录到 PrestaShop 后台，完成 SMTP 参数设置  
  
   - 依次打开：【配置】>【高级参数】>【邮箱】，选择第二项【设置我的SMTP参数】
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-smtp-1-websoft9.png)

   - 准确的填写你的 SMTP 参数
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-smtp-2-websoft9.png) 

3. 发送测试邮件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-smtp-3-websoft9.png)
     

### 域名额外配置（修改 URL） {#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需设置 PrestaShop URL:

1. 将 PrestaShop [设置为维护模式](#maintenance)

2. 打开 PrestaShop 的[配置文件](#path)，修改其中与域名有关的内容

3. 登录 PrestaShop 后台，打开：【Shop Parameters】>【Traffic&SEO】，修改它
  ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-seturl-websoft9.png)

### 导入演示数据

登录 PrestaShop 后台，打开：【Advanced Parameters】>【Import】，导入所需的数据 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/prestashop/prestashop-importdb-websoft9.png)


## 参数{#parameter}

PrestaShop 应用中包含 Apache, Nginx, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 PrestaShop 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 PrestaShop 本身的参数：

### 路径{#path}

PrestaShop 目录： */data/wwwroot/prestashop*  
PrestaShop 配置文件： */data/wwwroot/prestashop/app/config/parameters.php*  

### 端口{#port}

无特殊端口

### 版本{#version}

PrestaShop 控制台查看

### 服务{#service}

```shell
sudo docker start | restart | stop | stats prestashop
```

### 命令行{#cli}

PrestaShop 提供了一个用于安装和修改配置的 [CLI](https://doc.prestashop.com/display/PS17/Installing+PrestaShop+using+the+command-line+script)，进入根目录下运行：  

```
php index_cli.php --domain=example.com --db_server=sql.example.com --db_name=prestashop --db_user=root --db_password=123456789
```

### API

[Webservice API](https://devdocs.prestashop.com/1.7/webservice/)