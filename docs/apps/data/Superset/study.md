---
sidebar_position: 3
slug: /superset/study
tags:
  - Superset
  - 大数据分析
  - BI
---

# 原理学习

[Apache Superset](https://superset.apache.org/) 是一个开源的数据探查与可视化平台（曾用名 Panoramix、Caravel ），该工具在可视化、易用性和交互性上非常有特色，用户可以轻松对数据进行可视化分析。Superset 也是一款企业级商业智能 Web 应用程序。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-dash-websoft9.png)

## CLI

Superset 提供了强大的的命令行工具 `superset`

使用 **SSH** 登录到云服务器，登录到容器后即可使用 CLI  

```
# 登录到 Superset 容器
docker exec -it superset_app bash

# 运行 CLI 命令
superset
```

主要参数如下：

```
Usage: superset [OPTIONS] COMMAND [ARGS]...

  This is a management script for the Superset application.

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  db                        Perform database migrations.
  export-dashboards         Export dashboards to JSON
  export-datasource-schema  Export datasource YAML schema to stdout
  export-datasources        Export datasources to YAML
  fab                       FAB flask group commands
  flower                    Runs a Celery Flower web server Celery Flower
                            is...

  import-dashboards         Import dashboards from JSON
  import-datasources        Import datasources from YAML
  init                      Inits the Superset application
  load-examples             Loads a set of Slices and Dashboards and a...
  load-test-users           Loads admin, alpha, and gamma user for testing...
  refresh-druid             Refresh druid datasources
  routes                    Show the routes for the app.
  run                       Run a development server.
  set-database-uri          Updates a database connection URI
  shell                     Run a shell in the app context.
  sync-tags                 Rebuilds special tags (owner, type, favorited...
  update-datasources-cache  Refresh sqllab datasources cache
  version                   Prints the current version number
  worker                    Starts a Superset worker for async SQL query...
```