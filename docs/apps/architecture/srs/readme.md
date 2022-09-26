---
sidebar_position: 100
slug: /srs
tags:
  - Web 面板
  - 可视化
  - GUI
---

# 快速入门

SRS 介绍

部署 Websoft9 提供的 SRS 之后，请参考下面的步骤快速入门。

## 准备{#prepare}

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，确保 **Inbound（入）规则** 下的 **TCP:80** 端口已经开启
3. 在服务器中查看 SRS 的 **[默认账号和密码](./user/credentials)**  
4. 若想用域名访问 SRS，务必先完成 **[域名五步设置](./administrator/domain_step)** 过程

## SRS 初始化向导{#wizard}

### 详细步骤

1. 使用本地电脑浏览器访问网址：*http://域名* 或 *http://服务器公网IP*, 进入后台管理页面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-init-websoft9.png)

2. 点击【SRS控制台】，进入控制台进行监控以及各种设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-console-websoft9.png)

### 碰到问题？

若碰到问题，请第一时刻联系 **[技术支持](./helpdesk)**。也可以先参考下面列出的问题定位或  **[FAQ](./faq#setup)** 尝试快速解决问题。

参阅：

## SRS 使用入门{#quickstart}

下面以 **OBS 推送PC桌面流到 SRS** 作为一个任务，帮助用户快速入门：

1. 下载并安装[OBS](https://obsproject.com/download)

2. 启动 OBS，点击【+】来添加源
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-add-websoft9.png)

3. 选择【显示器采集】，新建源名称后点击【确定】
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-add1-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-add2-websoft9.png)

4. 选择【设置】，分别对【推流】和【输出】进行设置
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-set-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-set1-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-set2-websoft9.png)

  > 输出编码如果使用硬件，对显卡要求较高，可能无法推流成功

5. 点击【开始推流】，连接成功即推流成功
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-tl1-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-tl2-websoft9.png)

6. 回到后台，点击【SRS播放器】查看推流结果
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-view1-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-view2-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-view3-websoft9.png)

## SRS 常用操作{#guide}

## 参数{#parameter}

SRS 应用中包含 Docker, Portainer 等组件，可通过 **[通用参数表](./administrator/parameter)** 查看路径、服务、端口等参数。 

通过运行 `docker ps`，查看 SRS 运行时所有的服务组件：   

```bash
CONTAINER ID   IMAGE              COMMAND                  CREATED       STATUS       PORTS                                                                                                                                                                                             NAMES
49f6aed14ba8   ossrs/srs:latest   "./objs/srs -c conf/…"   2 hours ago   Up 2 hours   0.0.0.0:1935->1935/tcp, :::1935->1935/tcp, 0.0.0.0:1985->1985/tcp, :::1985->1985/tcp, 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp, 8000/udp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 10080/udp   srs
```

### 路径{#path}

SRS 安装目录： */data/apps/srs*      

### 端口{#port}

除 80, 443 等常见端口需开启之外，以下端口可能会用到：  

无特殊端口

### 版本{#version}

控制台查看

### 服务{#service}

```shell
sudo docker start | stop | restart | stats srs
```

### 命令行{#cli}

暂无

### API{#api}

SRS提供[API接口](https://ossrs.net/lts/zh-cn/docs/v4/doc/http-api)，供外部程序管理服务器