---
title: Prestashop
slug: /prestashop
tags:
  - PrestaShop
  - 电子商务
  - 建站
  - 跨境电商
---

import Meta from './_include/prestashop.md';

<Meta name="meta" />

## 入门指南{#guide}

### 登录后台修正 URL{#url}

1. Websoft9 控制台安装 Prestashop 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。 

2. 登录到 Prestashop 后台
   ![](./assets/prestashop-backend-websoft9.png)

3. 点击左侧菜单 "Shop Parameters" 项，在页面中下拉到 "Set shop URL" 设置项

4. 如果是域名访问 Prestashop，请去掉默认 URL 中的端口，"保存" 后生效

### 从 Marketplace 安装扩展

Prestashop8.0 不支持后台在线连接 Marketplace，故安装市场的扩展需：购买 > 下载扩展包 > 后台导入

## 配置选项{#configs}

- 维护模式（√）："Shop Parameters" > "General" >  "Maintenance"
- 扩展市场（√）
- SMTP（√）："Advanced Parameters" > "Email"
- 演示数据导入（√）："Advanced Parameters" > "Import"
- 在线安装扩展（√）：支持在线安装、卸载和升级扩展
- 多语言（√）
- 在线导入语言（√）："International" > "Translations" >  "Add / Update a language"，暂无**中文**导入选型
- 开发者模式（√）
- URL 更新：左侧菜单 "Shop Parameters" 项，在页面中下拉到 "Set shop URL" 设置项
- 后台登录地址：通过 Websoft9 控制台我的应用查看
- CLI
  ```
  # list all cli
  php bin/console list

  # get help of prestashop:config
  php bin/console prestashop:config -h
  ```

## 管理维护{#administrator}
     

### 数据库备份

PrestaShop 提供了后台数据库备份功能："Advanced Parameters" > "SQL Manager"

### 在线升级

PrestaShop 模块管理中，安装并启用 **1-Click Upgrade**


## 故障

#### 访问 PrestaShop 总出现端口？

需登录后台后[修正 URL](#url)

#### 配置 HTTPS 后，前台访问失败？ 

将数据库表 ps_configuration 属性 PS_SSL_ENABLED_EVERYWHERE 和 PS_SSL_ENABLED 值设为 1

#### Prestashop 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的 Prestashop 商店中文版会出现重定向

处理办法：

1. 分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则
2. 删除自行安装的语言包。再次重新导入，Prestashop 会自动生成伪静态规则，覆盖原有 `.htaccess` 文件