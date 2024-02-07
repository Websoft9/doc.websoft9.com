---
title: GitLab
slug: /gitlab
tags:
  - DevOps
  - CD/CI
  - 持续集成
  - 代码仓库
  - 开发全栈
---

import Meta from './_include/gitlab.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 GitLab 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 本地电脑浏览器访问后，进入初始化页面 
   ![GitLab 登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-login-websoft9.png)

  > 服务器启动后需要 1-2 分钟才显示 Gitlab 页面。若页面未显示时重启服务器，会导致密码无法登陆

2. 输入账号密码，进入 GitLab 控制台
   ![GitLab 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-backend-websoft9.png)

3. 进入管理设置面板（Admin Area）  
   ![GitLab 管理设置面板](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-adminpanel-websoft9.png)

4. 语言设置：【User Settings】>【Preferences】，设置自己喜欢的语言（包含中文）
   ![GitLab 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-setlanguage-websoft9.png)

5. SSH key 设置：【User Settings】>【SSH key】
   ![GitLab SSH key](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-sshkey-websoft9.png)

6. 如果你部署的是 GitLab-EE（企业版），通过：【管理中心】>【许可证】导入后，**试用**或**启用**企业版
   ![Gitlab 导入授权](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlabee-license-websoft9.png)

7. [设置](#setrepourl) GitLab 仓库地址

### 功能一览

下面介绍 Gitlab 在团队管理、权限管理、代码管理等方面的应用。

1. 项目管理：管理员新建项目，并进行项目初始化、添加开发分支 dev ，不对开发人员开放主分支 master

   创建 Websoft9-Site1 项目
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-add-project-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-add-project1-websoft9.png)

   初始化项目，添加自述文件 README.md 和 index.html 页面，并提交
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-add-file-websoft9.png)

   新建开发分支 dev
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-add-branch-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-create-branch-websoft9.png)

3. 成员管理：团队成员在登录页面注册账号，管理员在后台激活用户，并在项目成员中邀请用户，配置权限。用户须激活后才能登录系统。

   成员注册
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-register-websoft9.png)

   管理员激活注册用户
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-user-manager-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-user-manager1-websoft9.png)

   管理员邀请用户加入项目组，分配权限
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-add-member-websoft9.png)

4. 代码管理： 
   项目成员负责index.html页面开发， 通过 git clone 项目到本地 ，在vs code 开发。
   打开 Git Base 工具，通过 git clone 将项目克隆本地
  
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-clone-websoft9.png)

   在 vs code 中打开项目，编辑index.html

   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-vscode-websoft9.png)

   编辑完成，提交本地代码到服务器。开发账号登录 gitlab ，查看更新并创建合并请求

   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-pull-request-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-merge-request-websoft9.png)
   
   管理员登录 gitlab 合并请求

   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-merge-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-merge1-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-merge2-websoft9.png)

### 设置 GitLab 仓库地址{#setrepourl}

仓库地址不同于 GitLab 的控制台地址。参考：[Configure External URL](https://docs.gitlab.com/omnibus/settings/configuration.html#configuring-the-external-url-for-gitlab) 配置 **external_url** 项的值。

## 企业版

Websoft9 是 Gitlab（包括极狐） 的合作伙伴，通过 Websoft9 购买 Gitlab ，可以获得：

- 更优惠的折扣
- 更多的技术支持范围
- 更全面的其他 DevOpS 集成服务

### 设置极狐中文  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/jh-gitlab-setlanguge-websoft9.png)

### CE 升级到 EE

修改镜像标签，即可无缝升级到 EE。   

详情参考官方文档：[Updating Community Edition to Enterprise Edition](https://docs.gitlab.com/omnibus/update/README.html#updating-community-edition-to-enterprise-edition)

### EE 降级到 CE

如果安装了 GitLab 企业版，在没有导入 License 的情况下使用的是 社区版的所有功能。  

[GitLab-EE vs GitLab-CE](https://about.gitlab.com/install/ce-or-ee/)



## 配置选项{#configs}

- 命令行工具：`gitlab-ctl`
- [API](https://docs.gitlab.com/ee/api/) ：`curl "https://gitlab.example.com/api/v4/projects"`
- 配置文件：/path/gitlab.rb
- 多语言（✅）
- SMTP（✅）：配置文件中相关值如下
   ```
   gitlab_rails['smtp_enable'] = true
   gitlab_rails['smtp_address'] = "smtp.exmail.qq.com"
   gitlab_rails['smtp_port'] = 465
   gitlab_rails['smtp_user_name'] = "xxxx@xx.com"
   gitlab_rails['smtp_password'] = "password"
   gitlab_rails['smtp_authentication'] = "login"
   gitlab_rails['smtp_enable_starttls_auto'] = true
   gitlab_rails['smtp_tls'] = true
   gitlab_rails['gitlab_email_from'] = 'xxxx@xx.com'
   ```
- 配置文件：*/etc/gitlab/gitlab.rb*


## 管理维护{#administrator}

### 架构与组件

下面是一个简化的架构图，可用于了解 GitLab 的组件架构。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/architecture_simplified.png)

-nginx：静态web服务器。  
-gitlab-shell：用于处理Git命令和修改authorized keys列表。  
-gitlab-workhorse: 轻量级的反向代理服务器。  
-logrotate：日志文件管理工具。  
-postgresql：数据库。  
-redis：缓存数据库。  
-sidekiq：用于在后台执行队列任务（异步执行）。  
-unicorn：An HTTP server for Rack applications，GitLab Rails应用是托管在这个服务器上面的。

GitLab 包含数十种组件([查看](https://docs.gitlab.com/ee/development/architecture.html#component-list))，通过容器内路径 */opt/gitlab/version-manifest.txt* 查看所有组件名称和版本

### GitLab Runner

GitLab Runner 是额外的技术组件，需自行部署

### 设置 GitLab 仓库地址{#setrepourl}

仓库地址不同于 GitLab 的控制台地址。参考：[Configure External URL](https://docs.gitlab.com/omnibus/settings/configuration.html#configuring-the-external-url-for-gitlab) 配置 **external_url** 项的值。

### 设置 GitLab 仓库的 HTTPS{#setrepohttps}

GitLab 仓库的 HTTPS 不等同于 GitLab 自身的 HTTPS，前置还需额外设置：[Enabling HTTPS](https://docs.gitlab.com/omnibus/settings/nginx.html#enable-https)

### 重置管理员密码

忘记管理员密码时，请参考（[reset_user_password](https://docs.gitlab.com/13.11/ee/security/reset_user_password.html)）：  

1. 进入 GitLab 容器的 exec 模式
2. 输入 `gitlab-rails console` 命令，根据提示完成后续步骤

### 修改仓库目录

参考：[Repository storage paths](https://docs.gitlab.com/ee/administration/repository_storage_paths.html)

## 故障

#### 公司固定 IP 突然不能访问 Gitlab？

**现象描述**：通过公司网络（固定IP）突然（以前可以访问）不能访问Gitlab，而通过自己的手机wifi可以访问。   

**原因分析**：GitLab 有一个rack-attack安全机制。某种条件下（例如：公司大量并发访问 GitLab）rack-attack安全将你的 IP 错误地拦截，导致了从此不能访问 GitLab   

**解决方案**：修改 [Gitlab 配置文件](../gitlab#path) 相关项

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-attachip-websoft9.png)


#### 访问 GitLab 出现 502 错误？{#502}

**现象描述**：首次访问 GitLab 或 访问人数较多时，GitLab 出现 502 错误？   
![](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-502-websoft9.png)

**原因分析**：GitLab 所需内存最低为4G，若服务器配置不足，100% 会出现 502 错误。另外，对于单核CPU的服务器，Unicorn and Sidekiq 服务启动最少需要一分钟，如果没有启动完成，也会报502错误   

**解决方案**：升级服务器配置

#### 无法网络连接容器中的 PostgreSQL？

这种情况是正常的。  

默认安装下，GitLab 使用 Peer Authentication 与 PostgreSQL 通讯。这意味着客户端只能以 PostgreSQL 所在主机上的 Linux 系统账号访问数据库，无法远程访问。

