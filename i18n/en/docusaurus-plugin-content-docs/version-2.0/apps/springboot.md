---
title: Spring Boot
slug: /springboot
tags:
  - Spring Boot
  - Java
  - Developer Tools
---

import Meta from './_include/springboot.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initialize {#wizard}

After installing Spring Boot in the Websoft9 console, open **My Apps** > **Spring Boot** and find the application URL in the **Access** tab. Open the URL to see the default demo response: `Spring Boot is running...`.

### Try the demo endpoints {#endpoints}

Open `/hello` to get a JSON response, or `/actuator/health` to check the application health endpoint. You can also use Maven inside the container to run, test, or package the project.

### Develop the project {#development}

1. Open a terminal for the app in the Websoft9 console, or enter the container with `docker exec -it springboot bash`.
2. The demo Maven project is in `/workspace`. It is generated automatically on first startup. Edit its Java code or replace it with your own Maven project.
3. From `/workspace`, run `mvn spring-boot:run` to start the app, `mvn test` to run tests, or `mvn package` to package it.

## Best Practices

### Enable PostgreSQL {#postgres}

The default deployment does not start a database. To use the bundled PostgreSQL, enable `COMPOSE_PROFILES=postgres` in the app's `.env` on the **Compose** tab and rebuild the app. This starts the `postgres` service and activates Spring's `postgres` profile; database connection settings are supplied through `SPRING_DATASOURCE_*` environment variables. When running Maven commands in the shell, use `-Ppostgres` to load the JDBC dependencies.

## Configuration {#configs}

| Setting | Description | Default / location |
|---------|-------------|--------------------|
| Web Console | Web access port | 8080 |
| `COMPOSE_PROFILES` | Enables the optional PostgreSQL service and Spring `postgres` profile | Disabled by default |
| `SPRING_DATASOURCE_*` | Spring datasource settings used by the PostgreSQL profile | Configure in `.env` |
| `/workspace` | Demo project and custom Maven project directory | Persistent volume |
| `/root/.m2` | Local Maven dependency cache | Persistent volume |

Rebuild the app after changing Compose or environment settings.

## Administration {#administrator}

### Upgrade

Upgrade the app from the Websoft9 console. For production, pin a specific version instead of relying on the potentially changing `latest` tag. Back up the `/workspace` persistent data before upgrading.

### Backup and restore

Back up the `/workspace` project volume. If the optional PostgreSQL service is enabled, back up its data volume as well. Restore the data to the corresponding volumes, then start or recreate the app from the console.

## Troubleshooting {#troubleshooting}

#### The app does not start

Check the app's Compose logs for startup errors. On first startup, also confirm that the project was generated in `/workspace`.

#### The app is not reachable

Check the app status and access URL, then confirm that the relevant port is allowed by the server firewall or cloud security group.

## References {#references}

- [Spring Boot documentation](https://docs.spring.io/spring-boot/installing.html)
- [Spring Boot Docker image](https://github.com/spring-projects/spring-boot)
