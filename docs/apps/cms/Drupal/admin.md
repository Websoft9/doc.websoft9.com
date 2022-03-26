---
sidebar_position: 3
slug: /drupal/admin
tags:
  - Drupal
  - CMS
  - 建站系统
---

# 维护指南

## 场景

### 备份与恢复

通过安装 Drupal 扩展，可以实现后台在线备份：

1. 下载 [Backup and Migrate](https://www.drupal.org/project/backup_migrate)

2. 登录 Drupal 后台，通过上传压缩文件的方式安装 **Backup and Migrate** ，启用之

3. 打开：【管理】>【配置】，打开【Backup and Migrate】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-backupnow-websoft9.png)

4. 开始设置备份策略

5. 通过 **Backup and Migrate** 实现的备份可以在线恢复


### 升级

Drupal 目前没有提供后台可视化升级，但可以通过命令行的方式升级。

> 在升级之前请做好服务器的快照备份，这个是必须的步骤，因为谁都无法保证升级 100% 成功。

1. 登录 Drupal 后台，如果有升级需求系统会显示升级提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-update-websoft9.png)  

2. 参考官方文档 [Updating Drupal core via Composer](https://www.drupal.org/docs/updating-drupal/updating-drupal-core-via-composer#update-instructions)，完成升级

> 更多升级详情，请参考官方升级文档 [Drupal Upgrade](https://www.drupal.org/docs/updating-drupal)


## 故障速查

#### 初始化过程中的 【安装翻译】这一步骤总是报错？

问题原因：安装翻译过程中需要从网络上下载翻译文件，可能会有网络超时导致错误  
解决方案：重试多次，直至成功


#### Drupal 重定向错误？

多语言下，重定向错误比较常见。例如：打开您的 Drupal 中文版会出现重定向错误

处理办法：分析网站根目录下的 `.htaccess` 文件，看看有没有死循环规则

#### 修改了数据库密码 Drupal 不能访问？

若已完成 Drupal 安装向导，再通过 phpMyAdmin 修改数据库密码，Drupal 就会连不上数据库  

需要修改 [Drupal 配置文件](../drupal#path) 对应的数据库 password 参数即可。

#### Drupal 状态报告中有错误怎么办？（见下图）

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-status-websoft9.png)

请根据提示完成系统升级或设置，不过这个设置不是必须的，此“错误”称之为“警告”更为合适

#### Drupal8.x 版本以上，安装完后提示一个错误 **Protecting against HTTP HOST Header attacks**

解决方法如下：

1. 通过 WinSCP 远程连接上服务器，进入 */data/wwwroot/drupal/sites/default* 目录，将 settings.php 文件下载到本地；

2. 打开文件，找到如下图所示的配置段：
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-settings-1-websoft9.jpg)

3. 修改为如下图所示的配置（域名请根据实际情况更改，注意红框标注的注释符）：
   ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/drupal/drupal-settings-2-websoft9.jpg)

4. 重新上传至原目录下；

5. 执行 *chown -R apache: /data/wwwroot/drupal* 命令，刷新页面，错误提示消失。
   
> 官方参考链接：https://www.drupal.org/docs/8/install/trusted-host-settings

#### Drupal安装后系统提示如下的安全漏洞
settings.php 中的 trusted_host_patterns 设置未配置。这可能导致安全漏洞。强烈建议您配置此项。
解决方案：更多详情请参见 [防止 HTTP HOST 头攻击。](https://www.drupal.org/node/1992030)

## 问题解答

#### Drupal 支持多语言吗？

支持多语言（包含中文），建议在初始化安装的时候安装多语言

#### Drupal(LAMP)，Drupal(LNMP)等商品括号中的 LAMP,LNMP 是什么意思？

LAMP和LNMP代表支持 Drupal 运行所对应的基础环境，具体参考[环境说明](./runtime/php)

#### 是否可以使用云平台的 RDS 作为 Drupal 的数据库？

可以，修改 [Drupal 配置文件](../drupal#path) 即可

#### Drupal能在 Windows 服务器上运行吗？

可以，但是我们推荐在运行 Drupal 效率更高的 Linux 服务器上运行

#### Drupal数据库连接配置信息在哪里？

数据库配置信息 [Drupal 配置文件](../drupal#path)中

#### 如果没有域名是否可以部署 Drupal？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 phpMyAdmin on Docker，访问地址：http://服务器公网IP:9090

#### 如何禁止 phpMyAdmin 访问？

```
sudo docker stop phpmyadmin
```

#### 是否可以修改 Drupal 的源码路径？

可以，通过修改 [虚拟主机配置文件](../apache#virtualHost)中相关参数
