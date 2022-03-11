---
sidebar_position: 1
slug: /ruby
---

# 指南

## 场景

### RubyGems 包管理{#gems}

### Web 框架{#framework}

* Rails

### Ruby 版本变更{#version}

Ruby 的多版本管理非常灵活。

* RVM 支持多个 Ruby 版本安装和切换（包括默认设置）
* 每个 Ruby 版本下，都可以通过 gem 安装同一个包的多个版本

## 参数

### 路径{#path}

Java 安装目录： */data/java*  
Java 日志目录： */data/logs/java*  

### 命令行{#cmd}

下面列出常见的 Java 命令行工具，更多参考[官方文档](https://docs.oracle.com/javase/10/tools/tools-and-command-reference.htm)

* javac：读取 Java 类和接口定义并将它们编译成字节码和类文件。
* javap：反汇编一个或多个类文件。
* javadoc：从 Java 源文件生成 API 文档的 HTML 页面。
* java：启动 Java 应用程序。
* appletviewer：启动 AppletViewer 并在 Web 浏览器之外运行小程序。
* jar：为类和资源创建存档，并从存档中操作或恢复单个类或资源。
* jlink：将一组模块及其依赖项组装和优化为自定义运行时映像。
* jmod：创建 JMOD 文件并列出现有 JMOD 文件的内容。
* jdeps：启动 Java 类依赖关系分析器。
* jdeprscan：静态分析工具，用于扫描 jar 文件（或其他一些类文件的集合）以查找已弃用的 API 元素的使用情况。


### 服务{#service}

```
# Docker
sudo docker start jdk
sudo docker stop jdk
sudo docker restart jdk
sudo docker stats jdk
```