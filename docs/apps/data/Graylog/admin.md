---
sidebar_position: 3
slug: /graylog/admin
tags:
  - Graylog
  - 日志管理
  - 数据分析
---

# 维护指南

## 场景

### Graylog 集群

我们知道，Graylog 运行时，包括如下软件：

- Graylog 日志采集、分析
- ElasticSearch 日志存储
- MongoDB 系统配置系统

Graylog 支持如下最简答的部署方式：  
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-minisetup-websoft9.png)

也支持复杂的[集群](https://docs.graylog.org/v1/docs/multinode-setup)部署：  
![Graylog 集群部署架构图](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-hasetup-websoft9.png)

其中，MongoDB 实际上可以不做集群。

> 更多信息参考官方的[架构指南](https://www.slideshare.net/Graylog/graylog-engineering-design-your-architecture)

### 重置密码

如果无法找回管理员密码，可以通过下面的步骤重置密码

1. 使用 SSH 工具登录服务器，运行下面的密码重置命令

   ```
   new_password=admin123@graylog
   sha_password=$(echo -n $new_password | sha256sum | awk '{ print $1 }')
   sudo sed -i "s/8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918/$sha_password/g" /data/wwwroot/graylog/.env
   ```

2. 重新运行容器编排命令，密码就被重置为 `admin123@graylog`
   ```
   cd /data/wwwroot/graylog && sudo docker-compose up -d
   ```

> 你可以将 new_password 设置为任何你想要的密码

## 故障速查

除以下列出的 Graylog 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案：

#### 登录后告警和错误提示 ？

**现象 1**：提示 There is a node without any running inputs. This means ... ？
![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-nofiinput-websoft9.png)
**原因**：这只是一个当前没有 input 的提醒，并非错误。  
**方案**：新建一个本地的 input，即可消除此提醒

**现象 2**：提示 Index rotation strategy null not found... ?  
**原因**：磁盘可用空间低于 15% 的时候，会出现这个问题  
**方案**：释放冗余的文件或者增加服务器磁盘空间

## 常见问题

#### Graylog 系统架构示意图？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/graylog-arch-websoft9.png)

#### Graylog 的集群架构示意图？

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/graylog/architec_bigger_setup.png)

#### 如何访问 Graylog API?

访问的 URL 为：_https://Internet IP:9001/api/api-browser/global/index.html_。缺少 /global/index.html 是无法访问的

#### 如果没有域名是否可以部署 Graylog？

可以，直接端口访问即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 AdminMongo，访问地址：_http://服务器公网 IP:9091_

#### 是否可以修改 Graylog 的源码路径？

可以

#### 如何修改上传的文件权限?

```shell
# 拥有者
chown -R graylog.graylog /data/wwwroot/graylog
# 读写执行权限
find /data/wwwroot/graylog -type d -exec chmod 750 {} \;
find /data/wwwroot/graylog -type f -exec chmod 640 {} \;
```
