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

## 准备

部署 Websoft9 提供的 TensorFlow 之后，需完成如下的准备工作：

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80, 6006** 端口已经开启
3. 在服务器中查看 TensorFlow 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问  TensorFlow **[域名五步设置](./administrator/domain_step)** 过程


## TensorFlow 初始化向导{#init}

### 详细步骤

1. 使用本地电脑的浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入登陆页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-login-websoft9.png)

2. SSH登陆服务器，执行如下命令取得token后填入登陆页面，并点击【Login】
   ```
   $ docker exec -it tensorflow jupyter notebook list
   Currently running servers:
   http://0.0.0.0:8888/?token=c8929544462391e32bbf0d7763b7b5dda3ab00b2f14da5b9 :: /tf

   ```

3. 登陆控制台，体验jupyter的强大功能（编辑源码）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-main-websoft9.png)

4. 产品集成了 TensorBoard 工具，通过下面命令启动
   ```
   $ docker exec -it tensorflow bash
   $ cd /usr/local/lib/python3.8/dist-packages/tensorboard && tensorboard --logdir=/data/logs --port 6006 --host 0.0.0.0
   ```

5. 使用浏览器访问：*http://域名:6006* 或 *http://服务器公网IP:6006*, 验证图形化工具 - TensorBoard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-board-websoft9.png)

> 需要了解更多 TensorFlow 的使用，请参考官方文档：[TensorFlow Documentation](https://www.tensorflow.org/learn)


### 出现问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题：

## TensorFlow 使用入门

下面以 **运行一个 TensorFlow 范例，演示它的计算结果** 作为一个任务，帮助用户快速入门：

## TensorFlow 常用操作

### 密码管理


## TensorFlow 参数{#parameter}

TensorFlow 应用中包含 Python, Nginx, Docker 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。

通过运行`docker ps`，可以查看到 TensorFlow 运行时所有的 Container：

```bash
CONTAINER ID   IMAGE                                  COMMAND                  CREATED        STATUS         PORTS                                                                                  NAMES
f7e151917bec   tensorflow/tensorflow:latest-jupyter   "/bin/bash -c 'cd /u…"   15 hours ago   Up 2 minutes   0.0.0.0:6006->6006/tcp, :::6006->6006/tcp, 0.0.0.0:9001->8888/tcp, :::9001->8888/tcp   tensorflow
```

### 路径{#path}

TensorFlow 安装目录： */data/apps/tensorflow*  
TensorFlow notebooks目录： */data/apps/tensorflow/data/tensorflow*  

### 端口{#port}

| 端口号 | 用途                                          | 必要性 |
| ------ | --------------------------------------------- | ------ |
| 6006   | 通过 HTTP 访问 TensorBoard | 必选   |


### 版本{#version}

```shell
docker exec -it tensorflow grep "_VERSION =" /usr/local/lib/python3.8/dist-packages/tensorflow/tools/pip_package/setup.py| cut -d= -f2
```

### 服务{#service}

```shell
sudo docker start | stop | restart | stats tensorflow

```

### 命令行{#cli}

TensorFlow 提供了强大的的命令行工具 `tfx`，执行下列命令可安装：

```
source /data/apps/tensorflow/bin/activate
pip install tfx
```

 > tfx只支持到2.3.2，安装可能会导致TensorFlow版本降级

### API

[API Documentation](https://tensorflow.google.cn/api_docs)

