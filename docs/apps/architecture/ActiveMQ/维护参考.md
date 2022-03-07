---
sidebar_position: 2
slug: /activemq/admin
tags:
  - ActiveMQ 
  - IT 架构
  - 中间件
---

# 维护参考

## 系统参数

ActiveMQ 预装包包含 ActiveMQ 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

虽然运行 `whereis` 命令可以查看相关安装路径，但接下来我们仍然对路径信息进行更为准确的说明。

```
whereis activemq
whereis java
```

#### ActiveMQ

ActiveMQ 安装目录： */opt/apache-activemq/*  
ActiveMQ 配置目录： */opt/apache-activemq/conf*  
ActiveMQ 数据目录： */opt/apache-activemq/data*  
ActiveMQ 日志目录： */opt/apache-activemq/data/activemq.log*

> 通过修改 */opt/apache-activemq/conf/jetty-realm.propertie* 重置管理密码

#### Java

Java Directory: */usr/lib/jvm*


### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp`查看相关端口，下面列出本应用可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 8161 | 通过 HTTP 访问 ActiveMQ 控制台 | 可选 |
| TCP | 5672 | amqp | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Linux Version
lsb_release -a

# Java Version
java -version

# ActiveMQ version
ls /opt/apache-activemq | grep activemq
```

### 服务


使用由Websoft9提供的 ActiveMQ 部署方案，可能需要用到的服务如下：

#### ActiveMQ

```shell
sudo systemctl start activemq
sudo systemctl stop activemq
sudo systemctl restart activemq
sudo systemctl status activemq

# you can use this debug mode if ActiveMQ service can't run
/opt/apache-activemq/bin/activemq console
```

## 备份

### 全局自动备份

所有的云平台都提供了全局自动备份功能，基本原理是基于**磁盘快照**：快照是针对于服务器的磁盘来说的，它可以记录磁盘在指定时间点的数据，将其全部备份起来，并可以实现一键恢复。

```
- 备份范围: 将操作系统、运行环境、数据库和应用程序
- 备份效果: 非常好
- 备份频率: 按小时、天、周备份均可
- 恢复方式: 云平台一键恢复
- 技能要求：非常容易
- 自动化：设置策略后全自动备份
```

不同云平台的自动备份方案有一定的差异，详情参考 [云平台备份方案](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

### 程序手工备份

程序手工本地备份是通过**下载应用程序源码和导出数据库文件**实现最小化的备份方案。

下面以列表的方式介绍这种备份：
```
- 备份范围: 数据库和应用程序
- 备份效果: 一般
- 备份频率: 一周最低1次，备份保留30天
- 恢复方式: 重新导入
- 技能要求：非常容易
- 自动化：无
```
通用的手动备份操作步骤如下：

1. 通过WinSCP将网站目录（*/opt/apache-activemq*）**压缩后**再完整的下载到本地
2. 备份工作完成

## 恢复

## 升级

### 系统级更新

运行一条更新命令，即可完成系统级（包含rethinkdb小版本更新）更新：

``` shell
#For Ubuntu&Debian
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> 本部署包已预配置一个用于自动更新的计划任务。如果希望去掉自动更新，请删除对应的 Cron

### ActiveMQ升级

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

## 故障处理

此处收集使用 ActiveMQ 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/opt/apache-activemq/data/activemq.log`。检索关键词 **Failed** 或者 **error** 查看错误

#### ActiveMQ服务无法启动？

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

#### Active Classic 与 ActiveMQ Artemis 有什么区别？

ActiveMQ Artemis 是ActiveMQ下一代产品，未来将替换 ActiveMQ Classic。 具体参考：[ActiveMQ Classic](https://activemq.apache.org/getting-started), [ActiveMQ Artemis](https://activemq.apache.org/components/artemis/documentation/)

#### 如何以调试模式启动ActiveMQ服务？

```
systemctl stop activemq
/opt/apache-activemq/bin/activemq console
```

#### 如何修改ActiveMQ后台密码？

密码配置文件 */opt/apache-activemq/conf/jetty-realm.properties*，修改后重启activemq服务后生效

#### 如何退出 ActiveMQ 控制台？

暂无方案

#### 如果没有域名是否可以部署 ActiveMQ？

可以，访问`http://服务器公网IP` 即可

#### ActiveMQ 中是否包含Tomcat？

ActiveMQ 官方提供的二级制包中包含Tomcat，但已经集成到ActiveMQ服务中。

#### 是否可以修改ActiveMQ的源码路径？

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
