---
title: MingDao（明道云）
slug: /mingdao
tags:
  - 明道云
  - APaaS
  - 无代码平台
---

import Meta from './_include/mingdao.md';

<Meta name="meta" />

## 入门指南{#guide}

### 初始化{#wizard}

Websoft9 控制台安装 MingDao（明道云） 后，通过【我的应用】管理应用，在**访问**标签页中获取登录信息。  

明道云安装向导包含三个过程：初始化、安装数据、设置管理员：

1. 使用本地电脑的浏览器访问后，进入初始化页面

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-initial1-websoft9.png)

   > 上图中访问地址的默认端口 8880 可自行设置为其他端口号

2. 设置访问地址后，进入【下一步】，开始初始化（过程持续约 3~5 分钟）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-initial2-websoft9.png)

3. 初始化完成后，开始**安装数据** （此过程中会引导至明道云官网申请密钥）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-install1-websoft9.png)

4. 完成**注册系统管理员**信息（务必牢记账号密码）

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-set-admin-websoft9.png)

5. 访问第1步设置的访问地址（例如：**`http://服务器公网IP:8880`**），登陆明道云后台

    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-login-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-main-app-websoft9.png)
    ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/mingdao/mingdao-main-lib-websoft9.png)

## 配置选项{#configs}

- 免费版限制：用户数不超过 30 个，单个工作表最大行数 10 万行
- SMTP 设置：右上角用户图标下的【系统配置】>【邮件服务设置】
- [API](https://help.mingdao.com/API1.html)
- [维护命令](https://docs.pd.mingdao.com/deployment/command)
- 多语言：中文和英文
- 多版本
   * [SaaS 版本](https://www.mingdao.com/price)，其中又分为：免费版、标准版、专业版、旗舰版四种
   * [私有部署版](https://www.mingdao.com/pd)，其中又分为：社区版（免费）、标准版、专业版三种


## 管理维护{#administrator}

### 更换 URL{#url}

服务器 IP 变化后，需要修改 docker-compose 配置文件，修改 ENV_MINGDAO_HOST 为新的IP，再用重启服务

## 故障

#### 服务器重启后，程序打不开？

重启明道服务

## 定制服务

Websoft9 作为明道的合作伙伴，具备基于明道云的软件快速构建能力。我们可以为客户提供如下的服务：

- 基于实际业务，快速建立基础数据模型
- 提炼管理流程，将业务融合到软件操作中
- 将明道云与其他系统的连接集成，打破企业数据孤岛

![](https://alifile.mingdaocloud.com/wwwhome/dist/pack/static/src-common-partnerIntroduction-img-jj2.png)