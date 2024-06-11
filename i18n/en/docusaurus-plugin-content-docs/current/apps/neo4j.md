---
title: Neo4j
slug: /neo4j
tags:
  - Figure Database
  - Relationship analysis
---

import Meta from './_include/neo4j.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. When completed installation of Neo4j at Websoft9 console, get the applicaiton's overview and access information from "My Apps"  

2. Access Neo4j Browser and fill in the accurate Connection URL, account, and password to successfully login
   ![Neo4j Console](./assets/neo4j-ssui-websoft9.png)

3. From the **Neo4j Browser Sync**, click on **Clear local data** to logout

### Command Cypher Shell

1. Access the command mode of the Neo4j container and use the 'cypher shell' command

    ```
    Cypher shell
    username: neo4j
    password: *****
    Connected to Neo4j 4.1.0 at neo4j://localhost:7687 as user neo4j.
    Type :help for a list of available commands or :exit to exit the shell.
    Note that Cypher queries must end with a semicolon.
    neo4j@neo4j >
    ```

2. Enter the command ` CALL dbms. showCurrentUser()` View current user

    ```
    neo4j@neo4j >CALL dbms. showCurrentUser();
    +--------------------------+
    |Username | roles | flags|
    +--------------------------+
    |Neo4j | admin | []|
    +--------------------------+
    1 row available after 22 ms, consumed after another 1 ms
    ```

3. User management commands (Enterprise Edition only)
    ```
    #Show all users
    SHOW USERS;
    CALL dbms. security. listUsers();

    #Create a new user, the third parameter represents requestchangepassword
    CALL dbms. security. createUser ('username','password', false);

    #Delete user
    CALL dbms. security. deleteUser ('username');
    ```

4. Change password
    ```
    cypher-shell -u neo4j  -p neo4j  -d system
    ALTER CURRENT USER SET PASSWORD FROM 'neo4j' TO 'neo4j123';
    ```

## Enterprise Edition

### Hosting services

Websoft9 can provide comprehensive procurement and hosting support services for Neo4j Enterprise Edition.

### Application scenarios

* **Social field**: Facebook and LinkedIn analyze each user's friend information, further manage social relationships, and achieve friend recommendations
* **Retail field**: Building a Chain of Relationship Models between Retailers and E-commerce Platforms. Read [Beer and Diapers](https://book.douban.com/subject/3283973/), easy to make product recommendations
* **Financial field**: Build a network profile for users by crawling social relationships from their mobile phone contacts, facilitating risk control and collection
* **Automotive manufacturing field**: Relationship graph of automotive component suppliers, effectively reducing the supply chain risk of 20000 components for a single car
* **Telecommunications field**: Telecommunications operator companies manage complex network infrastructure topologies distributed globally, facilitating more effective operation and maintenance.
* **Knowledge graphs field**: knowledge graphs related to the relationship between companies and people, such as Qichacha and Tianyancha, can be understood as relationship search engines.
* **Public field**: the relationship map similar to the travel path of patients with COVID-19 epidemic can better make accurate troubleshooting.

As can be seen, graph databases are used to store the relationships between **people-people, objects-objects, and people-objects**, for purposes such as recommendations, knowledge graphs, and efficiency.

## Configuration options{#configs}

- Multi user: [User and role management](https://neo4j.com/docs/cypher-manual/current/administration/security/users-and-roles/#administration-security-users), only supported in the enterprise version

- Enable remote access: Add configuration section `dbms.default_listen_address=0.0.0.0`

- [Configuration file](https://neo4j.com/docs/operations-manual/current/configuration)(Mounted): */var/lib/neo4j/neo4j.cn*

- Port Description: [Port on Configuration file](https://neo4j.com/docs/operations-manual/current/configuration/ports/)

- Tools: [Neo4j Tools](https://neo4j.com/docs/operations-manual/current/tools/)

- Command line: [Crypto Shell](https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/)

- [Neo4j REST API](https://neo4j.com/docs/rest-docs/current/)

- [Neo4j Admin](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/)

- [Clustering](https://neo4j.com/docs/operations-manual/current/clustering/): Enterprise version features

- [Authentication and Authorization](https://neo4j.com/docs/operations-manual/current/authentication-authorization/)

## Administer{#administrator}

- **[Retrieve Password](https://neo4j.com/docs/operations-manual/current/configuration/password-and-user-recovery)**: Add `dbms.security.auth_enabled=false` to the configuration file, disable password verification, and reset the password before restoring.

## Troubleshooting{#troubleshooting}

#### Error connecting to database?

Problem description: Neo4j Browser encountered an error when connecting to the database.
Cause analysis: The **security group port** corresponding to your server is not enabled (entry rule), resulting in the inability to connect to the database

#### Is Role displayed as empty?

Neo4j Community Edition does not support Rules, so it is displayed as empty