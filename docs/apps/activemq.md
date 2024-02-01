---
title: ActiveMQ
slug: /activemq
tags:
  - ActiveMQ 
  - IT 架构
  - 中间件
---

import Meta from './_include/activemq.md';

<Meta name="meta" />

## 入门指南

阅读官方文档 [Using Apache ActiveMQ](https://activemq.apache.org/using-activemq) 并结合下面的指南快速掌握它的使用。

### 运行 ActiveMQ 演示

ActiveMQ 附带了许多 Web 演示，这些演示说明了如何将 ActiveMQ 代理与 REST 和 AJAX 一起使用。 Web 演示在默认配置中未激活，因此您必须按照以下步骤运行它们：

1. 进入ActiveMQ容器，编辑 /opt/apache-activemq/examples/conf/activemq-demo.xml 文件并更改位置属性以反映加密凭证文件的位置，该文件位于 /opt/activemq/conf/credentials-enc.properties：

  ```shell
  <property name="locations">
        <value>file:${activemq.conf}/credentials-enc.properties</value>
  </property>
  ```

2. 如果 ActiveMQ 服务器当前正在运行，先停止：
   
  ```shell
  docker stop activemq
  ```

3. 运行示例：
   
  ```shell
  docker exec -it activemq bash
  cd /opt/activemq
  sudo ./bin/activemq console xbean:/opt/activemq/examples/conf/activemq-demo.xml
  ```

4. 等待 ActiveMQ 代理启动。

5. 登录到 Web 管理面板查看演示： *http://服务器公网 IP:8161/demo* 

### 配置消息

官方方案：http://activemq.apache.org/configuration.html

## 管理维护

### 修改控制台密码

进入 ActiveMQ 容器，通过 */opt/apache-activemq/conf/jetty-realm.properties* 文件修改，重启 [ActiveMQ 服务](#service)后生效

### 升级

ActiveMQ 主要采用二级制安装方式，其升级方案差不多等于安装：

1. 进入容器，依次运行如下的命令做好准备：
   ```
   docker exec -it activemq bash
   # stop ActiveMQ service
   systemctl stop activemq

   # rename the dir of ActiveMQ for backup
   mv /opt/activemq  /opt/activemqBK
   ```
2. 访问 ActiveMQ 官方网站，[下载](http://activemq.apache.org/components/classic/download/)后解压并上传到：*/opt* 目录，并命名为 *activemq*

3. 分别运行下面的修改权限
   ```
   chown -R activemq. /opt/activemq
   chmod 640  /opt/activemq/examples/stomp/php/*
   chmod +x /opt/activemq/bin/activemq
   ```
4. 重启 [ActiveMQ服务](../activemq#service) 后升级完成

### 运行调试模式

```
docker exec -it activemq bash
systemctl stop activemq
/opt/activemq/bin/activemq console
```


## 故障

#### ActiveMQ 服务无法启动？

1. 以调试模式运行`activemq console`，便可以查看启动状态和错误
   ```
   docker exec -it activemq bash
   /opt/activemq/bin/activemq
   ```
2. 打开日志文件：*/opt/activemq/data/activemq.log*，检索 **failed** 关键词，分析错误原因

3. 常见的无法启动ActiveMQ服务的原因有如下几点：

   * 主机名不符合要求。例如：activemq5.6，这种包含"."的主机名就会导致ActiveMQ无法重启。参考如下命令重置主机名
   ```
   hostnamectl set-hostname activemq
   ```
   * 缺乏Java的环境变量。通过：`echo $JAVA_HOME` 或 `which java` 查看反馈信息。


#### 是否可以修改 ActiveMQ 的源码路径？

可以，但要参考如下的命令重试设置环境变量
```
echo 'export PATH="$PATH:/opt/activemq/bin"' >> /etc/profile
```

#### 如何修改上传的文件权限?

```shell
docker exec -it activemq bash
chown -R activemq.activemq /opt/activemq
find /opt/activemq -type d -exec chmod 750 {} \;
find /opt/activemq -type f -exec chmod 640 {} \;
```