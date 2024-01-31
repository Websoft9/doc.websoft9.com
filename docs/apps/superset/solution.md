---
sidebar_position: 2
slug: /superset/solution
tags:
  - Superset
  - 大数据分析
  - BI
---

# 场景方案

Superset 可以与其他的软件平台**集成**一起使用，解决 大数据分析 过程中的各种[场景问题](https://superset.apache.org/)。

## 集成 Superset 图表(Charts) 到其他 Web 应用    

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-charts-integrate-websoft9.png)

1. 修改 Superset 配置文件(/data/apps/superset/src/docker/pythonpath_dev/superset_config.py)，并重启容器
- 在配置文件中添加全局配置 PUBLIC_ROLE_LIKE = "Gamma"
- 执行 docker restart superset-app 命令，重启容器

2. 编辑角色 Public 权限 ：点击权限列表框末尾的空白处，添加 all database access on all_database_access 权限  

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-editrole-websoft9.png)

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-add-role-permissions-websoft9.png)

3. 获取图表(Charts)的URL，嵌入到 Web 应用页面  

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-copyurl-websoft9.png)

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/superset/superset-chart-in-page-websoft9.png)

[更多参考](https://github.com/apache/superset/blob/1.5.2/docs/docs/security.mdx)
 



