---
sidebar_position: 1
slug: /tensorflow
tags:
  - TensorFlow
  - 人工智能
  - 机器学习
---

# 快速入门

[TensorFlow](https://www.tensorflow.org/) 是一个端到端开源机器学习平台。它拥有一个全面而灵活的生态系统，其中包含各种工具、库和社区资源。在机器学习方面，它可以轻松地构建模型、随时随地进行可靠的机器学习生产、进行强大的研究实验。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/tensorflow/tensowflow-gui-websoft9.jpg)

部署 Websoft9 提供的 TensorFlow 之后，需完成如下的准备工作：

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:6006** 端口已经开启
3. 在服务器中查看 TensorFlow 的 **[默认账号和密码](./setup/credentials#getpw)**  
4. 若想用域名访问  TensorFlow **[域名五步设置](./dns#domain)** 过程


## TensorFlow 初始化向导{#init}

### 详细步骤

1. 使用 SSH 登录服务器后，查看 TensorFlow 服务状态
   ```
   sudo systemctl status tensorflow
   ```
2. 使用本地电脑的浏览器访问网址：*http://域名:6006* 或 *http://服务器公网IP:6006*, 进入登陆页面

3. 输入账号密码（[不知道账号密码？](./setup/credentials#getpw)），成功登录到 TensorBoard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-board-websoft9.png)

> 需要了解更多 TensorFlow 的使用，请参考官方文档：[TensorFlow Documentation](https://www.tensorflow.org/learn)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

**使用 TensorFlow 的时候为什么需要先 `source /data/apps/tensorflow/bin/activate`**

本部署方案中 TensorFlow 使用的 Python 隔离环境安装


## TensorFlow 使用入门

下面以 **运行一个 TensorFlow 范例，演示它的计算结果** 作为一个任务，帮助用户快速入门：

1. 使用 SSH 连接到服务器，运行下面的命令
   ```
   cd /data/apps/tensorflow
   source /data/apps/tensorflow/bin/activate
   python tensorflow_test.py
   ```
2. 登录到 TensorBoard，此时页面已经有运行的内容
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-simpletest-websoft9.png)


## TensorFlow 常用操作

### 密码管理

本部署方案通过 Nginx 验证访问控制 TensorBoard 的访问，通过如下两个步骤修改密码：

1. 编辑 Nginx 验证访问控制文件： */etc/nginx/.htpasswd/htpasswd.conf* 中的密码
2. 重启 Nginx 服务后生效
   ```
   sudo systemctl restart nginx

### 图形化工具

[TensorBoard](https://www.tensorflow.org/tensorboard/) 是 Tensorflow 的官方提供的可视化工具，它通过对 Tensoflow 程序运行过程中输出的日志文件进行可视化 Tensorflow 程序的运行状态。

1. 使用本地电脑的浏览器访问网址：*http://域名:6006* 或 *http://服务器公网IP:6006*, 进入登陆页面

2. 输入账号密码（[不知道账号密码？](#账号密码)），成功登录到 TensorBoard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-board-websoft9.png)

3. TensorBoard 工作台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/tensorflow/tensorboard.gif)

## 参数{#parameter}

**[通用参数表](../setup/parameter)** 中可查看 Nginx, Apache, Docker, MySQL 等 TensorFlow 应用中包含的基础架构组件路径、版本、端口等参数。 

通过运行`docker ps`，可以查看到 TensorFlow 运行时所有的 Container：

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
```


下面仅列出 TensorFlow 本身的参数：

### 路径{#path}

TensorFlow 安装目录： */data/apps/tensorflow*  
TensorFlow 日志目录： */data/logs/tensorflow*  
TensorFlow 配置目录： */data/apps/tensorflow/conf*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 6006   | 通过 HTTP 访问 TensorBoard | 可选   |



### 版本{#version}

```shell
sudo cat /data/logs/install_version.txt
```

### 服务{#service}

```shell
sudo systemctl start | stop | restart tensorflow

```

### 命令行{#cli}

TensorFlow 提供了强大的的命令行工具 `tfx`，执行下列命令可安装：

```
source /data/apps/tensorflow/bin/activate
pip install tfx
```

 >tfx只支持到2.3.2，安装可能会导致TensorFlow版本降级

### API

### 参考{#ref}

