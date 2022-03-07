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


在云服务器上部署 TensorFlow 预装包之后，请参考下面的步骤快速入门。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **Inbound（入）规则** 下的 **TCP:6006** 端口是否开启
3. 若想用域名访问 TensorFlow，请先到 **域名控制台** 完成一个域名解析


## 账号密码

通过**SSH**连接云服务器，运行 `cat /credentials/password.txt` 命令，可以查看所有相关账号和密码

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)

下面列出可能需要用到的几组账号密码：

### TensorBoard

* 管理员账号: `admin`
* 管理员密码: 存储在您的服务器中的文件中 */credentials/password.txt*  

> 本部署方案通过 [Nginx 验证访问](/维护参考.md#nginx)控制 TensorBoard 的访问

## TensorFlow 安装向导

1. 使用 SSH 登录服务器后，查看 TensorFlow 服务状态
   ```
   sudo systemctl status tensorflow
   ```
2. 使用本地电脑的浏览器访问网址：*http://域名:6006* 或 *http://服务器公网IP:6006*, 进入登陆页面

3. 输入账号密码（[不知道账号密码？](/zh/stack-accounts.md#rocketmq)），成功登录到 TensorBoard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-board-websoft9.png)

> 需要了解更多 TensorFlow 的使用，请参考官方文档：[TensorFlow Documentation](https://www.tensorflow.org/learn)


## TensorFlow 入门向导

下面通过运行一个 TensorFlow 范例，演示它的计算结果：

1. 使用 SSH 连接到服务器，运行下面的命令
   ```
   cd /data/apps/tensorflow
   source /data/apps/tensorflow/bin/activate
   python tensorflow_test.py
   ```
2. 登录到 TensorBoard，此时页面已经有运行的内容
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-simpletest-websoft9.png)


## 常用操作

### 密码管理

本部署方案通过 Nginx 验证访问控制 TensorBoard 的访问，通过如下两个步骤修改密码：

1. 编辑 Nginx 验证访问控制文件： */etc/nginx/.htpasswd/htpasswd.conf* 中的密码
2. 重启 Nginx 服务后生效
   ```
   sudo systemctl restart nginx

### CLI

TensorFlow 提供了强大的的命令行工具 `tfx`，执行下列命令可安装：

```
source /data/apps/tensorflow/bin/activate
pip install tfx
```

 >tfx只支持到2.3.2，安装可能会导致TensorFlow版本降级

### 图形化工具

[TensorBoard](https://www.tensorflow.org/tensorboard/) 是 Tensorflow 的官方提供的可视化工具，它通过对 Tensoflow 程序运行过程中输出的日志文件进行可视化 Tensorflow 程序的运行状态。

1. 使用本地电脑的浏览器访问网址：*http://域名:6006* 或 *http://服务器公网IP:6006*, 进入登陆页面

2. 输入账号密码（[不知道账号密码？](#账号密码)），成功登录到 TensorBoard
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/tensorflow/tensorflow-board-websoft9.png)

3. TensorBoard 工作台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/tensorflow/tensorboard.gif)

## 异常处理

#### 浏览器打开IP地址，无法访问 TensorFlow（白屏没有结果）？

您的服务器对应的安全组6006端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 使用 TensorFlow 的时候为什么需要先 `source /data/apps/tensorflow/bin/activate` ？

本部署方案中 TensorFlow 使用的 Python 隔离环境安装