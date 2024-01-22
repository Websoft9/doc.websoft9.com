---
sidebar_position: 7
slug: /function/git
---

# 仓库

Websoft9 遵循 [GitOps](https://about.gitlab.com/topics/gitops/) 思想，集成 Gitea 作为引用编排的管理平台，100% 保持其原生性。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/websoft9/websoft9-git.png)

[Gitea](https://docs.gitea.com/)  是一个开源的自托管Git服务，它是用 Go 语言编写的。它旨在提供一个简单、轻量级和可扩展的方式来设置你自己的 Git 服务。它提供了一个简洁的用户界面，使得用户可以轻松地浏览仓库、提交、分支和更多功能。

## 操作

### 编辑/上传应用文件

可以编辑应用已有的文件，也可以上传或删除文件，即使进行了错误的操作，还可以很方便的复原

### 新建 Repository

可以新增一个与应用毫无关系的 Repository，然后基于它做 Issue 管理，可以作为一种很好的知识协作。

## 常见问题

#### 改错应用编排文件，可以恢复吗？

可以很方便的对任何每一次修改进行恢复

#### 可以增加邮件地址吗？

可以，但不能更换主邮件地址后将安装时的邮件地址删除

#### 仓库还有其他用途吗？

您可以灵活使用仓库做任何知识协作的事情，包括问题管理、wiki、代码管理等