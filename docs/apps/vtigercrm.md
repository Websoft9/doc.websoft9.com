---
title: Vtiger CRM
slug: /vtiger
tags:
  - CRM
  - 客户关系管理
  - 销售管理
---

import Meta from './_include/vtiger.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

1. Websoft9 控制台安装 Vtiger CRM 后，通过 "我的应用" 查看应用详情

   - 在 **访问** 标签页中获取访问信息
   - 在 **数据库** 标签页中获取**数据库账号** 

2. 进入 Vtiger CRM 安装向导，当环境检测步骤通过后，开始填写数据库参数

   - Host Name:  应用管理中获取 
   - User Name: `vtiger`
   - Password: 应用管理中获取
   - Database Name: `vtiger`

3. 然后设置首个管理员账号

4. 依次完成后续设置，进入控制台


## 配置选项{#configs}

- 多语言（√）：需先下载 [Language Pack](https://marketplace.vtiger.com/app/listings)，然后在后台作为 Modules 导入

- 模块导入（√）：**Setting > CRM Setting > Module Management**

- 在线 Marketplace：后台设置 **Extension Store** 进入市场，注册登录后可以在线安装

- SMTP（√）： **Settings > CRM Settings > CONFIGURATION > Outgoing Server**

## 管理维护{#administrator}


## 故障

#### 更换域名后 Vtiger CRM 无法访问？

错误信息：*Invalid compiled template for 'modules/Install/Header.tpl'*  
问题原因：Vtiger CRM 启动后会生成一个记录访问地址的缓存文件    
解决方案：进入 Vtiger CRM 容器，使用下面的命令删除缓存文件  

```
- rm -rf path/test/templates_c/v7
- rm -rf path/vtigercrm/cache/*
```
