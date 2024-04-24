---
title: OpenJDK
slug: /openjdk
tags:
  - 运行环境
  - java
  - OpenJDK
---

import Meta from '../../apps/_include/openjdk.md';

<Meta name="meta" />

## 部署网站{#deploy}

### 手动部署

下面以 [Jenkins](https://www.jenkins.io) 为例，描述应用安装过程：

1. Websoft9 控制台安装 JDK 环境（Jenkins 仅仅支持 OpenJDK 17，21）

2. 进入 OpenJDK 容器，分别运行如下命令：

    ```
    #1 下载 war 包
    curl -L -O https://get.jenkins.io/war/latest/jenkins.war

    #2 直接运行程序或在后台运行程序（取其一）
    java -jar jenkins.war --httpPort=8080
    nohup java -jar jenkins.war --httpPort=8080 > output.log 2>&1 &
    ```

3. 此时，即可访问此 Web 程序

### 自动部署

参考 Web Runtime 通用的文档章节：[自动部署指南](./runtime#auto)

