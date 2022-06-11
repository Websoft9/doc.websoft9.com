---
sidebar_position: 3
slug: /joomla/admin
tags:
  - Joomla
  - CMS
---

# Joomla Maintenance

This chapter is special guide for Joomla maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### Backup and Restore

This section provides Joomla online backup solution

1. Download extension [Akeeda](https://www.akeebabackup.com/download.html)

2. Log in Joomla console as administrator, install **Akeeka** by uploading package

3. Go to【Dashboard】>【System】>【Control Panel】, find 【Backup is up-to-date】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-backup-websoft9.png)

4. Set the backup

5. You can **Restore** Joomla with **Akeeda** also
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-restore-websoft9.png)  

### Upgrade

Joomla provides a very user-friendly upgrade (update) portal

> Please completed backup of Server before any upgrade of Joomla

1. Log in Joomla backend, you can see the upgrade reminder when have latest version
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkupgradets-websoft9.png)  

2. Go to the upgrade interface, check the upgrade requirement and start to upgrade
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-update003-websoft9.png)

3. Upgrading, wait for it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-update004-websoft9.PNG)

4. Upgrade successfully
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-update005-websoft9.PNG)

5. You can upgrade extension of Joomla also
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/joomla/joomla-bkextupgrade-websoft9.png)


## Troubleshoot{#troubleshoot}

In addition to the Joomla issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

## FAQ{#faq}

#### Joomla support multi-language?

Yes

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
