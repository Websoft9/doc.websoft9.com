# PHP

一下内容适合于基于yum安装的PHP

## 安装与升级

### 安装

PHP提供yum安装和源码编译安装方式。
yum安装方式简单、易升级，故我们推荐此升级方式

```
# Fedora/CentOS/Red Hat Enterprise Linux


# Ubuntu/Debian

```


> 如果您使用了Websoft9提供的PHP相关镜像，说明PHP已经存在，请勿再次安装PHP。  

### 版本升级

在实际使用过程中，会遇到升级 PHP 大版本的情形，如：从 PHP5.5->PHP5.6 或 PHP5.6->PHP7.0等。对于我们提供的LAMP环境来说，升级方法非常简单。

以PHP5.5->PHP5.6为例，具体如下：

1. 连接到Linux服务器后，依次执行如下命令：
```
//首先，禁用当前 PHP55 源
yum-config-manager --disable remi-php55   

//然后，启用需升级 PHP56 源
yum-config-manager --enable remi-php56     

//最后，升级更新
yum update -y
```


2. 为了确保升级成功，请检查升级后的 PHP 版本
```
php -v
```

> 以上方案也适用于 PHP7.0->PHP7.2

### 版本降级

以PHP7.0降级到PHP5.6为例，具体步骤如下：

```
//禁用当前7.0版本的下载源
yum-config-manager --disable remi-php70

//然后，启用需降级的版本 PHP56 源
yum-config-manager --enable remi-php56     

# 卸载PHP7.0
yum remove php-* -y

# 安装主要的PHP模块
yum -y install php-pecl-imagick php php-mysql php-common php-gd php-mbstring php-mcrypt php-devel php-xml php-pdo php-bcmath php-pear php-opcache php-ldap php-odbc php-xmlrpc php-json php-mysqlnd php-pdo php-pdo_dblib php-recode php-snmp php-soap php-pecl-zip php-curl php-imap

# 安装其他包
pear install Mail
pear install net_smtp
```



## 配置

对PHP来说，配置主要通过修改`php.ini`文件来实现。

当我们在运行PHP应用的时候，常常会碰到类似提示 **“超过最大的文件大小”**, **“运行超时”**, **“超过内存限制”**等，这个时候就需要php.ini来进行最大值的调整。

以CentOS上的PHP为例，php.ini路径为：/etc/php.ini

```shell
# 修改文件大小限制，注意数字后面需要带上单位M
post_max_size = 16M
upload_max_filesize = 16M

# 修改超时时间限制
max_execution_time = 90

# 修改内存限制
memory_limit – Minimum: 256M
```

## 扩展

PHP的扩展（extension）这里应称为“模块（module）”是 C、C++ 编写的功能合集，扩展大多以动态链接 .dll、.so 形式加载。php扩展是php核心并不支持的功能，然后可以通过扩展的方式进行扩展PHP的功能，常见的扩展如MySQL，gb2等等。

### 查询

通过phpinfo()函数 或 执行`php -m` 命令可以查看扩展

### 安装

### 启用

## 包

包则是直接引入通过 require/include 方式加載

### Composer

Composer 是 PHP 的一个包管理和包依赖管理的工具 ( 官方的定义是 "Dependency Manager for PHP" ), CentOS 的 yum, Node.js 的 npm 和 Python 的 pip.

#### 安装
#### 使用
#### 更新

### PEAR 

## 缓存

OPcache
XCache
APCU
eAccelerator


## 开发工具

## 问题

#### PHP extension 与 PHP Package有什么区别？
为了便于理解，我们认为PHP extension是一种编译后的二进制文件，放在php的bin目录下，供所有应用调用
PHP Package是一种源码包，用户的项目若要用到源码包，需要通过Github下载，并引入到自己的项目中，或者通过composer工具下载
