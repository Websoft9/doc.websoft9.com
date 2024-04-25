---
title: Magento
slug: /magento
tags:
  - 电子商务
  - 支付
  - 跨境电商
---

import Meta from './_include/magento.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 Magento 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

### 安装插件{#installplugin}

建议通过 Magento 后台在线安装扩展：

1. 确保你的 Magento 已经[连接到官方的 Marketplace](#marketplace)

2. 在 Marketplace 找到您需要的扩展或主题，购买完成，点击【Install】

3. 登录 Magento 后台，打开：【SYSTEM】>【Web Setup Wizard】>【System Configration】 

4. 在左侧菜单栏选择【EXTENSION MANAGER】，单击【Refresh】 将购买信息同步到网站，然后通过【Review and Install】查看

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-theme-1-websoft9.png)

   > Refresh 可能会出现同步失败，请多次刷新

5. 在列表内选择插件或主题，即可进行安装

6. 安装时会进行系统环境检查，条件全面满足才可以开始安装

7. 安装过程时间较长且报错，请查看[故障原因](./magento/admin##updateerror)


### 连接 Magento Marketplace{#marketplace}

安装 Magento 后，建议把你安装的 Magento 系统与 Magento 官方的 Marketplace 资源进行在线连接，这样便可以使用 Marketplace 上的大量资源

![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-setuptools-websoft9.png)  

1. 到官方 [注册 Magento 账号](https://account.magento.com/applications/customer/login)

2. 登录 Marketplace，打到My Profile 的 Access Keys 页面新建一个自己的 Access Key; 
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-smtp-1-websoft9.png)  

3. 保存 Access Key  
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-savemykey-websoft9.png)  

4. 进入 Magento 容器的网站根目录，将 key 复制到 auth.json.example,并重命名为 auth.json 

```
{
    "http-basic": {
        "repo.magento.com": {
            "username": "<public-key>",
            "password": "<private-key>"
        }
    }
}

```

5. 连接后，就可以很方便的使用 Marketplace 上的资源

### 安装中文包{#setlanguage}

Websoft9 已经默认将 Magento 的中文包 zh_Hans_CN 设置好，只需启用即可：

1.  网页后台设置中文：在管理员页面右上角点击你的账户 Account Setting > Interface Local 中设置 Interface Local 为Chinese（China）

2.  网页前台设置中文：
   - 安装前台语言包：
      ```
      docker exec -it magento bash #进入Magento容器
      cd /bitnami/magento/
      php bin/magento config:set --scope=stores --scope-code=default general/locale/code zh_Hans_CN
      php bin/magento cache:clean
      php bin/magento cache:flush
      ```
   - 进入到Magento管理员界面，后台 Stores > Configuration > General > Local 中设置Local为Chinese(China)

### 刷新缓存

Cache（缓存）是 Magento 的一项重要设置：

1. 登录 Magento 后台，依次打开：【System】>【Tools】> 【Cache Management】
2. 选择需要刷新的缓存
3. 点击【Flush Magento Cache】和【Flush Cache Storage】开始刷新
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-flushcache-websoft9.png)
4. 也可以取消一些页面的缓存设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-dscache-websoft9.png)

### 重建索引

索引发生了变化后，可能会报错 One or more indexers are invalid....   

此时，需要重建索引：  

##### 方法1：控制台重置

1.  在管理员页面的左边控制栏点击“SYSTEM”,在弹出的选项中选择Index Management；
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron001.png)

2.  点击图中所示的选项框，选择下拉菜单中的Update by Schedule，然后点击序号4所示的选项框选择Select All，最后单击5所示的Submit即可。

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-cron002.png)

##### 方法2：命令行重置

1. 使用命令行工具 (SSH or Terminal)进入magento安装根目录：cd /data/wwwroot/magento/bin

2. 重新编制索引：php magento indexer:reindex

## 配置选项{#configs}

- 命令行： `magento list`
- [API](https://devdocs.magento.com/guides/v2.2/get-started/bk-get-started-api.html)
- 多语言（✅）：需下载语言包后导入

## 管理维护{#administrator}

### 配置 SMTP{#smtp}
     
请参照官方的 [SMTP 配置方案](https://experienceleague.adobe.com/zh-hans/docs/commerce-admin/systems/communications/email-communications)

### 更换 URL{#url}

域名更换后，需通过 CLI 更新 Magento URL:
   
   ```shell
   php bin/magento config:set web/unsecure/base_url http://www.mydomain.com/ # 修改成您的实际域名，必须以 / 结束
   php bin/magento config:set web/secure/base_url http://www.mydomain.com/ # 修改成您的实际域名，必须以 / 结束
   ```

### HTTPS 额外设置{#https}

通过 Websoft9 网关为 Magento 配置 HTTPS 后，还需运行 CLI 命令进行配置：

```
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/"
php bin/magento cache:flush  #将基础URL更改为https并刷新缓存
```

### 备份

Magento 支持在线备份方案：

1. 登录到 Magento 后台，依次打开：【System】>【System Backup】，设置备份
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-backup-websoft9.png)

2. 将备份加入到计划任务中

   - 登录 Magento 后台，依次打开：【Stores】>【Configuration】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-bkscheduleset-websoft9.png)

   - System】>【Backup Settings】，设置计划任务
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-bkschedulesets-websoft9.png)

### 升级

Magento 可以通过两种方式升级：后台升级界面和 Composer 升级命令。  

下面介绍后台升级界面升级步骤：

1. 以管理身份登录 Magento，依次打开：【System】>【Web Setup Wizard】>【System Upgrade】 
   ![Magento upgrade](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestart-websoft9.png)

2. 如果没有连接 Marketplace，系统会要求你输入 Access key
   ![Magento connect Marketplace](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestartkey-websoft9.png)

3. 点击升级按钮，开始在线升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-sysupgradestarting-websoft9.png)

## 故障

#### 线升级或在线安装插件报错？{#updateerror}

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-upgrade-dependency.png)

如果升级过程若报错，最可能的原因是内存不足，一方面需要保证服务器内存不低于 4G，另一方面需要修改 Magento 根目录下的 `.htaccess` 文件。

其中的 `php_value memory_limit` 不低于 2048M

    ```
        php_value memory_limit 2048M
        php_value max_execution_time 18000
    ```

#### Cron job 告警？

错误：**One or more indexers are invalid. Make sure your Magento cron job is running**   
方案：需重建索引后在后台刷新页面
  ```
  php bin/magento indexer:reindex
  ```

#### Magento 运行很慢？

Magento 是一个复杂的企业级电商系统，对计算资源要求较高

#### 找不到后台登陆地址？

进入 Magento 容器，通过命令一下命令查看或修改：  

```shell
# Show Magento(URL)
php bin/magento info:adminuri

# Update Magento(URL)
php bin/magento setup:config:set --backend-frontname=[yourAdminUrl] -n
```

#### 跳过登陆时的邮件验证？

关闭密码邮件**双重认证**，通过密码即可登陆：

```shell
# Close Magento_TwoFactorAuth
php bin/magento module:disable Magento_TwoFactorAuth
```
#### 重定向导致无法访问？

**现象描述**：错误信息为 ERR_TOO_MANY_REDIRECTS magento admin     
**原因分析**：如果排除 '.htaccess' 文件中的重定向问题，那么最有可能是 URL 导致的   
**解决方案**：通过命令行或  **core_config_data** 数据表修改 URL   

```shell
php bin/magento setup:store-config:set --use-secure=1 --use-secure-admin=1 --base-url-secure="https://www.yourdomain.com/"
php bin/magento cache:flush  #将基础URL更改为https并刷新缓存
```

#### 设置 HTTPS 后，页面混乱？

问题：设置 HTTPS 之后，网站可以访问，但是出现页面混乱的情况。  
原因：在确定配置文件正常后，可以通过【重新发布】来处理（建议先备份）
解决方案：

1. 开启维护模式
2. 删除静态文件和缓存文件
3. 更新数据库以及重新编译
4. 重新 deploy 静态文件
5. 更新索引，刷新缓存，关闭维护模式
    ```shell
    php bin/magento maintenance:enable
    php rm -rf var/di/* && rm -rf var/generation/* && rm -rf var/cache/* && rm -rf var/page_cache/* && rm -rf var/view_preprocessed/* && rm -rf pub/static/* && rm -rf generated/* 
    php bin/magento setup:upgrade 
    php bin/magento setup:di:compile
    php bin/magento setup:static-content:deploy -f
    php bin/magento indexer:reindex
    php bin/magento cache:clean && bin/magento cache:flush
    php bin/magento maintenance:disable 
    ```

#### 商品属性不能正常显示？

Magento 允许用户通过后台“STORES”->"Attributes"->"Product"添加额外的商品属性。  

添加的额外属性的属性值设置不正确就会影响前台的商品展示，出现如图错误。  

  ![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-products-matching-the-selection-websoft9.png)


通过以下步骤可以排查此问题：

1. 查看日志，是否是添加的属性引发的异常，本例中查看到“eanl3”属性有异常

   ![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-log-websoft9.png)

2. 进入后：“STORES”->"Attributes"->"Product"，查看相关属性设置.

   ![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-product-attribute-websoft9.png)

3. 在属性列表中点击“ean13”，进入设置界面

   ![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-product-attribute1-websoft9.png)

4. 属性设置

   ![magento](https://libs.websoft9.com/Websoft9/DocsPicture/zh/magento/magento-product-attribute2-websoft9.png)

5. 清空浏览器缓存，重新打开网站
