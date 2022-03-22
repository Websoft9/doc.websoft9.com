---
sidebar_position: 3
slug: /gitlab/admin
tags:
  - Gitlab
  - DevOps
---

# 维护参考


## 系统参数

本GitLab采用 [Omnibus GitLab包](https://gitlab.com/gitlab-org/omnibus-gitlab) 的安装方式。Omnibus GitLab 是官方推荐的一种安装方法，它自带了 GitLab 所需的所有组件和服务，并可以省去繁琐的配置，同时它自带 CLI 工具，便于 GitLab 升级和维护。

### 架构

下面是一个简化的架构图，可用于了解GitLab的架构。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/architecture_simplified.png)

### 组件和版本

GitLab 包含数十种组件([查看](https://docs.gitlab.com/ee/development/architecture.html#component-list))，通过 */opt/gitlab/version-manifest.txt* 查看服务器上所有组件名称和版本

### 路径
Gitlab 13.9以前的版本采用的Docker安装方式，持久化文件路径：/data/wwwroot/gitlab  
了解详细，请查看[GitLab Docker 安装](https://docs.gitlab.com/omnibus/docker/README.html)


#### GitLab

GitLab 配置文件： */etc/gitlab/gitlab.rb*    
GitLab 及所有组件配置： */opt/gitlab*  
GitLab Repository 存储目录： */var/opt/gitlab/git-data*  
GitLab 备份目录： */var/opt/gitlab/backups*

#### Unicorn

Unicorn 日志目录： */var/log/gitlab/unicorn*  

#### Sidekiq

Unicorn 日志目录： */var/log/gitlab/sidekiq*

#### Nginx

Nginx 日志目录: */var/log/gitlab/nginx*  
Nginx 配置文件: */var/opt/gitlab/nginx/conf/nginx.conf*  
GitLab 核心 Nginx 配置文件:  */var/opt/gitlab/nginx/conf/gitlab-http.conf*

#### PostgreSQL

PostgreSQL 安装目录： */var/opt/gitlab/postgresql*  
PostgreSQL 日志目录: */var/log/gitlab/postgresql*   
PostgreSQL-Exporter 日志目录： */var/log/gitlab/postgres-exporter*  
PostgreSQL 数据目录： */var/opt/gitlab/postgresql/data*

#### Redis

Redis 安装目录： */var/opt/gitlab/redis*  
Redis 日志目录： */var/log/gitlab/redis*

#### Potainer

potainer 安装目录： */data/apps/portainer*  
potainer 数据目录： */data/apps/portainer/data*


### 端口号

系统所用到的端口号，请通过官方文档 [Package defaults](https://docs.gitlab.com/omnibus/package-information/defaults.html) 查阅。在云服务器中，通过 **[安全组设置](https://support.websoft9.com/docs/faq/zh/tech-instance.html)** 来控制（开启或关闭）端口是否可以被外部访问。 

本应用建议开启的端口如下：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| HTTP | 80 | 通过http访问GitLab | 必须 |
| HTTPS | 443 | 通过https访问GitLab | 可选 |
| HTTP | 9000 | 通过http访问Portainer | 必须 |

### 版本号

组件版本号可以通过云市场商品页面查看。但部署到您的服务器之后，组件会自动进行更新导致版本号有一定的变化，故精准的版本号请通过在服务器上运行命令查看：

```shell
# Linux Version
lsb_release -a

# Nginx version:
nginx -v

# PostgreSQL version:
psql --version

# Dokcer:
docker --version
```

### 服务

使用由Websoft9提供的GitLab部署方案，可能需要用到的服务（[官方文档](https://docs.gitlab.com/omnibus/maintenance/README.html#get-service-status)）如下：


-Nginx：静态web服务器。  
-gitlab-shell：用于处理Git命令和修改authorized keys列表。  
-gitlab-workhorse: 轻量级的反向代理服务器。  
-logrotate：日志文件管理工具。  
-postgresql：数据库。  
-redis：缓存数据库。  
-sidekiq：用于在后台执行队列任务（异步执行）。  
-unicorn：An HTTP server for Rack applications，GitLab Rails应用是托管在这个服务器上面的。


#### GitLab

```shell
sudo gitlab-ctl start 
sudo gitlab-ctl stop 
sudo gitlab-ctl restart 
sudo gitlab-ctl status 
sudo gitlab-ctl reconfigure
```

#### Nginx

```shell
sudo gitlab-ctl start nginx
sudo gitlab-ctl stop nginx
sudo gitlab-ctl restart nginx
sudo gitlab-ctl status nginx
```

#### Unicorn
```shell
sudo gitlab-ctl start unicorn
sudo gitlab-ctl stop unicorn
sudo gitlab-ctl restart unicorn
sudo gitlab-ctl status unicorn
```

#### Sidekiq
```shell
sudo gitlab-ctl start sidekiq
sudo gitlab-ctl stop sidekiq
sudo gitlab-ctl restart sidekiq
sudo gitlab-ctl status sidekiq
```

#### PostgreSQL

```shell
sudo gitlab-ctl start postgresql 
sudo gitlab-ctl stop postgresql 
sudo gitlab-ctl restart postgresql 
sudo gitlab-ctl status postgresql 
```

#### Redis

```shell
sudo gitlab-ctl start redis
sudo gitlab-ctl stop redis
sudo gitlab-ctl restart redis
sudo gitlab-ctl status redis
```


#### 全局

等同于 GitLab 服务的效果，仅供参考

```shell
systemctl start gitlab-runsvdir.service
systemctl stop gitlab-runsvdir.service
systemctl status gitlab-runsvdir.service
systemctl restart gitlab-runsvdir.service
```

## 备份

GitLab 官方提供了详细的备份文档：[Backups](https://docs.gitlab.com/omnibus/settings/backups.html)

#### 快速备份方案

基于官方文档，我们建议的备份操作步骤如下：

1. 备份配置文件：通过 SFTP 工具将所有配置（*/etc/gitlab*）**压缩后**再完整的下载到本地
2. 备份整个 GitLab 系统：运行一条备份命令即可（[查看备份清单](https://docs.gitlab.com/ce/raketasks/backup_restore.html#creating-a-backup-of-the-gitlab-system)）
   ``` shell
   sudo gitlab-backup create
   ```
3. 将程序文件和数据库文件放到同一个文件夹，根据日期命名
4. 备份工作完成

## 恢复

## 升级

GitLab 是一个企业级软件，它所采用了大量的第三方开源组件，它的升级是一个系统化工程。  

所幸，GitLab 官方提供了一个稳妥可靠的 **逐级** [升级方案](https://docs.gitlab.com/omnibus/update/README.html#updating-using-the-official-repositories) 以弥补由于当前版本与最新版本之间的跨度太大儿无法升级的问题。

下面以 Gitlab 13.0.14 升级至 GitLab 14.1.6 为例，介绍详细的升级方案：  

1. 查询官方[升级路径](https://docs.gitlab.com/ee/update/index.html#upgrade-paths)文档，确认升级路径
   ```
   13.0.14 -> 13.1.11 -> 13.8.8 -> 13.12.10 -> 13.12.12 -> 14.0.11 -> 14.1.6
   ```

2. 可选步骤：检索当前升级库是否提供上述路径的各种版本（ce 可替换成 ee）
   ```
   # Ubuntu/Debian
   sudo apt-cache madison gitlab-ce

   # RHEL/CentOS 6 and 7
   yum --showduplicates list gitlab-ce

   # RHEL/CentOS 8
   dnf --showduplicates list gitlab-ce
   ```

3. 根据升级路径，一级一级逐渐向上升
   ```
   # Ubuntu/Debian
   sudo apt install gitlab-ce-<version>

   # RHEL/CentOS 6 and 7
   yum install gitlab-ce-<version>

   # RHEL/CentOS 8
   dnf install gitlab-ce-<version>
   ```

> 如果不填写版本号，例如：yum install gitlab-ce，即表明升级到最新版本。


#### CE升级到EE

GitLab Community Edition (CE) 升级到同版本的 GitLab Enterprise Edition 的操作步骤如下：

1. 获取当前CE的版本号
   ```
   # For Debian/Ubuntu
   sudo apt-cache policy gitlab-ce | grep Installed

   # For CentOS/RHEL
   sudo rpm -q gitlab-ce
   ```
2. 匹配EE版本号。例如获取的CE版本号为 *8.6.7-ce.0*，那么应该升级的EE版本号为：*8.6.7-ee.0*
3. Add the gitlab-ee Apt or Yum repository
   ```
   # For Debian/Ubuntu
   curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash

   # For CentOS/RHEL
   curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash
   ```
4. 安装 gitlab-ee 版本（同时系统自动卸载ce版）
   ```
   ........................................
   # For Debian/Ubuntu
   ........................................
   ## Make sure the repositories are up-to-date
   sudo apt-get update

   ## Install the package using the version you wrote down from step 1
   sudo apt-get install gitlab-ee=8.6.7-ee.0

   ## Reconfigure GitLab
   sudo gitlab-ctl reconfigure
   
   ........................................
   # For CentOS/RHEL
   ........................................
   ## Install the package using the version you wrote down from step 1
   sudo yum install gitlab-ee-8.6.7-ee.0.el7.x86_64

   ## Reconfigure GitLab
   sudo gitlab-ctl reconfigure
   ```
5. 在服务器的 GitLab 管理面板 (/admin/license/new) 上传许可证文件。
6. 确认 GitLab 按正常工作后，删除旧的社区版存储库
   ```
   # For Debian/Ubuntu
   sudo rm /etc/apt/sources.list.d/gitlab_gitlab-ce.list

   # For CentOS/RHEL
   sudo rm /etc/yum.repos.d/gitlab_gitlab-ce.repo
   ```
以上操作更详细说明请参考官方文档：[Updating Community Edition to Enterprise Edition](https://docs.gitlab.com/omnibus/update/README.html#updating-community-edition-to-enterprise-edition)


## 故障速查

我们收集使用 GitLab 过程中最常见的故障，供您参考：

#### 通过公司网络（固定IP）突然不能访问Gitlab？

问题场景：通过公司网络（固定IP）突然（以前可以访问）不能访问Gitlab，而通过自己的手机wifi可以访问。  
解决方案：原因是 GitLab 有一个rack-attack安全机制。某种条件下（例如：公司大量并发访问 GitLab）rack-attack安全将你的 IP 错误地拦截，导致了从此不能访问 GitLab，这个时候就需要对 [Gitlab 配置文件](/zh/stack-components.md#gitlab)进行修改

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-attachip-websoft9.png)


#### 502 错误
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-502-websoft9.png)

GitLab 所需内存最低为4G，若服务器配置太低会出现502错误。对于单核CPU的服务器，Unicorn and Sidekiq 服务启动最少需要一分钟，如果没有启动完成，也会报502错误

#### 数据库服务无法启动

数据库服务无法启动最常见的问题包括：磁盘空间不足，内存不足，配置文件错误。  
建议先通过命令进行排查  

```shell
# 查看磁盘空间
df -lh

# 查看内存使用
free -lh
```

## 常见问题

#### 没有购买 License 是否可以使用 GitLab 企业版？

如果安装了 GitLab 企业版，在没有导入 License 的情况下使用的是 社区版的所有功能。[GitLab-EE vs GitLab-CE](https://about.gitlab.com/install/ce-or-ee/)


#### GitLab支持多语言吗？

支持多语言（包含中文），通过控制台即可修改语言

#### GitLab数据库连接配置信息在哪里？

数据库配置信息在GitLab安装目录下的 */etc/gitlab/gitlab.rb* 中，[查阅安装目录路径](/zh/stack-components.md#gitlab)

#### 此预装包中的 PostgreSQL 是否可以远程访问？

不可以。默认缺情况下，GitLab 用户使用的是 Peer Authentication， 这意味着客户端只能以 PostgreSQL 所在主机上的Linux系统账号访问数据库， 无法远程访问。

#### 如果没有域名是否可以部署 GitLab？

可以，访问`http://服务器公网IP` 即可

#### 使用 SSH 的方式克隆GitLab的项目，默认端口是多少？

默认端口是22

#### 数据库密码是多少？

GitLab 使用的 Peer Authentication 方式连接 PostgreSQL, 没有设置数据库密码

#### 是否有可视化的数据库管理工具？

无

#### 是否可以修改 GitLab Repository 存储目录？

可以，参考官方文档 [Repository storage paths](https://docs.gitlab.com/ee/administration/repository_storage_paths.html)

