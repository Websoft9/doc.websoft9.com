---
title: Zookeeper
slug: /zookeeper
tags:
  - Distributed coordination
  - HA
  - Microservice
---

import Meta from './\_include/zookeeper.md';

<Meta name="meta" />

## Getting Started {#guide}

After installing Zookeeper via the **Websoft9 console**, retrieve the application’s overview and access information from **My Apps**.

### Client Connection

1. Obtain the container name for Zookeeper, referred to as `zk_name`.

2. Connect to the client by running the following command (replace `zk_name` with the actual value):

   ```bash
   docker run -it --rm --net=container:zk_name zookeeper zkCli.sh -server zookeeper
   ```

3. Once connected, run `ls /` to query the znodes.

### Setup Super Digest Authentication

1. Upon connection, running `getAcl /` will show the following, indicating open access:

   ```bash
   [zk: zookeeper (CONNECTED) 3] getAcl /
   'world,'anyone
   : cdrwa
   ```

2. Modify permissions with:

   ```bash
   addauth digest super:yourpassword
   setAcl / digest:super:yourpassword:cdrwa
   ```

3. Running `getAcl /` again should now result in **Insufficient permission : /**.

## Configuration Options {#configs}

- **ACL Authentication Mode**: Enabled (√)
- **Configuration File**: Not enabled by default; configured via environment variables.

## Administration {#administrator}

- **Manage via Websoft9 Console**: Administer and monitor Zookeeper through the Websoft9 interface.

## Troubleshooting {#troubleshooting}

- **Common Issues**: Review the official Zookeeper documentation for known issues and their resolutions.
