---
sidebar_position: 2
slug: /jenkins/admin
tags:
  - Jenkins
  - DevOps
---

# 维护参考


## 系统参数

在维护 Jenkins 过程中，您可能需要如下的参数：  

### 路径

Jenkins 安装目录： */data/wwwroot/jenkins*  
Jenkins 日志目录： */data/logs/jenkins*  

其他组件：Nginx, Java 等路径

### 端口号

下面列出可能要用到的端口：

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| TCP | 80 | 通过 HTTP 访问 Jenkins | 必选 |
| TCP | 443 | 通过 HTTPS 访问 Jenkins | 可选 |
| TCP | 8080 | Jenkins 网络端口，已通过 Nginx 转发到 80 端口 | 可选 |

### 版本号

```shell
# Check all components version
sudo cat /data/logs/install_version.txt

# Linux Version
lsb_release -a

# Nginx  Version
nginx -V

# Java version
java -v
```

### 服务

Jenkins 的服务如下

```shell
sudo systemctl start jenkins
sudo systemctl stop jenkins
sudo systemctl restart jenkins
sudo systemctl status jenkins
```

## 备份

除通用的备份策略之外，还可以通过 [Backup plugin](https://plugins.jenkins.io/backup/) 备份 Jenkins

## 恢复

## 升级

除通用的升级方案之外，Jenkins 内置升级功能：

1. 登陆Jenkins后台，如果当前版本不是最新的稳定版本，会在右上角警告栏出现提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-warning-websoft9.png)

2. 点击警告，在弹出页面选择自动升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-selectauto-websoft9.png)

3. 在升级页面等待直到自动升级完成
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-autoupdate-websoft9.png)

4. 重启jenkins服务，Jenkins已经更新到最新稳定版  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-updatecok-websoft9.png)


## 故障处理

此处收集使用 Jenkins 过程中最常见的故障，供您参考

> 大部分故障与云平台密切相关，如果你可以确认故障的原因是云平台造成的，请参考[云平台文档](https://support.websoft9.com/docs/faq/zh/tech-instance.html)

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Jenkins服务无法启动？

1. 通过查看服务状态以及日志定位错误原因
   ```
   systemctl status jenkins
   journalctl -xe
   ```
2. 打开日志文件：*/data/logs/jenkins*，检索 **failed** 关键词，分析错误原因

## 常见问题

#### Jenkins 是否支持中文？

支持，可以很方便的切换多语言（包括中文），Jenkins根据浏览器的语言显示文本，详情参照[Jenkins 语言设置](https://www.jenkins.io/doc/book/using/using-local-language/)。

#### Jenkins 是否提供CLI工具？

是，参考 [Jenkins CLI](/zh/solution-cli.md)

#### 如何扩展Jenkins的功能？

安装更多[插件](https://plugins.jenkins.io/)

#### 如果没有域名是否可以部署 Jenkins？

可以，直接通过服务器公网IP访问即可

#### 是否可以修改Jenkins的源码路径？

不可以
