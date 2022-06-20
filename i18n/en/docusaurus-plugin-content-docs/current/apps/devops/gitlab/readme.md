---
sidebar_position: 1
slug: /gitlab
tags:
  - Gitlab
  - DevOps
---

# GitLab Getting Started

[GitLab](https://github.com/gitlabhq/gitlabhq) is a complete DevOps platform. With GitLab, you get a complete CI/CD toolchain out-of-the-box. One interface. One conversation. One permission model. Thousands of features. You'll be amazed at everything GitLab can do today.  

![GitLab devops](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-devopsall-websoft9.png)

If you have installed Websoft9 GitLab, the following steps is for your quick start  

## Preparation{#prepare}

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Connect your Server and get **[default username and password](./user/credentials)** of GitLab
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for GitLab

## GitLab Getting Started

### Steps for you

1. Using local browser to visit the URL http://DNS or http://Server's Internet IP, login to your GitLab([Don't have password?](./user/credentials))
   ![GitLab Login](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-login-websoft9.png)

2. Go to GitLab dashboard to start use it 
   ![GitLab dashboard](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-backend-websoft9.png)

3. Go to GitLab Admin Area to configure it
   ![GitLab admin area](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-adminpanel-websoft9.png)

4. Open: **User Settings** > **Preferences** to set your language
   ![GitLab language](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-setlanguage-websoft9.png)

5. Open: **User Settings** > **SSH key** to set your keys
   ![GitLab SSH key](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-sshkey-websoft9.png)

6. If you have installed GitLab-EE, go to 【Admin Area】>【License】, import your license or try it
   ![Gitlab license](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlabee-license-websoft9.png)

> More useful GitLab guide, please refer to [GitLab Documentation](https://docs.gitlab.com/omnibus/README.html)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**GitLab interface 502 error?**  

Refer to：[here](./gitlab/admin#502)

**GitLab need long time to start?**  

Refer to：[here](./gitlab/admin#502)

## GitLab QuickStart

This task【Manage team, member and code in GitLab】 is for your GitLab QuickStart

1. Domain binding, the complete real path needs to be used in the subsequent project management. After Gitlab is installed, the default domain name is http://gitlab.example.com, you need to modify it to your existing domain name in the configuration file, or modify it to IP to access http://IP. Reference[Domain binding](http://support.websoft9.com/docs/gitlab/solution-more.html#domain-binding)。

2. Project management: The administrator creates a new project, initializes the project, adds a development branch "dev", and does not open the master branch master to developers

   Create project: Websoft9-Site1 
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-add-project-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-add-project1-websoft9.png)

   Initialize the project, add README.md and index.html pages, and submit
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-add-file-websoft9.png)

   New development branch dev
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-add-branch-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-create-branch-websoft9.png)

3. Member management: team members register an account on the login page. The administrator activates users in the system, and then invites users among project members and configures permissions. The user must be activated to log in to the system.

   User registration
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-register-websoft9.png)

   Administrator activates registered users
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-user-manager1-websoft9.png)

   The administrator invites users to join the project group and assigns rights
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-add-member-websoft9.png)

4. Code management:
   Project members are responsible for the development of the "index.html" page, through git clone the project to the local, development in vs code.
   Use the "Git Base" and clone the project locally via "git clone"
  
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-clone-websoft9.png)

   Use vs code to edit index.html locally, and then submit the local code to the server.
   Log in to gitlab with your development account, view updates and create a merge request

   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-pull-request-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-merge-request-websoft9.png)
   
   Administrator login Gitlab merge request

   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-merge-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-merge1-websoft9.png)
   ![gitlab](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-merge2-websoft9.png)

## Gitlab Setup

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

### Configure SMTP

Sending mail is a common feature for GitLab. After a large number of user practice feedback, only one way is recommended, that is, using the **third-party STMP service** to send the email.

> Do not try to install **Sendmail** or other Mail server software on your Cloud Server for sending mail, because it is very difficulty in maintenance.

Follow is the sample using **SendGrid's SMTP Service** to configure sending mail for GitLab:

1. Log in SendGrid console, prepare your SMTP settings like the follow sample
   ```
   SMTP host: smtp.sendgrid.net
   SMTP port: 25 or 587 for unencrypted/TLS email, 465 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9smpt
   SMTP password: #fdfwwBJ8f    
   ```
2. Use SSH or SFTP to connect Server, modify the GitLab configuration file: */etc/gitlab/gitlab.rb*
   ```
   gitlab_rails['smtp_enable'] = true
   gitlab_rails['smtp_address'] = "smtp.sendgrid.net"
   gitlab_rails['smtp_port'] = 587
   gitlab_rails['smtp_user_name'] = "a_sendgrid_crendential"
   gitlab_rails['smtp_password'] = "a_sendgrid_password"
   gitlab_rails['smtp_domain'] = "smtp.sendgrid.net"
   gitlab_rails['smtp_authentication'] = "login"
   gitlab_rails['smtp_enable_starttls_auto'] = true
   gitlab_rails['smtp_tls'] = false
   ```
4. Restart Service
   ```
   sudo gitlab-ctl reconfigure
   ```

GitLab provides configuration methods for dozens of different SMTP service providers, please refer to the official documentation:[SMTP settings](https://docs.gitlab.com/omnibus/settings/smtp.html)

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

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage GitLab 

下面是一个简化的架构图，可用于了解 GitLab 的组件架构。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/architecture_simplified.png)

-nginx：静态web服务器。  
-gitlab-shell：用于处理Git命令和修改authorized keys列表。  
-gitlab-workhorse: 轻量级的反向代理服务器。  
-logrotate：logs file管理工具。  
-postgresql：数据库。  
-redis：缓存数据库。  
-sidekiq：用于在后台执行队列任务（异步执行）。  
-unicorn：An HTTP server for Rack applications，GitLab Rails应用是托管在这个服务器上面的。

GitLab 包含数十种组件([查看](https://docs.gitlab.com/ee/development/architecture.html#component-list))，通过 */opt/gitlab/version-manifest.txt* 查看服务器上所有组件名称和版本

### Path{#path}

##### GitLab

GitLab 配置文件： */etc/gitlab/gitlab.rb*    
GitLab 及所有组件配置： */opt/gitlab*  
GitLab Repository 存储目录： */var/opt/gitlab/git-data*  
GitLab 备份目录： */var/opt/gitlab/backups*

##### Unicorn

Unicorn 日志目录： */var/log/gitlab/unicorn*  

##### Sidekiq

Unicorn 日志目录： */var/log/gitlab/sidekiq*

##### Nginx

Nginx 日志目录: */var/log/gitlab/nginx*  
Nginx 配置文件: */var/opt/gitlab/nginx/conf/nginx.conf*  
GitLab 核心 Nginx 配置文件:  */var/opt/gitlab/nginx/conf/gitlab-http.conf*

##### PostgreSQL

PostgreSQL installation directory： */var/opt/gitlab/postgresql*  
PostgreSQL 日志目录: */var/log/gitlab/postgresql*   
PostgreSQL-Exporter 日志目录： */var/log/gitlab/postgres-exporter*  
PostgreSQL 数据目录： */var/opt/gitlab/postgresql/data*

##### Redis

Redis installation directory： */var/opt/gitlab/redis*  
Redis 日志目录： */var/log/gitlab/redis*

### Port{#port}

暂无特殊端口

### Version

```shell
gitlab-ctl status  | grep gitlab-workhorse
```

### Service

GitLab 提供的（[gitlab-ctl ](https://docs.gitlab.com/omnibus/maintenance/README.html#get-service-status)）可以很方便的管理各个组件的服务：

```shell
sudo gitlab-ctl start | stop | restart | status reconfigure nginx
sudo gitlab-ctl start | stop | restart | status reconfigure unicorn
sudo gitlab-ctl start | stop | restart | status reconfigure sidekiq
sudo gitlab-ctl start | stop | restart | status reconfigure postgresql
sudo gitlab-ctl start | stop | restart | status reconfigure redis
```

GitLab 自身的启动/停止，是通过 Systemd 服务来管理的：

```shell
systemctl start | stop | restart | status gitlab-runsvdir.service
```

### CLI

GitLab 提供了命令行工具 `gitlab-ctl` 用于全面管理和配置 GitLab

```
$ gitlab-ctl -h

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