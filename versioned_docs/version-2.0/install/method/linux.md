---
sidebar_position: 1
slug: /install-linux
---


# Linux 下安装

Websoft9 目前仅支持在 Linux 主机下安装。  

## 在线安装与升级

安装脚本同时支持**全新安装**和**升级**，会自动检测当前环境。升级前建议先[备份数据](../../admin/backup)。

```
# 快速安装
wget -O install.sh https://artifact.websoft9.com/websoft9/release/install.sh && sudo bash install.sh

# 自定义参数
sudo bash install.sh --console-port 9000 --path "/data/websoft9/source" --version "latest"
```

> 升级过程不会影响已部署的应用。

## 离线安装

针对无法访问 Internet 的政企用户或等保用户，我们通过人工服务的方式提供安装服务。

## 卸载

Websoft9 支持卸载，默认**保留所有数据**。如需彻底清除，可使用 `--purge` 模式。

```
# 卸载（保留数据）
curl -fsSL https://artifact.websoft9.com/websoft9/release/uninstall.sh | sudo bash

# 彻底清除所有数据
sudo bash uninstall.sh --purge --yes
```