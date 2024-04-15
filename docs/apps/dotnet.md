---
title: .NET SDK
slug: /dotnet
tags:
  - 运行环境
  - runtime
  - .NET
---

import Meta from './_include/dotnet.md';

<Meta name="meta" />

## 入门指南{#guide}

### 安装应用{#install}

下面通过 [dotnet-docker 示例](https://github.com/dotnet/dotnet-docker) 为例，描述应用安装过程：

1. Websoft9 控制台安装 .NET SDK 运行环境


2. 在编排修改 **.src/cmd.sh**，使注释掉的安装脚本生效
   ```
   git clone --depth=1 https://github.com/dotnet/dotnet-docker
   cd dotnet-docker/samples/aspnetapp/aspnetapp
   otnet publish -c Release -o out
   ./bin/container/Release/net8.0/aspnetapp
   ```

3. 重建应用生效后，即可访问访问示例 Web 应用 

## 配置选项{#configs}


## 管理维护{#administrator}


## 故障