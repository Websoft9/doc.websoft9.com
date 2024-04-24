---
title: Maven
slug: /maven
tags:
  - 运行环境
  - Java 编译打包
  - Maven
---

import Meta from '../../apps/_include/maven.md';

<Meta name="meta" />

## 入门指南{#guide}

### 安装应用{#install}

下面通过 [ springboot-jsp 示例](git clone https://github.com/hellokoding/springboot-jsp.git) 为例，描述应用安装过程：

1. Websoft9 控制台安装 Maven 运行环境


2. 在编排修改 **.src/cmd.sh**，使注释掉的安装脚本生效
   ```
    git clone https://github.com/hellokoding/springboot-jsp.git
    cd springboot-jsp
    mvn package
   ```

3. 重建应用生效后，即可查看编译成功的 war 包 

## 配置选项{#configs}


## 管理维护{#administrator}


## 故障