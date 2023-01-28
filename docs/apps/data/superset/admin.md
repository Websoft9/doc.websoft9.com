---
sidebar_position: 3
slug: /superset/admin
tags:
  - Superset
  - 大数据分析
  - BI
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### Superset 升级

升级方法操作如下：

```
cd /data/apps/superset
sudo docker compose down
# such as: upgrade version=2.0.1
sudo sed -i 's/APP_VERSION=.*/APP_VERSION=2.0.1/g' /data/apps/superset/.env
cd /tmp && git clone https://github.com/apache/superset
git checkout 2.0
rm -rf /data/apps/superset/src/docker
cp -r docker /data/apps/superset/src
docker compose up -d

```

 > 该升级方法仅作为参照，对于版本跨度较大的情况可能不会成功，请联系客服处理。

## 故障排除

除以下列出的 Superset 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案：

#### Superset 容器中安装数据库驱动报错？

**现象描述**：ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: '/home/superset'
Check the permissions.

**原因分析**：权限不足

**解决方案**：以 root 用户进入容器 `docker exec -it --user root superset-app bash`，然后再安装驱动

#### Superset 密码正确，但仍然登录失败？{#loginfail}

**现象描述**：用户名和密码完全正确，但 Superset 仍然登录失败，错误信息 Invalid login, Please try again

**原因分析**：暂时未知

**解决方案**：重启所有 Superset 容器 `cd /data/wwwroot/superset && docker-compose restart`

## 问题解答

#### Superset 支持多语言吗？

支持（包含中文)，但测试版不支持多语言。

#### 如何以 root 身份进入容器运行命令？

```
docker exec -it --user root superset-app bash
```

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R superset.superset /data/wwwroot/superset
# 读写执行权限
find /data/wwwroot/superset -type d -exec chmod 750 {} \;
find /data/wwwroot/superset -type f -exec chmod 640 {} \;
```

#### 是否支持 Google Authentication？

SuperSet 默认只提供了邮件登录，更多登录方式使用需参考其框架文档：[Flask-AppBuilder](https://flask-appbuilder.readthedocs.io/en/latest/security.html#supported-authentication-types)
