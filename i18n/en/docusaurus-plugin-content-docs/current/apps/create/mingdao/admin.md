---
sidebar_position: 3
slug: /mingdao/admin
tags:
  - Mingdao
  - APaaS
  - No-code Development Platform
---

# Mingdao Maintenance

This chapter is special guide for Mingdao maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide


## Troubleshoot{#troubleshoot}

In addition to the Mingdao issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### How can I check the error logs?

```
cat /data/mingdao/script/mingdaoyun.log
docker logs $(docker ps | grep mingdaoyun-community | awk '{print $1}')
```

More logs please refer to official docs: [Mingdao Logs](https://docs.pd.mingdao.com/deployment/docker-compose/command.html#日志)

#### 服务器重启后，程序打不开{#restart}

服务器重启后，明道云容器没有启动，使用下面的命令，启动服务，稍等片刻即可打开

```
cd /data/wwwroot/mingdao/installer/
 ./service.sh restartall

```
#### 服务器IP变化，导致工作流等服务异常？{#workflow}

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


## FAQ{#faq}

#### Does Mingdaoyun support multiple languages?

Chinese and English

#### 明道云有哪些版本？

明道云为不同的用户提供了多种版本，主要包括：

* [SaaS 版本](https://www.mingdao.com/price)，其中又分为：免费版、标准版、专业版、旗舰版四种
* [私有部署版](https://www.mingdao.com/pd)，其中又分为：社区版（免费）、标准版、专业版三种

本部署方案中提供的就是 **私有部署版** 中的免费版本

#### 为什么采用单机部署？

私有部署版虽然是一个单机部署方式，单其内部依然是一个微服务集合，所以为了保证容器内各服务进程的可用性，在容器内部预置了健康检查线程，当某服务出现故障时能自动恢复。

#### What method does this Mingdao deployment?

Docker

#### Websoft9 与明道云是什么关系？

Websoft9 是明道云的全球战略合作伙伴，我们的与明道云有关的服务包括：

1. 主要在全球的主流云平台发布 **明道云私有部署版（免费）** 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/shouquanshu.jpg)
2. 为明道云私有云客户提供托管与运维支持服务
3. 提供基于明道云的无代码开发与系统建模服务

#### 无代码开发的报价？

Websoft9 提供最低 20000元起的开发服务，诚意服务于广大的中小企业。  