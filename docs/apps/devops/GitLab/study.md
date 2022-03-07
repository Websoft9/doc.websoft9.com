---
sidebar_position: 3
slug: /gitlab/study
tags:
  - Gitlab
  - DevOps
---

# 原理学习

本GitLab采用 [Omnibus GitLab包](https://gitlab.com/gitlab-org/omnibus-gitlab) 的安装方式。Omnibus GitLab 是官方推荐的一种安装方法，它自带了 GitLab 所需的所有组件和服务，并可以省去繁琐的配置，同时它自带 CLI 工具，便于 GitLab 升级和维护。

### 架构

下面是一个简化的架构图，可用于了解GitLab的架构。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/gitlab/architecture_simplified.png)

## 组件和版本

GitLab 包含数十种组件([查看](https://docs.gitlab.com/ee/development/architecture.html#component-list))，通过 */opt/gitlab/version-manifest.txt* 查看服务器上所有组件名称和版本