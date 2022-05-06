---
slug: /ruby/advanced
---

# 进阶

## 安装

### 安装

使用 Ansible 可以很方便安装由 Websoft9 提供的多版本 Ruby 安装：  

```
git clone https://github.com/websoft9/role_ruby
ansible-playbook role_ruby/tests/test.yml
```

> 项目基于 rvm 安装，支持多版本

### 升级

#### Patch 升级

Ruby 基于 RVM 部署，小版本的更新非常简单

```
rvm upgrade 1.9.2-p136 1.9.2-p180
rvm upgrade ree-2011.01 ree-2011-02
```

#### 版本升级

例如需将 Ruby 2.5 升级到 Ruby 2.6，实际上等于新安装

```
rvm install 2.6
```

### 扩展

## 概念与原理

### Phusion passenger

[Phusion passenger](https://www.phusionpassenger.com/) 是被广泛应用于 Ruby 的应用程序服务器，它与 Nginx 或 Apache 配合一起为 Ruby 提供高性能的 Web 应用方案。它处理 HTTP 请求，管理进程和资源，并启用管理、监控和问题诊断。乘客非常易于使用，使生产中的部署更加容易并且具有可扩展性。

Phusion passenger 除了支持 Ruby 之外，也可用于 Python, Node, Meteor 等应用程序。  

### RubyGems 

Maven 是一个项目管理工具，可以对 Java 项目进行构建、依赖管理。

### RVM

RVM 是一个用于安装和管理多版本 Ruby 的命令行工具，虽然不是 Ruby 官方出品，但非常流行。

### 隔离环境

有两种隔离环境的解决方案：

* RVM Gemset
* Bundler

经过实验验证，bundle 可以很方便的将项目所需的软件包安装到项目目录中。  

## 故障速查{#troubleshoot}

## 问题解答

#### Gem, Bundler, Rake, Rails 是什么？

- RubyGems 是 Ruby 的包管理工具，类似 Python 中的 pip
- Gems 是 Ruby 通过 RubyGems 安装的包，为例避免误解，建议用“包”这个名字替代
- Bundler 是基于 Ruby 应用程序目录中的 Gemfile ，用于拉取依赖包的管理工具
- Gemfile 是 Ruby 依赖包清单文件
- Rake 是 Ruby 的构建程序，类似 Linux 中的 make
- Rails 是一个流行的 Ruby 应用程序开发框架

#### Ruby 有哪些常用的应用程序服务器？

WEBrick, passenger, Puma 等

#### 什么是 Gemset？

Ruby RVM 允许我们为依赖项创建一个隔离的环境，这意味着 ruby，gems和irb都是独立的，与系统以及其他环境独立。如果你对 Python 非常熟悉，那么 RVM Gemset 就类似于 Python3 中的 VENV 或者 Python 2 中的 Virtualenv。RVM为每个Ruby版本和 gemset 提供了一个单独的 gem 目录。

#### 如何找到 Ruby 资源？

参考：[Awesome Ruby](https://github.com/markets/awesome-ruby)


#### Rails 如何才能被外网访问？

```text
rails s -b 0.0.0.0
```

#### Ansible 下 `gem install bundler` 报错？

原因：有待进一步研究  
方案：通过 bash -lc 运行 gem install 命令  

```
- name: Install version {{ruby_bundle_version}} of bundler
  shell: bash -lc "gem install bundler -v {{ ruby_bundle_version }} -N"
```

#### 可执行目录下没有 gem, ruby 文件或链接？

本项目通过 RVM 安装，通过 `source /etc/profile.d/rvm.sh` 实现 gem, ruby 等命令的全局化。

#### 如何将 Ruby 包安装到项目目录下？

```
# 安装第三方包到项目 vendor/bundle 目录
bundle install --deployment

# 安装所有包到项目目录
bundle install --path=$(pwd)
```

#### 一个 rails 框架可以部署几个应用？

有待研究。建议部署部署一个。

#### rvm 安装后如何立即生效？

`rvm export -p`

#### 如何使用 gem 设定 rails 包的默认版本？

#### Gemfile.local 与 Gemfile 有什么区别？
