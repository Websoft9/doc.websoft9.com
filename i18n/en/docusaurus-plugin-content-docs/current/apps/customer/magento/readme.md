---
sidebar_position: 1
slug: /magento/readme
tags:
  - Magento
  - eCommerce
---

# Magento Getting Started

[Magento](https://magento.org) is a Commerce Platform,it is the most popular commerce platform in the world, with more than 250,000 merchants around the globe selling more and driving innovation. Just check out our customer stories to find out how the Magento Advantage really works.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magentogui-websoft9.png)  

If you have installed Websoft9 Magento, the following steps is for your quick start


## Preparation

1. Get the **Internet IP** on your Cloud Platform
2. Check you **[Inbound of Security Group Rule](https://support.websoft9.com/docs/faq/tech-instance.html)** of Cloud Console to ensure the **TCP:80** is allowed
3. **[Get](./user/credentials)** default username and password of Magento  
4. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Magento  

## Magento Initialization

### Steps for you

The latest Magento has used the CLI to complete the installation wizard, so you can use it directly:

1. Using local browser visit the URL *http://DNS* or *http://Server's Internet IP*, enter to Magento Mall home page 
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/magento/magento-mall-websoft9.png)

2. Using local browser visit the URL *http://DNS* or *http://Server's Internet IP/admin*, enter to login interface  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/magento/magento-login-websoft9.png)

3. Login it to Magento console [(Don't know password?)](./user/credentials)  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/en/magento/magento-backend-websoft9.png)

> Refer to [Magento Docs](https://magento.com/resources/technical) to get more details

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.

**Can I use Cloud database for Magento?**

Yes, Use the following command to replace Magento's database.  

```
magento setup:config:set --db-host=DB-HOST --db-name=DB-NAME --db-user=DB-USER --db-engine=DB-ENGINE --db-password=DB-PASSWORD
```  

## Magento QuickStart

下面以 **使用 Magento 构建在线商城** 作为一个任务，帮助用户快速入门：
  
  
## Magento Setup

### Magento install modules

Below is the methods for you installing modules online

1. Make sure your Magento is [Linking Marketplace](/stack-installation.html#link-magento-marketplace)
2. Search the modules on Marketplace, 【buy】it and【Install】 it
3. Log in your Magento, open【SYSTEM】>【Web Setup Wizard】>【System Configration】 
4. On the left memu, click 【EXTENSION MANAGER】>【Refresh】, synchronize the your purchase to your Magento, then【Review and Install】 it
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-theme-1-websoft9.png)
   > Refresh not always successful, so please Refresh it repeatedly
5. Select the modules in the catalog and install it
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-theme-2-websoft9.png)
6. Magento will check the system environment before installation
7. If installation is very slowly and have error, please refer to [Troubleshooting](/else-troubleshooting.html#magento-upgrade-or-install-module-failed)

### Link Magento Marketplace

Completed installation of Magento, suggest you make your Magento system link Magento's Marketplace. Once you have linked it, you can use many resourses on Marketplace.

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setuptools-websoft9.png)  

1. [Register a Magento Account](https://account.magento.com/applications/customer/login)
2. Log in to Magento's Marketplace, create your **Access Key** from My Profile setting
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-1-websoft9.png)  
3. Save Access Key
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-savemykey-websoft9.png)  
4. Log in your Magento backend, open **SYSTEM** > **Web Setup Wizard**
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-websetupwz-websoft9.png) 
5. Fill in the **System config** with your Access Key from Marketplace
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setmkkey-websoft9.png) 
6. Save it, and wait for the Waiting for a successful connection
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setmkkeyss-websoft9.png) 
7. Then, you can use the resources of Marketplace online

### Magento set language

1. Download language package
1. Set language for Magento front page: go to Stores > Configuration > General > Local
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setlan-websoft9.png)
2. Set language for Magento backend page: go to Account Setting > Interface Local
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/magento/magento-adminlanguages-websoft9.png)

### Magento Cache

Cache is a important function for Magento

1. Log in Magento, go to【System】>【Tools】> 【Cache Management】
2. Select items
3. Click 【Flush Magento Cache】and【Flush Cache Storage】to start 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-flushcache-websoft9.png)
4. You can cancel cache from here
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-dscache-websoft9.png)

### SMTP
  
Sending mail is a common feature for Magento. With a large number of users' practice and feedback, only one way is recommended, that is, using the **third-party SMTP service** to send the email.

> Do not try to install **Sendmail** or other Mail server software on your Cloud Server for sending mail, because it has great difficulty in maintenance.

Taking **SendGrid's SMTP Service** as an example, refer to the following steps to configure sending mail:

1. Log in SendGrid console, and prepare your SMTP settings.
   ```
   SMTP host: smtp.sendgrid.net
   SMTP port: 25 or 587 for unencrypted/TLS email, 465 for SSL-encrypted email
   SMTP Authentication: must be checked
   SMTP Encryption: must SSL
   SMTP username: websoft9smtp
   SMTP password: #fdfwwBJ8f    
   ```
2. Make sure your Magento is [linking Magento's Marketplace](/stack-installation.html#link-magento-marketplace)
3. Connect Server, use below commands for installing Magento SMTP module
   ```
    cd /data/wwwroot/magento` 
	composer require mageplaza/module-smtp
	php bin/magento setup:upgrade 
	php bin/magento setup:di:compile
   ```
   If you don't want to use command, you can buy it from Marketplace and install it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtpplugin-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-buysmtpplugin-websoft9.png)

4. Log in Magento backend, configure SMTP  
   - Click **MAGEPLAZA** to start settings
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/magento/magento-smtp-2-websoft9.png)

   - Setting details
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/magento/magento-smtp-3-websoft9.png)

5. Log in Magento backend, set send from and send to Email address
   - Click **MAGEPLAZA** to start settings
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-4-websoft9.png)
   - Set it   
     ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-5-websoft9.png)
     

More SMTP Service(Gmail, Hotmail, QQ mail, Yahoo mail, SendGrid and so on)  settings or Issues with SMTP, please refer to Websoft9's *[SMTP Guide](https://support.websoft9.com/docs/faq/tech-smtp.html)*
     

### DNS Additional Configure（Modify URL）{#dns}

Complete **[Five steps for Domain](./administrator/domain_step)** ，Set the URL for Magento :

Connect to server via SSH and run  CLI commands to configure parameters
   
   ```shell
   cd /data/wwwroot/magento
   php bin/magento config:set web/unsecure/base_url http://www.mydomain.com/ # 修改成您的实际域名，必须以 / 结束
   php bin/magento config:set web/secure/base_url http://www.mydomain.com/ # 修改成您的实际域名，必须以 / 结束
   ```

### HTTPS 额外设置{#https}

**[标准 HTTPS 配置](../administrator/domain_https)** 完成后，还需运行下面的 CLI 命令进行配置：

```
cd /data/wwwroot/magento
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/"
php bin/magento cache:flush  #将基础URL更改为https并刷新缓存
```

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Magento

通过运行`docker ps`，可以查看到 Magento 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```

### Path{#path}
  
Magento installation directory: */data/wwwroot/magento*  
Magento configuration file: */data/wwwroot/magento/app/etc/env.php*  
Magento 多语言目录： */data/wwwroot/magento/vendor/magento/language-zh_hans_cn*   
Magento 命令行工具：* /data/wwwroot/magento/bin/magento*  
  
> Magento 配置文件中包含数据库连接信息，更改了 MySQL 数据库账号密码，此处也需要对应修改
  
### Port{#port}

| Port | Use                                          | Necessity |
| ------ | --------------------------------------------- | ------ |
| 3306 | Remote connect MySQL | Optional |
| 80 | HTTP requests for Magento | Required |
| 443 | HTTPS requests Magento | Optional |


### Version{#version}

```shell
magento -V
```

### Service{#service}

```shell
systemctl start | stop | restart | status magento
```

### CLI{#cli}

```
$ /data/wwwroot/magento/bin/magento list
Magento CLI 2.4.2

Usage:
  command [options] [arguments]

Options:
  -h, --help            Display this help message
  -q, --quiet           Do not output any message
  -V, --version         Display this application version
      --ansi            Force ANSI output
      --no-ansi         Disable ANSI output
  -n, --no-interaction  Do not ask any interactive question
  -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Available commands:
  help                                                 Displays help for a command
  list                                                 Lists commands
 admin
  admin:user:create                                    Creates an administrator
  admin:user:unlock                                    Unlock Admin Account
 app
  app:config:dump                                      Create dump of application
  app:config:import                                    Import data from shared configuration files to appropriate data storage
  app:config:status                                    Checks if config propagation requires update
 braintree
  braintree:migrate                                    Migrate stored cards from a Magento 1 database
 cache
  cache:clean                                          Cleans cache type(s)
  cache:disable                                        Disables cache type(s)
  cache:enable                                         Enables cache type(s)
  cache:flush                                          Flushes cache storage used by cache type(s)
  cache:status                                         Checks cache status
 catalog
  catalog:images:resize                                Creates resized product images
  catalog:product:attributes:cleanup                   Removes unused product attributes.
 cms
  cms:wysiwyg:restrict                                 Set whether to enforce user HTML content validation or show a warning instead
 config
  config:sensitive:set                                 Set sensitive configuration values
  config:set                                           Change system configuration
  config:show                                          Shows configuration value for given path. If path is not specified, all saved values will be shown
 cron
  cron:install                                         Generates and installs crontab for current user
  cron:remove                                          Removes tasks from crontab
  cron:run                                             Runs jobs by schedule
 customer
  customer:hash:upgrade                                Upgrade customer's hash according to the latest algorithm
 deploy
  deploy:mode:set                                      Set application mode.
  deploy:mode:show                                     Displays current application mode.
 dev
  dev:di:info                                          Provides information on Dependency Injection configuration for the Command.
  dev:profiler:disable                                 Disable the profiler.
  dev:profiler:enable                                  Enable the profiler.
  dev:query-log:disable                                Disable DB query logging
  dev:query-log:enable                                 Enable DB query logging
  dev:source-theme:deploy                              Collects and publishes source files for theme.
  dev:template-hints:disable                           Disable frontend template hints. A cache flush might be required.
  dev:template-hints:enable                            Enable frontend template hints. A cache flush might be required.
  dev:template-hints:status                            Show frontend template hints status.
  dev:tests:run                                        Runs tests
  dev:urn-catalog:generate                             Generates the catalog of URNs to *.xsd mappings for the IDE to highlight xml.
  dev:xml:convert                                      Converts XML file using XSL style sheets
 dotdigital
  dotdigital:connector:automap                         Auto-map data fields
  dotdigital:connector:enable                          Add Dotdigital API credentials and enable the connector
  dotdigital:migrate                                   Migrate data into email_ tables to sync with Engagement Cloud
  dotdigital:sync                                      Run syncs to populate email_ tables before importing to Engagement Cloud
  dotdigital:task                                      Run dotdigital module tasks on demand
 downloadable
  downloadable:domains:add                             Add domains to the downloadable domains whitelist
  downloadable:domains:remove                          Remove domains from the downloadable domains whitelist
  downloadable:domains:show                            Display downloadable domains whitelist
 encryption
  encryption:payment-data:update                       Re-encrypts encrypted credit card data with latest encryption cipher.
 i18n
  i18n:collect-phrases                                 Discovers phrases in the codebase
  i18n:pack                                            Saves language package
  i18n:uninstall                                       Uninstalls language packages
 indexer
  indexer:info                                         Shows allowed Indexers
  indexer:reindex                                      Reindexes Data
  indexer:reset                                        Resets indexer status to invalid
  indexer:set-dimensions-mode                          Set Indexer Dimensions Mode
  indexer:set-mode                                     Sets index mode type
  indexer:show-dimensions-mode                         Shows Indexer Dimension Mode
  indexer:show-mode                                    Shows Index Mode
  indexer:status                                       Shows status of Indexer
 info
  info:adminuri                                        Displays the Magento Admin URI
  info:backups:list                                    Prints list of available backup files
  info:currency:list                                   Displays the list of available currencies
  info:dependencies:show-framework                     Shows number of dependencies on Magento framework
  info:dependencies:show-modules                       Shows number of dependencies between modules
  info:dependencies:show-modules-circular              Shows number of circular dependencies between modules
  info:language:list                                   Displays the list of available language locales
  info:timezone:list                                   Displays the list of available timezones
 inventory
  inventory:reservation:create-compensations           Create reservations by provided compensation arguments
  inventory:reservation:list-inconsistencies           Show all orders and products with salable quantity inconsistencies
 inventory-geonames
  inventory-geonames:import                            Download and import geo names for source selection algorithm
 maintenance
  maintenance:allow-ips                                Sets maintenance mode exempt IPs
  maintenance:disable                                  Disables maintenance mode
  maintenance:enable                                   Enables maintenance mode
  maintenance:status                                   Displays maintenance mode status
 media-content
  media-content:sync                                   Synchronize content with assets
 media-gallery
  media-gallery:sync                                   Synchronize media storage and media assets in the database
 module
  module:config:status                                 Checks the modules configuration in the 'app/etc/config.php' file and reports if they are up to date or not
  module:disable                                       Disables specified modules
  module:enable                                        Enables specified modules
  module:status                                        Displays status of modules
  module:uninstall                                     Uninstalls modules installed by composer
 newrelic
  newrelic:create:deploy-marker                        Check the deploy queue for entries and create an appropriate deploy marker.
 queue
  queue:consumers:list                                 List of MessageQueue consumers
  queue:consumers:start                                Start MessageQueue consumer
 remote-storage
  remote-storage:sync                                  Synchronize media files with remote storage.
 sampledata
  sampledata:deploy                                    Deploy sample data modules for composer-based Magento installations
  sampledata:remove                                    Remove all sample data packages from composer.json
  sampledata:reset                                     Reset all sample data modules for re-installation
 security
  security:recaptcha:disable-for-user-forgot-password  Disable reCAPTCHA for admin user forgot password form
  security:recaptcha:disable-for-user-login            Disable reCAPTCHA for admin user login form
  security:tfa:google:set-secret                       Set the secret used for Google OTP generation.
  security:tfa:providers                               List all available providers
  security:tfa:reset                                   Reset configuration for one user
 setup
  setup:backup                                         Takes backup of Magento Application code base, media and database
  setup:config:set                                     Creates or modifies the deployment configuration
  setup:db-data:upgrade                                Installs and upgrades data in the DB
  setup:db-declaration:generate-patch                  Generate patch and put it in specific folder.
  setup:db-declaration:generate-whitelist              Generate whitelist of tables and columns that are allowed to be edited by declaration installer
  setup:db-schema:upgrade                              Installs and upgrades the DB schema
  setup:db:status                                      Checks if DB schema or data requires upgrade
  setup:di:compile                                     Generates DI configuration and all missing classes that can be auto-generated
  setup:install                                        Installs the Magento application
  setup:performance:generate-fixtures                  Generates fixtures
  setup:rollback                                       Rolls back Magento Application codebase, media and database
  setup:static-content:deploy                          Deploys static view files
  setup:store-config:set                               Installs the store configuration. Deprecated since 2.2.0. Use config:set instead
  setup:uninstall                                      Uninstalls the Magento application
  setup:upgrade                                        Upgrades the Magento application, DB data, and schema
 store
  store:list                                           Displays the list of stores
  store:website:list                                   Displays the list of websites
 theme
  theme:uninstall                                      Uninstalls theme
 varnish
  varnish:vcl:generate                                 Generates Varnish VCL and echos it to the command line
 yotpo
  yotpo:reset                                          Reset Yotpo sync flags &/or configurations
  yotpo:sync                                           Sync Yotpo manually (reviews module)
  yotpo:update-metadata                                Manually send platform metadata to Yotpo
```

### API

Support for both REST (Representational State Transfer) and SOAP (Simple Object Access Protocol). In Magento 2, the web API coverage is the same for both REST and SOAP.

Refer to Magento [API official docs](https://devdocs.magento.com/guides/v2.2/get-started/bk-get-started-api.html)