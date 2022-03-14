---
sidebar_position: 3
---

# 进阶

## 核心原理


### API/CLI

阿里云为服务器提供一套功能强大、完整的 [API](https://next.api.aliyun.com/) 以及 CLI 操作方式，为自动化提供了坚实的基础。  

###  对象存储

#### 自建对象存储

我们都知道对象存储的强大特征，除了使用阿里云的 OSS 之外，是否可以将磁盘改造成对象存储呢？  
答案是：当然可以。
云原生时代，有非常优秀的对象存储开源软件可用，推荐部署：[Minio](https://github.com/Websoft9/docker-minio)



#### HTTPS 设置

主要步骤：

1. 完成 CNMAE 域名解析以及绑定至目标 Bucket
2. 进入阿里云控制台的[云盾](https://yundun.console.aliyun.com/)下，申请一个免费赠书（有效期为一年）
3. 证书申请成功后，下载它
4. 到 Bucket 的 HTTPS 配置项中绑定证书
5. 等待几分钟，HTTPS 生效


## 问题解答

#### 服务器常见操作有哪些？

下面是一些常见的ECS操作，包括：

- 启动
- 停止
- 重启
- 释放
- 升降配

释放=删除ECS，适用于按量购买的服务器

#### 阿里云如何对服务器进行首次初始化？

阿里云与其他主流的云平台一样，目前都采用 [Cloud-init](https://cloudinit.readthedocs.io/) 这个开源的初始化工具完成相关任务。  

#### 阿里云磁盘支持扩容吗？

阿里云支持在线扩容系统盘和数据盘，即无需重启ECS实例便可以完成扩容。

#### 阿里云 WorkBench 是用来干什么的？

它用于连接 ECS。支持命令连接，也支持桌面连接；支持 Linux，也支持 Windows

![WorkBench](http://libs.websoft9.com/Websoft9/DocsPicture/zh/aliyun/aliyun-workbench-websoft9.png)

#### 推荐将 OSS 挂载到 ECS 吗？

不推荐，理由有三：

* OSS 不同于磁盘，它不是 ECS 的组成部分，挂载后后期维护难以察觉
* OSS 挂载到 ECS 涉及多层计费，财务成本和管理成本大大增加
* OSS 主要是独立的向外部提供图片和视频的载体，与ECS并没有强相关性


## 故障相关

#### 如何进行阿里云故障诊断？

如果您已经明确问题原因是云服务器产生的，那么请直接阅读[阿里云实例故障排查](https://help.aliyun.com/knowledge_detail/127067.html)。


#### 开启了全站加速的 HTTPS 选项，访问 HTTPS 网站，显示 Testing 123.. 页面

经过实践发现，一旦使用了阿里云的全站加速HTTPS之后，需要下载阿里云的SSL证书，然后用这个证书给网站再做一次手工的HTTPS配置，这个时候全站HTTPS才会生效。即需要：客户端-阿里云CDN-服务器 全链路采用相同的证书方可访问

#### 阿里云香港服务器 SSH 总是断线？

您需要购买阿里云的弹性公网IP，并选择【BGP(多线)_精品/公网】模式，这样才会有稳定的效果

#### 上传的 OracleLinux 镜像无法重置密码？

确保上传镜像等选择等是【CentOS】类别，如果是【OtherLinux】等类别，就会导致无法在控制台重置密码


