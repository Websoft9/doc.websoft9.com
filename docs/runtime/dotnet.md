---
title: .NET
slug: /dotnet
tags:
  - 运行环境
  - runtime
  - .NET
---

import Meta from '../apps/_include/dotnet.md';

<Meta name="meta" />

## 配置选项{#configs}

- 命令行：`dotnet -h`
- 其他生态工具：ASP.NET, Visual Studio,
- .NET 运行时 [架构图](./assets/swimlane-architecture-framework.svg)

## 部署网站{#deploy}

### 手动部署

下面通过一个范例，描述应用安装过程：

1. Websoft9 控制台安装 .NET 运行环境

2. 进入 .NET 容器，分别运行如下命令：

    ```
    #1 创建程序框架
    git clone --depth=1 https://github.com/dotnet/dotnet-docker
    cd dotnet-docker/samples/aspnetapp/aspnetapp

    #2 构建可运行的程序    
    dotnet publish -c Release -o out

    #3 直接运行程序或在后台运行程序（取其一）
    ./bin/container/Release/net8.0/aspnetapp
    nohup ./bin/container/Release/net8.0/aspnetapp > output.log 2>&1 &
    ```

3. 此时，即可访问此 Web 程序 

### 自动部署

参考 Web Runtime 通用的文档章节：[自动部署指南](./runtime#auto)

## 管理维护{#administrator}

## 问题与故障

#### 如何找到 .NET 资源？

* [Awesome .NET](https://github.com/quozd/awesome-dotnet)
* [.NET Foundation](https://dotnetfoundation.org/)

#### 什么是 Xamarin/Mono？

Xamarin 是 Microsoft 旗下的 .NET 的扩展，用于使用 C# 和 .NET 构建现代和高性能的 iOS 和 Android 应用。

#### .NET 平台支持哪些语言？

C#, F#, Visual Basic.

#### .NET 与 .NET Framework 的区别？

.NET 是一组用于为 Linux、macOS、Windows、iOS、Android 等构建应用程序的技术的统称。  
.NET Framework 是用于在 Windows 上构建和运行应用程序的软件开发框架。

#### 什么是 .NET Core？

.NET Core 全名是 ASP.NET Core，它是 .NET 的 Web 应用程序开发框架