---
title: Node.js
slug: /nodejs
tags:
  - 运行环境
  - runtime
  - Node.js
---

import Meta from './_include/nodejs.md';

<Meta name="meta" />

## 入门指南{#guide}

### 安装应用{#install}

下面通过常见的 Node.js 应用 [docusaurus](https://docusaurus.io/docs)为例，描述应用安装过程：

1. Websoft9 控制台安装 Node.js 运行环境

2. 进入容器，安装 docusaurus，命令如下：
   ```
   cd /home/node/app && npx create-docusaurus@latest classic
   cd classic && yarn install
   ```

3. 应用被安装在路径： **/home/node/app/classic**

4. 在编排修改 **docker-comopse.yml**，使 **command**生效，重建应用后即可访问 docusaurus
   ```
   - command: sh -c "cd /home/node/app/classic && npm run start -- --host 0.0.0.0"
   ```

### Command 使用

您可以在**docker-comopse.yml** 的 **command** 添加您的命令，它支持多行和shell的语法，并支持  
引入环境变量，也就是说，它可以做任何您想做的事情。以下是示例：

      ```
      command: |
        /bin/bash -c "
        if [ -z \"$W9_URL\" ]; then
          echo 'W9_URL is empty, not need to change, exiting...'
          exit 0
        fi
        "
    ```

## 配置选项{#configs}


## 管理维护{#administrator}


## 故障

