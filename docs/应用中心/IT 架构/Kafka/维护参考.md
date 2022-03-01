---
sidebar_position: 2
slug: /kafka/admin
tags:
  - Kafka
  - IT 架构
  - 中间件
---

# 维护参考

## 系统参数

Kafka 预装包包含 Kafka 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

下来我们对路径信息进行更为准确的说明：

#### Kafka

Kafka 安装目录：*/opt/kafka*  
Kafka 日志目录：*/opt/kafka/logs*  
Kafka bin目录：*/opt/kafka/bin*  
Kafka 配置目录：*/opt/kafka/config*  

#### Java

Java 虚拟机目录： */usr/bin/java*  

#### CMAK

[CMAK](https://github.com/yahoo/CMAK) 是管理 Kafka 集群的可视化工具，基于 Docker 安装

CMAK 安装目录： */data/apps/cmak*  

#### Zookeeper

Zookeeper 配置文件路径：/opt/zookeeper/conf/  
Zookeeper 日志文件：/opt/zookeeper/tmp/zookeeper.out  

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 9092 | Kafka | 可选 |
| TCP | 2181 | Zookeeper | 可选 |
| TCP | 9091 | CMAK | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Java  Version
java -version

# Kafka version
ls /opt/kafka/libs | grep kafka_

# CMAK version
docker exec -it cmak bash -c 'ls /cmak/lib/cmak.cmak-*-assets.jar'
```

### 服务


使用由Websoft9提供的 Kafka 部署方案，可能需要用到的服务如下：

#### Kafka

```shell
sudo systemctl start kafka
sudo systemctl stop kafka
sudo systemctl restart kafka
sudo systemctl status kafka

# you can use this debug mode if Kafka service can't run
bash /opt/kafka/bin/kafka-server-start.sh
```

#### Zookeeper

```shell
sudo systemctl start zookeeper
sudo systemctl stop zookeeper
sudo systemctl restart zookeeper
sudo systemctl status zookeeper

# you can use this debug mode if Kafka service can't run
bash /opt/kafka/bin/zookeeper-server-start.sh
```

#### Docker
```shell
sudo systemctl start docker
sudo systemctl stop docker
sudo systemctl restart docker
sudo systemctl status docker
```

#### CMAK
```shell
sudo docker inspect cmak
sudo docker start cmak
sudo docker restart cmak
sudo docker stop cmak
sudo docker rm cmak
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

1. 通过WinSCP将网站目录（*/opt//kafka*）**压缩后**再完整的下载到本地
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

### Kafka升级

Kafka 主要采用二级制安装方式，其升级方案差不多等于安装：

1. 依次运行如下的命令做好准备：
   ```
   # stop Kafka,Zookeeper service
   systemctl stop kafka
   systemctl stop zookeeper

   # rename the dir of Kafka for backup
   mv /opt/kafka  /opt/kafkaBK
   ```
2. 从官网[下载Kafka](https://kafka.apache.org/downloads)后解压并上传到：*/opt* 目录，并命名为 *kafka*
3. 分别运行下面的修改权限
   ```
   chown -R kafka. /opt/kafka
   ```
4. 重启 [Kafka服务](#服务) 后升级完成

    ```

## 故障处理

此处收集使用 Kafka 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Kafka服务无法启动？

1. 以调试模式运行`bash /opt/kafka/bin/kafka-server-start.sh`，便可以查看启动状态和错误
2. 打开日志文件：*/data/logs*，检索 **failed** 关键词，分析错误原因

#### 运行 *kafka-run-class.sh* 显示 **java: not found...**的错误？

这是Java环境变量缺失导致的问题，请设置环境变量：$JAVA_HOME=/usr/bin/java


#### 如何以调试模式启动 Kafka 服务？

```
systemctl stop kafka zookeeper
bash /opt/kafka/bin/kafka-server-start.sh
```

## 常见问题

#### 是否提供了 Kafka 可视化管理工具？

是的。参考 [CMAK](/zh/solution-gui.md)

#### 为何 CMAK 中无法支持所需的 Kafka 版本？

CMAK 并不是支持所有 Kafka 版本，具体以使用为准

#### 是否可以修改Kafka的源码路径？

不建议修改，除非你熟悉环境变量设置、后台服务的编写