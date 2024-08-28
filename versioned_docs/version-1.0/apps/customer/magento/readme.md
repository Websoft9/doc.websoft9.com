---
sidebar_position: 1
slug: /magento
tags:
  - Magento
  - 电子商务
---

# 快速入门

[Magento Open Source](https://business.adobe.com/products/magento/open-source.html) 是一个老牌的开源电子商务平台，它满足 B2C 电商入门所需的一切。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magentogui-websoft9.png) 


部署 Websoft9 提供的 Magento 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Magento 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Magento **[域名五步设置](./administrator/domain_step)** 过程


## Magento 初始化向导

### 详细步骤

Magento 最新版本已经采用命令行完成了安装向导，即可直接使用：

1. 使用本地电脑浏览器访问网址：http://域名 或 http://服务器公网IP, 可以直接进入商城首页  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-mall-websoft9.png)

2. 访问网址：*http://域名/admin* 或 *http://服务器公网IP/admin*，进入后台登陆页面  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-login-websoft9.png)

3. 输入用户名和密码[获取解锁密码](./user/credentials)，登录到 Magento 后台管理界面  
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-backend-websoft9.png)

> 需要了解更多 Magento 的使用，请参考官方文档：[Magento 用户文档中心](https://magento.com/resources/technical)

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**想将 Magento 默认的 MySQL 数据库更换为自己的 RDS？**

执行下面命令可以更换 Magento 所使用的数据库

```
magento setup:config:set --db-host=DB-HOST --db-name=DB-NAME --db-user=DB-USER --db-engine=DB-ENGINE --db-password=DB-PASSWORD
```

## Magento 使用入门

下面以 **使用 Magento 构建在线商城** 作为一个任务，帮助用户快速入门：


## Magento 常用操作

### 安装插件{#installplugin}

建议通过 Magento 后台在线安装扩展：

1. 确保你的 Magento 已经[连接到官方的 Marketplace](#marketplace)

2. 在 Marketplace 找到您需要的扩展或主题，购买完成，点击【Install】

3. 登录 Magento 后台，打开：【SYSTEM】>【Web Setup Wizard】>【System Configration】 

4. 在左侧菜单栏选择【EXTENSION MANAGER】，单击【Refresh】 将购买信息同步到网站，然后通过【Review and Install】查看

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-theme-1-websoft9.png)

   > Refresh 可能会出现同步失败，请多次刷新

5. 在列表内选择插件或主题，即可进行安装

6. 安装时会进行系统环境检查，条件全面满足才可以开始安装

7. 安装过程时间较长且报错，请查看[故障原因](./magento/admin)

### 连接 Magento Marketplace{#marketplace}

安装 Magento 后，建议把你安装的 Magento 系统与 Magento 官方的 Marketplace 资源进行在线连接，这样便可以使用 Marketplace 上的大量资源

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setuptools-websoft9.png)  

1. 到官方 [注册 Magento 账号](https://account.magento.com/applications/customer/login)

2. 登录 Marketplace，打到My Profile 的 Access Keys 页面新建一个自己的 Access Key; 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-1-websoft9.png)  

3. 保存 Access Key  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-savemykey-websoft9.png)  

4. 进入 Magento 容器的网站根目录，将 key 复制到 auth.json.example,并重命名为 auth.json 

```
{
    "http-basic": {
        "repo.magento.com": {
            "username": "<public-key>",
            "password": "<private-key>"
        }
    }
}

```

5. 连接后，就可以很方便的使用 Marketplace 上的资源

### 安装中文包{#setlanguage}

中文包 zh_Hans_CN 已经存在 [Magento 多语言目录](#path)中 

需要启用中文方法如下：  

1.  网页后台设置中文：在管理员页面右上角点击你的账户 Account Setting > Interface Local 中设置 Interface Local 为Chinese（China）

2.  网页前台设置中文：
   - 安装前台语言包：
   ```
	docker exec -it magento bash #进入Magento容器
	cd /bitnami/magento/
	php bin/magento config:set --scope=stores --scope-code=default general/locale/code zh_Hans_CN
	php bin/magento cache:clean
	php bin/magento cache:flush
   ```
   - 进入到Magento管理员界面，后台 Stores > Configuration > General > Local 中设置Local为Chinese(China)

### 刷新缓存

Cache（缓存）是 Magento 的一项重要设置：

1. 登录 Magento 后台，依次打开：【System】>【Tools】> 【Cache Management】
2. 选择需要刷新的缓存
3. 点击【Flush Magento Cache】和【Flush Cache Storage】开始刷新
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-flushcache-websoft9.png)
4. 也可以取消一些页面的缓存设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-dscache-websoft9.png)

### 配置 SMTP{#smtp}

请参照官方的 [SMTP 配置方案](https://experienceleague.adobe.com/zh-hans/docs/commerce-admin/systems/communications/email-communications)
     

### 域名额外配置（修改 URL） {#dns}

**[域名五步设置](./administrator/domain_step)** 完成后，需设置 Magento URL:

通过SSH连接云服务器，运行下面的 CLI 命令进行参数配置
   
   ```shell
   docker exec -it magento bash #进入Magento容器
   cd /bitnami/magento
   php bin/magento config:set web/unsecure/base_url http://www.mydomain.com/ # 修改成您的实际域名，必须以 / 结束
   php bin/magento config:set web/secure/base_url http://www.mydomain.com/ # 修改成您的实际域名，必须以 / 结束
   ```

### HTTPS 额外设置{#https}

**[标准 HTTPS 配置](./administrator/domain_https)** 完成后，还需运行下面的 CLI 命令进行配置：

```
docker exec -it magento bash #进入Magento容器
cd /bitnami/magento/
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/"
php bin/magento cache:flush  #将基础URL更改为https并刷新缓存
```

## 参数{#parameter}

Magento 应用中包含 Nginx, Docker, MySQL, phpMyAdmin, Varnish, RabbitMQ, Elasticsearch等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Magento 运行时所有的 运行时所有的服务组件：

```bash
CONTAINER ID   IMAGE                     COMMAND                  CREATED              STATUS              PORTS                                                       NAMES
0cb53e8158c3   bitnami/magento:latest    "/opt/bitnami/script…"   About a minute ago   Up About a minute   8080/tcp, 8443/tcp, 0.0.0.0:9001->80/tcp, :::9001->80/tcp   magento
99a9a1e1e20d   bitnami/elasticsearch:7   "/opt/bitnami/script…"   About a minute ago   Up About a minute   9200/tcp, 9300/tcp                                          magento-elasticsearch
09b196940f88   bitnami/mariadb:10.4      "/opt/bitnami/script…"   About a minute ago   Up About a minute   3306/tcp                                                    magento-db
```

### 路径{#path}

Magento 配置文件目录 */data/apps/magento*  
Magento 数据目录： */data/apps/magento/data*     

### 端口{#port}

无特殊端口

### 版本{#version}

```shell
sudo docker exec -it magento magento -V
```

### 服务{#service}

```shell
systemctl start | stop | restart | status magento
systemctl start | stop | restart | status magento-elasticsearch
systemctl start | stop | restart | status magento-db
```

### 命令行{#cli}

```
$ sudo docker exec -it magento magento list
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

Magento API 支持 REST（表述性状态传递）和 SOAP（简单对象访问协议）。 在 Magento 2 中，REST 和 SOAP 的 Web API 覆盖范围是相同的。

参考[官方文档](https://devdocs.magento.com/guides/v2.2/get-started/bk-get-started-api.html)
