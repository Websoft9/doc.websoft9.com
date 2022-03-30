---
sidebar_position: 3
slug: /seafile/admin
tags:
  - Seafile
  - 网盘
  - 知识管理
  - 团队协作
---

# 维护指南

## 场景

### 备份与恢复

### 升级

Seafile 升级大致流程：先拉取最新版本的 Seafile 镜像，然后重新运行容器。

> Seafile 升级之前请完成服务器的快照备份，以防不测。

1. 使用 SSH 登录 Seafile 服务器后，停止容器

   ```
   cd /data/wwwroot/seafile 
   docker-compose down -v
   ```

2. 拉取最新版本镜像
   ```
   docker image pull seafileltd/seafile-mc:latest
   ```

3. 重新运行 docker-compose 编排文件，启用新的容器
    ```
    docker-compose up -d
    ```
    
4. 登录 Seafile 后台查看升级后的版本
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-aboutversion-websoft9.png)

更多参考官方升级文档：[升级 Seafile 服务](https://cloud.seafile.com/published/seafile-manual-cn/docker/%E7%94%A8Docker%E9%83%A8%E7%BD%B2Seafile.md#user-content-%E5%8D%87%E7%BA%A7%20Seafile%20%E6%9C%8D%E5%8A%A1)

## 故障速查

#### Seafile 无法上传文件？

设置 Seafile 的主机地址（**必选项，否则无法使用文件上传功能**）

   - SERVICE_URL：*http://服务器公网IP*
   - FILE_SERVER_ROOT：*http://服务器公网IP/seafhttp*

   ![Seafile后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-seturl-websoft9.png)
   
   
#### 完成文档服务器配置，Seafile 仍然无法编辑和预览文件？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-canotaccess-websoft9.png)  

问题原因：SERVICE_URL 与实际不符  
解决方案：需登录控制台的系统设置，修改 SERVICE_URL 为实际值

#### 完成 ONLYOFFICE Docs 配置，Seafile 编辑和预览显示错误 “文档安全令牌未正确形成”？

问题原因：ONLYOFFICE docs 安全设置过高   
解决方案：需修改 ONLYOFFICE docs 编排文件中的环境变量 JWT_ENABLED，设置为 false  

```
  onlyoffice-document-server:
    container_name: onlyoffice-docs
    image: onlyoffice/documentserver:6.0.2
    stdin_open: true
    tty: true
    restart: always
    environment:
     - JWT_ENABLED=flase
```

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

#### Seafile 无法打开？

查看启动日志，分析错误原因

```
docker logs seafile
```

## 常见问题

#### Seafile 支持多语言吗？

支持多种语言（中文，英文等）

#### 为什么要推荐使用企业版Seafile？

企业版用户拥有很多社区版没有的功能，如下：
![Seafile企业版社区版功能对比](https://libs.websoft9.com/Websoft9/DocsPicture/zh/seafile/seafile-compare-websoft9.png)

#### 为什么采用 Docker 方式部署 Seafile？

官方推荐

#### Seafile 是如何与MySQL 连接的？

容器内部连接，即容器编排

#### Seafile 默认能否对文档进行预览和编辑？

支持，如果不能预览，请参考[Office设置](../seafile/solution#onlyoffice)

#### 如果没有域名是否可以部署 Seafile？

可以，访问`http://服务器公网IP` 即可

#### 如何管理 MySQL/MariaDB 数据库？

参考本文档的 [MySQL 章节](../mysql)

#### 是否有可视化的数据库管理工具？

有，提供可视化的数据库管理工具 phpMyAdmin

#### 是否可以修改Seafile的数据路径？

可以，但需要对历史数据进行迁移