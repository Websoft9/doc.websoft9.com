---
sidebar_position: 3
slug: /metabase/admin
tags:
  - Metabase
  - 大数据分析
  - BI
---

# 维护指南

## 场景

### 升级

Metabase 有升级包的时候，后台会及时给出提示。参考下面的步骤完成升级：

1. Metabase 后台->设置->升级，如果有新的升级包，系统会给与提示
   ![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereminder-websoft9.png)

2. 点击“更新”按钮后，系统会跳转到 Metabase 官方的安装页面。
3. 我们提供的部署包采用的是 jar 包安装模式，因此在安装页面我们选择“Custom install”模式，
   ![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatedl-websoft9.png)

4. 下载 Metabase.jar 包后，上传到服务器 `/data/wwwroot/metabase`, 覆盖已有的同名文件
   ![Metabase升级提示](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereplace-websoft9.png)

5. 重新加载 Metabase，升级成功

## 故障速查

除以下列出的 Metabase 故障问题之外， [通用故障处理](../troubleshooting) 专题章节提供了更多的故障方案。

## 问题解答

#### Metabase 支持多语言吗？

支持多语言（包含中文），系统默认根据浏览器自动选择语言

#### Metabase 数据库连接配置信息在哪里？

数据库配置信息在 Metabase 安装目录下的 _metabase.conf_ 中

#### 如果没有域名是否可以部署 Metabase？

可以，访问`http://服务器公网IP` 即可

#### 数据库 root 用户对应的密码是多少？

密码存放在服务器相关文件中：`/credentials/password.txt`

#### 是否有可视化的数据库管理工具？

有，内置 phpMyAdmin，访问地址：http://服务器公网 IP:9090

#### 如何禁止 phpMyAdmin 访问？

关闭服务器安全组的 9090 端口即可禁止

#### 是否可以修改 Metabase 的源码路径？

可以，通过修改 Nginx 虚拟主机配置文件中相关参数

#### 如何修改上传的文件权限?

```shell
chown -R nginx.nginx /data/wwwroot/metabase
find /data/wwwroot/metabase -type d -exec chmod 750 {} \;
find /data/wwwroot/metabase -type f -exec chmod 640 {} \;
```
