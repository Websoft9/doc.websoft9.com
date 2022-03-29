---
sidebar_position: 3
slug: /mingdao/admin
tags:
  - 明道云
  - APaaS
  - 无代码平台
---

# 维护指南

## 场景

### 备份与恢复


### 升级


## 故障速查

#### 如何查看错误日志？

```
cat /data/mingdao/script/mingdaoyun.log
docker logs $(docker ps | grep mingdaoyun-community | awk '{print $1}')
```

更多与日志香港的操作[参考](https://docs.pd.mingdao.com/deployment/docker-compose/command.html#日志)

#### 明道云服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
systemctl status mingdao
journalctl -u mingdao
```

#### 服务器重启后，程序打不开{#restart}

服务器重启后，明道云容器没有启动，使用下面的命令，启动服务，稍等片刻即可打开

```
cd /data/wwwroot/mingdao/installer/
 ./service.sh restartall

```
#### 服务器重启后，服务器IP地址变化，导致工作流等一些服务无法使用{#workflow}

服务器IP变化后，需要修改 docker-compose 配置：
打开 /data/mingdao/script/docker-compose.yaml，修改 ENV_MINGDAO_HOST 为新的IP，再用重启服务

```
version: '3'

services:
  app:
    image: registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-community:2.10.1
    environment:
      ENV_MINGDAO_PROTO: "http"
      ENV_MINGDAO_HOST: "123.57.218.118"  
      ENV_MINGDAO_PORT: "8880"
      COMPlus_ThreadPool_ForceMinWorkerThreads: 100
      COMPlus_ThreadPool_ForceMaxWorkerThreads: 500
    ports:
      - 8880:8880
    volumes:
      - ./volume/data/:/data/
      - ./volume/tmp/:/usr/local/MDPrivateDeployment/wwwapi/tmp/
      - /usr/share/zoneinfo/Etc/GMT-8:/etc/localtime
      - ../data:/data/mingdao/data

  doc:
    image: registry.cn-hangzhou.aliyuncs.com/mdpublic/mingdaoyun-doc:1.2.0
```


## 问题解答

#### 明道云 是否支持多语言？

支持中文和英文

#### 明道云有哪些版本？

明道云为不同的用户提供了多种版本，主要包括：

* [SaaS 版本](https://www.mingdao.com/price)，其中又分为：免费版、标准版、专业版、旗舰版四种
* [私有部署版](https://www.mingdao.com/pd)，其中又分为：社区版（免费）、标准版、专业版三种

本部署方案中提供的就是 **私有部署版** 中的免费版本

#### 为什么采用单机部署

私有部署版虽然是一个单机部署方式，单其内部依然是一个微服务集合，所以为了保证容器内各服务进程的可用性，在容器内部预置了健康检查线程，当某服务出现故障时能自动恢复。

#### 本项目中 明道云 采用何种安装方式？

采用 Docker 部署

#### Websoft9 与明道云是什么关系？

Websoft9 是明道云的全球战略合作伙伴，主要在全球的主流云平台发布 **明道云私有部署版（免费）** 

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/shouquanshu.jpg)

#### 是否可以通过命令行重置明道云后台密码？

暂无方案

#### 如果没有域名是否可以部署 明道云？

可以，访问`http://服务器公网IP:8880` 即可

#### 是否可以修改明道云的目录？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R nginx.nginx /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```