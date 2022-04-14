---
sidebar_position: 1
slug: /odoo
tags:
  - Odoo
  - 企业管理
  - ERP
---

# 快速入门

[Odoo](https://www.odoo.com/) 是一个开源的企业**全业务链**管理平台，ERP, 采购，库存，财务，营销，CRM，生产，人事，服务支持、电子商务、建站等各个应用程序完美集成在一起，使您能够完全实现业务流程自动化，省时省力，受益良多。Odoo 的开源开发模式利用数千名开发人员和业务专家来打造全球最大的完全集成的商业应用程序及其生态系统。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odooui-websoft9.png)

## 准备

部署 Websoft9 提供的 Odoo 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 Odoo 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  Odoo **[域名五步设置](./administrator/domain_step)** 过程


## Odoo 初始化向导{#init}

### 详细步骤

#### 社区版

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入初始化页面
   ![Odoo 社区版初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-startcreatedb-websoft9.png)

2. 填写好所有参数，点击【create database】按钮，开始初始化安装。
   > 其中 Email 和 Password 是登录账号密码，务必牢记之

3. 初始化安装完成后，登录后台，安装所需的 APP
  ![Odoo APPS](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-consoleui-websoft9.png)

#### 企业版

部署 Odoo 企业版后，根据镜像引导页获取试用授权，便可以免费试用一个月。

1. 使用本地 Chrome 或 Firefox 浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入欢迎页面
  ![Odoo 欢迎页面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/odoo/odoo-eewelcome-websoft9.png)

2. 获取授权后，登录云服务器，运行如下命令解锁企业版
   ```
   bash /etc/odoo/ee_init.sh
   ```

3. 刷新欢迎页面后，显示初始化安装步骤
  ![Odoo 初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-startcreatedb-websoft9.png)

4. 完成初始化后，提示一旦安装第一个应用之后，系统就会提示要求注册订阅号（You will be able to register your database once you have installed your first app.）
  ![Odoo 注册提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-registersb000-websoft9.png)

5. 系统提示 **Register your subscription or buy a subscription**，请输入试用码
  ![Odoo 注册提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-registersb001-websoft9.png)

6. 开始试用企业版  
  ![Odoo 注册提示](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-registersb002-websoft9.png)

> 免费试用期结束之后，数据库可能会被被清空，请到 [Odoo 官方](https://www.odoo.com/zh_CN/pricing)进行企业版订阅，需折扣可以直接[联系我们](./helpdesk#contact)。


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**安装时勾选了 Demo data，想删除这些数据?**

官方并没有提供 Demo data 的删除工具，建议直接删除数据库，然后再新增（此时不再勾选 Demo data）

## Odoo 使用入门

下面以 **Odoo 构建企业ERP** 作为一个任务，帮助用户快速入门：

> 需要了解更多Odoo的使用，请参考官方文档：[Odoo Documentation](https://www.odoo.com/documentation/master/index.html)

## Odoo 常用操作

### 配置 SMTP{#smtp}

1. 在邮箱管理控制台获取 [SMTP](./administrator/smtp) 相关参数
   
2. 登录 Odoo 控制台，安装 SMTP 所需的 **Discuss** 模块
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-discussmodule-websoft9.png)

3. 通过：【Settings】>【General Settings】>【Discuss】开始配置邮箱
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-gsetmail-websoft9.png)

4. 填写 SMTP 参数
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-smtps-websoft9.png)
5. 点击【Test Connection】

### 数据库管理器{#dbadmin}

Odoo 自带一个数据库管理器，参考：  

1. 在 Odoo 登录界面点击【Manage Database】链接    
![Odoo manage database](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-loginpage-websoft9.png)

2. 点击【set a master password】给数据库设置一个主密码保护数据库（非常重要）  
![Odoo set a password](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-setmasterpw-websoft9.png)

3. 设置密码  
![Odoo set a password](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-setapw-websoft9.png)

4. 选择操作项，管理数据库  
![Odoo set a password](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-manages-websoft9.png)

#### 新增

Odoo 支持多租户（多企业组织），增加一个数据库就等于增加一个企业。  

多个企业共同使用一套 Odoo，采用不同的账号登录，相互不干扰。

1. 点击【create database】，输入密码，设置名称
   ![Odoo 新增数据库](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-multidb-websoft9.png)

2. 新增完成后，你会看到数据库管理界面列出新增的数据库

#### 备份

1. 输入密码，选择备份格式，点击【Backup】
   ![Odoo 备份](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesbk-websoft9.png)

2. 备份完成后，系统会自动下载备份数据（zip文件）

#### 复制

可以完整复制一个企业组织，作为新企业组织的数据

1. 输入密码，设置名称，点击【Continue】
![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesdp-websoft9.png)

2. 复制成功后，数据库管理栏目会列出新复制的数据库

#### 删除

请谨慎操作

#### 恢复

数据库被删除后，可以通过备份进行恢复

1. 输入密码，选择备份文件，命名恢复后的数据库名称，点击【Continue】
![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesrs-websoft9.png)

1. 数据库恢复过程中可能会出现"413 Request Entity Too Large"，[解决办法](./odoo/admin#attachment)

#### 修改主密码

修改主密码是一项非常重要的安全操作。  

### 管理 Odoo

本章列出使用 Odoo 过程中最常见的一些配置

#### 基础设置

Odoo 后台提供了设置界面，参考：

1. 登录 Odoo 后，打开点击左上角的设置图标，打开【Settings】项
   ![Odoo设置界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingspanel-websoft9.png)
2. 接下来可以进行：安装apps，设置语言，增加用户，企业初始化等操作

#### 设置企业 Logo

![Odoo 设置logo](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingslogo-websoft9.png)

#### 增加语言{#setlang}

1. 通过【Settings】控制台增加一个语言
  ![Odoo 增加语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingslangs-websoft9.png)
2. 转到【Administrator】>【Prefrences】  
  ![Odoo 用户管理](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-pref-websoft9.png)
3. 给用户设置语言
  ![Odoo 设置语言](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-language002-websoft9.png)

#### 开发者模式{#dev-mode}

Odoo 默认是管理者模式，如果需要深度设置，请先开启开发者模式

1. 登录 Odoo 后，打开点击左上角的设置图标，打开【Settings】项
2. 在 Settings 界面的右下点击【Active the developer mode】
   ![Odoo 开发者模式](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-enabledev-websoft9.png)
3. 在开发者模式下，Settings 控制台的功能更多了

#### 安装 wkhtmltopdf

Odoo 镜像默认已经安装 wkhtmltopdf，如何你想重新安装它，具体操作步骤如下：

1.  卸载已经安装的 wkhtmltopdf 旧版本:

    ~~~
    ~# sudo apt-get remove wkhtmltopdf 
    ~# sudo apt-get autoremove
    ~~~

2.  去官网下载最新版本的 wkhtmltopdf 压缩包:

    ~~~
    ~# wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
    ~~~

3.  解压下载好的压缩包，得到一个名为：wkhtmltox 的文件夹：

    ~~~
    ~# tar –xf [filename]
    ~~~

4.  将 wkhtmltox/bin/wkhtmltomage 和 wkhtmmltox/bin/wkhtmltoodf 这两个文件复制到 /usr/bin 目录下去：

    ~~~
    ~# cp wkhtmltox/bin/wkhtmltoimage /usr/bin/
    ~# cp wkhtmmltox/bin/wkhtmltoodf /usr/bin/
    ~~~

5.  重启Odoo服务

    ~~~
    ~# systemctl restart odoo
    ~~~

#### Apps 市场

Odoo除了基础模块之外，通过[Odoo Apps 市场](https://www.odoo.com/apps/modules)提供了大量优质的第三方模块。通过使用第三方模块，用户可以快速找到所需的功能，以免费或极小的代价满足需求，快速上线业务，这是Odoo开源生态的带给用户的巨大价值，商业ERP在这方面是无法取代的。



## 参数{#parameter}

Odoo 应用中包含 Nginx, Docker, PostgreSQL, pgAdmin, Python 等组件，可通过 **[通用参数表](./setup/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 Odoo 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Odoo 本身的参数：

### 路径{#path}

Odoo 安装目录： */usr/lib/python3/dist-packages/odoo*  
Odoo 配置文件： */etc/odoo/odoo.conf*  
Odoo 日志目录： */var/log/odoo*

### 端口{#port}

无特殊端口


### 版本{#version}

```shell
odoo --version
```

### 服务{#service}

```shell
sudo docker start | stop | restart | status odoo
```

### 命令行{#cli}

Odoo CLI 是用于管理和配置Odoo的命令行工具，通过 SSH 连接服务器，运行 `odoo -h` 命令，列出如下可用的功能。

```
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit

  Common options:
    -c CONFIG, --config=CONFIG
                        specify alternate config file
    -s, --save          save configuration to ~/.odoorc (or to
                        ~/.openerp_serverrc if it exists)
    -i INIT, --init=INIT
                        install one or more modules (comma-separated list, use
                        "all" for all modules), requires -d
    -u UPDATE, --update=UPDATE
                        update one or more modules (comma-separated list, use
                        "all" for all modules). Requires -d.
    --without-demo=WITHOUT_DEMO
                        disable loading demo data for modules to be installed
                        (comma-separated, use "all" for all modules). Requires
                        -d and -i. Default is none
    -P IMPORT_PARTIAL, --import-partial=IMPORT_PARTIAL
                        Use this for big data importation, if it crashes you
                        will be able to continue at the current state. Provide
                        a filename to store intermediate importation states.
    --pidfile=PIDFILE   file where the server pid will be stored
    --addons-path=ADDONS_PATH
                        specify additional addons paths (separated by commas).
    --upgrades-paths=UPGRADES_PATHS
                        specify an additional upgrades path.
    --load=SERVER_WIDE_MODULES
                        Comma-separated list of server-wide modules.
    -D DATA_DIR, --data-dir=DATA_DIR
                        Directory where to store Odoo data

  HTTP Service Configuration:
    --http-interface=HTTP_INTERFACE
                        Listen interface address for HTTP services. Keep empty
                        to listen on all interfaces (0.0.0.0)
    -p PORT, --http-port=PORT
                        Listen port for the main HTTP service
    --longpolling-port=PORT
                        Listen port for the longpolling HTTP service
    --no-http           Disable the HTTP and Longpolling services entirely
    --proxy-mode        Activate reverse proxy WSGI wrappers (headers
                        rewriting) Only enable this when running behind a
                        trusted web proxy!

  Web interface Configuration:
    --db-filter=REGEXP  Regular expressions for filtering available databases
                        for Web UI. The expression can use %d (domain) and %h
                        (host) placeholders.

  Testing Configuration:
    --test-file=TEST_FILE
                        Launch a python test file.
    --test-enable       Enable unit tests.
    --test-tags=TEST_TAGS
                        Comma separated list of spec to filter which tests to
                        execute. Enable unit tests if set.
                        A filter spec has the format:
                        [-][tag][/module][:class][.method]
                        The '-' specifies if we want to include or exclude
                        tests matching this spec.                          The
                        tag will match tags added on a class with a @tagged
                        decorator. By default tag value is 'standard' when not
                        given on include mode. '*' will match all tags. Tag
                        will also match module name (deprecated, use /module)
                        The module, class, and method will respectively match
                        the module name, test class name and test method name.
                        examples: :TestClass.test_func,/test_module,external
    --screencasts=DIR   Screencasts will go in DIR/{db_name}/screencasts. '1'
                        can be used to force the same dir as for screenshots.
    --screenshots=DIR   Screenshots will go in DIR/{db_name}/screenshots.
                        Defaults to /tmp/odoo_tests.

  Logging Configuration:
    --logfile=LOGFILE   file where the server log will be stored
    --syslog            Send the log to the syslog server
    --log-handler=PREFIX:LEVEL
                        setup a handler at LEVEL for a given PREFIX. An empty
                        PREFIX indicates the root logger. This option can be
                        repeated. Example: "odoo.orm:DEBUG" or
                        "werkzeug:CRITICAL" (default: ":INFO")
    --log-request       shortcut for --log-handler=odoo.http.rpc.request:DEBUG
    --log-response      shortcut for --log-
                        handler=odoo.http.rpc.response:DEBUG
    --log-web           shortcut for --log-handler=odoo.http:DEBUG
    --log-sql           shortcut for --log-handler=odoo.sql_db:DEBUG
    --log-db=LOG_DB     Logging database
    --log-db-level=LOG_DB_LEVEL
                        Logging database level
    --log-level=LOG_LEVEL
                        specify the level of the logging. Accepted values:
                        ['info', 'debug_rpc', 'warn', 'test', 'critical',
                        'debug_sql', 'error', 'debug', 'debug_rpc_answer',
                        'notset'].

  SMTP Configuration:
    --email-from=EMAIL_FROM
                        specify the SMTP email address for sending email
    --smtp=SMTP_SERVER  specify the SMTP server for sending email
    --smtp-port=SMTP_PORT
                        specify the SMTP port
    --smtp-ssl          if passed, SMTP connections will be encrypted with SSL
                        (STARTTLS)
    --smtp-user=SMTP_USER
                        specify the SMTP username for sending email
    --smtp-password=SMTP_PASSWORD
                        specify the SMTP password for sending email

  Database related options:
    -d DB_NAME, --database=DB_NAME
                        specify the database name
    -r DB_USER, --db_user=DB_USER
                        specify the database user name
    -w DB_PASSWORD, --db_password=DB_PASSWORD
                        specify the database password
    --pg_path=PG_PATH   specify the pg executable path
    --db_host=DB_HOST   specify the database host
    --db_port=DB_PORT   specify the database port
    --db_sslmode=DB_SSLMODE
                        specify the database ssl connection mode (see
                        PostgreSQL documentation)
    --db_maxconn=DB_MAXCONN
                        specify the maximum number of physical connections to
                        PostgreSQL
    --db-template=DB_TEMPLATE
                        specify a custom database template to create a new
                        database

  Internationalisation options. :
    Use these options to translate Odoo to another language. See i18n
    section of the user manual. Option '-d' is mandatory. Option '-l' is
    mandatory in case of importation

    --load-language=LOAD_LANGUAGE
                        specifies the languages for the translations you want
                        to be loaded
    -l LANGUAGE, --language=LANGUAGE
                        specify the language of the translation file. Use it
                        with --i18n-export or --i18n-import
    --i18n-export=TRANSLATE_OUT
                        export all sentences to be translated to a CSV file, a
                        PO file or a TGZ archive and exit
    --i18n-import=TRANSLATE_IN
                        import a CSV or a PO file with translations and exit.
                        The '-l' option is required.
    --i18n-overwrite    overwrites existing translation terms on updating a
                        module or importing a CSV or a PO file.
    --modules=TRANSLATE_MODULES
                        specify modules to export. Use in combination with
                        --i18n-export

  Security-related options:
    --no-database-list  Disable the ability to obtain or view the list of
                        databases. Also disable access to the database manager
                        and selector, so be sure to set a proper --database
                        parameter first

  Advanced options:
    --dev=DEV_MODE      Enable developer mode. Param: List of options
                        separated by comma. Options : all,
                        [pudb|wdb|ipdb|pdb], reload, qweb, werkzeug, xml
    --shell-interface=SHELL_INTERFACE
                        Specify a preferred REPL to use in shell mode.
                        Supported REPLs are: [ipython|ptpython|bpython|python]
    --stop-after-init   stop the server after its initialization
    --osv-memory-count-limit=OSV_MEMORY_COUNT_LIMIT
                        Force a limit on the maximum number of records kept in
                        the virtual osv_memory tables. The default is False,
                        which means no count-based limit.
    --osv-memory-age-limit=OSV_MEMORY_AGE_LIMIT
                        Force a limit on the maximum age of records kept in
                        the virtual osv_memory tables. This is a decimal value
                        expressed in hours, and the default is 1 hour.
    --max-cron-threads=MAX_CRON_THREADS
                        Maximum number of threads processing concurrently cron
                        jobs (default 2).
    --unaccent          Use the unaccent function provided by the database
                        when available.
    --geoip-db=GEOIP_DATABASE
                        Absolute path to the GeoIP database file.

  Multiprocessing options:
    --workers=WORKERS   Specify the number of workers, 0 disable prefork mode.
    --limit-memory-soft=LIMIT_MEMORY_SOFT
                        Maximum allowed virtual memory per worker, when
                        reached the worker be reset after the current request
                        (default 2048MiB).
    --limit-memory-hard=LIMIT_MEMORY_HARD
                        Maximum allowed virtual memory per worker, when
                        reached, any memory allocation will fail (default
                        2560MiB).
    --limit-time-cpu=LIMIT_TIME_CPU
                        Maximum allowed CPU time per request (default 60).
    --limit-time-real=LIMIT_TIME_REAL
                        Maximum allowed Real time per request (default 120).
    --limit-time-real-cron=LIMIT_TIME_REAL_CRON
                        Maximum allowed Real time per cron job. (default:
                        --limit-time-real). Set to 0 for no limit.
    --limit-request=LIMIT_REQUEST
                        Maximum number of request to be processed per worker
                        (default 8192).

```

更多详细情况，请参考官方文档：[Command-line interface: odoo-bin](https://www.odoo.com/documentation/13.0/reference/cmdline.html)

### API

[Odoo External API](https://www.odoo.com/documentation/14.0/developer/misc/api/odoo.html)

