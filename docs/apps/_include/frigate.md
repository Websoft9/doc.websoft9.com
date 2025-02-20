[Frigate](https://frigate.video) 是一个 **为 IP 摄像机配备实时本地对象检测功能的 NVR**，它被用于 视频音频  等场景。Frigate 是一款完整的本地 NVR，专为家庭助理设计，具有 AI 物体检测功能。它使用 OpenCV 和 Tensorflow 对本地 IP 摄像头进行实时物体检测。


![界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/frigate/frigate-gui-websoft9.png)


## 准备

在参阅本文档使用 Frigate 时，需要确保如下几点：

- [登录 Websoft9 控制台](./login-console)，然后找到（或安装）Frigate：
  - **我的应用** 菜单找到应用 
  - **应用商店** 菜单部署应用

- 应用是基于 Websoft9 安装的


- 应用的用途符合 [MIT](https://opensource.org/licenses/MIT) 开源许可协议


- 为应用准备配置访问方式：[配置域名](./domain-set) 或 **服务器安全组**开启网外端口