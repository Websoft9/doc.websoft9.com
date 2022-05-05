---
sidebar_position: 3
slug: /gitlab/admin
tags:
  - Gitlab
  - DevOps
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### 备份与恢复

基于 GitLab [官方备份文档](https://docs.gitlab.com/omnibus/settings/backups.html)，我们建议的备份操作步骤如下：

1. 备份 GitLab 配置文件：通过 SFTP 工具将所有配置（*/etc/gitlab*）目录 **压缩后**再下载到本地电脑
2. 备份 GitLab 系统：运行一条备份命令即可（[查看备份清单](https://docs.gitlab.com/ce/raketasks/backup_restore.html#creating-a-backup-of-the-gitlab-system)）
   ``` shell
   sudo gitlab-backup create
   ```

### 升级

GitLab 是一个企业级软件，它所采用了大量的第三方开源组件，它的升级是一个系统化工程。  

#### 逐级升级

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


#### CE 升级到 EE

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


## 故障排除

除以下列出的 GitLab 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。  

### 公司固定 IP 突然不能访问 Gitlab？

**现象描述**：通过公司网络（固定IP）突然（以前可以访问）不能访问Gitlab，而通过自己的手机wifi可以访问。   

**原因分析**：GitLab 有一个rack-attack安全机制。某种条件下（例如：公司大量并发访问 GitLab）rack-attack安全将你的 IP 错误地拦截，导致了从此不能访问 GitLab   

**解决方案**：修改 [Gitlab 配置文件](../gitlab#path) 相关项

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-attachip-websoft9.png)


### 访问 GitLab 出现 502 错误？{#502}

**现象描述**：首次访问 GitLab 或 访问人数较多时，GitLab 出现 502 错误？   
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-502-websoft9.png)

**原因分析**：GitLab 所需内存最低为4G，若服务器配置不足，100% 会出现 502 错误。另外，对于单核CPU的服务器，Unicorn and Sidekiq 服务启动最少需要一分钟，如果没有启动完成，也会报502错误   

**解决方案**：升级服务器配置




## 问题解答

#### 没有买 License 可使用 GitLab 企业版吗？

如果安装了 GitLab 企业版，在没有导入 License 的情况下使用的是 社区版的所有功能。[GitLab-EE vs GitLab-CE](https://about.gitlab.com/install/ce-or-ee/)

#### 采用哪种方式安装 GitLab？

本项目采用 [Omnibus GitLab包](https://gitlab.com/gitlab-org/omnibus-gitlab) 的安装方式。Omnibus GitLab 是官方推荐的一种安装方法，它自带了 GitLab 所需的所有组件和服务，并可以省去繁琐的配置，同时它自带 CLI 工具，便于 GitLab 升级和维护。

#### GitLab 支持多语言吗？

支持多语言（包含中文），通过控制台即可修改语言

#### GitLab 数据库连接配置信息在哪里？

存储在 [Gilab 配置文件](../gitlab#path)中

#### 应用中的 PostgreSQL 是否可以远程访问？

不可以。默认安装下，GitLab 使用 Peer Authentication 与 PostgreSQL 通讯。这意味着客户端只能以 PostgreSQL 所在主机上的 Linux 系统账号访问数据库，无法远程访问。

#### 使用 SSH 的克隆项目时端口多少？

22

#### 为什么没有提供数据库密码？

GitLab 使用的 Peer Authentication 方式连接 PostgreSQL, 没有设置数据库密码

#### 是否提供了数据库管理工具？

无

#### 可否修改 GitLab Repository 存储目录？

可以，参考：[Repository storage paths](https://docs.gitlab.com/ee/administration/repository_storage_paths.html)