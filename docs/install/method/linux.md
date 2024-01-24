---
sidebar_position: 1
slug: /install/linux
---


# Linux 下安装

Websoft9 目前仅支持在 Linux 主机下安装。  

## 在线安装

安装 Websoft9 需要您具有操作系统的 root 权限，否则需要 *sudo su* 进行提权后再运行如下的脚本：

```
# 快速安装
wget -O install.sh https://websoft9.github.io/websoft9/install/install.sh && bash install.sh

# 自定义参数安装。-- channel 有 release 和 dev 两个可选项，分别代表生产版和测试版，默认值为 release
wget -O install.sh https://websoft9.github.io/websoft9/install/install.sh && bash install.sh --port 9000 --channel release --path "/data/websoft9/source" --version "latest"
```

> 升级 Websoft9 也只需要运行上面的脚本。  

## 离线安装

针对无法访问 Internet 的政企用户或等保用户，我们通过人工服务的方式提供安装服务。

## 卸载

Websoft9 支持[卸载](https://github.com/Websoft9/websoft9?tab=readme-ov-file#uninstall)，且卸载后不会在服务器中存留数据。

```
curl https://websoft9.github.io/websoft9/install/uninstall.sh | bash
```
