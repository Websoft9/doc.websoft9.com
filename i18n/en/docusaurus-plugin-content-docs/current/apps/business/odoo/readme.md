---
sidebar_position: 1
slug: /odoo
tags:
  - Odoo
  - 企业管理
  - ERP
---

# Odoo Getting Started

[Odoo](https://www.odoo.com/) is a suite of web based open source business apps.The main Odoo Apps include an Open Source CRM, Website Builder, eCommerce, Warehouse Management, Project Management, Billing & Accounting, Point of Sale, Human Resources, Marketing, Manufacturing, Purchase Management,Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get a full-featured Open Source ERP when you install several Apps.

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odooui-websoft9.png)

If you have installed Websoft9 Odoo, the following steps is for your quick start

## Preparation

1. Get the **Internet IP** of your Server on Cloud
2. Check your **[Inbound of Security Group Rule](./administrator/firewall#security)** of Cloud Console to ensure the **TCP:80** is allowed
3. Complete **[Five steps for Domain](./administrator/domain_step)** if you want to use Domain for Odoo
4. [Get](./user/credentials) default username and password of Odoo

## Odoo Initialization

### Steps for you

1. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will enter installation wizard of Odoo
 ![Odoo初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-startcreatedb-websoft9.png)

2.Fill in all items, then click **create database** button to start create one Company's database
  > The Email and Password is credentials for log in to Odoo

3. After the create database is complete, log in to the Odoo Console and install the apps your required.
  ![Odoo APPS](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-consoleui-websoft9.png)

4. Log out, click the **Manage Database** in the log in page of Odoo  
  ![Odoo manage database](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-loginpage-websoft9.png)

5. Click the **set a master password** to set a management password for Odoo's databases(very important)
  ![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-setmasterpw-websoft9.png)

6. Odoo Support for multi-enterprise, so you can **create database** again for creating new company
  ![Odoo create database again](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-multidb-websoft9.png)

7. Return to log in page, you can see a new database listed for log in
  ![Odoo login](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-multidblogin-websoft9.png)

> More useful Odoo guide, please refer to [Odoo Documentation](https://www.odoo.com/documentation/master/index.html)

### Having trouble?

Below is for you to solve problem, and you can contact **[Websoft9 Support](./helpdesk)** or refer to **[Troubleshoot + FAQ](./faq#setup)** to get more.  

**Check the Demo data, can you delete the data later?**

Their no tools for you to delete Demo data. It is recommended to delete the database directly and then add it again (the Demo data is no longer checked)

## Odoo QuickStart

下面以 **Odoo 构建企业ERP** 作为一个任务，帮助用户快速入门：

> 需要了解更多Odoo的使用，请参考官方文档：[Odoo Documentation](https://www.odoo.com/documentation/master/index.html)

## Odoo Setup

### Configure SMTP{#smtp}

1. Get [SMTP](./administrator/smtp) related parameters in the mailbox management console

2. Log in to the Odoo Console, intall the **Discuss** module that SMTP need
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-discussmodule-websoft9.png)

3. Open **Settings** > **General Settings** > **Discuss** to start configure SMTP
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-gsetmail-websoft9.png)

3. Fill in the SMTP parameters
   ![Odoo SMTP](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-smtps-websoft9.png)

4. Click the **Test Connection**

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

**新增**

Odoo 支持多租户（多企业组织），增加一个数据库就等于增加一个企业。  

多个企业共同使用一套 Odoo，采用不同的账号登录，相互不干扰。

1. 点击【create database】，输入密码，设置名称
   ![Odoo 新增数据库](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-multidb-websoft9.png)

2. 新增完成后，你会看到数据库管理界面列出新增的数据库

**备份**

1. 输入密码，选择备份格式，点击【Backup】
   ![Odoo 备份](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesbk-websoft9.png)

2. 备份完成后，系统会自动下载备份数据（zip文件）

**复制**

可以完整复制一个企业组织，作为新企业组织的数据

1. 输入密码，设置名称，点击【Continue】
![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesdp-websoft9.png)

2. 复制成功后，数据库管理栏目会列出新复制的数据库

**删除**

请谨慎操作

**恢复**

数据库被删除后，可以通过备份进行恢复

1. 输入密码，选择备份文件，命名恢复后的数据库名称，点击【Continue】
![Odoo set a pssword](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-managesrs-websoft9.png)

1. 数据库恢复过程中可能会出现"413 Request Entity Too Large"，[解决办法](./odoo/admin#attachment)

**修改主密码**

修改主密码是一项非常重要的安全操作。  

### Basic Settings

Go to Odoo's Settings panel

1. Log in Odoo, and click the **Settings icon** in the left top menu
   ![Odoo  Settings ](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingspanel-websoft9.png)
2. Then, you can install apps, set language, add user, set up company and more

### Set your Logo

![Odoo set logo](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingslogo-websoft9.png)doo 设置logo](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingslogo-websoft9.png)

### Set Language{#setlang}

1. Go to **Settings** console to add a new language
  ![Odoo add new language](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-settingslangs-websoft9.png)
2. Then go to **Administrator** > **Prefrences**    
  ![Odoo user prefrences](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-pref-websoft9.png)
3. Set language for administrator
  ![Odoo set language](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-language002-websoft9.png)

### Enable developer mode{#dev-mode}

1. Log in to Odoo, open the **Settings** item by clicking the settings icon in the upper left corner.
2. Click **Active the developer mode** on the lower right of the Settings screen.
   ![Odoo Developer Mode](https://libs.websoft9.com/Websoft9/DocsPicture/en/odoo/odoo-enabledev-websoft9.png)
3. In the developer mode, the Settings console has more features.

### Install wkhtmltopdf

Odoo has installed the wkhtmltopdf, if you want to reintall it, follow is the steps:

1.  Remove the old version of wkhtmltopdf

    ~~~
    ~# sudo apt-get remove wkhtmltopdf 
    ~# sudo apt-get autoremove
    ~~~

2.  Download wkhtmltopdf tar file from Github

    ~~~
    ~# wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
    ~~~

3.  Unzip it and you can find a new folder named wkhtmltox in your Server

    ~~~
    ~# tar –xf [filename]
    ~~~

4.  Copy the file *wkhtmltox/bin/wkhtmltomage* and *wkhtmmltox/bin/wkhtmltoodf* the directory */usr/bin*

    ~~~
    ~# cp wkhtmltox/bin/wkhtmltoimage /usr/bin/
    ~# cp wkhtmmltox/bin/wkhtmltoodf /usr/bin/
    ~~~

5.  Restart Odoo service

    ~~~
    ~# systemctl restart odoo
    ~~~

### Apps Marketplace

In addition to the base modules, Odoo offers a number of premium third-party modules through [Odoo Apps Marketplace](https://www.odoo.com/apps/modules)

## Reference sheet

The below items and **[General parameter sheet](./administrator/parameter)** is maybe useful for you manage Odoo 

通过运行`docker ps`，可以查看到 Odoo 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 Odoo 本身的参数：

### Path{#path}

Odoo installation directory： */usr/lib/python3/dist-packages/odoo*  
Odoo 配置文件： */etc/odoo/odoo.conf*  
Odoo 日志目录： */var/log/odoo*

### Port{#port}

无特殊端口


### Version{#version}

```shell
odoo --version
```

### Service{#service}

```shell
sudo docker start | stop | restart | status odoo
```

### CLI{#cli}

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

