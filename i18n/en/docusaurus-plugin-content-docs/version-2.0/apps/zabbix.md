---
title: Zabbix
slug: /zabbix
tags:
  - DevOps
  - 监控
  - 日志
---

import Meta from './_include/zabbix.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Zabbix 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问登录地址, 进入登录界面
   ![Zabbix 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-login-websoft9.png)

2. 输入账号密码后登录到后台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboard-websoft9.png)

3. 打开用户管理界面，更换所需的语言（如果语言为灰色状态，参考[启用语言方案](#i18)）
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-changelang-websoft9.png)  
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboardzh-websoft9.png)

### 快速了解

需要了解更多 Zabbix 的使用，请参考：

- 多语言：支持多语言（包含中文），通过后台设置即可

- 官方文档：[Zabbix Documentation](https://www.zabbix.com/documentation/current/)

- Zabbix 能监控的对象：监控各种IT组件，包括网络、服务器、虚拟机和云服务

- 主要组件：Zabbix-Server，Zabbix-Web，Zabbix-Proxy，Zabbix-Agent，Zabbix-java-gateway

- Zabbix-Proxy 从 Zabbix 分布式部署架构中从 Zabbix-Agent 采集数据，用于减轻 Zabbix-Server 的压力

- Zabbix sender： 是一个命令行应用程序，可用于将性能数据发送到 Zabbix server 进行处理

### 连接 Zabbix Agent

通过连接一个客户端的实际应用场景，帮助用户快速入门。  

1. 先到目标服务器安装 Zabbix-Agent （推荐容器安装）

2. 登录到 Zabbix 控制台后， 依次打开：【配置】>【主机】，打开主机列表
   ![Zabbix 添加主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-edithost001-websoft9.png)

3. 输入目标服务器的 IP 地址，保存配置
   ![Zabbix 添加主机](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-edithost002-websoft9.png)

4. 回到主机列表页，启用主机监控，当主机【可用性】列变成**绿色**即表明监控已成功

### 设置多语言{#i18}

Zabbix 默认已经内置多种语言包，非常方便进行在线切换。

1. 登录到 Zabbix 后台

2. 依次打开：【管理】>【用户】，编辑用户信息管理界面，更换所需的语言
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/zabbix/zabbix-changelang-websoft9.png)  
   ![Zabbix 更换语言](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-dashboardzh-websoft9.png)

> 如果语言为灰色状态,参考官方字符编码安装方案：[How to install locale](https://zabbix.org/wiki/How_to/install_locale)


## 管理维护{#administrator}

### 配置 SMTP{#smtp}

1. 登录到 Zabbix 后台，完成 SMTP 参数设置  
  
   - 依次打开：【管理】>【报警媒介类型】，选择【Email】
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-opensmtp-websoft9.png)
   - 准确的填写你的 SMTP 参数
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-smtpsetting-websoft9.png) 

2. 自测是否可以发送邮件

### 修改密码

1. 登录 Zabbix 后台，依次打开：【管理】>【用户】，编辑目标用户
  ![Zabbix 修改密码](https://libs.websoft9.com/Websoft9/DocsPicture/zh/zabbix/zabbix-modifypw-websoft9.png)

2. 点击【修改密码】

### 找回密码

忘记了密码需要通过修改数据库相关字段来重置密码：

进入 Zabbix 数据库，在 SQL 窗口运行重置密码的命令：

```
sudo mysql -uroot -p new_password -e "update zabbix.users set passwd=md5(new_password) where alias='Admin';"
```

### 升级

参考官方文档：[INSTALLATION FROM CONTAINERS](https://www.zabbix.com/documentation/5.0/manual/installation/containers)

## 故障

