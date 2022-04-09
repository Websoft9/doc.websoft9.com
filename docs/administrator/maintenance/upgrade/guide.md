---
sidebar_position: 1
slug: /upgrade
---

# 指南

## 场景

### Docker 应用升级{#dockerapp}

对于基于 Docker 部署的，其升级流程具备通用性：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 修改 Docker 应用的根目录 [.env 文件](#path)中的版本号

2. 拉取目标版本的镜像
   ```
   cd /data/wwwroot/appname
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 appname 容器
    ```
    docker-compose down
    docker-compose up -d
    ```

### 操作系统更新

#### Linux 更新{#linux}

Linux服务器的更新，只需要运行一条更新命令，即可安装操作系统、运行环境和数据库等更新

```
#CentOS or Redhat
sudo yum update -y

#Ubuntu
apt update && apt upgrade -y
```

实际上，Websoft9提供的镜像已经将以上更新命令通过计划任务定期执行。

#### Windows 更新{#windows}

Windows服务器的更新与本地电脑类似，手动找到更新管理程序，设置自动下载自动更新即可。

Windows服务器中的运行环境、数据库等，需要采用手工下载补丁替换的方式完成更新


## 参数

### 路径{#path}

* Docker 应用配置文件：*/data/wwwroot/appname/.env*

### 服务{#service}