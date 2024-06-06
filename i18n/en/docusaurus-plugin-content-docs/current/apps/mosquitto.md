---
title: Mosquitto
slug: /mosquitto
tags:
  - IOT
  - MQTT
  - MQ
---

import Meta from './_include/mosquitto.md';

<Meta name="meta" />

## Getting started{#guide}

### Enable authentication 

There are multiple ways to [enable authentication for Mosquitto](https://mosquitto.org/documentation/authentication-methods/), below is [password file](https://mosquitto.org/man/mosquitto_passwd-1.html) method:

1. Access to Mosquitto container and create a password file using the below command (file name, username, and password can be customized) 
   ``` 
   mosquitto_passwd -H sha512  -c -b /mosquitto/config/passwd_file yourusername yourpasssord 
   ``` 

2. Modify below items in the configuration file */mosquito/config/mosquito.conf* : 

   - password_file path: */mosquitto/passwd_file*
   - allow_anonymous: `false`

3. Rebuild the application

### GUI for Mosquitto

Reference: [MQTTX](./mqttx)

## Configuration options{#configs}

- Configuration file(volumed): */mosquito/config/mosquito.conf* 
- User authentication(√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### docker logs Error: Address not available？

Mosquitto 2.0 requires you to configure listeners and authentication before it will allow connections from anything other than the loopback interface. 
