---
sidebar_position: 3
slug: /tensorflow/admin
tags:
  - TensorFlow
  - 人工智能
  - 机器学习
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../installation/setup/) 相关章节。

## 场景

### 备份与恢复

### 升级

TensorFlow 是基于 pip 安装，故可以很方便的通过 pip 进行升级

```
# 激活隔离环境下的 TensorFlow
source /data/apps/tensorflow/bin/activate

# 升级
pip install -U TensorFlow
```

## 故障速查

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### TensorFlow服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status tensorflow
journalctl -u tensorflow
```

 >更多故障详细请参照[官方问题](https://www.tensorflow.org/install/errors)


## 问题解答

#### TensorFlow 管理员用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### TensorFlow 是如何安装的？

是创建 Python 隔离环境后，基于 pip 安装。

#### 是否有可视化的管理工具？

有，内置TensorBoard，访问地址：*http://服务器公网IP:6006/*

#### 是否可以修改TensorFlow的源码路径？

不可以，TensorFlow使用pip安装，服务启动文件设定路径为目前源码路径，修改后服务可能无法启动

#### TensorFlow 实现 GPU 支持需要哪些条件？

需要 NVIDIA® GPU显卡以及驱动程序和工具。详细请参照[TensorFlow GPU 支持软硬件要求](https://www.tensorflow.org/install/gpu)

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```