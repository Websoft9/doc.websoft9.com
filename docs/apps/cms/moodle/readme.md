---
sidebar_position: 1
slug: /moodle
tags:
  - Moodle
  - 在线学习管理
---

# 快速入门

[Moodle LMS](https://moodle.com) 是一个开源的在线教育系统（慕课）。它符合 SCORM/AICC标准，功能强大、界面简单精巧。Moodle具有先进的教学理念，创设的包含技术管理、学习任务和社交三个虚拟学习维度，提倡师生或学生彼此间共同思考，合作解决问题。它是先进在线教学理念和实践的集大成者，已成为全球大中学院校建立开放式课程系统的首选软件。  

主要模块：课程管理、作业模块、聊天模块、投票模块、论坛模块、测验模块、资源模块、问卷调查模块、互动评价（workshop）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodlegui-websoft9.jpg)

## 准备

部署 Websoft9 提供的 Moodle 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Moodle 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  Moodle **[域名五步设置](./dns#domain)** 过程


## Moodle 初始化向导

### 详细步骤

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 就进入引导首页

2. 根据系统提示，选择语言，进入下一步 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install001-websoft9.png)

3. 选择数据库类型，默认为【改进的MySQL】，然后进入确认路径设置（保持默认设置），进入下一步 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install002-websoft9.png)

4. 填写数据库连接信息，建议采用预装环境自带的 MySQL 数据库([不知道账号密码？](./setup/credentials账号密码))
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install003-websoft9.png)

5. 经过几次确认后，安装进入环境检测步骤，继续后续步骤 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install004-websoft9.png)

6. 设置后台账号信息，请务必设置好并牢记之。进入下一步 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install005-websoft9.png)

7. 设置网站初始化信息 
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install006-websoft9.png)

8. 跟随安装提示直到完成，过程中尽量选择默认设置，勾选安装所有模块

9.  系统完成最后一步安装，建议进入 Moodle 后台（以管理身份登录即进入后台），体验完整功能 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-install007-websoft9.png)

10. [注册 Moodle 官方账号](#register)，打通你的 Moodle 与官方的连接，便于在线安装插件。

> 需要了解更多Moodle的使用，请参考官方文档：[Moodle Documentation](https://docs.moodle.org)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## Moodle 使用入门

下面以 **使用 Moodle 构建学习管理系统** 作为一个任务，帮助用户快速入门：

[Moodle 快速搭建学习管理系统](https://cloud.tencent.com/developer/article/1822682)


## Moodle 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./automation/smtp) 相关参数

2. 以管理员身份登录 Moodle控制台

3. 依次打开：【网站管理】>【服务器】>【电子邮件】>【发送邮件设置】
   ![Moodle SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-smtp-websoft9.png)

4. 点击【Test outgoing mail configuration】测试设置

### 向 Moodle 注册你的网站{#register}

Moodle 初始化安装完成之后，建议注册成为 Moodle 官方网站的会员，注册好处包括：升级通知，课程共享，在线安装插件等

1. 以管理员身份登录 Moodle 后台
2. 依次打开：【网站管理】>【注册】
   ![Moodle 注册](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-registermd-websoft9.png)
3. 注册完成后登陆，这样你的 Moodle 与官方便建立了一个连接关系

### Moodle 语言设置{#setlanguge}

1. 以管理员身份登录 Moodle 后台
2. 依次打开：【网站管理】>【语言】
   ![Moodle 语言设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-languageset-websoft9.png)
3. 根据实际情况进行语言设置
   * 语言设置：即在线切换语言
   * 定制语言：即在线编辑语言翻译内容
   * 语言包： 即上传系统默认没有内置的语言

### Moodle 客户端{#client}

1. 以管理身份登录 Moodle 后台

2. 依次打开：【网站管理】>【移动应用程序】>【移动设备设置】
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-app-1-websoft9.jpg)

3. 将【为移动设备启用网络服务】设为 **启用** 状态；
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-app-2-websoft9.jpg)

4. 保存设置；

5. 安装 [Moodle 手机客户端](https://download.moodle.org/mobile/)

6. 打开后在地址栏输入 Moodle 的访问地址，就可以开始使用移动端
   ![moodle-apps](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mobile-websoft9.png)

### Moodle 插件{#plugin}

Moodle 是一个非常灵活的平台，大部分核心功能以插件的形式存在，系统默认安装了400多个插件。同时，官方提供了[插件市场](https://moodle.org/plugins/)供用户作用更多功能扩展。

1. [注册 Moodle 官方账号](#register)，打通你的 Moodle 与官方的连接，便于在线安装插件。

2. 以管理员身份登录 Moodle 后台

3. 依次打开：【网站管理】>【插件】，会看到**安装插件**和**插件概况**两个链接
   ![moodle 插件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-plugins-websoft9.png)

   * 安装插件：安装新插件入口
   * 插件概况：查看已经安装的插件列表

4. 点击【安装插件】，提供**从Moodle插件目录安装插件**和**从ZIP文件中安装插件**两种安装插件的方式
   ![moodle 安装插件](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-pluginsmk-websoft9.png)

   * 从Moodle插件目录安装插件：自动跳转并登录到 Moodle 的[官方插件市场](https://moodle.org/plugins/)，便可以在线安装
   * 从ZIP文件中安装插件：需提前下载插件压缩文件，再从此处**上传**安装

5. 点击【插件概况】，列出默认安装的插件，可以进行停用、卸载等操作
   ![moodle 插件概况](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-plugininfo-websoft9.png)
   
6. 点击[插件概况](https://moodle.org/plugins/)寻找所需的插件，然后安装它们

> 更多插件管理查看官方文档 [Moodle Plugins](https://docs.moodle.org/37/en/Installing_plugins)

### Moodle 主题{#theme}

Moodle 主题实际上是一个插件，因此需要安装新主题，必须通过【安装插件】的方式先进行安装。  

1. 以管理员身份登录 Moodle

2. 依次打开：【网站管理】>【插件】，进入插件市场后，选择【Theme】类型的插件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-mktheme-websoft9.png)

3. 在线安装所需的主题

4. 打开【网站管理】>【外观】>【主题选择器】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-addtheme001-websoft9.png)

5. 点击【更改主题】即可完成主题更换
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-addtheme002-websoft9.png)

### 重置密码{#resetpwd}

常用的 Moodle 重置密码相关的操作主要有修改密码和找回密码两种类型：

#### 修改密码

1. 登录 Moodle 后台，点击头像，进入【个人档案】设置下的**小齿轮图标**
  ![Moodle 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-modifypw-websoft9.png)

2. 点击【更改密码】链接，开始修改密码

#### 找回密码

如果用户忘记了密码，有两种找回密码的方案：

* 登录界面通过邮件找回密码（需提前完成 [SMTP 设置](#smtp）
* 数据库中重置密码两种方案

下面介绍通过数据库找回密码的方案：

1. 登录 [phpMyAdmin](./setup/parameter#managedb)，并找到你的网站数据库下的 *mdl_user*表

  ![Moodle user表](https://libs.websoft9.com/Websoft9/DocsPicture/zh/moodle/moodle-phpmyadminuser-websoft9.png)

2. 编辑【admin】用户，将其中的 `password` 字段的值用 `21232f297a57a5a743894a0e4a801fc3` 替换

3. 点击【执行】，新的密码就被重置为`admin`


## Moodle 参数{#parameter}

Moodle 应用中包含 PHP, Nginx, Apache, Docker, MySQL 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。 

通过运行`docker ps`，可以查看到 Moodle 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Moodle 本身的参数：

### 路径{#path}

Moodle 安装目录： */data/wwwroot/moodle*  
Moodle 配置文件： */data/wwwroot/moodle/config.php*  


### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | Moodle 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats moodle
```

### 命令行{#cli}

[Administration via command line](https://docs.moodle.org/311/en/Administration_via_command_line)

```
$ cd /path/to/your/moodle/dir
$ sudo -u apache /usr/bin/php admin/cli/somescript.php --params
$ sudo -u apache /usr/bin/php admin/cli/install.php --help
```
### API

[Core APIs](https://docs.moodle.org/dev/Core_APIs)