---
title: Spring Boot
slug: /springboot
tags:
  - Spring Boot
  - Java
  - 开发工具
---

import Meta from './_include/springboot.md';

<Meta name="meta" />

## 入门指南 {#guide}

### 初始化 {#wizard}

在 Websoft9 控制台安装 Spring Boot 后，打开 **我的应用** > **Spring Boot**，在 **访问** 标签页获取访问地址。打开地址后，默认示例应用会显示 `Spring Boot is running...`。

### 运行示例接口 {#endpoints}

访问 `/hello` 查看 JSON 响应，访问 `/actuator/health` 检查应用健康状态。若需要开发项目，可在容器中使用 Maven 命令运行应用、执行测试或打包。

### 开发项目 {#development}

1. 在 Websoft9 控制台的应用页面打开终端，或通过 Docker 执行 `docker exec -it springboot bash` 进入容器。
2. 示例 Maven 项目位于 `/workspace`。首次启动时会自动生成示例项目，可在此目录编辑 Java 代码，或替换为自己的 Maven 项目。
3. 在 `/workspace` 中运行 `mvn spring-boot:run` 启动项目；运行 `mvn test` 执行测试，或运行 `mvn package` 打包。

## 最佳实践

### 启用 PostgreSQL {#postgres}

默认部署不启动数据库。需要使用随应用提供的 PostgreSQL 时，在应用 **Compose** 页面的 `.env` 中启用 `COMPOSE_PROFILES=postgres` 并重建应用。此配置会启动 `postgres` 服务并启用 Spring 的 `postgres` profile；数据库连接参数由 `SPRING_DATASOURCE_*` 环境变量提供。在终端执行 Maven 命令时，使用 `-Ppostgres` 加载相应的 JDBC 依赖。

## 配置选项 {#configs}

| 配置项 | 说明 | 默认值/位置 |
|--------|------|------------|
| Web Console | 应用 Web 访问端口 | 8080 |
| `COMPOSE_PROFILES` | 启用可选 PostgreSQL 服务及 Spring `postgres` profile | 默认不启用 |
| `SPRING_DATASOURCE_*` | PostgreSQL profile 使用的 Spring 数据源设置 | 在 `.env` 中配置 |
| `/workspace` | 示例项目和自定义 Maven 项目目录 | 持久化卷 |
| `/root/.m2` | Maven 本地依赖缓存 | 持久化卷 |

修改 Compose 或环境变量配置后，需要重建应用使其生效。

## 管理维护 {#administrator}

### 升级

通过 Websoft9 控制台升级应用。生产环境建议指定固定版本，而不是依赖可能变化的 `latest` 标签。升级前先备份项目所在的 `/workspace` 持久化数据。

### 备份与恢复

备份 `/workspace` 项目卷；若使用可选 PostgreSQL，也需一并备份其数据卷。恢复时将数据还原到对应卷，再通过控制台启动或重建应用。

## 故障排除 {#troubleshooting}

#### 应用无法启动？

查看应用的 Compose 日志，确认启动错误；首次启动时检查项目是否已在 `/workspace` 生成。

#### 访问端口失败？

确认应用运行状态及访问地址，并检查服务器防火墙或云安全组是否允许对应端口。

## 参考 {#references}

- [Spring Boot 官方文档](https://docs.spring.io/spring-boot/installing.html)
- [Spring Boot Docker 镜像](https://github.com/spring-projects/spring-boot)
