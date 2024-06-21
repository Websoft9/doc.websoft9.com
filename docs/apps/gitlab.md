---
title: GitLab
slug: /gitlab
tags:
  - DevOps
  - CD/CI
  - 持续集成
  - 代码仓库
  - 开发全栈
  - 极狐
---

import Meta from './_include/gitlab.md';

<Meta name="meta" />

## 入门指南{#guide}

### 验证安装{#wizard}

Websoft9 控制台安装 GitLab 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 本地电脑浏览器访问后，进入登陆页面（首次加载需2-3分钟，此时切勿重启，否则导致登陆密码无效）
   ![GitLab 登录](./assets/gitlab-login-websoft9.png)

2. 输入账号密码，进入 GitLab 控制台
   ![GitLab 后台](./assets/gitlab-backend-websoft9.png)

3. 开始设置语言，新建仓库，新建用户等操作

### 设置 GitLab 仓库地址{#setrepourl}

仓库地址不同于 GitLab 的控制台地址。  

参考：[Configure External URL](https://docs.gitlab.com/omnibus/settings/configuration.html#configuring-the-external-url-for-gitlab) 配置 **external_url** 项的值。

## 企业版

#### 为什么与 Websoft9 合作？{#why}

Websoft9 是 Gitlab（包括[极狐](#jihu)） 的合作伙伴，通过 Websoft9 购买 GitLab ，可以获得：

- 更优惠的折扣
- 更多的技术支持范围
- 更全面 DevOps 技术集成与咨询
- 提供极狐企业版 2 个月的试用授权（极狐官方授权 Websoft9 在公有云上提供企业版支持）

#### 关于极狐 Gitlab{#jihu}

极狐是 GitLab 在中国控股的独立经营运作的公司，向用户提供本地化的 GitLab 产品与服务：

- 极狐(GitLab) 包含基础版、企业版和旗舰版，其中基础版可以免费试用
- 极狐(GitLab) 的上游仓库为 GitLab，并保持较高频率的同步
- 极狐(GitLab) 的 SaaS 服务基于中国本地基础设施，与 GitLab 全球 SaaS 完全独立
- 极狐(GitLab) 的功能和操作与 GitLab 一样，只是增加了部分本地化功能，专为帮助本地用户体验而量身定制

### 导入企业版 License{#lic}

1. 准备所需的许可证

   - **极狐 GitLab 许可证**：可以通过 [这个链接](https://websoft9.github.io/docker-library/apps/jihu/src/gitlab.license) 下载。
   - **GitLab 许可证**：需要自行申请。您可以访问 [GitLab 官方网站](https://about.gitlab.com/pricing/) 进行申请。
     
2. 登录 GitLab，通过：**管理中心 > 许可证** 导入 License
   ![Gitlab 导入授权](./assets/gitlabee-license-websoft9.png)

### CE 与 EE 的转换

GitLab CE（社区版）和 GitLab EE（企业版）之间的转换[关系](https://about.gitlab.com/install/ce-or-ee)：

- 如果安装了 GitLab EE，试用期结束后，EE 功能被禁用，但仍然 CE 功能可用
- 如果安装了 GitLab CE，需修改镜像标签为 EE，重建容器后无缝[升级到 EE](https://docs.gitlab.com/omnibus/update/README.html#updating-community-edition-to-enterprise-editio)

## 配置选项{#configs}

- 命令行工具：`gitlab-ctl`
- [API](https://docs.gitlab.com/ee/api/) ：`curl "https://gitlab.example.com/api/v4/projects"`
- 多语言（✅）：后台【User Settings】>【Preferences】设置语言
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
- 配置文件（已挂载）：*/etc/gitlab/gitlab.rb*
- [GitLab 架构](https://docs.gitlab.com/ee/development/architecture.html)：GitLab 包含[数十种组件](https://docs.gitlab.com/ee/development/architecture.html#component-list)，可通过 */opt/gitlab/version-manifest.txt* 查看

- GitLab Runner：GitLab Runner 是额外的技术组件，需自行部署

## 管理维护{#administrator}

- **重置管理员密码**：进入容器的命令模式，运行 `gitlab-rails console` 命令[重置密码](https://docs.gitlab.com/13.11/ee/security/reset_user_password.html)
- **修改仓库目录**：[Repository storage paths](https://docs.gitlab.com/ee/administration/repository_storage_paths.html)

## 故障

#### 公司固定 IP 突然不能访问 Gitlab？

**现象描述**：通过公司网络（固定IP）突然（以前可以访问）不能访问Gitlab，而通过自己的手机wifi可以访问。   

**原因分析**：GitLab 有一个 rack-attack 安全机制。某种条件下（例如：公司大量并发访问 GitLab）rack-attack 安全将你的 IP 错误地拦截，导致了从此不能访问 GitLab   

**解决方案**：修改 [Gitlab 配置文件](../gitlab#path) 的 rack-attack 相关项


#### 访问 GitLab 出现 502 错误？{#502}

**现象描述**：首次访问 GitLab 或 访问人数较多时，GitLab 出现 502 错误？   

**原因分析**：GitLab 所需内存最低为4G，若服务器配置不足，100% 会出现 502 错误。另外，对于单核CPU的服务器，Unicorn and Sidekiq 服务启动最少需要一分钟，如果没有启动完成，也会报502错误   

**解决方案**：升级服务器配置

#### 无法连接 PostgreSQL？

**现象描述**：使用数据库客户端，无法连接 GitLab 容器中的 PostgreSQL？ 

**原因分析**：默认安装下，GitLab 使用 Peer Authentication 与 PostgreSQL 通讯。这意味着客户端只能以 PostgreSQL 所在主机上的 Linux 系统账号访问数据库，无法远程访问。
