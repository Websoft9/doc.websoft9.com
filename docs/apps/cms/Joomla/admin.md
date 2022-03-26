---
sidebar_position: 3
slug: /joomla/admin
tags:
  - Joomla
  - CMS
---

# 维护指南

## 场景

### 备份与恢复

通过安装 Joomla 扩展，可以实现后台在线备份：

1. 下载 [Akeeda](https://www.akeebabackup.com/download.html)

2. 登录 Joomla 后台，通过上传压缩文件的方式安装 **Akeeda** 

3. 打开：【Dashboard】>【System】>【Control Panel】，找到【Backup is up-to-date】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-backup-websoft9.png)

4. 开始设置备份策略

5. 通过 Akeeda 实现的备份可以在线恢复
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-restore-websoft9.


### 升级

Joomla 提供了非常人性化的在线升级方案，根据系统的更新提示完成升级

> 在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级 100% 成功。

1. 登录 Joomla 后台，如果有升级需求系统会显示升级提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkupgradets-websoft9.png)  

2. 根据提示进入升级中心，确认是否具备升级条件
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-update003-websoft9.png)

3. 升级中，请耐心等待
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-update004-websoft9.PNG)

4. 升级成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-update005-websoft9.PNG)

5. 扩展也可以在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/joomla/joomla-bkextupgrade-websoft9.png)


> 更多升级详情，请参考官方升级文档 [Joomla Upgrading](https://docs.joomla.org/Portal:Upgrading_Versions/zh-cn)


## 故障速查

除以下列出的 Joomla 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。 

#### Joomla 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的 Joomla 中文版会出现重定向错误

处理办法：分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### 修改了数据库密码 Joomla 不能访问？

若已完成 Joomla 安装向导，再通过 phpMyAdmin 修改数据库密码，Joomla 就会连不上数据库  

需要修改 [Joomla 配置文件](../joomla#path) 对应的数据库 password 参数即可。


## 问题解答

#### Joomla 支持多语言吗？

支持多语言（包含中文），建议在初始化安装的时候安装多语言

#### Joomla(LAMP)，Joomla(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持 Joomla 运行所对应的基础环境，具体参考[环境说明](./runtime/php)

#### 是否可以使用云平台的 RDS 作为 Joomla 的数据库？

可以，修改 [Joomla 配置文件](../joomla#path) 即可

#### Joomla能在 Windows 服务器上运行吗？

可以，但是我们推荐在运行 Joomla 效率更高的 Linux 服务器上运行

#### Joomla数据库连接配置信息在哪里？

数据库配置信息 [Joomla 配置文件](../joomla#path)中

#### 如果没有域名是否可以部署 Joomla？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置phpMyAdmin，访问地址：http://服务器公网IP:9090

#### 如何禁止phpMyAdmin访问？

连接服务器，编辑 phpMyAdmin 配置文件，将其中的 Require all granted 更改为 Require ip 192.160.1.0，然后重启 Apache 服务

#### 在组件中如何加载其他扩展的语言文件?

开发一个Joomla投稿组件的时候，需要调用joomla文章组件的语言文件，因为界面很多字符串都来自系统的文章组件，本来打算直接将系统的文章组件的语言文件直接复制一份的，但感觉那样做不优雅，因此，查了一下源码，发现是Joomla是可以在任何时间，任何地方调用任何组件的语言文件的。

直接上代码了，并不难理解

~~~
`$lang` `= JFactory::getLanguage();`

`$extension` `= ``'com_content'``;`

`$base_dir` `= JPATH_ADMINISTRATOR;`

`$language_tag` `= ``'zh-CN'``;`

`$reload` `= true;`

`$lang``->load(``$extension``, ``$base_dir``, ``$language_tag``, ``$reload``);`
~~~

上面的代码没有什么好解释的。需要什么扩展就将extension变量赋值即可。

#### 是否可以修改 Joomla 的源码路径？

可以，通过修改 [虚拟主机配置文件](../apache#virtualHost)中相关参数