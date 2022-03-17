---
sidebar_position: 1
slug: /runtime/php
tags:
  - PHP
  - LAMP
  - LNMP
  - 运行环境
---

# PHP

## 安装网站

在 PHP 应用环境上安装一个网站，也就是我们常说的增加一个虚拟主机。

宏观上看，只需两个步骤：**上传网站代码** + **虚拟机主机配置文件** 中增加**配置段**

* Apache 下，这个配置段为：`<VirtualHost *:80>...</VirtualHost>`
* Nginx 下，这个配置段为：`server{}`


### 安装第一个网站

下面通过**替换示例网站**（默认存在一个示例网站）的方式来教你安装你的第一个网站：

1. 使用 WinSCP 连接服务器

2. 删除示例网站 */data/wwwroot/www.example.com* 下的所有文件（保留目录）

3. 将本地电脑上的网站源码上传到示例目录下
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-uploadcodestoexample-websoft9.png)

4. 修改虚拟主机配置文件，实现绑定域名、修改网站目录名称等操作。
   * **Apache** 下，修改 *vhost.conf* 中已有的 `<VirtualHost *:80>...</VirtualHost>`
   * **Nginx** 下，修改 *default.conf* 中已有的 `server{}`


5. 保存虚拟主机配置文件，重启服务后生效
    ~~~
    # 重启 Apache
    systemctl restart httpd
    
    # 重启 Nginx
    systemctl restart httpd
    ~~~

6. 本地浏览器访问网站：*http://域名* 或 *http://服务器公网IP* 

### 安装第二个网站

从安装第二个网站开始，需要在**虚拟机主机配置文件**中增加对应的配置段，具体如下

1. 使用 WinSCP 连接服务器，在 /data/wwwroot 下新建一个网站目录，假设命令为“mysite2”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-createmysite2-websoft9.png)

2. 将本地网站源文件上传到：*/data/wwwroot/mysite2* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-uploadcodes-websoft9.png)

3. 编辑 **虚拟机主机配置文件** 文件，实际情况获取代码段：

    | Web Server | 场景                                          | 获取代码段                    |
    | ---------- | --------------------------------------------- | ----------------------------- |
    | Apache     | **有域名，通过 http://域名 访问网站**         | [获取](../apache#wwwtemplate) |
    |            | **没有域名，通过 http://IP/mysite2 访问网站** | [获取](../apache#aliastemplate) |
    | Nginx      | **有域名，通过 http://域名 访问网站**         | [获取](../apache#wwwtemplate) |
    |            | **没有域名，通过 http://IP/mysite2 访问网站** | [获取](../apache#aliatemplate) |

4. 保存虚拟主机配置文件，重启服务后生效
    ~~~
    # 重启 Apache
    systemctl restart httpd
    
    # 重启 Nginx
    systemctl restart httpd
    ~~~

5. 本地浏览器访问网站：*http://域名* 或 *http://服务器公网IP* 


### 安装第 N 个网站

安装第n个网站与安装第二个网站的操作步骤一模一样

最后我们温故而知新，总结 PHP 应用环境安装网站步骤： 

1. 上传网站代码
2. 绑定域名（非必要）
3. 新增站点配置或修改示例站点配置
4. 增加网站对应的数据库（非必要）
5. 进入安装向导

## 维护 PHP 环境

参考本文档：[PHP 指南](../php) 和 [PHP 进阶](../php/advanced) 



