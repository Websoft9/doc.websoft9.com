---
title: MinIO
slug: /minio
tags:
  - 对象存储
  - S3
  - 云原生
---

import Meta from './_include/minio.md';

<Meta name="meta" />

## 入门指南{#guide}

### 登录后台{#wizard}

Websoft9 控制台安装 MinIO 后，通过 "我的应用" 查看应用详情，在 "访问" 标签页中获取登录信息。  

1. 使用本地电脑浏览器访问，进入登录页面

   ![](./assets/minio-login-websoft9.png)

2. 输入账号密码，直接进入后台

   ![](./assets/minio-main-websoft9.png)

### 创建存储桶

1. 登录后台，点击【Create Bucket】，创建新的存储桶

   ![](./assets/minio-bucket-websoft9.png)

2. 上传文件后可以下载和预览
   ![](./assets/minio-upload-websoft9.png)
   ![](./assets/minio-preview-websoft9.png)

## 配置选项{#configs}

- 多语言（×）
- cli：需额外安装
- 端口：本应用有后台端口和 API 端口

## 管理维护{#administrator}

- **安装 CLI**：Websoft9 控制台进入 MinIO 容器的命令模式，安装并启用 CLI
   ```
   curl https://dl.min.io/client/mc/release/linux-amd64/mc \
   --create-dirs \
   -o $HOME/minio-binaries/mc
   chmod +x $HOME/minio-binaries/mc
   export PATH=$PATH:$HOME/minio-binaries/

   mc --help    
   ```

## 故障