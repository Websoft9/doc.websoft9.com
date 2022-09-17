---
sidebar_position: 1
slug: /gitlab
tags:
  - Gitlab
  - DevOps
---

# 快速入门

[GitLab](https://github.com/gitlabhq/gitlabhq) 是一个完整的 DevOps 平台软件。 使用GitLab，您可以获得开箱即用的完整 CI/CD 工具链。

![GitLab devops](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-devopsall-websoft9.png)

部署 Websoft9 提供的 GitLab 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 GitLab 的 **[默认管理员账号和密码](./user/credentials)**  
4. 若想用域名访问  GitLab，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## GitLab 初始化向导

### 详细步骤

1. 本地电脑浏览器访问：*http://域名* 或 *http://服务器公网IP*，进入初始化页面 
   ![GitLab 登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-login-websoft9.png)

2. 输入账号密码，进入 GitLab 控制台
    ```
    # 用户:root，密码：通过脚本查看
    sudo docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password    
    ```
   ![GitLab 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-backend-websoft9.png)

3. 进入管理设置面板（Admin Area）  
   ![GitLab 管理设置面板](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-adminpanel-websoft9.png)

4. 依次打开：【User Settings】>【Preferences】设置语言（支持中文）
   ![GitLab 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-setlanguage-websoft9.png)

5. 依次打开：【User Settings】>【SSH key】设置秘钥
   ![GitLab SSH key](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-sshkey-websoft9.png)

6. 如果你部署的是 GitLab-EE（企业版），通过：【管理中心】>【许可证】导入后，**试用**或**启用**企业版
   ![Gitlab 导入授权](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlabee-license-websoft9.png)

7. [设置 GitLab 仓库地址](#setrepourl)

> 需要了解更多 GitLab 的使用，请参考官方文档：[GitLab Documentation](https://docs.gitlab.com/omnibus/README.html)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**GitLab能打开，但总是出现 502 错误？**  

参阅：[此处](./gitlab/admin#502)

**GitLab 每次启动需等1分钟才能使用？**  

参阅：[此处](./gitlab/admin#502)

## GitLab 使用入门

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

## 常用操作

### 设置 GitLab 仓库地址{#setrepourl}

在初始化之前的 **[准备](#prepare)** 环节，如果您已经完成 **[域名五步设置](./administrator/domain_step)**，GitLab 可以域名访问，但是 GitLab 仓库的网址还不是用户自己的域名。

因此，还需要参考下面的步骤[设置 GitLab 仓库地址](https://docs.gitlab.com/omnibus/settings/configuration.html#configuring-the-external-url-for-gitlab)：

1. 通过 SSH 或 SFTP 登录云服务器
2. 修改 [GitLab 配置文件](#path)，将 **external_url** 项的值 *http://gitlab.example.com* 修改为你的域名
   ```text
   external_url "http://gitlab.example.com" # 改为自定义域名
   ...
   ``` 
3. 保存配置文件，重启下面的服务
   ```
   sudo gitlab-ctl reconfigure
   ```

### 设置 GitLab 仓库的 HTTPS{#setrepohttps}

GitLab 仓库的 HTTPS 不等同于 GitLab 自身的 HTTPS，前置还需额外设置：[Enabling HTTPS](https://docs.gitlab.com/omnibus/settings/nginx.html#enable-https)

### 配置 SMTP

1. 参考 GitLab 官方提供的 [SMTP Setting 范例](https://docs.gitlab.com/omnibus/settings/smtp.html) ，准备好 SMTP 参数

2. 通过 SFTP 连接服务器，修改 GitLab 配置文件：*/etc/gitlab/gitlab.rb*
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
3. 重启服务后生效
   ```
   sudo gitlab-ctl reconfigure
   ```

### 重置管理员密码

忘记管理员密码时，请参考如下方案重置密码（[方案来源](https://docs.gitlab.com/13.11/ee/security/reset_user_password.html)）：  

1. 使用 SSH 登陆 GitLab 服务器
2. 输入 `gitlab-rails console` 命令，根据提示完成后续步骤
   ```

   $ gitlab-rails console     //进入控制台命令
   --------------------------------------------------------------------------------
    Ruby:         ruby 2.7.2p137 (2020-10-01 revision 5445e04352) [x86_64-linux]
    GitLab:       13.8.4 (9fb9cbf50c3) FOSS
    GitLab Shell: 13.15.1
    PostgreSQL:   12.5
   --------------------------------------------------------------------------------

   Loading production environment (Rails 6.0.3.4)
   irb(main):001:0>
   irb(main):002:0> user = User.find_by_username 'root'  //找到用户，默认管理员用户名为 root
   => #<User id:1 @root>
   irb(main):003:0> user.password='Websoft9'   //修改密码
   => "Websoft9"
   irb(main):004:0> user.password_confirmation='Websoft9'  //二次确认密码
   => "Websoft9"
   irb(main):006:0>  user.save! //保存更改
   Enqueued ActionMailer::MailDeliveryJob (Job ID: 3f4ac447-9869-412a-9b5a-988c06cf          eaa2) to Sidekiq(mailers) with arguments: "DeviseMailer", "password_change_by_ad          min", "deliver_now", {:args=>[#<GlobalID:0x00007fb7e5337990 @uri=#<URI::GID gid:          //gitlab/User/1>>]}
   => true
   irb(main):007:0>

   ```

## 参数

GitLab 应用中包含 Docker, Portainer 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

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

通过运行 `docker ps`，查看 GitLab 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE                         COMMAND                  CREATED       STATUS                 PORTS                                                                               NAMES
c5b22639c668   gitlab/gitlab-ce:latest       "/assets/wrapper"        2 hours ago   Up 2 hours (healthy)   443/tcp, 0.0.0.0:23->22/tcp, :::23->22/tcp, 0.0.0.0:9001->80/tcp, :::9001->80/tcp   gitlab
49995b282a20   gitlab/gitlab-runner:latest   "/usr/bin/dumb-init …"   2 hours ago   Up 2 hours                                                                                                 gitlab-runner

```

### 路径{#path}

GitLab 安装目录： */data/apps/gitlab*   
GitLab 数据目录： */data/apps/gitlab/data/gitlab_data*  
GitLab 日志目录： */data/apps/gitlab/data/gitlab_logs*  

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到： 

暂无特殊端口

### 版本

```shell
docker exec -i gitlab head -n+1 /opt/gitlab/version-manifest.txt
```

### 服务

```shell
sudo docker start | stop | restart | stats gitlab
sudo docker start | stop | restart | stats gitlab-runner
```

### 命令行

GitLab 提供了命令行工具 `gitlab-ctl` 用于全面管理和配置 GitLab

```
$ docker exec -it gitlab gitlab-ctl -h

I don't know that command.
omnibus-ctl: command (subcommand)
check-config
  Check if there are any configuration in gitlab.rb that is removed in specified version
deploy-page
  Put up the deploy page
diff-config
  Compare the user configuration with package available configuration
get-redis-master
  Get connection details to Redis master
prometheus-upgrade
  Upgrade the Prometheus data to the latest supported version
remove-accounts
  Delete *all* users and groups used by this package
reset-grafana
  Reset Grafana instance to its initial state by removing the data directory
set-grafana-password
  Reset admin password for Grafana
upgrade
  Run migrations after a package upgrade
upgrade-check
  Check if the upgrade is acceptable
General Commands:
  cleanse
    Delete *all* gitlab data, and start from scratch.
  help
    Print this help message.
  reconfigure
    Reconfigure the application.
  show-config
    Show the configuration that would be generated by reconfigure.
  uninstall
    Kill all processes and uninstall the process supervisor (data will be preserved).
Service Management Commands:
  graceful-kill
    Attempt a graceful stop, then SIGKILL the entire process group.
  hup
    Send the services a HUP.
  int
    Send the services an INT.
  kill
    Send the services a KILL.
  once
    Start the services if they are down. Do not restart them if they stop.
  restart
    Stop the services if they are running, then start them again.
  service-list
    List all the services (enabled services appear with a *.)
  start
    Start services if they are down, and restart them if they stop.
  status
    Show the status of all the services.
  stop
    Stop the services, and do not restart them.
  tail
    Watch the service logs of all enabled services.
  term
    Send the services a TERM.
  usr1
    Send the services a USR1.
  usr2
    Send the services a USR2.
Gitlab Geo Commands:
  geo
    Interact with Geo
  geo-replication-pause
    Replication Process
  geo-replication-resume
    Replication Process
  promote-db
    Promote secondary PostgreSQL database
  promote-to-primary-node
    Promote to primary node
  promotion-preflight-checks
    Run preflight checks for promotion to primary node
  replicate-geo-database
    Replicate Geo database
  set-geo-primary-node
    Make this node the Geo primary
Pgbouncer Commands:
  pgb-console
    Connect to the pgbouncer console
  pgb-kill
    Send the "resume" command to pgbouncer
  pgb-notify
    Notify pgbouncer of an update to its database
  pgb-resume
    Send the "resume" command to pgbouncer
  pgb-suspend
    Send the "suspend" command to pgbouncer
Database Commands:
  get-postgresql-primary
    Get connection details to the PostgreSQL primary
  patroni
    Interact with Patroni
  pg-password-md5
    Generate MD5 Hash of user password in PostgreSQL format
  pg-upgrade
    Upgrade the PostgreSQL DB to the latest supported version
  revert-pg-upgrade
    Run this to revert to the previous version of the database
  set-replication-password
    Set database replication password
  write-pgpass
    Write a pgpass file for the specified user
Consul Commands:
  consul
    Interact with the gitlab-consul cluster
Container Registry Commands:
  registry-garbage-collect
    Run Container Registry garbage collection.
Let's Encrypt Commands:
  renew-le-certs
    Renew the existing Let's Encrypt certificates
Gitaly Commands:
  praefect
    Interact with Gitaly cluster
Backup Commands:
  backup-etc
    Backup GitLab configuration [options]
```

### API

GitLab 提供[多种 API](https://docs.gitlab.com/ee/api/) 方式，包括：REST API, SCIM API, GraphQL API

```
curl "https://gitlab.example.com/api/v4/projects"
```
