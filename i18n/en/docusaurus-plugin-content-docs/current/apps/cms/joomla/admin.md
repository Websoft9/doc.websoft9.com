---
sidebar_position: 3
slug: /joomla/admin
tags:
  - Joomla
  - CMS
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup/) 相关章节。

## 场景

### 在线备份

通过安装 Joomla 扩展，可以实现后台在线备份：

1. 下载 [Akeeda](https://www.akeebabackup.com/download.html)

2. 登录 Joomla 后台，通过上传压缩文件的方式安装 **Akeeda** 

3. 打开：【Dashboard】>【System】>【Control Panel】，找到【Backup is up-to-date】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-backup-websoft9.png)

4. 开始设置备份策略

5. 通过 Akeeda 实现的备份可以在线恢复
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-restore-websoft9.


### 在线升级

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


## 故障排除

除以下列出的 Joomla 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

## 问题解答

#### Joomla 支持多语言吗？

支持多语言（包含中文），建议在初始化安装的时候安装多语言

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

#### 如何设置数据库默认连接？

向文件 *path/joomla/installation/model/forms/database.xml* 中，添加 default="xxxx" 即可