---
sidebar_position: 1
slug: /iis
---

# IIS

IIS即Windows®Server的Internet信息服务，它是一种灵活，安全和可管理的Web服务器，用于托管Web上的任何内容。 从媒体流到Web应用程序，IIS的可扩展和开放的架构已经准备好处理最苛刻的任务。由于IIS的可视化配置界面，使得在此环境中增加和管理网站变得非常容易。

![](https://oss.aliyuncs.com/photogallery/photo/1904996544835414/4734/9207f5e7-e626-4afa-ac19-8c44ad2b315b.png)

## 修改网站根目录

也许你希望将网站根目录设置到D盘或不喜欢现在根目录的位置，这个时候就需要修改网站默认根目录了。IIS环境的根目录是可以被修改的，具体只需2个步骤：

*   打开IIS，邮件点击Default Web Site，依次选择管理网站-高级设置， ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-changeroot-websoft9.png)
*   将物理路径修改为新的路径即可（要提前将wwwroot内容拷贝到新目录）
*   重启IIS后生效

## IIS重启

进入IIS，点击主机名称，右侧的操作就会显示重启启动，停止等操作

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-restart-websoft9.png)

## 如何发布PHP应用？

IIS环境中部署网站主要分为5个步骤： **①**上传网站代码-&gt;**②**配置域名（非必要）-&gt;**③**增加网站对应的数据库（非必要）-&gt;**⑤**完成安装向导

注意：部署一个网站还是多个网站、有无域名这两种情况对应的部署操作细节略有不一样，下面分别说明： 

### 场景一：服务器只安装一个网站

如果您打算此服务器上只部署一个网站或应用，建议采用此方式：

1. 远程桌面到Windows服务器，将网站源文件拷贝到根目录
2. 如果没有可用域名，请直接通过 [http://公网IP](http://公网IP) 的方式来访问应用
3. 如果有可用的域名，请完成 **《域名配置》** 后通过 [http://公网IP](http://公网IP)  的方式来访问应用
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

网站默认根目录为：C:\inetpub\wwwroot

### 场景二：服务器部署多个网站（无域名）

无域名情况下，以部署两个网站为例，具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 通IIS增加一个虚拟目录或应用程序 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1-websoft9.png)
3. 通过 [http://ip/mysite1](http://ip/mysite1) 的方式来访问应用，即可访问mysite1
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤同样

网站默认根目录为：C:\inetpub\wwwroot

### 场景三：服务器部署多个网站（共用一个域名）

共用一个域名情况下（即每个网站都打算以 [http://域名/mysite1](http://域名/mysite1) 这样的方式访问），以部署两个网站为例，具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 通IIS增加一个虚拟目录或应用程序 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1-websoft9.png)
3. 完成 **《域名配置》** 后通过 [http://域名/mysite1](http://域名/mysite1) 的方式来访问应用
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤同样

网站默认根目录为：C:\inetpub\wwwroot

### 场景四：服务器部署多个网站（多个域名）

多个域名下（即每个网站都有自己的域名），以部署一个网站为例（假设域名为www.abc.com），具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 提前将您的域名**www.abc.com**解析到服务器公网IP地址，并确保已经解析成功
3. 打开IIS-网站-添加网站，参考下图完成路径、域名填写，然后保存 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1d-websoft9.png)
4. 通过 [http://域名/](http://域名/)_** **_的方式来访问应用
5. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤和部署一个网站的一样。

网站默认根目录为：C:\inetpub\wwwroot

## 如何发布ASP.NET应用？

IIS环境中部署网站主要分为5个步骤： **①**上传网站代码-&gt;**②**配置域名（非必要）-&gt;**③**增加网站对应的数据库（非必要）-&gt;**⑤**完成安装向导

注意：部署一个网站还是多个网站、有无域名这两种情况对应的部署操作细节略有不一样，下面分别说明：

### 场景一：服务器只安装一个网站

如果您打算此服务器上只部署一个网站或应用，建议采用此方式：

1. 远程桌面到Windows服务器，将网站源文件拷贝到根目录
2. 如果没有可用域名，请直接通过 [http://公网IP](http://公网IP) 的方式来访问应用
3. 如果有可用的域名，请完成 **《域名配置》** 后通过 [http://公网IP](http://公网IP) 的方式来访问应用
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过[http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

网站默认根目录为：C:\inetpub\wwwroot

### 场景二：服务器部署多个网站（无域名）

无域名情况下，以部署两个网站为例，具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 通IIS增加一个虚拟目录或应用程序 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1-websoft9.png)
3. 通过 [http://ip/mysite1](http://ip/mysite1)  的方式来访问应用，即可访问mysite1
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过 [http://ip/phpmyadmin](http://ip/phpmyadmin)  创建数据库

安装第二个网站**mysite2**，操作步骤同样

网站默认根目录为：C:\inetpub\wwwroot

### 场景三：服务器部署多个网站（共用一个域名）

共用一个域名情况下（即每个网站都打算以 [http://域名/mysite1](http://域名/mysite1) 这样的方式访问），以部署两个网站为例，具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 通IIS增加一个虚拟目录或应用程序 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1-websoft9.png)
3. 完成 **《域名配置》** 后通过 [http://域名/mysite1](http://域名/mysite1) 的方式来访问应用
4. 如果在安装向导过程中提示数据库无法自动创建，需要通过 [http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤同样

网站默认根目录为：C:\inetpub\wwwroot

### 场景四：服务器部署多个网站（多个域名）

多个域名下（即每个网站都有自己的域名），以部署一个网站为例（假设域名为www.abc.com），具体操作如下：

1. 远程桌面到Windows服务器，将第一个网站目录上传到根目录下面，假设应用程序目录命为“mysite1”
2. 提前将您的域名 **www.abc.com** 解析到服务器公网IP地址，并确保已经解析成功
3. 打开IIS-网站-添加网站，参考下图完成路径、域名填写，然后保存 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-addsite1d-websoft9.png)
4. 通过 [http://域名/](http://域名/) 的方式来访问应用
5. 如果在安装向导过程中提示数据库无法自动创建，需要通过 [http://ip/phpmyadmin](http://ip/phpmyadmin) 创建数据库

安装第二个网站**mysite2**，操作步骤和部署第一个网站的步骤一样。

网站默认根目录为：C:\inetpub\wwwroot

## 如何发布Java应用？

* tomcat 路径:`C:\websoft9\Tomcat8.5`
* JDK 路径:`C:\Program Files\Java`
* 网站存储路径 `C:\inetpub\wwwroot`

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


## IIS SSL 配置 

### 腾讯申请的免费证书配置


腾讯免费证书申请成功后下载证书为一个压缩包,解压后内容大致如图所示:(test.websoft9.cn为测试域名)

![1523418632922](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX1-websoft9.png)



进入 IIS 文件夹内容如下:

![1523418668438](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX2-websoft9.png)

打开 IIS 开始导入证书 

![1523428081837](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX3-websoft9.PNG)



![1523428307113](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX4-websoft9.png)



导入成功

![1523428321945](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX5-websoft9.png)

给站点配置SSL证书

![1523428488886](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX6-websoft9.png)

![f1523428617943](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-SSL-TX7-websoft9.png)

最后在浏览器上测试 `https://域名` 是否配置成功



### 阿里云免费证书配置

免费申请阿里云证书成功后,配置可以直接参考阿里提供的方案进行操作

![1523432385204](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-Aliyun-websoft9.png)




### 使用let's encrypt自动配置证书

前往 `https://github.com/PKISharp/win-acme/releases`下载程序 

![1523429626325](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt1-websoft9.png)

下载好后解压

![1523429704719](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt2-websoft9.png)

将解压出的文件夹 复制到 `C:\Program Files` (目录可以随意设置,建议存放在这个目录下,配置好证书后程序切勿删除)

![1523429808764](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt3-websoft9.png)



进入程序目录,内容大致如下:

![1523429865345](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt4-websoft9.png)



创建证书,输入`N`

![1523430024664](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt5-websoft9.png)



绑定单个IIS站点

![1523430136570](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt6-websoft9.png)



这里会列出当前IIS上已有的站点根据序号选择需要配置SSL的站点

![1523430270351](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt7-websoft9.png)

配置成功,如图所示:(到这一步后先别关闭这个窗口)

![1523430320474](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt8-websoft9.png)





打开IIS 检测ssl是否配置成功 

![1523430359697](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt9-websoft9.png)

浏览器在测试SSL是否配置成功



设置自动续订(如果之前窗口关闭了,重新打开程序输入`L`)

![1523430513122](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt10-websoft9.png)



选择需要自动续订证书的站点

![1523430937571](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt11-websoft9.png)

自动续订成功

![1523431002175](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/IIS-lets-encrypt12-websoft9.png)

## 如何设置HTTP自动跳转HTTPS？
### 1. 安装 URL 重写模块
访问[IIS官方下载页面](https://www.iis.net/downloads/microsoft/url-rewrite)，下载对应版本的安装文件进行安装。
### 2. 设置自动跳转
#### 2.1 示例一：http://www.example.com 跳转到 https://www.example.com
a. 在需要跳转的网站上，双击“url 重写”；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-1-websoft9.png)
b. 添加空白规则；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-2-websoft9.png)
c. 添加 URL 重写规则；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-3-websoft9.png)
d. 继续添加；
    ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-4-websoft9.png)
e. 继续添加 URL 重写规则；
     ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrewrite-5-websoft9.png)
f. 最后一步，单击右边的“应用”按钮，不需重启 IIS 服务，即可测试是否自动跳转了。
#### 2.2 示例二：不带 www 的域名跳转至 www 域名
如果您的 www.example.com 用的不是通配证书，则如示例一设置跳转后，还需按照示例二进行设置。
a. 在IIS中新建站点时，确保绑定域名 [example.com](example.com) 和 [www.example.cm](www.example.cm)；
a. 进入 URL 重写模块，添加规则（操作和示例一相同）；
b. 添加规则时选择**规范域名**，确定进入下一步；
c. 选择主域名即需要重定向的域名；
d. 完成后访问 [example.com](example.com) 即可跳转至 [www.example.cm](www.example.cm)，如果 [www.example.cm](www.example.cm) 设置了 https 自动跳转，则访问 [example.cm](example.cm) 会直接跳转到 [https://www.example.com](https://www.example.com)

## 如何设置伪静态？

本镜像默认安装了针对于IIS伪静态设置的“**URL重写**”组件，下面以Wordpress为例描述如何设置伪静态：

1.  进入IIS后选择具体的网站，打开URL重写工具 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-urlrew-websoft9.png)
2.  依次添加规则
3.  重启IIS后生效

## 编辑网站绑定

请远程登录到Windows服务器后，修改IIS下对应的网站的域名绑定，具体如下：

*   打开IIS，右键点击需要配置域名的网站，选择“编辑绑定”，系统弹出网站绑定列表。选择一个没用绑定域名的网站后，点击“编辑” 按钮 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-adddomain001-websoft9.png)
*   在主机名处填写域名，然后保存 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/iis/iis-adddomain002-websoft9.png)
*   需要增加多个域名，请在第一步选择“添加”按钮

**说明**：如果你计划在服务器上增加多个应用，本步骤是必要的
