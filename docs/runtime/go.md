---
title: Go
slug: /go
tags:
  - 运行环境
  - runtime
  - Go
---

import Meta from '../apps/_include/go.md';

<Meta name="meta" />

## 配置选项{#configs}

- 版本号： `go version`
- Node 应用根目录： */usr/src/app*  
- 包管理器：`go get`, `go mod`, `go list`
- 命令行：`go`
- 开发框架：Gin, Beego

## 部署网站{#deploy}

### 手动部署

下面通过 [Gin Web Framework 示例](https://github.com/gin-gonic/gin) 为例为例，描述应用安装过程：

1. Websoft9 控制台安装 Go 运行环境

2. 进入 Go 容器，分别运行如下命令：

    ```
    #1 创建程序框架
    go mod init myapp
    go get -u github.com/gin-gonic/gin

    #2 创建程序主文件（下载）    
    wget https://websoft9.github.io/docker-library/apps/php/src/myapp.go

    #3 直接运行程序或在后台运行程序（取其一）
    go run myapp.go
    nohup go run myapp.go > output.log 2>&1 &
    ```

3. 此时，即可访问此 Web 程序 

### 自动部署

参考 Web Runtime 通用的文档章节：[自动部署指南](./runtime#auto)


## 管理维护{#administrator}


## 故障