---
sidebar_position: 3
slug: /ghost/admin
tags:
  - Ghost
  - CMS
  - 建站系统
  - 博客系统
---
# 维护指南

## 场景

### 备份与恢复


### 升级

不部署采用 Docker 安装 Ghost，官方提供的通过 Node.js 升级 Ghost 不适用。

请按照下面的流程完成升级：

1. 手工[备份 Ghost](/zh/solution-backup.md#程序手工备份)，一定要确保万无一失
2. 登录云服务器，分别运行下面的命令
   ```
   #停止并删除现有的 Ghost 容器
   sudo docker stop ghost && sudo docker rm ghost

   #删除本地 Ghost 镜像
   docker image rm ghost

   #重新运行容器
   cd /data/wwwroot/ghost && docker-compose up -d
   ```
3. 本地浏览器重新访问 Ghost，开始升级

## 故障速查

除以下列出的 Ghost 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Ghost服务无法启动？

服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh

# 查看服务状态和日志
sudo docker ps
sudo docker logs ghost
```

#### 无法打开默认主题 casper 文件夹？

官方表示，casper 是内核的组成部分，仅自上传的主题方可修改。


## 问题解答

#### Ghost 支持中文吗？

Ghost 的后台不支持中文，但是前台支持中文（需主题中有中文）

#### Ghost 系统中的 Post 与 Page 有什么区别？

Post 是文章的意思，每一篇博客文章即一个 Post；Page 是页面的意思，网站中的首页，公司介绍等都可称之为 Page。  

在 Ghost 系统中，每一个新建的 Page，都需要在主题中有对应的模板文件与之匹配。

#### Ghost 有哪些用户角色？

参考官方文档 [Managing your team in Ghost](https://ghost.org/help/managing-your-team/)

#### Ghost 是否支持对默认主题 casper 进行修改？

不支持，只可以修改自上传的主题。

#### 是否可以通过命令行修改Ghost后台密码？

不可以

#### 如果没有域名是否可以部署 Ghost？

可以，访问`http://服务器公网IP` 即可

#### 设置域名访问？

首先要解析域名，然后登录服务完成[域名绑定操作](../ghost#dns)

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：*http://服务器公网IP:9090*

#### 如何禁止外界访问phpMyAdmin？

云控制台安全组中关闭 9090 端口即可

#### 是否可以修改Ghost目录路径？

可以，通过修改 Ghost 容器编排文件： */data/wwwroot/ghost/docker-compose.yml* 中的持久化目录实现
