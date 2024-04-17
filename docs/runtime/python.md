---
title: Python
slug: /python
tags:
  - 运行环境
  - runtime
  - Python
---

import Meta from '../apps/_include/python.md';

<Meta name="meta" />

## 配置选项{#configs}

## 安装范例{#guide}

下面通过 [ Web 框架 FastAPI](https://github.com/tiangolo/fastapi) 为例，描述应用安装过程：

1. Websoft9 控制台安装 Python 运行环境

2. 在编排修改 **.src/cmd.sh**，使注释掉的安装脚本生效
   ```
    pip install fastapi uvicorn[standard]
    cat << 'EOF' > main.py
    from typing import Union

    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
    EOF
    uvicorn main:app --host 0.0.0.0 --port 8080
   ```

3. 重建应用生效后，即可访问访问示例 Web 应用 


## 管理维护{#administrator}
## 故障