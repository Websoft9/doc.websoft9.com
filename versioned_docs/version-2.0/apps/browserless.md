---
title: Browserless
slug: /browserless
tags:
  - 无头浏览器 
  - API驱动
  - Browserless
---

import Meta from './_include/browserless.md';

<Meta name="meta" />

## 入门指南{#guide}

### 测试应用

1. Websoft9 控制台安装 Browserless 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取访问 URL

2. 运行如下脚本测试应用，成功会下载网站的图片

    ```
    curl -X POST \
      http://访问URL/screenshot?token=YOUR_API_TOKEN_HERE \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -d '{
      "url": "https://www.websoft9.com/",
      "options": {
        "fullPage": true,
        "type": "png"
      }
    }' \
      --output "screenshot.png"
    ```

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障