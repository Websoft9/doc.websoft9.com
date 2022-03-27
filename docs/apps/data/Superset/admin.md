---
sidebar_position: 3
slug: /superset/admin
tags:
  - Superset
  - 大数据分析
  - BI
---

# 维护指南

## 场景

除以下列出的 Superset 维护场景问题之外， [管理员指南](../administrator) 专题提供了通用的维护方案。

## 故障速查

除以下列出的 Superset 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案：

#### Superset 容器中安装数据库驱动报错？

**现象描述**：ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: '/home/superset'
Check the permissions.    

**原因分析**：权限不足

**解决方案**：以 root 用户进入容器 `docker exec -it --user root superset_app bash`，然后再安装驱动  

#### Superset 密码正确，但仍然登录失败？{#loginfail}

**现象描述**：用户名和密码完全正确，但 Superset 仍然登录失败，错误信息 Invalid login, Please try again   

**原因分析**：暂时未知

**解决方案**：重启所有 Superset 容器 `cd /data/wwwroot/superset && docker-compose restart` 

## 问题解答

#### Superset 支持多语言吗？

支持（包含中文)，但测试版不支持多语言

#### 如何查看所有容器？

```
sudo docker ps
```

#### 是否可以通过命令行修改 Superset 后台密码？

不支持，需登录控制台修改

#### 如果没有域名是否可以部署 Superset？

可以，访问 `http://服务器公网IP` 或 `http://服务器公网IP:8088` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置pgAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何以 root 身份进入容器运行命令？

```
docker exec -it --user root superset_app bash
```

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R superset.superset /data/wwwroot/superset
# 读写执行权限
find /data/wwwroot/superset -type d -exec chmod 750 {} \;
find /data/wwwroot/superset -type f -exec chmod 640 {} \;
```

#### 是否支持 google authentication 或 OKTA based authentication (OIDC)?

SuperSet 默认只提供了邮件登录，更多登录方式使用需参考其框架文档：[Flask-AppBuilder](https://flask-appbuilder.readthedocs.io/en/latest/security.html#supported-authentication-types)
