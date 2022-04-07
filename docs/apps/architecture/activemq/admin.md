---
sidebar_position: 3
slug: /activemq/admin
tags:
  - ActiveMQ 
  - IT 架构
  - 中间件
---

# 维护参考

## 场景

### ActiveMQ 升级

ActiveMQ 主要采用二级制安装方式，其升级方案差不多等于安装：

1. 依次运行如下的命令做好准备：
   ```
   # stop ActiveMQ service
   systemctl stop activemq

   # rename the dir of ActiveMQ for backup
   mv /opt/apache-activemq  /opt/apache-activemqBK
   ```
2. 访问 ActiveMQ 官方网站，[下载](http://activemq.apache.org/components/classic/download/)后解压并上传到：*/opt* 目录，并命名为 *apache-activemq*
3. 分别运行下面的修改权限
   ```
   chown -R activemq. /opt/apache-activemq
   chmod 640  /opt/apache-activemq/examples/stomp/php/*
   chmod +x /opt/apache-activemq/bin/activemq
   ```
4. 重启 [ActiveMQ服务](/zh/admin-services#activemq) 后升级完成

## 故障排除

除以下列出的 ActiveMQ 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### ActiveMQ 服务无法启动？

1. 以调试模式运行`activemq console`，便可以查看启动状态和错误
   ```
   /opt/apache-activemq/bin/activemq
   ```
2. 打开日志文件：*/opt/apache-activemq/data/activemq.log*，检索 **failed** 关键词，分析错误原因

3. 常见的无法启动ActiveMQ服务的原因有如下几点：

   * 主机名不符合要求。例如：activemq5.6，这种包含"."的主机名就会导致ActiveMQ无法重启。参考如下命令重置主机名
   ```
   hostnamectl set-hostname activemq
   ```
   * 缺乏Java的环境变量。通过：`echo $JAVA_HOME` 或 `which java` 查看反馈信息。

## 常见问题

#### Active Classic vs ActiveMQ Artemis？

ActiveMQ Artemis 是 ActiveMQ 下一代产品，未来将替换 ActiveMQ Classic。 具体参考：[ActiveMQ Classic](https://activemq.apache.org/getting-started), [ActiveMQ Artemis](https://activemq.apache.org/components/artemis/documentation/)

#### 如何以调试模式启动ActiveMQ服务？

```
systemctl stop activemq
/opt/apache-activemq/bin/activemq console
```
#### 如何退出 ActiveMQ 控制台？

暂无方案

#### ActiveMQ 中是否包含 Tomcat？

ActiveMQ 官方提供的二级制包中包含 Tomcat，但已经集成到 ActiveMQ 服务中。

#### 是否可以修改 ActiveMQ 的源码路径？

可以，但要参考如下的命令重试设置环境变量
```
echo 'export PATH="$PATH:/opt/apache-activemq/bin"' >> /etc/profile
```

#### 如何修改上传的文件权限?

```shell
chown -R activemq.activemq /opt/apache-activemq
find /opt/apache-activemq -type d -exec chmod 750 {} \;
find /opt/apache-activemq -type f -exec chmod 640 {} \;
```
