---
title: Zookeeper
slug: /zookeeper
tags:
  - Web 面板
  - 可视化
  - GUI
---

import Meta from './\_include/zookeeper.md';

<Meta name="meta" />

## Getting Started {#guide}

After installing Zookeeper in the Websoft9 console, view the application details through “My Applications” and get access information in the “Access” tab.

### Client Connection

1. Get the container name of Zookeeper, assuming it is zk_name.

2. Start the client connection by running the following command connection (replace zk_name with the actual value)
   `docker run -it --rm --net=container:zk_name zookeeper zkCli.sh -server zookeeper`

3. After a successful connection, run `ls /` to query the znode.

### Setting up super_digest authentication

1. The client connects to the Zookeeper node and runs `getAcl /` and sees the following message, indicating that the node is open to any user

   ```
    [zk: zookeeper(CONNECTED) 3] getAcl /
    'world,'anyone
    : cdrwa
   ```

2. Run the following command to change the permissions

   ```
   addauth digest super:yourpassword
   setAcl / digest:super:password:cdrwa
   ```

3. Run `getAcl /` again and you'll see **Insufficient permission : /**

## Configuration options {#configs}

- ACL authentication mode (√)
- Configuration file (√), but not enabled, set using environment variables

## Administrative maintenance {#administrator}

## Troubleshooting
