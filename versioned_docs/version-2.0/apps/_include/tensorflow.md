[TensorFlow](https://www.tensorflow.org/) 是一个 **端到端机器学习平台**，它被用于 机器学习与模型训练 虚拟仿真  等场景。由 Websoft9 提供的 TensorFlow 镜像环境，预装了 TensorFlow 2.8, Nginx 1.20, Python3.8等组件，可在云服务器上一键部署。TensorFlow 是一个端到端开源机器学习平台。它可以轻松地构建模型、随时随地进行可靠的机器学习生产、进行强大的研究实验。


![gui](https://libs.websoft9.com/Websoft9/DocsPicture/en/tensorflow/tensowflow-gui-websoft9.jpg)


## 准备

在参阅本文档使用 TensorFlow 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）TensorFlow：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [apache2](https://opensource.org/licenses/Apache-2.0) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口