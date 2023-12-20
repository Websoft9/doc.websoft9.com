---
sidebar_position: 2
slug: /administrator/migration_app
---

# Application Migration


There is no precise solution for application migration that is completely suitable for all applications, but the migration law of applications is universal.

The migration of the application mainly consists of the following steps:  


## Migrate Docker-based application 

对于 Docker 应用来说，环境与操作系统被打包到一个【虚拟盒子】中，很容易被迁移。下面介绍具体步骤：

1. 列出当前应用所有的容器
   ```
   cd /data/wwwroot/appname
   docker-compose ps
   ```
2. 为每一个相关的容器创建镜像以及导出为压缩文件
   ```
   # 创建镜像
   sudo docker commit appname image_name

   # 导出镜像到当前目录
   sudo docker save image_name > image_name.tar
   ```

3. 将应用的根目录以及所有 .tar 文件拷贝到目标服务器

4. 在目标服务器上逐个将 .tar 文件恢复为镜像
   ```
   sudo docker load < image-name.tar
   ```

5. 将应用的持久化存储目录拷贝到目标服务器（保持路径一致）

6. 检查 docker-compose.yml 和 .env 文件，保证 volume 和 image 符合真实情况

7. 重新创建容器
   ```
   cd /path/appname
   docker-compose up -d
   ```

## Migrate not Docker-based application 

对于非 Docker 等应用来说，环境与应用是分离的，环境与操作系统是紧耦合的。意味着迁移环境难度很大，所以大部分时候用户会在目的地服务器上重新部署一致的环境。  

具体的迁移步骤如下：

1. 目标服务器准备好应用所需的环境（程序环境、数据库、中间件、Web Server），务必保证版本一致

2. 将应用的源码（数据）拷贝到目标目录
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-copysite1todata2-websoft9.png)

3. 数据库迁移

4. 检查应用的配置文件，确保与真实环境一致

5. 测试迁移的结果


## Migration follow-up

完成应用迁移之后，可能还有一些后续的工作：

* 域名重新解析和绑定
* 文件（文件夹）权限修正