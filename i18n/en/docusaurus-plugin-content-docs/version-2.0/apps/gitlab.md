---
title: Gitlab
slug: /gitlab
tags:
  - DevOps
  - CI/CD
  - Continuous Integration
  - Code Repository
  - Development Full Stack
  - JuHu Gitlab 
---

import Meta from './_include/gitlab.md';

<Meta name="meta" />

## Getting started{#guide}

### Login verification{#verification}

1. After installing GitLab through the **Websoft9 console**, view the application details in the **My Applications** section. Get the login information from the **Access** tab.  

2. After accessing from your local computer's browser, go to the login page (it will take 2-3 minutes to load for the first time, do not reboot at this time, as it will invalidate the login password.)
   ![GitLab login](./assets/gitlab-login-websoft9.png)

3. Enter your account and password, then access the GitLab console.
   ![GitLab backend](./assets/gitlab-backend-websoft9.png)

4. Start setting the language, creating a new repository and adding new users, etc.

### Set the GitLab repository address{#setrepourl}

The repository address differs from the GitLab console address.  

Refer to: [Configure External URL](https://docs.gitlab.com/omnibus/settings/configuration.html#configuring-the-external-url-for-gitlab) to configure the value of the **external_url** entry.

## Enterprise Edition

#### Why work with Websoft9?{#why}

Websoft9 is a partner of Gitlab (including [JiHu Gitlab](#jihu)), and by purchasing GitLab through Websoft9, you can benefit from:

- More favorable discounts
- Enhanced technical support coverage
- Comprehensive DevOps technology integration and consulting
- A 2-month trial license of Jihu Gitlab Enterprise Edition (Jihu Gitlab officially licenses Websoft9 to provide Enterprise Edition support on the public cloud)

#### About JiHu Gitlab{#jihu}

JiHu Gitlab is an independently owned and operated GitLab company in China that provides localized GitLab products and services to users:

- JiHu GitLab is available in Free, Premium, and Ultimate editions, with a free trial available for the Free edition.
- JiHu GitLab upstream repository is GitLab and is synchronized at a high frequency.
- JiHu GitLab SaaS service is based on local Chinese infrastructure and is completely independent of GitLab global SaaS.
- JiHu GitLab functionality and operations are the same as GitLab, with some localized features tailored to help the local user experience.

### Import an Enterprise license{#lic}

1. Prepare the required license

   - **JiHu GitLab license**: This can be downloaded from [this URL](https://websoft9.github.io/docker-library/apps/jihu/src/gitlab.license).
   - **GitLab license**: You have to apply for this yourself. Visit the [official GitLab website](https://about.gitlab.com/pricing/) to apply.

2. Log in to GitLab and Import the license: Go to **Admin Area > Setting > General > Add Licenses**, and upload a license file
   ![Gitlab Import License](./assets/gitlabee-license-websoft9.png)

### Convert CE to EE

The conversion [relationship](https://about.gitlab.com/install/ce-or-ee) between GitLab CE and GitLab EE:

- If GitLab EE is installed, EE functionality is disabled at the end of the trial period, but CE functionality remains available
- If GitLab CE is installed, you need to change the image label to EE and rebuild the container to [upgrade to EE](https://docs.gitlab.com/omnibus/update/README.html#updating-community-edition-to-)


## Configuration options{#configs}

- CLI: `gitlab-ctl`
- [API](https://docs.gitlab.com/ee/api/) : `curl "https://gitlab.example.com/api/v4/projects"`
- Multilingual(✅): Select **User Settings > Preferences** to set the language
- SMTP(✅): The relevant values in the configuration file are as follows
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
- Configuration file (mounted) : */etc/gitlab/gitlab.rb*
- [GitLab architecture](https://docs.gitlab.com/ee/development/architecture.html) : GitLab contains [dozens of components](https://docs.gitlab.com/ee/development/architecture.html#component-list), detailed in  */opt/gitlab/version-manifest.txt*.

- GitLab Runner: The GitLab Runner is an additional component that you need to deploy yourself.


## Administer{#administrator}

- **Reset the administrator password**: Access the container and use the `gitlab-rails console` to [reset password](https://docs.gitlab.com/13.11/ee/security/reset_user_password.html)
- **Modify repository directory**: Refer to [Repository storage paths](https://docs.gitlab.com/ee/administration/repository_storage_paths.html)

## Troubleshooting{#troubleshooting}

#### Company fixed IP suddenly cannot access Gitlab?

Description: Gitlab is inaccessible through the company network (fixed IP), but it can be accessed through your own cell phone wifi.   
Reason: GitLab’s rack-attack security mechanism might block your IP due to a high volume of concurrent accesses from the company network.
Solution: Modify the Gitlab configuration file to adjust the rack-attack settings.

#### Getting a 502 error accessing GitLab? {#502}

Description: A 502 occurs when accessing GitLab for the first time or during high traffic?   
Reason: GitLab requires at least 4G of RAM, so if the server configuration is insufficient, 502 errors will occur. In addition, single-core CPU servers may take at least one minute for the Unicorn and Sidekiq services to start, and if they don't finish, a 502 error may also be reported!   
Solution: Upgrade your server configuration

#### Cannot connect to PostgreSQL?

Description: Unable to connect to PostgreSQL in the GitLab container using a database client?  
Reason: By default, GitLab uses Peer Authentication for PostgreSQL, restricting access to the database to the Linux system account on the host where PostgreSQL is located, and does not allow remote access.
Solution: Adjust PostgreSQL configuration to enable remote connections if needed.

