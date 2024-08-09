---
title: Dgraph
slug: /dgraph
tags:
  - Graph Database
  - Distributed
  - NoSQL
---

import Meta from './_include/dgraph.md';

<Meta name="meta" />

## Getting started{#guide}

### Initial setup{#wizard}

1. After completing the installation of Dgraph in the **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from the **My Apps** section

2. Select **Launch Latest** to access the Dgraph console

### Test publicly available database nodes

1. Metal can connect to the official public instance at https://play.dgraph.io for testing.

2. After a successful connection, run the following code to get the relationship graph.
   ```
   {
    user(func: eq(name, "Alice")) {
        user(func: eq(name, "Alice")) { name
        friend {
        user(func: eq(name, "Alice")) { name
        name { name
        }
    }
    }
   ```

### Test the database node for this application(alpha)

1. Connect to `http://URL:port` 

   - The URL must be a public IP or domain name; container names are not supported.
   - The port is the external port of the alpha(database) node

2. Login without a password

> Setting a password for the groot user is an enterprise feature(ACL)

## Configuration options{#configs}

- The Dgraph application consists of three nodes: zero(cluster), alpha(database), and ratel(graphical interface)
- ACL (Access Control List) features are available in the enterprise edition.

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### ratel load incomplete?

The application includes some external JavaScript files.

#### ratel can be accessed without password?

Yes, it is recommended to use a **Gateway** to set a password.

#### What is the purpose of whitelist and token?

They control administrative operations on the database, such as building tables. However, they do not control queries, allowing any external connection to perform queries.
