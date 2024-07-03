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

1. When completed installation of Dgraph at **Websoft9 Console**, get the applicaiton's **Overview** and **Access** information from **My Apps**  

2. Select **Launch Latest**, access Dgraph console

### Test publicly available database nodes

1. Metal can connect to the official public instance https://play.dgraph.io for testing.

2. After connecting successfully, run the following code, then you can run to get the relationship graph.
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

   - The URL does not support container names and must be a public IP or domain name.
   - port is the external port of the alpha(database) node

2. Login without password

> groot Password setting is an enterprise feature(ACL)

## Configuration options{#configs}

- Dgraph application contains three nodes: zero(cluster), alpha(database), ratel(graphical)
- ACL: enterprise edition features

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### ratel load incomplete?

The application itself contains some external js.

#### ratel can be accessed without password?

Yes, it is recommended to use **Gateway** for setting password.

#### What is the purpose of whitelist and token?

Controls administrative operations on the database, e.g. building tables. But it does not control queries, any external connection can be queried.