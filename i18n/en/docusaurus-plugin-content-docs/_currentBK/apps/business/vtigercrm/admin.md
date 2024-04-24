---
sidebar_position: 3
slug: /vtiger/admin
tags:
  - VtigerCRM
  - CRM
  - 客户成功
---

# VtigerCRM Maintenance

This chapter is special guide for VtigerCRM maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

### VtigerCRM Upgrade

VtigerCRM 自身提供了升级功能和[升级文档](http://community.vtiger.com/help/vtigercrm/administrators/migration.html)，具体操作如下：

1. 到 VtigerCRM 官网[下载升级包](https://www.vtiger.com/open-source-crm/download-open-source/)（注意：是升级包，不是最新的软件包）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-dlupgradepack-websoft9.png)
   
   > 如果下载不到匹配的升级包，升级就无法进行。
  
2. 将下载包解压后，通过 SFTP 上传到 VtigerCRM 根目录（*data/wwwroot/defualt/vtigercrm*）
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/vtigercrm/vtigercrm-unzippatch-websoft9.png)

3. 运行一条修改文件权限的命令：
    ~~~
    chown -R apache.apache /data/wwwroot
    ~~~

4.  浏览器访问：http://服务器公网IP地址/migrate 开始升级流程


## Troubleshoot{#troubleshoot}

In addition to the VtigerCRM issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### 更换服务器IP，VtigerCRM 无法访问？

错误信息：*Invalid compiled template for 'modules/Install/Header.tpl'*  
问题原因：VtigerCRM 启动后会生成一个记录服务器IP地址的缓存文件    
解决方案：使用下面的命令删除缓存文件  

```
- rm -rf /data/wwwroot/vtigercrm/test/templates_c/v7
- rm -rf /data/wwwroot/vtigercrm/cache/*
```

## FAQ{#faq}

#### 能推荐 VtigerCRM 实施商吗？

[TMC](https://www.louishe.com/) 是 SuiteCRM、ODOO、VtigerCRM 、Sugar CRM 金牌技术服务商，一家提供企业管理咨询和 ERP 信息化解决方案的专业顾问公司，在国内外拥有众多 ERP（企业资源管理）、CRM（客户资源管理）成功案例及行业解决方案。

