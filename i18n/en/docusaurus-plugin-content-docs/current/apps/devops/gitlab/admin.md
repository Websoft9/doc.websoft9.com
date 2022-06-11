---
sidebar_position: 3
slug: /gitlab/admin
tags:
  - Gitlab
  - DevOps
---

# Gitlab Maintenance

This chapter is special guide for Gitlab maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Gitlab Backup and Restore

Based the official docs, we suggest you backup by these steps:

1. Backup configuration files: Use SFTP  **compression** and download（*/etc/gitlab*）
2. Backup all GitLab system: run a backup command. ([view the backup lists](https://docs.gitlab.com/ce/raketasks/backup_restore.html#creating-a-backup-of-the-gitlab-system))
   ``` shell
   sudo gitlab-backup create
   ```
3. Put the system files and configuartion files in the same folder, named according to the date
4. Backup completed

> GitLab provide the official docs for [Backups](https://docs.gitlab.com/omnibus/settings/backups.html)


### Gitlab Upgrade

GitLab officially provides **level by level**[upgrade plan](https://docs.gitlab.com/omnibus/update/README.html#updating-using-the-official-repositories), each version has an upgrade The path must be gradually upgraded to the **specified version**, the method is as follows:

#### Specify version upgrade

The update method of updating to a specified version is very useful. On the one hand, it meets the requirements of a specific version of the user, and on the other hand, it achieves a **gradual upgrade** in this way, which solves the situation that the version span is too large to be upgraded.

For example: Gitlab12 to GitLab14 cannot be upgraded directly, you need to refer to the official step-by-step [upgrade path](https://docs.gitlab.com/ee/update/index.html#upgrade-paths) to achieve this. 

Take the Gitlab 13.0.14 to GitLab 14.1.6 as sample for your reference below:    

1. Get the **upgrade paths** from [official docs](https://docs.gitlab.com/ee/update/index.html#upgrade-paths), computing your correct path like this:  
   ```
   13.0.14 -> 13.1.11 -> 13.8.8 -> 13.12.10 -> 13.12.12 -> 14.0.11 -> 14.1.6
   ```

2. Optional step: search all versions in GitLab repository (ce can be instead to ee)
   ```
   # Ubuntu/Debian
   sudo apt-cache madison gitlab-ce

   # RHEL/CentOS 6 and 7
   yum --showduplicates list gitlab-ce

   # RHEL/CentOS 8
   dnf --showduplicates list gitlab-ce
   ```

3. Update step by step
   ```
   # Ubuntu/Debian
   sudo apt install gitlab-ce-<version>

   # RHEL/CentOS 6 and 7
   yum install gitlab-ce-<version>

   # RHEL/CentOS 8
   dnf install gitlab-ce-<version>
   ```

> If you update by `yum install gitlab-ce` which not include version, it mean update to latest version


#### CE to EE

To upgrade an existing GitLab Community Edition (CE) server to GitLab Enterprise Edition (EE), all you have to do is install the EE package on top of CE. 

1. Get the CE version nubmer
   ```
   # For Debian/Ubuntu
   sudo apt-cache policy gitlab-ce | grep Installed

   # For CentOS/RHEL
   sudo rpm -q gitlab-ce
   ```
2. Match the EE version number.e.g. the CE number is *8.6.7-ce.0*, then the EE number should be *8.6.7-ee.0*
3. Add the gitlab-ee Apt or Yum repository
   ```
   # For Debian/Ubuntu
   curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash

   # For CentOS/RHEL
   curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash
   ```
4. Install the correct GitLab-EE version(system will automatically uninstall CE version the same time)
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
5. Go to the GitLab admin panel of your server (/admin/license/new) and upload your license file.
6. After you confirm that GitLab is working as expected, you may remove the old Community Edition repository:
   ```
   # For Debian/Ubuntu
   sudo rm /etc/apt/sources.list.d/gitlab_gitlab-ce.list

   # For CentOS/RHEL
   sudo rm /etc/yum.repos.d/gitlab_gitlab-ce.repo
   ```
More details about CE upgrade to EE, please refer to official docs: [Updating Community Edition to Enterprise Edition](https://docs.gitlab.com/omnibus/update/README.html#updating-community-edition-to-enterprise-edition)

## Troubleshoot{#troubleshoot}

In addition to the Gitlab issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 公司固定 IP 突然不能访问 Gitlab？

**现象描述**：通过公司网络（固定IP）突然（以前可以访问）不能访问Gitlab，而通过自己的手机wifi可以访问。   

**原因分析**：GitLab 有一个rack-attack安全机制。某种条件下（例如：公司大量并发访问 GitLab）rack-attack安全将你的 IP 错误地拦截，导致了从此不能访问 GitLab   

**解决方案**：修改 [Gitlab 配置文件](../gitlab#path) 相关项

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gitlab/gitlab-attachip-websoft9.png)


#### GitLab 502 error when loading?{#502}

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/gitlab-502-websoft9.png)

The minimum required free memory for GitLab is 4G. If the Server memory is limit, a 502 error will occur. For a single-core CPU server, the Unicorn and Sidekiq service starts up to a minute, and if it is not started, it will report a 502 error.


## FAQ{#faq}

#### 没有买 License 可使用 GitLab 企业版吗？

如果安装了 GitLab 企业版，在没有导入 License 的情况下使用的是 社区版的所有功能。[GitLab-EE vs GitLab-CE](https://about.gitlab.com/install/ce-or-ee/)

#### 采用哪种方式安装 GitLab？

本项目采用 [Omnibus GitLab包](https://gitlab.com/gitlab-org/omnibus-gitlab) 的安装方式。Omnibus GitLab 是官方推荐的一种安装方法，它自带了 GitLab 所需的所有组件和服务，并可以省去繁琐的配置，同时它自带 CLI 工具，便于 GitLab 升级和维护。

#### GitLab support multi-language?

Yes, you can change the language from the Admin Panel of GitLab

#### Where is the database connection configuration of GitLab?

Database configuration information in */etc/gitlab/gitlab.rb* in the [Gilab Configure](../gitlab#path)

#### Can I remote connect PostgreSQL?

No, Omnibus GitLab use the PostgreSQL Peer Authentication mode for local connection

#### What is the default port for cloning gitlab Projects Using SSH?  

Default port is 22

#### What is the password for the database root user?

Omnibus GitLab use the PostgreSQL Peer Authentication mode for local connection, no username and pssword

#### Is there a web-base GUI database management tools?

No

#### Is it possible to modify the repository path of GitLab?

Yes, Refer to official docs [Repository Storage Paths](https://docs.gitlab.com/ee/administration/repository_storage_paths.html)