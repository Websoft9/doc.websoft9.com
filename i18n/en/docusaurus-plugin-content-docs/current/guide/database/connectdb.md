---
sidebar_position: 2.0
slug: /connectdb
---

# Connect App database

Two methods for you to connect application database at Websoft9 platform

- Web-based online tools
- Local client tools

We suggest you use [Web-based online tools](./dbtools) which connect database at **Private network**. It simplifies database access, avoiding local software maintenance. 

## Prerequisites

The two aspects required to connect to and manage a database:

- **Prepare database management tools**

  - [Install web-based tools](./dbtools) at Websoft9 Console
  - or install client tool at your local computer

- **Prepare your database connection strings**, like host, user, password, port

  - [Get database connection strings from Websoft9 console](./app-getdetail#db)
  - [Fleet for databases](./createdb#table)


## Web-based online connect

Popular [database management tools](./apps/#databases) in different database product ecosystems, here are the popular tools

- [phpMyAdmin](./phpmyadmin)
- [pgAdmin](./pgadmin)
- [CloudBeaver](./cloudbeaver)
- [RedisInsight](./redisinsight)

## Local client connect

The application database of Websoft9 not allowed from Internet access by default, if you want to use local client to connect it, you should enable the database to be accessed from Internet.  

There one of below methods for you to expose database port for Internet access:

- Add [TCP Proxy at Websoft9 Gateway](./gateway-proxy#stream) for database
- Add [SSH tunnel proxy at host machine](./gateway-proxy#stream) for database
- [Update the application deployment](./app-compose), expose the database container port to host machine