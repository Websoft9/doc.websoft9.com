---
title: Tomcat
slug: /tomcat
tags:
  - Java web 服务器
  - JSP
  - Tomcat
---

import Meta from '../../apps/_include/tomcat.md';

<Meta name="meta" />

## 入门指南{#guide}

### 部署 Tomcat 应用{#deploy}

以 Tomcat 官方示例包来展示部署过程：

1. 进入 Tomcat 容器

2. 进入 web 应用目录并下载示例 war 包
    ```
    cd /usr/local/tomcat/webapps && wget https://tomcat.apache.org/tomcat-10.0-doc/appdev/sample/sample.war
    ```

3. Tomcat会自动解压包，Websoft9 控制台可访问 URL


## 配置选项{#configs}

## 管理维护{#administrator}

## 故障

#### 安装后访问 Tomcat 报404 ？

原因：默认的 Tomcat 容器没有部署任何 web 应用
对应方法：部署自己的 web 应用即可正常访问
