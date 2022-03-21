---
sidebar_position: 2
slug: /jenkins/admin
tags:
  - Jenkins
  - DevOps
---

# 维护参考

## 备份与恢复

[Backup plugin](https://plugins.jenkins.io/backup/) 提供对 Jenkins 的备份和恢复功能。  

## 升级

Jenkins 内置升级功能，操作简单：

1. 登陆Jenkins后台，如果当前版本不是最新的稳定版本，会在右上角警告栏出现提示
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-warning-websoft9.png)

2. 点击警告，在弹出页面选择自动升级
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-selectauto-websoft9.png)

3. 在升级页面等待直到自动升级完成
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-autoupdate-websoft9.png)

4. 重启jenkins服务，Jenkins已经更新到最新稳定版  
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/jenkins/jenkins-updatecok-websoft9.png)

## 参数

Jenkins 应用中包含：Nginx, Java, Docker, MySQL 等基础架构组件，通过：**[通用参数表](../setup/parameter)** 查看。  

下面仅列出 Jenkins 本身的参数：

##### 端口

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 8080   | Jenkins 原始端口，已通过 Nginx 转发到 80 端口 | 可选   |


##### 版本

```shell
jenkins -v
```

##### 服务

```shell
sudo systemctl start | stop | restart | status jenkins
```

##### 命令行

```shell
jenkins -h
```

## 故障速查

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

## 问题解答

#### Jenkins 是否支持中文？

支持，可以很方便的切换多语言（包括中文），Jenkins根据浏览器的语言显示文本，详情参照[Jenkins 语言设置](https://www.jenkins.io/doc/book/using/using-local-language/)。

#### Jenkins 是否提供CLI工具？

是，参考 [Jenkins CLI](/zh/solution-cli.md)

#### 如何扩展 Jenkins 的功能？

安装更多[插件](https://plugins.jenkins.io/)
