---
sidebar_position: 3
slug: /codeserver/admin
tags:
  - code-server
  - Online Code Editor
---

# code-server Maintenance

This chapter is special guide for code-server maintenance and settings. And you can refer to [Administrator](../administrator) and [Steps after installing](../install/setup) for some general settings that including: **Configure Domain, HTTPS Setting, Migration, Web Server configuration, Docker Setting, Database connection, Backup & Restore...**  

## Maintenance guide

## Troubleshoot{#troubleshoot}

In addition to the code-server issues listed below, you can refer to [Troubleshoot + FAQ](../troubleshoot) to get more.  

#### Insufficient file permissions for files created by code-server?

You can run below command to solve file permission issue

```
chown -R docker.docker /data/wwwroot/codeserver/volumes/config/workspace
```

## FAQ{#faq}

#### code-server 容器默认预装哪些组件？

code-server 容器默认已经运行 Node, Yarn, Git等工具，可以很方便的配合 code-server 进行 Node 相关程序的开发。 

#### code-server is powered by Microsoft?

No, is powered by [CODER](https://coder.com/)

#### Does code-server support multiple accounts?

No, but you can deploy multiple code-server for different user, refer to: [解决方案](../codeserver#multi-developer)

#### Can I install extension for code-server?

Yes

#### 如何退出 code-server 界面？

打开控制台左上角菜单，点击【Log out】即可退出

#### Can I reset password of code-server by command?

No, you should reset password by re-create code-server container

