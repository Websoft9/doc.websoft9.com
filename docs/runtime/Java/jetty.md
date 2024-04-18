---
title: Jetty
slug: /jetty
tags:
  - 运行环境
  - Java Web 服务器
  - Jetty
---

import Meta from '../../apps/_include/jetty.md';

<Meta name="meta" />

## 入门指南{#guide}

### 安装应用{#install}

下面通过 [ Tomcat war 包](https://tomcat.apache.org/tomcat-11.0-doc/appdev/sample/sample.war) 为例，描述应用安装过程：

1. Websoft9 控制台安装 Jetty 运行环境


2. 在编排修改 **.src/cmd.sh**，使注释掉的安装脚本生效
   ```
   cd /var/lib/jetty/webapps
   curl -o ROOT.war https://tomcat.apache.org/tomcat-11.0-doc/appdev/sample/sample.war
   ```

3. 重建应用生效后，即可访问访问示例 Web 应用 

## 配置选项{#configs}


## 管理维护{#administrator}


## 故障