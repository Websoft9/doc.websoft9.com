---
sidebar_position: 1
slug: /gitlab
tags:
  - Gitlab
  - DevOps
---

# 快速入门

[GitLab](https://github.com/gitlabhq/gitlabhq) 最初是一个代码仓库系统，现在已经发展成为一个完整的 DevOps 平台软件（参考下图）。 使用GitLab，您可以获得开箱即用的完整CI/CD工具链。 一个界面、一个对话、 一个权限模型，成千上万的功能。

![GitLab devops](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-devopsall-websoft9.png)

在云服务器上部署 GitLab 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 若想用域名访问 GitLab，请先到 **域名控制台** 完成一个域名解析

## 账号密码

通过**SSH**连接云服务器，运行 `sudo cat /credentials/password.txt` 命令，查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### GitLab

* 管理员账号: `admin`
* 管理员密码: `admin` 或 存储在您的服务器中的文件中 */credentials/password.txt*  

### PostgreSQL

Omnibus GitLab 使用的是 Peer 认证模式，即从操作系统获得客户端的操作系统用户，并且检查它是否匹配被请求的数据库用户名，这只对本地连接可用。

## GitLab 安装向导

1. 登陆系统（[不知道账号密码？](/zh/stack-accounts.md#GitLab)） 
   ![GitLab 登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-login-websoft9.png)

2. 进入 GitLab 控制台，开始使用系统 
   ![GitLab 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-backend-websoft9.png)

3. 进入管理设置面板（Admin Area）
   ![GitLab 管理设置面板](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-adminpanel-websoft9.png)

4. 通过：【User Settings】>【Preferences】设置语言，目前已经支持中文
   ![GitLab 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-setlanguage-websoft9.png)

5. 通过：【User Settings】>【SSH key】设置秘钥
   ![GitLab SSH key](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-sshkey-websoft9.png)

6. 如果你部署的是 GitLab-EE（企业版），请打开：【管理中心】>【许可证】，然后**试用**或**启用**企业版
   ![Gitlab 导入授权](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlabee-license-websoft9.png)

> 需要了解更多 GitLab 的使用和配置，请参考官方文档：[GitLab Documentation](https://docs.gitlab.com/omnibus/README.html)

## GitLab 入门向导

下面以一个项目的团队开发为例，介绍 Gitlab 在团队管理、权限管理、代码管理等方面的应用。

1. 修改域名，在后面的项目管理中需要用到完整的项目路径。Gitlab 安装完成后，默认的域名是 http://gitlab.example.com，需要在配置文件中修改成你已有的域名，或修改为 IP 访问 http://IP。 参考[域名修改](http://support.websoft9.com/docs/gitlab/zh/solution-more.html#%E5%9F%9F%E5%90%8D%E7%BB%91%E5%AE%9A)。

2. 项目管理：管理员新建项目，并进行项目初始化、添加开发分支 dev ，不对开发人员开放主分支 master

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

### 域名绑定

绑定域名的前置条件是：GitLab已经可以通过解析后的域名访问。  

虽然如此，从服务器安全和后续维护考量，**域名绑定**步骤不可省却  

GitLab 域名绑定操作步骤（[官方文档](https://docs.gitlab.com/omnibus/settings/configuration.html#configuring-the-external-url-for-gitlab)）：

1. 通过 SSH 或 SFTP 登录云服务器
2. 修改 [GitLab 配置文件](/zh/stack-components.md#gitlab)：*/etc/gitlab/gitlab.rb*，将其中的 **external_url** 项的值 *http://gitlab.example.com* 修改为你的域名
   ```text
   external_url "http://gitlab.example.com" # 改为自定义域名
   ...
   ``` 
3. 保存配置文件，重启下面的服务
   ```
   sudo gitlab-ctl reconfigure
   ```

### SSL/HTTPS

网站完成域名绑定且可以通过HTTP访问之后，方可设置HTTPS。

GitLab Omnibus 包是一个高度集成的可配置环境，HTTPS的设置与通常自行安装Nginx是不一样的。具体参考官方文档：[Enabling HTTPS](https://docs.gitlab.com/omnibus/settings/nginx.html#enable-https)

### 配置 SMTP

大量用户实践反馈，使用**第三方 SMTP 服务发送邮件**是一种最稳定可靠的方式。  

请勿尝试在服务器上安装sendmail等发邮件方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不易维护、诊断故障困难。

下面以**QQ企业邮箱**为例，提供设置 GitLab 发邮件的步骤：

1. 在QQ邮箱管理控制台获取 SMTP 相关参数
   ```
   SMTP host: smtp.exmail.qq.com
   SMTP port: 465 or 587 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: xxxx@xx.com
   SMTP password: #wwBJ8    //需要注意的是密码中不能包含单引号，否则出错
   ```
2. 通过 SFTP 工具远程连接服务器，修改 GitLab 配置文件：*/etc/gitlab/gitlab.rb*
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
4. 重启服务
   ```
   sudo gitlab-ctl reconfigure
   ```

GitLab 官方提供了数十种不同 SMTP 服务提供商的配置方法，请参考官方文档： [SMTP settings](https://docs.gitlab.com/omnibus/settings/smtp.html)

### 重置管理员密码

1. 使用ssh登陆GitLab服务器
2. 输入 `gitlab-rails console` 命令，参考下面示例修改密码
   ```

   root@iZ2zea1ri7y5hqhq9dmh4hZ:~# gitlab-rails console     //进入控制台命令
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

[gitlab官方文档](https://docs.gitlab.com/13.11/ee/security/reset_user_password.html)



## 异常处理

#### 浏览器打开IP地址，无法访问 GitLab（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### GitLab能打开，但总是出现502错误？

GitLab 所需内存最低为4G，若服务器配置太低会出现502错误

#### GitLab 新装或重启后，需要等待1分钟才能使用？

对于单核CPU的服务器，Unicorn and Sidekiq 服务启动最少需要一分钟

#### 本部署包采用的哪个数据库来存储 GitLab 数据？

是PostgreSQL

#### 没有购买 License 是否可以使用 GitLab 企业版？

如果安装了 GitLab 企业版，在没有导入 License 的情况下使用的是 社区版的所有功能。[GitLab-EE vs GitLab-CE](https://about.gitlab.com/install/ce-or-ee/)
