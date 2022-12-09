---
sidebar_position: 2
slug: /gitlab/solution
tags:
  - Gitlab
  - DevOps
---

# 场景方案

GitLab 可以与其他的软件平台集成一起使用，解决 DevOps 过程中的各种[场景问题](https://docs.gitlab.com/ee/integration/)。

## GitLab 集成 Jenkins

GitLab 集成  [Jenkins](../jenkins) {#gitlab-jenkins} 能让 DevOps 更加得心应手。主要过程是当代码出现变更时，由gitlab将事件通知给jenkins，从而触发jenkins执行构建操作。其中关键过程有：
 - Jenkins 开启 Gitlab 插件
 - Gitlab 设置外发请求
 - 配置 Gitlab API访问认证及操作权限

>更加详细的内容请参照[官方文档](https://docs.gitlab.com/ee/integration/jenkins.html)。

