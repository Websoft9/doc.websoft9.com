---
title: Go
slug: /go
tags:
  - 运行环境
  - runtime
  - Go
---

import Meta from './_include/go.md';

<Meta name="meta" />

## 入门指南{#guide}

### 安装应用{#install}

下面通过 [Gin Web Framework 示例](https://github.com/gin-gonic/gin) 为例，描述应用安装过程：

1. Websoft9 控制台安装 Go 运行环境


2. 在编排修改 **.src/cmd.sh**，使注释掉的安装脚本生效
  ```
    go mod init myapp
    go get -u github.com/gin-gonic/gin
    cat > myapp.go <<EOF
    package main

    import (
      "net/http"
      "github.com/gin-gonic/gin"
    )

    func main() {
      r := gin.Default()
      r.GET("/", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{
          "message": "Hello World!",
        })
      })
      r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
    }
    EOF
    go run myapp.go
  ```

3. 重建应用生效后，即可访问访问示例 Web 应用 

## 配置选项{#configs}


## 管理维护{#administrator}


## 故障