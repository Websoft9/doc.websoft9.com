---
title: Teleport
slug: /teleport
tags:
  - 堡垒机
  - 代理访问
  - 远程登陆
  - SSH
  - 应用访问
---

import Meta from './_include/teleport.md';

<Meta name="meta" />

## 入门指南{#guide}

### 安装后续步骤（必要）{#create-user}

Websoft9 控制台安装 Teleport 后，还需要完成如下几个步骤，方可登录到后台：

1. 确保为 Teleport 绑定域名，并设置 HTTPS 访问（**必要条件**）

2. 修改 Teleport 的配置文件，将 public_addr 配置项中的范例域名更改为自己的真实域名（保留 443 端口），重建应用后生效。

   ```
    public_addr:
      - 'example.domain.com:443'
   ```

3. 在 Teleport 容器中运行如下命令，创建一个超级用户，同时会生产注册链接（URL）
   ```
   tctl users add admin --roles=editor,auditor,access --logins=root,ubuntu,ec2-user
   ```
   > --logins=root,ubuntu,ec2-user 是必须的，否则后面无法连接到被管理的 Linux

4. 在本地浏览中运行注册链接，完成密码设置  

   > 如果链接不可访问或不成功，则说明步骤 1-2 没有完成或有问题

   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teleport/teleport-invitelinux-ss-websoft9.png)

5. 使用上述步骤生成的用户名和密码，便可以登录 Teleport 控制台
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teleport/teleport-loginss-websoft9.png)

### 管理资源

#### 连接远程 Linux

1. 登录到 Teleport 控制台，Resource > Enroll New Resource

2. 选择一个操作系统，并生成一个客户端安装链接
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teleport/teleport-linuxcreate-websoft9.png)

3. 登录到远程 Linux 服务器，将上一步的链接复制到命令行界面，开始安装

4. 安装成功后，回到 Teleport 控制台，Teleport 会自动检测到客户端并提示用户根据向导完成后续步骤
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/teleport/teleport-connectlinux-ss-websoft9.png)

## 配置选项{#configs}

- 配置文件：src/config/teleport.yaml
- 多语言（×）
- IP:端口的访问方式（×）：自生成证书不安全

## 管理维护{#administrator}

### Two-Factor 认证

我们在 Teleport 默认配置文件中禁用了 Two-Factor 认证，如需开启请修改配置文件后重建应用。


## 故障

#### 注册过程中填写密码后，注册仍然失败？

确保注册链接通过 HTTPS 访问。  

#### 公网+端口方式连接服务器失败？

问题描述：增加资源时，在被连接的服务器上运行安装命令，显示 curl failed to verify ...  

问题原因：自签名证书被认定为不安全，不允许连接  

解决方案：为 Teleport 配置域名，申请公共证书
