---
title: Meilisearch
slug: /meilisearch
tags:
  - 模糊搜索
  - 实时索引
  - Meilisearch
---

import Meta from './_include/meilisearch.md';

<Meta name="meta" />

## 入门指南{#guide}

### 添加索引

1. Websoft9 控制台安装 Meilisearch 后，通过 **我的应用** 查看应用详情，在 **访问** 标签页中获取访问 URL

2. 浏览器访问 URL，目前还没有任何 Index

3. 使用下列命令发送一个索引数据

    ```
    curl \
      -X POST 'http://IP:Port/indexes/movies/documents' \
      -H 'Content-Type: application/json' \
      --data-binary '[
        { "id": 1, "title": "Justice League", "genre": ["Action", "Adventure"] },
        { "id": 2, "title": "Wonder Woman", "genre": ["Action", "Fantasy"] },
        { "id": 3, "title": "The Avengers", "genre": ["Action", "Sci-Fi"] },
        { "id": 4, "title": "Inception", "genre": ["Action", "Sci-Fi", "Thriller"] },
        { "id": 5, "title": "The Dark Knight", "genre": ["Action", "Crime", "Drama"] }
      ]'
    ```

4. 再次回到页面，索引数据可以正常显示了

## 配置选项{#configs}

## 管理维护{#administrator}

## 故障