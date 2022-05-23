---
sidebar_position: 3
slug: /scratch/admin
tags:
  - Scratch
  - 少儿编程
---

# 维护指南

本章提供的是本应用自身特殊等维护与配置。而**配置域名、HTTPS设置、数据迁移、应用集成、Web Server 配置、Docker 配置、修改数据库连接、服务器上安装更多应用、操作系统升级、快照备份**等操作通用操作请参考：[管理员指南](../administrator) 和 [安装后配置](../install/setup) 相关章节。

## 场景

### Scratch 升级

Scratch 的升级是通过NPM来实现的，通过SSH工具，依次运行如下命令：

```
cd /data/wwwroot/scratch-gui
npm install https://github.com/LLK/scratch-gui.git
npm run build

```

## 故障排除

#### Scratch 访问很慢？{#slowy}

Scratch首次加载数据超过20M。例如：您使用的是2M带宽，那么理想情况下的加载时间为：20000k/(128k/s×2)=78s。显然，如果带宽不足，速度会非常慢。

## 问题解答

#### Scratch 支持多语言吗？

支持多语言（包含中文），系统默认根据浏览器自动选择语言，并可以实时切换 

#### Scratch 支持用户注册和登录吗？

暂时不支持

#### scratch-www 项目 和 scratch-gui 项目 有什么区别？

[scratch-www](https://github.com/LLK/scratch-www)  = [scratch-gui](https://github.com/LLK/scratch-gui)  + 分享社区，现在 scratch-www 用户登录功能还在开发中
