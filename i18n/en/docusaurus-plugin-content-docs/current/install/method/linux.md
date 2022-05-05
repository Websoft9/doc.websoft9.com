---
sidebar_position: 1
slug: /install/linux
---


# For Linux

Websoft9 目前仅支持在 Linux 主机下安装。  

## 脚本安装

如果您不具备以上所需的 Docker, Git, Ansible 等环境，推荐使用我们**脚本安装**。

```
sudo wget -N https://raw.githubusercontent.com/Websoft9/StackHub/main/docker-installer.sh; sudo bash docker-installer.sh -r akeneo
```

## 手动安装

1. 安装命令行工具 StackHub
      ```
   pip install stackhub
   ```
2. 使用 stackhub 安装应用

## 离线安装

针对无法访问 Internet 的政企用户或等保用户，我们即将提供了离线安装包服务。
