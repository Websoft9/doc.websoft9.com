---
title: OpenJDK
slug: /openjdk
tags:
  - 运行环境
  - java
  - OpenJDK
---

import Meta from './_include/openjdk.md';

<Meta name="meta" />

## 入门指南{#guide}

### 部署应用{#sample}

#### war包部署

下面通过常见的 Java 应用 [Jenkins](https://www.jenkins.io) 为例，描述应用安装过程：
> Jenkins 仅仅支持 OpenJDK 17，21

1. Websoft9 控制台安装 OpenJDK 运行环境

2. 进入容器，安装 Jenkins，命令如下：
   ```
   cd /home/openjdk/app && curl -L -O https://get.jenkins.io/war/latest/jenkins.war
   ```

3. 应用被安装在路径： **/home/openjdk/app/jenkins.war**

4. 在编排修改 **docker-comopse.yml**，使 **command** 生效
   ```
   - command: sh -c "cd /home/openjdk/app && java -jar jenkins.war"
   ```

5. 重建应用生效后即可访问 Jenkins


## 配置选项{#configs}

## 管理维护{#administrator}

## 故障

#### Jenkins 无法正常启动?

Jenkins 仅仅支持 OpenJDK 17、21，其他版本的 OpenJDK 无法运行。 