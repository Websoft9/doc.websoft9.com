---
sidebar_position: 5
slug: /runtime/ruby
tags:
  - Ruby
  - Rails
  - 运行环境
---

# Deploy Ruby app

## 安装 Ruby 应用

在 Ruby Runtime 环境上安装一个网站，一般是基于已有的 Rails 环境配置。  

主要步骤包括：

```
# 安装应用包
gem install yourapp

# 基于 rails 创建应用脚手架
rail new yourapp

# 安装依赖包
cd yourapp
bundle install

# 自动配置
bin/rake ..

# 运行
rails s -b 0.0.0.0
```

## 维护 Ruby 环境

参考本文的相关专题：[《Ruby 指南》](../ruby) 和 [《Ruby 进阶》](../ruby/advanced) 

