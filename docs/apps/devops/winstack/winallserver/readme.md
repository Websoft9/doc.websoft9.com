---
sidebar_position: 1
slug: /winallstack
tags:
  - 全能环境
  - DevOps
---

# 快速入门

**WinAllServer（全能环境）** 是以 IIS 作为 WebServer 集成环境，预装 PHP/JDK/.NET, Tomcat, MySQL/SQLServer 等。

部署 Websoft9 提供的 WinAllServer 之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 WinAllServer 的 **[默认账号和密码](./setup/credentials)**  
4. 若想用域名访问  WinAllServer，务必先完成 **[域名五步设置](./dns#domain)** 过程


## WinAllServer初始化向导

### 详细步骤

远程桌面到服务器后，检查 IIS 的可用性

### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。


## WinAllServer发布应用

### 发布 PHP 应用

IIS 环境中部署网站主要分为5个步骤： **①**上传网站代码-&gt;**②**配置域名（非必要）-&gt;**③**增加网站对应的数据库（非必要）-&gt;**⑤**完成安装向导

注意：部署一个网站还是多个网站、有无域名这两种情况对应的部署操作细节略有不一样，下面分别说明： 

#### 场景一：安装一个网站

如果您打算此服务器上只部署一个网站或应用，建议采用此方式：

1. 远程桌面到Windows服务器，将网站源文件拷贝到根目录
2. 如果没有可用域名，请直接通过 [http://公网IP](http://公网IP) 的方式来访问应用
3. 如果有可用的域名，请完成 **《域名配置》** 后通过 [http://公网IP](http://公网IP)  的方式来访问应用
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

网站默认根目录为：C:\inetpub\wwwroot

#### 场景二：安装多个网站（无域名）

无域名情况下，以部署两个网站为例，具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 通IIS增加一个虚拟目录或应用程序 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1-websoft9.png)
3. 通过 [http://ip/mysite1](http://ip/mysite1) 的方式来访问应用，即可访问mysite1
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤同样

网站默认根目录为：C:\inetpub\wwwroot

#### 场景三：安装多个网站（共用域名）

共用一个域名情况下（即每个网站都打算以 [http://域名/mysite1](http://域名/mysite1) 这样的方式访问），以部署两个网站为例，具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 通IIS增加一个虚拟目录或应用程序 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1-websoft9.png)
3. 完成 **《域名配置》** 后通过 [http://域名/mysite1](http://域名/mysite1) 的方式来访问应用
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤同样

网站默认根目录为：C:\inetpub\wwwroot

#### 场景四：安装多个网站（多个域名）

多个域名下（即每个网站都有自己的域名），以部署一个网站为例（假设域名为www.abc.com），具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 提前将您的域名**www.abc.com**解析到服务器公网IP地址，并确保已经解析成功
3. 打开IIS-网站-添加网站，参考下图完成路径、域名填写，然后保存 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1d-websoft9.png)
4. 通过 [http://域名/](http://域名/)_** **_的方式来访问应用
5. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤和部署一个网站的一样。

网站默认根目录为：C:\inetpub\wwwroot

### 发布 ASP.NET 应用

IIS环境中部署网站主要分为5个步骤： **①**上传网站代码-&gt;**②**配置域名（非必要）-&gt;**③**增加网站对应的数据库（非必要）-&gt;**⑤**完成安装向导

注意：部署一个网站还是多个网站、有无域名这两种情况对应的部署操作细节略有不一样，下面分别说明：

#### 场景一：安装一个网站

如果您打算此服务器上只部署一个网站或应用，建议采用此方式：

1. 远程桌面到Windows服务器，将网站源文件拷贝到根目录
2. 如果没有可用域名，请直接通过 [http://公网IP](http://公网IP) 的方式来访问应用
3. 如果有可用的域名，请完成 **《域名配置》** 后通过 [http://公网IP](http://公网IP) 的方式来访问应用
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

网站默认根目录为：C:\inetpub\wwwroot

#### 场景二：安装多个网站（无域名）

无域名情况下，以部署两个网站为例，具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 通IIS增加一个虚拟目录或应用程序 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1-websoft9.png)
3. 通过 [http://ip/mysite1](http://ip/mysite1)  的方式来访问应用，即可访问mysite1
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过 [http://ip/phpmyadmin](http://ip/phpmyadmin)  创建数据库

安装第二个网站**mysite2**，操作步骤同样

网站默认根目录为：C:\inetpub\wwwroot

#### 场景三：安装多个网站（共用域名）

共用一个域名情况下（即每个网站都打算以 [http://域名/mysite1](http://域名/mysite1) 这样的方式访问），以部署两个网站为例，具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 通IIS增加一个虚拟目录或应用程序 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1-websoft9.png)
3. 完成 **《域名配置》** 后通过 [http://域名/mysite1](http://域名/mysite1) 的方式来访问应用
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过 [http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤同样

网站默认根目录为：C:\inetpub\wwwroot

#### 场景四：安装多个网站（多个域名）

多个域名下（即每个网站都有自己的域名），以部署一个网站为例（假设域名为www.abc.com），具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 提前将您的域名 **www.abc.com** 解析到服务器公网IP地址，并确保已经解析成功
3. 打开IIS-网站-添加网站，参考下图完成路径、域名填写，然后保存 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1d-websoft9.png)
4. 通过 [http://域名/](http://域名/) 的方式来访问应用
5. 如果在安装向导过程中提示数据库无法自动创建，需要通过 [http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤和部署第一个网站的步骤一样。

网站默认根目录为：C:\inetpub\wwwroot

### 发布Java应用 


1. 修改hosts文件
    - 使用编辑器打开 `C:\Windows\System32\drivers\etc` 目录下得 hosts 文件
    - 在 hosts 文件内增加一下内容
      ![..](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/iis/iis-hosts-websoft9.cn.png)

2.  新增虚拟主机
    - 使用编辑器打开 `C:\websoft9\Tomcat8.5\conf\server.xml` 找到默认 `<Host>`  段,如下图所示
      ![1](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/iis/tomcat-serer-websoft9.png)
    在  `</Host>` 下面添加虚拟主机配置,修改对应的域名和网站路径
   ```
    <Host name="www.websoft9.com" appBase="C:\inetpub\wwwroot\test">
         <Context path="" docBase="." debug="0" />
    </Host>
   ```


3. 重启 tomcat

3. 配置IIS,步骤如图所示:

   * 新增IIS网站

   ![52315343586](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/iis/iis-add1-websoft9.png)

   * 配置网站

   ![52315373069](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/iis/iis-add2-websoft9.png)

4. IIS设置反向代理,操作步骤如图所示:

   ![52315383514](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/iis/iis-reproxy1-websoft9.png)

   ![52315389569](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/iis/iis-reproxy2-websoft9.png)

   ![52315405165](http://libs-websoft9-com.oss-cn-qingdao.aliyuncs.com/Websoft9/DocsPicture/zh/iis/iis-reproxy3-websoft9.png)

5. 如果tomcat虚拟主机所设置目录下是war包会自动解压,如果上传程序是文件夹,请将文件夹重名为`ROOT`

6. 访问所配置的域名,测试网站是否正常访问

注意: 如果网站物理路径设置到C盘下非`C:\inetpub\wwwroot`目录下会存在权限问题,造成网站访问时出错,需要手动为目录设置`IUSR`和`IIS_IUSRS`用户或组


## 参数

**[通用参数表](../setup/parameter)** 中可查看 Nginx, Java, Docker, MySQL 等 全能环境（IIS） 应用中包含的基础架构组件路径、版本、端口等参数。 

下面仅列出 全能环境（IIS）本身的参数：

### 路径{#path}

网站默认根目录为：*C:\inetpub\wwwroot*  
Tomcat 路径: *C:\websoft9\Tomcat8.5*  
Tomcat 配置文件：*C:\websoft9\Tomcat8.5\conf\server.xml*  
JDK 路径: *C:\Program Files\Java*  

### 命令行

无

### API

无


