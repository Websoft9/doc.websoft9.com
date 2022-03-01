---
sidebar_position: 1
slug: /rocketmq
tags:
  - RocketMQ 
  - IT 架构
  - 中间件
---

# 快速入门

[RocketMQ](http://rocketmq.apache.org/) 是阿里主导开发的分布式开源消息队列系统，是一个低延迟、高并发、高可用、高可靠的分布式消息中间件。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-console-websoft9.png)

在云服务器上部署 RocketMQ 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:9003** 端口是否开启
3. 若想用域名访问 RocketMQ，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### RocketMQ-Console

* 管理员账号: `admin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

> 本部署方案通过 Nginx 中的密码管理来控制 RocketMQ-Console 的访问，文件地址：*/etc/nginx/.htpasswd/htpasswd.conf*  

## RocketMQ 安装向导

1. 使用 SSH 登录到 RocketMQ 所在服务器后，运行如下命令，检查 RocketMQ 服务状态
   ```
   sudo systemctl status mqnamesrv
   sudo systemctl status mqbroker
   ```
2. 使用本地浏览器访问可视化工具 [RocketMQ-Console](#可视化工具)，进一步验证。
   ![RocketMQ-Console](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-console-websoft9.png)

## RocketMQ 入门向导

现在开始针对于如何使用 RocketMQ 发送（生产者）和接受消息（消费者），进行完整的实验说明。  

> 建议开始下面的步骤之前，先花5分钟时间阅读由通俗易懂的 [RocketMQ 知识要点](原理学习.md) 

1. 对实验所需准备的工具或程序做出说明

   * 发送人（本实验对应的是一个程序）：*/data/rocketmq/bin/tools.sh*
   * 接收人（本实验对应的是一个程序）：*/data/rocketmq/bin/tools.sh*
   * 消息信件：示例代码生成 `org.apache.rocketmq.example.quickstart.Producer` （Java 类）
   * 消息存储地： **RabbitMQ Broker**
   * 消息订单处理中心：**NAMESRV_ADDR** 用于根据消息存储地资源情况进行消息的动态分配

2. 使用 SSH 登录到 RocketMQ 服务器，运行下面命令，以发件人的身份发送消息
   ```
   export NAMESRV_ADDR=localhost:9876
   cd /data/rocketmq/bin
   sh tools.sh org.apache.rocketmq.example.quickstart.Producer
   ```

3. 发送成功会收到 *SendResult [sendStatus=SEND_OK, msgId= ...* 之类的反馈结果

4. 在运行下面的命令，以收件人的身份接受消息
   ```
   cd /data/rocketmq/bin
   sh tools.sh org.apache.rocketmq.example.quickstart.Consumer
   ```
5. 接受成功会收到 *ConsumeMessageThread_%d Receive New Messages: [MessageExt...* 之类的反馈结果

6. 登录到可视化界面 [RocketMQ-Console](/zh/solution-gui.md) 中可更直观的查看运行结果
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-send-websoft9.png)

> 需要了解更多 RocketMQ 的使用，请参考官方文档：[RocketMQ Documentation](http://rocketmq.apache.org/docs/quick-start/)


## 常用操作

### 消息示例

对于如何发送消息以及接受消息，本文档章节：RocketMQ 入门向导 中有详细的讲解。


### RocketMQ-Console 密码

RocketMQ-Console 工具默认没有提供账号管理功能，但部署方案中通过在 Nginx 的密码功能实现。  
 
需修改密码，请修改 */etc/nginx/.htpasswd/htpasswd.conf* 后，然后重启 Nginx 服务。

### 可视化工具

RocketMQ 扩展项目中提供了管理和监控 RocketMQ 的可视化工具：[RocketMQ-Console-NG ](https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console). 本部署方案默认安装了它，参考下面的步骤即可使用：  

#### 连接

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：*http://服务器公网IP:9003*, 进入登陆页面

   ![RocketMQ-Console-NG 登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-loginonly-websoft9.png)

2. 输入账号密码（[不知道账号密码？](/zh/stack-accounts.md#rocketmq)），成功登录到 RocketMQ 后台

   ![RocketMQ-Console](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-console-websoft9.png)

3. 设置自己喜欢的语言

   ![RocketMQ-Console 语言设置](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-language-websoft9.png)

3. 接下来便可以在可视化界面查看驾驶舱、集群、消费者等信息（[参考](https://github.com/apache/rocketmq-externals/blob/master/rocketmq-console/doc/1_0_0/UserGuide_CN.md)官网文档）


#### 常见问题

##### 这个可视化工具是如何安装的？

基于 Docker 安装。

##### 如何修改可视化工具的密码？

可视化工具默认没有提供账号管理功能，我们的部署方案中通过在 Nginx 的密码功能实现。需修改密码，请修改 */etc/nginx/.htpasswd/htpasswd.conf* 后，然后重启 Nginx 服务。

##### 连接失败，右上角出现如下错误信息？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-error-websoft9.png)

问题原因：可视化工具的 docker-compose 文件中 RocketMQ 服务的地址错误。  
解决方案：修改 RocketMQ 服务地址


## 异常处理

#### 浏览器打开IP地址，无法访问 RocketMQ（白屏没有结果）？

您的服务器对应的安全组9003端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

