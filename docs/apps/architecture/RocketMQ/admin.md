
---
sidebar_position: 2
slug: /rocketmq/admin
tags:
  - RocketMQ
  - IT 架构
  - 中间件
---

# 维护参考

## 系统参数

RocketMQ 预装包包含 RocketMQ 运行所需一序列支撑软件（简称为“组件”），下面列出主要组件名称、安装路径、配置文件地址、端口、版本等重要的信息。

### 路径

#### RocketMQ

RocketMQ 安装目录： */data/rocketmq*  
RocketMQ 日志目录： */data/logs/rocketmq*  
RocketMQ 配置文件： */data/config/rocketmq*

#### RocketMQ-Console

[RocketMQ-Console-NG ](https://github.com/apache/rocketmq-externals/tree/master/rocketmq-console) 是一款可视化 RocketMQ 管理工具，在本项目中它基于 Docker 安装。  

RocketMQ-Console 安装目录：*/data/apps/rocketmq-console-ng*  
RocketMQ-Console Compose文件：*/data/apps/rocketmq-console-ng/docker-compose.yml* 

#### Docker

Docker 根目录: */var/lib/docker*  
Docker 镜像目录: */var/lib/docker/image*   
Docker daemon.json 文件：默认没有创建，请到 */etc/docker* 目录下根据需要自行创建   

### 端口号

在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

通过命令`netstat -tunlp` 看查看相关端口，下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 9876 | RocketMQ Name Server | 必须 |
| TCP | 9003 | 通过 HTTP 访问 RocketMQ-Console-Ng    | 可选 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Java version
java -v

# Docker Version
docker -v

# RocketMQ version
ls /data/rocketmq/lib |grep rocketmq-broker
```

### 服务

使用由 Websoft9 提供的 RocketMQ 部署方案，可能需要用到的服务如下：

#### RocketMQ

```shell
sudo systemctl start mqnamesrv
sudo systemctl stop mqnamesrv
sudo systemctl restart mqnamesrv
sudo systemctl status mqnamesrv
```

```shell
sudo systemctl start mqbroker
sudo systemctl stop mqbroker
sudo systemctl restart mqbroker
sudo systemctl status mqbroker
```

#### Docker

```shell
systemctl start docker
systemctl stop docker
systemctl restart docker
systemctl status docker
```

#### Nginx

```shell
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl status nginx
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

程序手工本地备份是通过**下载应用程序源码**实现最小化的备份方案。

下面以列表的方式介绍这种备份：
```
- 备份范围: 应用程序
- 备份效果: 一般
- 备份频率: 一周最低1次，备份保留30天
- 恢复方式: 重新导入
- 技能要求：非常容易
- 自动化：无
```
通用的手动备份操作步骤如下：

1. 通过 SFTP 将网站目录（*/data/rocketmq/*）**压缩后**再完整的下载到本地
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

## 故障处理

此处收集使用 RocketMQ 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### RocketMQ服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status mqnamesrv
journalctl -u mqnamesrv

systemctl status mqbroker
journalctl -u mqbroker
```

RocketMQ 最低内存设置查看 **runserver.sh** 和 **runbroker.sh**` JAVA_OPT 设置

>更多的故障问题请参照[官方文档](http://rocketmq.apache.org/docs/faq/)


## 常见问题

#### RocketMQ-Console-Ng 是否支持多语言？

目前支持英文和简体中文，可以登陆后可以直接在顶部菜单进行设置。

#### 本项目中 RocketMQ 采用何种安装方式？

采用二进制包解压的安装方式

#### RocketMQ-Console-Ng 管理员用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### RocketMQ 的消息保存多久？

消息将最多保存3天，未使用超过3天的消息将被删除。

#### 如何修改 RocketMQ 最低运行内存？

分别修改如下两个配置文件：

* *rocketmq/bin/runserver.sh* 文件中 Java 启动内存大小（非必要）
* */data/rocketmq/bin/runbroker.sh* 文件中 Java 启动内存大小（非必要）

#### 是否有可视化的管理工具？

有，内置RocketMQ-Console-Ng，访问地址：*http://服务器公网IP*

#### 是否可以修改RocketMQ的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```
