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

### 扩展

## 概念与原理

### RubyGems 

Maven 是一个项目管理工具，可以对 Java 项目进行构建、依赖管理。

### RVM

RVM 是一个用于安装和管理多版本 Ruby 的命令行工具，虽然不是 Ruby 官方出品，但非常流行。

## 问题

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
