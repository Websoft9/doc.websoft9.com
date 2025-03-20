---
sidebar_position: 1
slug: /developer/architecture
---

# 架构

Websoft9 是一个以应用为中心的微服务架构模式，它入门极简，扩展能力极强。  

## 架构哲学

**"一切皆应用，一切可组装"** 是 Websoft9 的根本哲学思想，基于这个哲学思想，我们灵活的将优秀的开源软件融合到产品体系中。  

我们的架构中遵循一些主要的技术思想：

- 通过组装实现产品创新
- [云原生 12 要素](https://12factor.net/zh_cn/)
- 开源迭代，持续演化
- 专注于连接，减少非必要的原创组件
- 使用已经流行的技术要素，避免再创造新的技术规范
- GitOps 云原生持续交付模型
- Unix 哲学 KISS 原则： Keep It Simple, Stupid!

## 架构图

我们采用的技术要素包括：Linux, Docker, K8s, API 网关，服务发现，应用网关，应用编排，Git等。  

对应的产品架构图如下：  

![](/img/websoft9-architecture.png)


- Apphub：应用管理服务，负责应用整个生命周期
- Git：应用安装模板的仓库，实现先申明、再部署的模式
- Deployment：负责与 Docker, K8s 交付的部署工作模块，同时提供可视化的管理容器的界面
- App Gateway：发布和控制应用的访问

## 开放兼容

Websoft9 采用 [Docker Compose](https://docs.docker.com/compose/) 作为应用程序的模板，同时开源由 Websoft9 维护的[模板库](https://github.com/Websoft9/docker-library)。  

也就是说，应用实际上最终运行在 Docker Compose 编排下，即使不使用 Websoft9 的控制台管理应用，也不会被任何技术体系绑架，做到绝对的收放自如、自主可控。  
