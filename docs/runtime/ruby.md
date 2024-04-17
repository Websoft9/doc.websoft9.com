---
title: Ruby
slug: /ruby
tags:
  - 运行环境
  - runtime
  - Ruby
---

import Meta from '../apps/_include/ruby.md';

<Meta name="meta" />

## 配置选项{#configs}

- 版本号： `ruby -v`
- 应用目录： */usr/src/app*  
- 命令行：`ruby`, `gem`, `bundle`, `rake`
- 开发框架：Rails, Sinatra, jekyll
- 应用程序服务器：WEBrick, Passenger, Puma
- 多版本管理器：[RVM](https://rvm.io/)

## 部署网站{#install}

下面通过 [ Jekyll](https://github.com/jekyll/jekyll) 和 Rails 为例，描述应用安装过程：

### 自动部署

自动部署即通过修改 cmd.sh 文件，让容器在启动时可以自动执行部署命令

1. Websoft9 控制台安装 Ruby 程序环境

2. Websoft9 控制台，我的应用管理的 **编排** 标签页，开始对应用进行编排

3. 修改 **.src/cmd.sh**，注释掉的安装脚本生效
   ```
    gem install bundler jekyll
    jekyll new mysite
    cd mysite
    bundle exec jekyll serve --host 0.0.0.0 --port 8080
   ```

4. Websoft9 控制台 **重建应用** 后生效，方可访问此 Web 应用 

### 手工部署

手工部署即用户登录到容器中，手工运行相关命令的部署方式：

1. Websoft9 控制台安装 Ruby 程序环境

2. 进入 Ruby 容器的命令模式，选择安装 jekyll 或 Rails 的命令

   - 部署 jekyll
      ```
      gem install bundler jekyll
      jekyll new mysite
      cd mysite
      nohup bundle exec jekyll serve --host 0.0.0.0 --port 8080 > output.log 2>&1 &
      ```

   - 部署 Rails
      ```
      gem install rails
      rails new mysite
      cd mysite
      bundle install
      bin/rake ..
      nohup rails s -b 0.0.0.0 -p 8080 > output.log 2>&1 &
      ```
3. 此时，即可访问此 Web 程序 

## 管理维护{#administrator}

### RubyGems 包管理{#gems}

**gem 源更换**

rubygems.org 存放在 Amazon S3 上，有时由于网络问题导致无法安装

```
# 查询当前源，假设为：https://rubygems.org/
gem sources -l

# 删除当前源
gem sources --remove https://rubygems.org/

# 安装替换源
gem sources -a https://gems.ruby-china.com/

# 查询替换后的结果
gem sources -l

# bundle 源更换  
bundle config mirror.https://rubygems.org https://gems.ruby-china.com/
```

> gemfile 中也可以指定源，这样就无需全局设置

### Phusion passenger 提升性能

[Phusion passenger](https://www.phusionpassenger.com/) 是被广泛应用于 Ruby 的应用程序服务器，它与 Nginx 或 Apache 配合一起为 Ruby 提供高性能的 Web 应用方案。它处理 HTTP 请求，管理进程和资源，并启用管理、监控和问题诊断。乘客非常易于使用，使生产中的部署更加容易并且具有可扩展性。

Phusion passenger 除了支持 Ruby 之外，也可用于 Python, Node, Meteor 等应用程序。  

## 问题与故障

#### Gem, Bundler, Rake, Rails 是什么？

- RubyGems 是 Ruby 的包管理工具，类似 Python 中的 pip
- Gems 是 Ruby 通过 RubyGems 安装的包，为例避免误解，建议用“包”这个名字替代
- Bundler 是基于 Ruby 应用程序目录中的 Gemfile ，用于拉取依赖包的管理工具
- Gemfile 是 Ruby 依赖包清单文件
- Rake 是 Ruby 的构建程序，类似 Linux 中的 make
- Rails 是一个流行的 Ruby 应用程序开发框架


#### 如何将 Ruby 包安装到项目目录下？

```
# 安装第三方包到项目 vendor/bundle 目录
bundle install --deployment

# 安装所有包到项目目录
bundle install --path=$(pwd)
```