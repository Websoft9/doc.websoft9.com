---
title: Ruby
slug: /ruby
tags:
  - 运行环境
  - runtime
  - Ruby
---

import Meta from './_include/ruby.md';

<Meta name="meta" />

## 入门指南{#guide}

### 安装应用{#install}

下面通过 [ jekyll web 应用](https://github.com/jekyll/jekyll) 为例，描述应用安装过程：

1. Websoft9 控制台安装 Ruby 运行环境


2. 在编排修改 **.src/cmd.sh**，使注释掉的安装脚本生效
   ```
    gem install bundler jekyll
    jekyll new mysite
    cd mysite
    bundle exec jekyll serve --host 0.0.0.0 --port 8080
   ```

3. 重建应用生效后，即可访问访问示例 Web 应用 

## 配置选项{#configs}


## 管理维护{#administrator}


## 故障