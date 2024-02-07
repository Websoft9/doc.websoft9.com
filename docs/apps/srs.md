---
title: SRS
slug: /srs
tags:
  - 视频流
  - 直播
---

import Meta from './_include/srs.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 SRS 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

1. 本地浏览器访问后，进入后台管理页面

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-init-websoft9.png)

2. 点击【SRS控制台】，进入控制台进行监控以及各种设置

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/srs/srs-console-websoft9.png)

### 快速了解

- [API接口](https://ossrs.net/lts/zh-cn/docs/v4/doc/http-api)

### OBS 推送PC桌面流到 SRS

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


## 管理维护{#administrator}

## 故障
