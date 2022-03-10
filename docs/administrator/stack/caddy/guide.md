---
sidebar_position: 1
slug: /caddy
tags:
  - Caddy
  - Web 服务器
---


# Caddy

LCMP环境中部署网站主要分为5个步骤： **①**上传网站代码-&gt;**②**修改文件系统用户权限-&gt;**③**配置域名（非必要）-&gt;**④**增加网站对应的数据库（非必要）-&gt;**⑤**完成安装向导

LCMP环境中只部署一个网站还是多个网站、有无域名这两种情况对应的部署操作细节略有不一样，下面分别说明：

## 场景一：服务器只安装一个网站

1.  通过SFTP工具，将网站源文件上传到默认的根目录下：/data/wwwroot/default
2.  通过Putty工具修改用户权限，运行如下一条命令即可：

    ```
    chown -R caddy.caddy /data/wwwroot/default/
    ```
3.  无域名，请直接通过 http://公网ip 的方式来开始安装
4.  有域名，通过域名控制台解析成功后通过 http://域名 的方式来开始安装
上传站点程序到 `/data/wwwroot/default/`目录下,修改 `/etc/caddy/caddy.conf`文件

```
:80 { #这里 :80 修改成你的域名 注意①(内容在后面)
index index.php index.html
gzip
root /data/wwwroot/default/ # 这里修改成你程序的路径(默认)
fastcgi / /dev/shm/php-fpm-default.sock php
log /var/log/caddy/access.log
errors /var/log/caddy/error.log
}

import conf.d/*.conf

```
6.  如果在安装向导过程中提示数据库无法自动创建，请自行创建数据库

## 场景二：服务器部署多个网站（无域名）

无域名情况下，以部署两个网站为例，具体操作如下：

1.  通过SFTP将第一个网站目录上传到/data/wwwroot/default/目录下面，假设应用程序目录命为“mysite1”
2.  通过Putty工具修改用户权限，运行如下一条命令即可：

    ```   
    chown -R caddy.caddy /data/wwwroot/default/
    ```
3. 在`/etc/caddy/caddy.conf` 新增配置文件内容如下::
    ```
    :80/mysite1/ {   # 网站访问路径 可以自定义
    gzip
    root /data/wwwroot/default/mysite1  # 网站程序路径
    fastcgi / /dev/shm/php-fpm-default.sock php
    log /var/log/caddy/mysite1-access.log
    errors /var/log/caddy/mysite1-error.log
    }
    ````
4. 运行命令 `systemctl restart caddy` 重启服务器,重载配置文件
5.  通过_http://ip/mysite1 _的方式来访问应用，进入安装向导
6.  如果在安装向导过程中提示数据库无法自动创建，需要通过http://ip/phpmyadmin 创建数据库

安装第二个网站，操作步骤同样

## 场景三：服务器部署多个网站（共用一个域名）

以部署两个网站为例，具体操作如下：

1.  通过SFTP将第一个网站目录上传到/data/wwwroot/default/目录下面，假设应用程序目录命为“mysite1”
2.  通过Putty工具修改用户权限，运行如下一条命令即可：

    ```
    chown -R caddy.caddy /data/wwwroot/default/
    ```

3.  通过域名控制台将域名解析到服务器公网IP，确保解析成功进入下一步
4.  在`/etc/caddy/caddy.conf` 新增配置文件内容如下::
    ```
    www.youdomain.com/mysite1/ {   # 前半部分为域名 后半部分网站访问路径 可以自定义
    gzip
    root /data/wwwroot/default/mysite1  # 网站程序路径
    fastcgi / /dev/shm/php-fpm-default.sock php
    log /var/log/caddy/mysite1-access.log
    errors /var/log/caddy/mysite1-error.log
    }
    ````
5.  通过_http://域名 /mysite1 _的方式来访问应用，进入安装向导
6.  如果在安装向导过程中提示数据库无法自动创建，需要通过http://ip/phpmyadmin 创建数据库

安装第二个网站，操作步骤同样

## 场景四：服务器部署多个网站（多个域名）

以部署其中一个网站为例，具体操作如下：

1.  通过SFTP将第一个网站目录上传到/data/wwwroot/default/目录下面，假设应用程序目录命为“mysite1”
2.  通过Putty工具修改用户权限，运行如下一条命令即可：

    ```
    chown -R caddy.caddy /data/wwwroot/default/
    ```

3.  通过域名控制台将域名解析到服务器公网IP，确保解析成功进入下一步
4.  在`/etc/caddy/caddy.conf` 新增配置文件内容如下::
    ```
    www.youdomain.com {   # 域名
    gzip
    root /data/wwwroot/default/mysite1  # 网站程序路径
    fastcgi / /dev/shm/php-fpm-default.sock php
    log /var/log/caddy/mysite1-access.log
    errors /var/log/caddy/mysite1-error.log
    }
    ````

5.  重启http服务或重启服务器

    ```
    # systemctl restart caddy
    ```

6.  通过_http://域名 _的方式来访问应用，进入安装向导
7.  如果在安装向导过程中提示数据库无法自动创建，需要通过http://ip/phpmyadmin 创建数据库

安装第二个网站，操作步骤同样

