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
3. 在服务器中查看 GitLab 的 **[默认管理员账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  GitLab，务必先完成 **[域名五步设置](./dns#domain)** 过程

## GitLab 初始化向导

本步骤是用户首次接触软件的时间点（万事开头难）。若碰到障碍，请第一时刻联系 **[技术支持](./helpdesk)** 或参阅 [FAQ](./faq#setup)

下面是 Jenkins 初始化向导的具体步骤：

1. 本地电脑浏览器访问：*http://域名* 或 *http://服务器公网IP*，进入初始化页面 
   ![GitLab 登录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-login-websoft9.png)

2. 输入[默认账号密码](./setup/credentials#getpw)，进入 GitLab 控制台
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

在初始化之前的 **[准备](#prepare)** 环节，如果您已经完成 **[域名五步设置](./dns#domain)**，GitLab 可以域名访问，但是 GitLab 仓库的网址还不是用户自己的域名。

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

## 异常处理

#### GitLab能打开，但总是出现502错误？

GitLab 所需内存最低为 4G，若服务器配置太低会出现 502 错误

#### GitLab 新装或重启后，需要等待1分钟才能使用？

对于单核CPU的服务器，GitLab 中的 Unicorn and Sidekiq 服务最少需要一分钟的启动时间