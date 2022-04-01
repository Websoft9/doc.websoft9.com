---
sidebar_position: 1
slug: /opencart
tags:
  - OpenCart
  - 电子商务
---

# 快速入门

[OpenCart](https://opencart.com) 是一个易用性很高，100% 开源的电子商务系统。它支持多语言、多货币和多店铺。生态中超过 10000+ 个扩展可用。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-gui-websoft9.png)

## 准备

部署 Websoft9 提供的 OpenCart 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 OpenCart 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  OpenCart **[域名五步设置](./dns#domain)** 过程


## OpenCart 初始化向导

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 就进入引导首页

2. 进入安装界面，同意安装协议
   ![oc1](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc1.png)  

3. 通过环境检测后，进入下一步  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc2.png)

3. 填写数据库信息（[不知道账号密码？](./setup/credentials#getpw)并设置后台管理账号
   ![oc1](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc3.png)

4. 安装成功后，系统提示【删除安装目录】
   ![oc1](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/oc4.png)

5. SSH 工具连接服务器，删除安装目录
   ```
   rm -rf /data/wwwroot/opencart/upload/install
   ```

6. 体验商城前台和后台

> 需要了解更多 OpenCart 的使用，请参考官方文档：[OpenCart Docs](http://docs.opencart.com)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## OpenCart 使用入门

下面以 **使用 OpenCart 构建在线商城** 作为一个任务，帮助用户快速入门：


## OpenCart 常用操作

### 安装插件{#installplugin}

OpenCart 提供了大量的扩展发布在 Marketplace 上，下面是具体的安装扩展步骤：

1. 在 Marketplace 上下载所需的扩展

2. 登录 OpenCart 后台，依次打开：【Extensions】>【Installer】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/opencart/opencart-installex-websoft9.png)

3. 上传扩展文件

4. 等待安装完成


### 安装语言包{#setlanguage}

在 Opencart 中增加一个新的语言（以中文包为例），主要有三个步骤：

1. 到 [OpenCart Marketplace](https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=19126&filter_category_id=2&page=8)下载中文语言包（请注意版本）；

2. 将下载好的语言包解压出来，会得到一个名为 upload 的文件夹，内有 admin 和 catalog 两个文件夹分别为后台和前台的文件夹；

3. 使用 SFTP 软件将前后台中文包分别上传到服务器：
   ```
   admin->language->zh_cn 文件夹 上传到  /data/wwwroot/opencart/admin/language 目录下
   catalog->language->zh-cn 文件夹 上传到 /data/wwwroot/opencart/catalog/language 目录下
   ```
4. 登录 OpenCart，打开【System】>【localization】>【languages】，增加一个语言并填写配置信息
	![websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-language-1-websoft9.png)

5. 店铺前后台分别选择所需的语言：【System】>【Settings】  

   - Language 为前台默认语言
   - Administration Language 为后台默认语言

	![websoft9](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-language-2-websoft9.png)



6. 刷新前后台页面，系统显示新的语言

### OpenCart vQmod

Opencart 2.0 使用vQmod机制安装扩展，需提前安装并启用vQmod，具体如下：

1. [下载vQmod](https://github.com/vqmod/vqmod)
2. Go to Extensions > Installer，上传下载的 vqmod.zip 文件
3. Go to Extensions > Extensions > Modules > Integrated VQmod to install and then edit to enable this module

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数 

2. 登录到 OpenCart 后台，完成 SMTP 参数设置  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/opencart/opencart-smtp-websoft9.png)
  
   - 输入提供SMTP服务的服务器地址，其中的 ssl://  一定不能省略
   - 务必准确的填写你的 SMTP 参数

3. 发送测试邮件

### 域名额外配置（修改 URL） {#dns}

**[域名五步设置](./dns#domain)** 完成后，需设置 OpenCart URL:

1. 修改 OpenCart 根目录下的[配置文件](#path) `config.php`
   ```
   // HTTP
   define('HTTP_SERVER', 'http://example.com/');
   // HTTPS
   define('HTTPS_SERVER', 'https://example.com/');
   ```

2. 修改 OpenCart 后台目录下的[配置文件](#path) `admin/config.php`
   ```
   // HTTP
   define('HTTP_SERVER', 'http://www.example.com/admin/');
   define('HTTP_CATALOG', 'http://www.example.com/');
   // HTTPS
   define('HTTPS_SERVER', 'http://www.example.com/admin/');
   define('HTTPS_CATALOG', 'http://www.example.com/');
   ```

3. 重启服务后生效

## 参数{#parameter}

OpenCart 应用中包含 Nginx, Apache, Docker, MySQL, phpMyAdmin 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 OpenCart 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

下面仅列出 OpenCart 本身的参数：

### 路径{#path}

OpenCart 安装目录： */data/wwwroot/opencart*  
OpenCart 前台配置文件： */data/wwwroot/opencart/config.php*  
OpenCart 后台配置文件： */data/wwwroot/opencart/admin/config.php* 


### 端口{#port}

无特殊端口

### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats opencart
```

### 命令行{#cli}

无

### API


```
curl http://myopencart.example.com/index.php?route=api/cart/add
```

官方文档：[OpenCart API](http://docs.opencart.com/en-gb/system/users/api/)