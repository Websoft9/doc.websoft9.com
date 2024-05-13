---
title: Ruby
slug: /runtime/ruby
tags:
  - 运行环境
  - runtime
  - Ruby
---

## 配置选项{#configs}

- 版本号： `ruby -v`
- 应用目录： */usr/src/app*  
- 命令行：`ruby`, `gem`, `bundle`, `rake`
- 包管理器：`gem` 用于安装单独报，`bundle` 用于根据依赖文件安装一堆包
- 开发框架：Rails, Sinatra, jekyll
- 应用程序服务器：WEBrick, [Phusion passenger](https://www.phusionpassenger.com/), Puma
- 多版本管理器：[RVM](https://rvm.io/)


## 部署网站{#deploy}

参考：[Web Runtime 入门指南](../runtime#quick)

## 环境管理{#administrator}

- 更换 gem 源
  ```
  gem sources --remove https://rubygems.org  && gem sources -a https://gems.ruby-china.com
  ```

- 更换 bundle 源
  ```
  bundle config mirror.https://rubygems.org https://gems.ruby-china.com
  ```

- 项目源更换：gemfile 中也可以指定源，即无需全局设置


## 问题与故障