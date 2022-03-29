---
sidebar_position: 3
slug: /scratch/admin
tags:
  - Scratch
  - 少儿编程
---

# 维护指南

## 场景

### 备份与恢复


### 升级

Scratch的升级是通过NPM来实现的，通过SSH工具，依次运行如下命令：

```
cd /data/wwwroot/scratch-gui
npm install https://github.com/LLK/scratch-gui.git
npm run build

```

## 故障速查

#### 如何查看错误日志？

日志文件路径为：`/data/logs`。检索关键词 **Failed** 或者 **error** 查看错误

#### Scratch 访问很慢？

Scratch首次加载数据超过20M。例如：您使用的是2M带宽，那么理想情况下的加载时间为：20000k/(128k/s×2)=78s。显然，如果带宽不足，速度会非常慢。

## 问题解答

#### Scratch支持多语言吗？

支持多语言（包含中文），系统默认根据浏览器自动选择语言，并可以实时切换 

#### Scratch 支持用户注册和登录吗？

暂时不支持

#### scratch-www 项目 和 scratch-gui 项目 有什么区别？

[scratch-www](https://github.com/LLK/scratch-www)  = [scratch-gui](https://github.com/LLK/scratch-gui)  + 分享社区，现在 scratch-www 用户登录功能还在开发中

#### 如果没有域名是否可以部署 Scratch？

可以，访问`http://服务器公网IP` 即可

#### 是否可以修改Scratch的源码路径？

可以，通过修改 [Nginx 虚拟主机配置文件](../nginx#virtualHost)中相关参数

#### 如何修改上传的文件权限?

```shell
chown -R nginx.nginx /data/wwwroot
find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```