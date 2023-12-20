---
sidebar_position: 2
slug: /runtime/java
tags:
  - Java
  - 运行环境
---

# Java 应用

## 安装 Java 应用

在 Java 环境上安装一个网站（应用），也就是我们常说的增加一个虚拟主机。

全局上看，只需三个步骤：**上传网站代码** + **配置 Tomcat** + [**虚拟机主机配置文件**](../runtime#path) **中增加 server{} 配置段**

> server{} 又称之为虚拟主机配置段，每个网站必定在 default.conf 中对应唯一的 server{}。

对 Java 项目来说，Tomcat 是应用服务器的作用，是运行Java 程序的入口，而 Nginx 是 Web 服务器的作用，负责处理 HTTP 请求，并将Java运行的请求转发给 Tomcat。

### 安装第一个Java应用{#installone}

系统中默认有示例网站，可以通过替换示例网站代码的方式安装第一个网站。

> 如果不考虑修改示例网站，请阅读[安装第二个Java网站](#installsecond)。

1. 使用 WinSCP 连接服务器
2. 删除示例目录下的所有文件，只保留目录（*/data/wwwroot/www.example.com*）
3. 上传代码到默认的示例目录，并修正所属用户和组权限，保证上传的代码具有访问权限
   ```
   chown www: -R /data/wwwroot/www.example.com
   ```
4. 编辑 Tomcat 配置文件 *server.xml* 文件，修改默认 `<host>...</host>` 配置段中 name 等
   ```
   <Host name="mysite2.yourdomain.com" appBase="/data/wwwroot/www.example.com" unpackWARs="true" autoDeploy="true">
  		<Context path="" docBase="/data/wwwroot/www.example.com" reloadable="false" crossContext="true"/>
  		<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
    	prefix="localhost_access_log" suffix=".txt" pattern="%h %l %u %t &quot;%r&quot; %s %b" />
  		<Valve className="org.apache.catalina.valves.RemoteIpValve" remoteIpHeader="X-Forwarded-For"
    	protocolHeader="X-Forwarded-Proto" protocolHeaderHttpsValue="https"/>
	 </Host>
   ```
5. 编辑 Nginx 配置文件 *default.conf* 文件，启用 `include jsp.conf`，注释掉 `#include php.conf`，然后修改 server_name, root 等参数   
   ``` nginx
   server
    {
        listen 80;
        server_name mysite2.yourdomain.com; # 修自己的域名
        index index.html index.htm index.jsp index.do index.php;
        root  /data/wwwroot/mysite2; # 修改为自己的路径
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
        
        #include php.conf; # 注释掉
        include jsp.conf; # 启用
    }
    ```
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/java/lnmp-modifynginx001-websoft9.jpg)

6. 保存配置文件，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
    ~~~
    sudo systemctl restart tomcat
    sudo systemctl restart nginx
    ~~~
7. 通过：*http://域名* 或 *http://服务器公网IP* 访问网站


### 安装第二个Java应用{#installsecond}

我们现在介绍新增一个网站的详细步骤：

1. 使用 WinSCP 连接服务器，在 /data/wwwroot 下新建一个网站目录，假设命令为“mysite2”
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-createmysite2-websoft9.png)

2. 将本地网站源文件上传到：*/data/wwwroot/mysite2* 
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/lamp-uploadcodes-websoft9.png)

3. 使用命令修正所属用户和组权限，保证上传的代码具有访问权限
   ```
   chown www: -R /data/wwwroot/mysite2
   ```
4. 编辑 Tomcat 配置文件 *server.xml* 文件   
   新增 `<Host></Host>` 配置段，**插入**到 server.xml 中，并修改其中的 name, appBase, docBase, prefix等（[参数说明](../java#tomcattp)）
    ```
    # host segment template
    <Host name="mysite2.yourdomain.com" appBase="/data/wwwroot/mysite2" unpackWARs="true" autoDeploy="true">
    <Context path="" docBase="/data/wwwroot/mysite2" reloadable="false" crossContext="true"/>
    <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" prefix="mysite2.yourdomain.com_access_log" suffix=".txt" pattern="%h %l %u %t &quot;%r&quot; %s %b" />
    <Valve className="org.apache.catalina.valves.RemoteIpValve" remoteIpHeader="X-Forwarded-For" protocolHeader="X-Forwarded-Proto" protocolHeaderHttpsValue="https"/>
    </Host>
    ```
4. 编辑 Nginx 配置文件 *default.conf* 文件    
   将下面 **server{ } **配置段，插入到 default.conf 中，并修改其中的 server_name, root, error_log, access_log等
 
    ```
       # server segment template
       server
       {
        listen 80;
        server_name mysite2.yourdomain.com;
        index index.html index.htm index.jsp index.do index.php;
        root  /data/wwwroot/mysite2;
        error_log /var/log/nginx/mysite2.yourdomain.com-error.log crit;
        access_log  /var/log/nginx/mysite2.yourdomain.com-access.log;
        
        #include php.conf;
        include jsp.conf;
        }
    ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/lnmp/java/lnmp-modifynginx001-websoft9.jpg)

4. 保存配置文件，然后在 WinSCP 中运行重启服务命令 或 云控制台重启服务器 ：
    ~~~
    sudo systemctl restart tomcat
    sudo systemctl restart nginx
    ~~~
5. 本地浏览器访问：http://域名 访问你的网站。

### 安装第N个Java应用

安装第 N 个网站与安装第二个网站的操作步骤一模一样

最后我们温故而知新，总结 PHP&Java 双能环境 安装 Java 网站步骤： 

1. 上传网站代码
2. 解析域名（非必要）
3. Tomcat 配置文件中增加 host 配置段
4. Nginx 配置文件中增加 server 配置段
5. 进入应用的安装向导


## 维护 Java 环境

参考本文档相关专题章节：

* [Java 指南](../java) 和 [Java 进阶](../java/advanced) 



