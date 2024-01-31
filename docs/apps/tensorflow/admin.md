---
sidebar_position: 3
slug: /tensorflow/admin
tags:
  - TensorFlow
  - 人工智能
  - 机器学习
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### TensorFlow 升级

## 故障排除

除以下列出的 TensorFlow 故障问题之外， [通用故障处理](../troubleshoot) 专题章节提供了更多的故障方案。 

> 更多故障详细请参照[官方问题](https://www.tensorflow.org/install/errors)


## 问题解答

#### TensorFlow 是如何安装的？

使用docker安装

#### 是否有可视化的管理工具？

有，内置TensorBoard，访问地址：*http://服务器公网IP:6006/*

#### TensorFlow 实现 GPU 支持需要哪些条件？

需要 NVIDIA® GPU显卡以及驱动程序和工具。详细请参照[TensorFlow GPU 支持软硬件要求](https://www.tensorflow.org/install/gpu)