---
sidebar_position: 1
slug: /activemq
tags:
  - ActiveMQ 
  - IT 架构
  - 中间件
---

# 快速入门

[Apache ActiveMQ](https://activemq.apache.org) 是老牌的开源消息总线，完全支持 JMS1.1 和 J2EE 1.4 规范，它支持多种语言和协议编写客户端。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/activemq/activemq-logined-websoft9.png)


部署 Websoft9 提供的 ActiveMQ 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:8161** 端口已经开启
3. 在服务器中查看 ActiveMQ 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  ActiveMQ，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程


## ActiveMQ 初始化向导

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名:8161* 或 *http://服务器公网IP:8161*, 进入初始化页面
   ![ActiveMQ初始化页面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/activemq/activemq-login-websoft9.png)

2. 点击【Manage ActiveMQ broker】登录 ActiveMQ 控制台 （[不知道账号密码？](./user/credentials)）
   ![ActiveMQ控制台](http://libs.websoft9.com/Websoft9/DocsPicture/zh/activemq/activemq-logined-websoft9.png)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

## ActiveMQ 使用入门

[Using Apache ActiveMQ](https://activemq.apache.org/using-activemq)

## ActiveMQ 常用操作

### 修改控制台密码

通过 */opt/apache-activemq/conf/jetty-realm.properties* 文件修改，重启 [ActiveMQ 服务](#service)后生效

### 运行 ActiveMQ 演示

ActiveMQ 附带了许多 Web 演示，这些演示说明了如何将 ActiveMQ 代理与 REST 和 AJAX 一起使用。 Web 演示在默认配置中未激活，因此您必须按照以下步骤运行它们：

1. 编辑 /opt/apache-activemq/examples/conf/activemq-demo.xml 文件并更改位置属性以反映加密凭证文件的位置，该文件位于 /opt/activemq/conf/credentials-enc.properties：

  ```shell
  <property name="locations">
        <value>file:${activemq.conf}/credentials-enc.properties</value>
  </property>
  ```

2. 如果 ActiveMQ 服务器当前正在运行，先停止：
   
  ```shell
  systemctl stop activemq
  ```

3. 运行示例：
   
  ```shell
  cd /opt/activemq
  sudo ./bin/activemq console xbean:/opt/activemq/examples/conf/activemq-demo.xml
  ```

4. 等待 ActiveMQ 代理启动。

5. 登录到 Web 管理面板查看演示： *http://服务器公网 IP:8161/demo* 

### 配置消息

官方方案：http://activemq.apache.org/configuration.html

## 参数

ActiveMQ 应用中包含 Docker 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行 `docker ps`，查看 ActiveMQ 运行时所有的服务组件：

CONTAINER ID   IMAGE                                                 COMMAND                  CREATED          STATUS          PORTS                                                                                                                                                                                NAMES
abeaf50ef7ec   alfresco/alfresco-activemq:5.18.2-jre17-rockylinux8   "/bin/sh -c './init.…"   37 minutes ago   Up 37 minutes   0.0.0.0:5672->5672/tcp, :::5672->5672/tcp, 0.0.0.0:8161->8161/tcp, :::8161->8161/tcp, 0.0.0.0:61613->61613/tcp, :::61613->61613/tcp, 0.0.0.0:61616->61616/tcp, :::61616->61616/tcp   activemq

### 路径{#path}

ActiveMQ 安装目录： */data/apps/activemq*   
ActiveMQ 配置目录： */data/apps/activemq/data*   

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8161   | HTTP 访问 ActiveMQ Web 界面 | 可选   |
| 5672   | amqp | 可选   |


### 版本{#version}

```shell
sudo docker exec -it activemq find /opt/activemq -name activemq-all* | cut -d- -f3
```

### 服务{#service}

```shell
sudo systemctl start | stop | restart | status activemq
```

### 命令行{#cmd}

暂无

### API

[ActiveMQ API](https://activemq.apache.org/maven/apidocs/index.html)
