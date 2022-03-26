---
sidebar_position: 2
slug: /rocketmq/admin
tags:
  - RocketMQ
  - IT 架构
  - 中间件
---

# 维护参考

## 场景

### RocketMQ 升级

升级之前请做好备份。  

RocketMQ 升级等同于重新安装，下面介绍升级步骤：

1. 访问 RocketMQ [下载页面](http://rocketmq.apache.org/docs/quick-start/)，检查服务器环境是否匹配安装要求

2. 停止 RocketMQ 服务，删除
    ```
    sudo systemctl stop mqnamesrv
    sudo systemctl stop mqbroker
    ```
3. 删除 RocketMQ 文件夹下所有的文件
   ```
   rm -rf /data/rocketmq/*
   ```
4. 下载新的 RocketMQ，并解压到 /data/rocketmq 目录下

5. 修改 *rocketmq/bin/runserver.sh* 文件中 Java 启动内存大小（非必要）

   > Xms4g -Xmx4g -Xmn2g 改成 Xms400M -Xmx400M -Xmn200M 表示降低了内存下限。

6. 修改 */data/rocketmq/bin/runbroker.sh* 文件中 Java 启动内存大小（非必要）

7. 重新启动服务，其状态正常就代表升级成功
    ```
    sudo systemctl start mqnamesrv
    sudo systemctl start mqbroker
    systemctl status mqnamesrv
    systemctl status mqbroker
    ```

## 故障速查

除以下列出的 [RocketMQ 故障](http://rocketmq.apache.org/docs/faq)问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### 内存不足？

RocketMQ 最低内存设置查看 **runserver.sh** 和 **runbroker.sh**` JAVA_OPT 设置

##### RocketMQ-Console-Ng 连接失败？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/rocketmq/rocketmq-error-websoft9.png)

问题原因：可视化工具的 docker-compose 文件中 RocketMQ 服务的地址错误。  
解决方案：修改 RocketMQ 服务地址



#### 问题解答

##### RocketMQ-Console-Ng 是如何安装的？

基于 Docker 安装。

#### RocketMQ-Console-Ng 支持多语言？

目前支持英文和简体中文，可以登陆后可以直接在顶部菜单进行设置。

#### RocketMQ 采用何种安装方式？

采用二进制包解压的安装方式

#### RocketMQ 的消息保存多久？

消息将最多保存3天，未使用超过3天的消息将被删除。