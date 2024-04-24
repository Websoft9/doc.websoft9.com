---
title: code-server
slug: /codeserver
tags:
  - Code
  - IDE
  - 可视化
  - 在线开发
  - 构建
  - vscode
---

import Meta from './_include/codeserver.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 code-server 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 使用本地浏览器访问后，进入登录页面
   ![code-server 登录界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-login-websoft9.png)

2. 输入密码，成功登录到 code-server 后台  
   ![code-server 后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-consolegui-websoft9.png)

3. 在 code-server 界面上打开 workspace 文件夹  
   ![code-server 打开项目目录](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-openfolder-websoft9.png)

4. 打开 Terminal，查看系统环境
   ![code-server 打开Terminal](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-terminal-websoft9.png)

5. 参考下一节安装所需的开发环境

### 安装环境

code-sever 默认并没有安装 Python, Node, Java 等环境。需要 `sudo su` 到管理员账号后开始安装

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-sudosu-websoft9.png)

> 密码为 code-server 控制台登录密码

#### Node.js

```
# 安装 Node,yarn
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install --global yarn

# 删除正在运行的 npm run
ps aux
kill -9
```

#### Python

```
# 安装环境
sudo apt update
sudo apt install python3-pip
```

#### Java
```
apt update
apt install openjdk-8-jre
java -version
```

### Python 开发范例

下面以 Python 开发为范例，介绍如何使用 code-server：

1. 登录 code-server，新建一个文件夹和文件，文件命名为：myfile.py，并拷贝下面的 Python 程序实例代码。
   ```
   #!/usr/bin/env python2
   #!/usr/bin/env python3
   #coding: utf-8

   import os, io, sys

   print("hello world")
   ```
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-createfile-websoft9.png)

2. 在【窗口的终端栏】中执行 `python myfile.py` 命令，运行 Python 程序
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/codeserver/codeserver-runpython-websoft9.png)

3. 查看正确的输出结果

### 预览应用

通过 code-server 容器的 Terminal 以开发者模式构建应用后，如何发布外网访问呢？

有两个方案：

- 推荐：使用 Websoft9 控制台的【网关】为预览端口做一个代理，这样不需要绑定端口到宿主机
- docker-compose.yml 绑定容器端口到宿主机，构建时指定此端口。  
  例如：npm run start -- --host 0.0.0.0 --port 3002

### 多开发者

单个 code-server 应用不支持多用户开发协同工作的场景。    

那么如何才能支持多开发者协作使用 code-server 呢？  

其实，非常简单，只需要通过 Websoft9 控制台安装多个 code-server 多个应用。

## 配置选项{#configs}

- sudo（✅）：密码与控制台密码相同
- 代码编译构建（✅）


## 管理维护{#administrator}


## 故障

#### 文件权限不足？

如果上传到宿主机的文件，code-server 容器没有访问权限，则需要修正它们。   

#### Terminal 安装组件时权限不足？

`sudo su` 切换到 root 账号

#### 无法复制命令到 Terminal？

ctrl+V

#### git push 时与远程待拉取冲突？

问题描述：  git push 时，由于有待 pull 的代码，导致冲突  
解决方案：  `git pull --rebase origin main`