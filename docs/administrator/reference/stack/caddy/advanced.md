---
sidebar_position: 2
slug: /caddy/advanced
---

# 进阶

## 安装

Caddy 提供了一个官方兼容性的二进制包，可以下载后直接运行。  
当然，我们也可以采用下面的命令快速安装：

```
# Fedora, RedHat, CentOS
yum install yum-plugin-copr
yum copr enable @caddy/caddy
yum install caddy

# Debian, Ubuntu, Raspbian
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo tee /etc/apt/trusted.gpg.d/caddy-stable.asc
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

## 原理

#### 匹配器标记

1. * 匹配所有请求（通配符；默认）。
2. /path 以正斜杠开头以匹配请求路径。
3. @name 指定一个命名匹配器。

## 问题解答


## 故障速查{#troubleshooting}