
---
slug: /lamp/installation/zh/laravel
---

# Laravel

Websoft9提供的 **Laravel 运行环境(LAMP)**，基于 [LAMP 环境镜像](https://support.websoft9.com/docs/lamp/zh)制作，节省你的安装部署时间。

### Laravel安装原理

下面介绍Laravel是如何基于LAMP安装的

> 如果您使用 **Laravel 运行环境(LAMP)**，只需了解原理即可，无需再次安装 Laravel。

1. 服务器部署 [LAMP 镜像](https://support.websoft9.com/docs/lamp/zh)
2. 将 Laravel 包下载后上传到服务器目录：*/data/wwwroot/laravel*
3. WinSCP 连接服务器，编辑虚拟主机配置文件：*/etc/httpd/vhost/vhost.conf* 
4. 将 DocumentRoot, Directory 路径指向：*laravel/public*
   ~~~
   <VirtualHost *:80>
   DocumentRoot "/data/wwwroot/default/laravel/public"
    ...
   <Directory "/data/wwwroot/default/laravel/public">
   ...
   ~~~
5. 保存，并重启服务

### 更新Laravel程序

当 Laravel 镜像版本过低的时候，您可能希望下载Laravel官方最新版本替换镜像内版本，我们建议的步骤如下：

 1. 将Laravel下载解压，上传后替换原来的目录
 2. 运行修改文件权限的命令
   ~~~
   chown -R apache.apache /data/wwwroot/laravel
   ~~~
   
 >下载的新版本目录结构中应用根目录（如public文件夹）与配置文件中的路径（DocumentRoot,Directory）需要保持一致