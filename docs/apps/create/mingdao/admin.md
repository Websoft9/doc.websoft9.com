---
sidebar_position: 3
slug: /mingdao/admin
tags:
  - 明道云
  - APaaS
  - 无代码平台
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

## 故障排除

除以下列出的 明道云 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

#### 如何查看错误日志？

```
cat /data/mingdao/script/mingdaoyun.log
docker logs $(docker ps | grep mingdaoyun-community | awk '{print $1}')
```

详细查看：[日志命令](https://docs.pd.mingdao.com/deployment/docker-compose/command.html#日志)

#### 服务器重启后，程序打不开{#restart}

服务器重启后，明道云容器没有启动，使用下面的命令，启动服务，稍等片刻即可打开

```
cd /data/wwwroot/mingdao/installer/
 ./service.sh restartall

```
#### 服务器IP变化，导致工作流等服务异常？{#ipchange}

服务器 IP 变化后，需要修改 docker-compose 配置：

打开[明道云容器配置文件](../mingdao#path)，修改 ENV_MINGDAO_HOST 为新的IP，再用重启服务

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

#### 明道云是否支持多语言？

支持中文和英文

#### 明道云有哪些版本？

明道云为不同的用户提供了多种版本，主要包括：

* [SaaS 版本](https://www.mingdao.com/price)，其中又分为：免费版、标准版、专业版、旗舰版四种
* [私有部署版](https://www.mingdao.com/pd)，其中又分为：社区版（免费）、标准版、专业版三种

本部署方案中提供的就是 **私有部署版** 中的免费版本

#### 为什么采用单机部署？

私有部署版虽然是一个单机部署方式，单其内部依然是一个微服务集合，所以为了保证容器内各服务进程的可用性，在容器内部预置了健康检查线程，当某服务出现故障时能自动恢复。

#### 明道云采用何种安装方式？

采用 Docker 部署

#### Websoft9 与明道云是什么关系？

Websoft9 是明道云的全球战略合作伙伴，我们的与明道云有关的服务包括：

1. 主要在全球的主流云平台发布 **明道云私有部署版（免费）** 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/shouquanshu.jpg)
2. 为明道云私有云客户提供托管与运维支持服务
3. 提供基于明道云的无代码开发与系统建模服务

#### 无代码开发的报价？

Websoft9 提供最低 20000元起的开发服务，诚意服务于广大的中小企业。  