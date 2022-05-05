---
slug: /php/advanced
---

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

### 查询模块

通过phpinfo()函数 或 执行`php -m` 命令可以查看扩展

### 更新

## 概念与原理

### Composer

Composer 是 PHP 的一个包管理和包依赖管理的工具 ( 官方的定义是 "Dependency Manager for PHP" ), CentOS 的 yum, Node.js 的 npm 和 Python 的 pip.


### PEAR 

### PHP-FPM

### 缓存

OPcache
XCache
APCU
eAccelerator

### phar

[phar](https://www.php.net/manual/zh/intro.phar.php) 扩展提供了一种将整个 PHP 应用程序放入称为“phar”（PHP 存档）的单个文件的方法，以便于分发和安装。

## 故障速查{#troubleshooting}

#### PHP 不支持 SMTP？

PHP 与 SMTP 相关的问题

1.  需要了解你所使用的STMP功能是否调用了PHP软件包（或扩展类）
   	* php官方提供的mail()类，这个类不支持SMTP验证
    * php扩展包-[PHPMailer](https://github.com/PHPMailer/PHPMailer)，这个类功能比较全面

2.  php_openss版本过低或者没有安装，php_openssl的CA证书确实或异常


## 问题解答

#### PHP extension 与 PHP Package 区别？

为了便于理解，我们认为PHP extension是一种编译后的二进制文件，放在php的bin目录下，供所有应用调用
PHP Package是一种源码包，用户的项目若要用到源码包，需要通过Github下载，并引入到自己的项目中，或者通过composer工具下载

#### 如何引入 PHP 包？

包则是直接引入通过 require/include 方式加载

#### 如何重置 php.ini 文件？

[下载 php.ini 模板](https://github.com/Websoft9/ansible-lamp/blob/master/roles/php/templates/php.ini) 后覆盖你服务器上的 */ect/php.ini*

#### 如何找到 PHP 资源？

参考[Awesome PHP](https://github.com/ziadoz/awesome-php)

#### PHP on Windows 如何安装扩展？

1. 选择需要管理PHP版本的网站，然后打开PHP Manager，点击“Add an Extension”
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addphp-websoft9.png)
2. 弹出的对话框中上传php扩展文件（.dll）
3. 重启IIS后生效