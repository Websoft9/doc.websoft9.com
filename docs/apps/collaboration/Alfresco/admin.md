---
sidebar_position: 3
slug: /alfresco/admin
tags:
  - Alfresco
  - 企业管理
  - ERP
---

# 维护指南

## 场景

### 备份与恢复

### 升级

Alfresco 基于 Docker 部署，其升级流程：拉取镜像 > 删除容器 > 重建容器

> 升级之前请确保您已经完成了服务器的镜像（快照）备份

1. 登录服务器，编辑 */data/wwwroot/alfresco/.env* 文件，将版本变量的值修改为目标版本号

2. 拉取目标版本的镜像
   ```
   cd /data/wwwroot/alfresco
   docker-compose pull
   ```
   > 如果显示没有镜像可拉取，则无需升级

3. 删除旧容器，重新创建 Alfresco 容器
    ```
    docker-compose down -v
    docker-compose up -d
    ```

## 故障速查

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Alfresco 服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
docker ps
```

## 问题解答

#### 中文 Markdown 格式预览乱码？

暂无方案

#### Alfresco 是否支持多语言？

支持（包含中文），后台可以自行切换

#### Alfresco Content Services Enterprise 与 Alfresco Community Edition 有什么不同？

Alfresco Community Edition 是 Alfresco Content Services Enterprise 的开源版本，参考[对比](https://www.alfresco.com/alfresco-content-services-enterprise-vs-alfresco-community-edition)

#### Alfresco 支持哪些文件格式？

参考[Alfresco支持所有文件格式](https://www.alfresco.com.cn/alfresco-formats)

#### 本项目中 Alfresco 采用何种安装方式？

Docker

#### 如果没有域名是否可以部署 Alfresco？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 pgAdmin，访问地址：*http://服务器公网IP:9090*

#### 是否可以修改Alfresco的源码路径？

不可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R apache.apache /data/wwwroot/
# 读写执行权限
find /data/wwwroot/ -type d -exec chmod 750 {} \;
find /data/wwwroot/ -type f -exec chmod 640 {} \;
```