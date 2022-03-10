# 进阶

## 安装

### 基本安装

PHP提供yum安装和源码编译安装方式。yum安装方式简单、易升级，故我们推荐此升级方式

```
# Fedora/CentOS/Red Hat Enterprise Linux

# Ubuntu/Debian
```

> 如果您使用了Websoft9提供的PHP相关镜像，说明PHP已经存在，请勿再次安装PHP。  

### 升级

###  安装扩展

PHP的扩展（extension）这里应称为“模块（module）”是 C、C++ 编写的功能合集，扩展大多以动态链接 .dll、.so 形式加载。php扩展是php核心并不支持的功能，然后可以通过扩展的方式进行扩展PHP的功能，常见的扩展如MySQL，gb2等等。

### 查询

通过phpinfo()函数 或 执行`php -m` 命令可以查看扩展

## 配置原理

## PHP on Windows

Windows系统下的IIS环境，安装了多版本的PHP，可以直接修改php配置文件，也可以通过图形化界面操作：

### 切换PHP版本

选择需要管理PHP版本的网站，然后打开PHP Manager，点击“Change PHP Version”，重启IIS后生效

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-changephpver-websoft9.png)

> 注意：PHP版本影响范围为一个网站或网站中的应用程序，没有整个IIS全局PHP版本设置，这样大大的方便了多版本的应用访问。

### php.ini修改

1.远程桌面到Windows服务器，直接编辑php.ini（_C:\websoft9\php-\*\php.ini_ ），修改对应的参数值（“\#”在前的项表示没有启用，需要删除“\#”后启用），保存

```
//修改文件大小对应的参数
post_max_size = 16M
upload_max_filesize = 16M

//修改系统最大响应时间对应的参数
max_execution_time = 90

//修改最大内存限制对应的参数
memory_limit – Minimum: 256M
```

2.重启IIS

### 安装PHP扩展

1. 选择需要管理PHP版本的网站，然后打开PHP Manager，点击“Add an Extension”![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addphp-websoft9.png)
2. 弹出的对话框中上传php扩展文件（.dll）
3. 重启IIS后生效

### Composer

Composer 是 PHP 的一个包管理和包依赖管理的工具 ( 官方的定义是 "Dependency Manager for PHP" ), CentOS 的 yum, Node.js 的 npm 和 Python 的 pip.

#### 安装
#### 使用
#### 更新

## PEAR 

## PHP-FPM

## 缓存

OPcache
XCache
APCU
eAccelerator

## 问题

#### PHP extension 与 PHP Package有什么区别？

为了便于理解，我们认为PHP extension是一种编译后的二进制文件，放在php的bin目录下，供所有应用调用
PHP Package是一种源码包，用户的项目若要用到源码包，需要通过Github下载，并引入到自己的项目中，或者通过composer工具下载