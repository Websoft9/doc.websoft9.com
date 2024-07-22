---
title: Zookeeper
slug: /zookeeper
tags:
  - Distributed coordination
  - HA
  - Microservice
---

import Meta from './_include/zookeeper.md';

<Meta name="meta" />

## Getting started{#guide}

Completed installation Zookeeper at **Websoft9 console**, get the applicaiton's overview and access information from **My Apps**  

### Client connection 

1. Get the container name for Zookeeper, assuming `zk_name` 

2. Run the following command to connect and start the client connection (replace `zk_name` with the actual value) 
    ``` 
    docker run -it --rm --net=container:zk_name zookeeper zkCli.sh -server zookeeper 
    ``` 

3. After successful connection, run `ls /` to query znode

### Setup super_digest authentication

1. When the client connects to the Zookeeper node and runs `getAcl /`, it will see the following information, indicating that the node is open to any user 
    ``` 
    [zk: zookeeper (CONNECTED) 3] getAcl / 
    'world,'anyone
    : cdrwa 
    ``` 

2. Run the following command to modify permissions 
    ``` 
    addauth digest super:yourpassword 
    setAcl / digest:super:password:cdrwa 
    ``` 

3. If you run `getAcl /` again, you will find that **Insufficient permission : /**

## Configuration options{#configs}

- ACL authentication mode(√) 
- Configuration file(√): Not enabled by default, using environment variable settings

## Administer{#administrator}

## Troubleshooting{#troubleshooting}
