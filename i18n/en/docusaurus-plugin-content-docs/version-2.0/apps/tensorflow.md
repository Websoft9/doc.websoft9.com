---
title: TensorFlow
slug: /tensorflow
tags:
  - 人工智能
  - 机器学习
---

import Meta from './_include/tensorflow.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 TensorFlow 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 进入登陆页面
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

5. 浏览器访问 6006 端口，验证图形化工具 - TensorBoard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-board-websoft9.png)

### 快速了解

- CLI: tfx
- [API](https://tensorflow.google.cn/api_docs)
- [TensorFlow GPU 支持软硬件要求](https://www.tensorflow.org/install/gpu)

## 管理维护{#administrator}

## 故障
