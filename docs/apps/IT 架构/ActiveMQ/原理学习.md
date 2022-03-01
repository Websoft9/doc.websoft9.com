---
sidebar_position: 3
slug: /activemq/study
tags:
  - ActiveMQ 
  - IT 架构
  - 中间件
---

# 原理学习

## ActiveMQ Web 演示

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
5. 登录到 Web 管理面板查看演示：在浏览器中输入 *http://Internet IP:8161/demo* ，如果需要，使用从服务器仪表板获得的凭据登录。