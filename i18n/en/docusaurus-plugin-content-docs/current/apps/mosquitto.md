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

There are multiple ways to [enable authentication for Mosquitto](https://mosquitto.org/documentation/authentication-methods/), we will introduce the [password file](https://mosquitto.org/man/mosquitto_passwd-1.html) Method:

1. Access the Mosquitto container and create a password file using the following command (file name, username, and password can be customized) 
   ``` 
   mosquitto_passwd -H sha512  -c -b /mosquitto/config/passwd_file yourusername yourpasssord 
   ``` 

2. Modify the following two items in the configuration file (mandatory): 

   - Set password_file to: */mosquitto/passwd_file*
   - allow_anonymous: false 

3. Effective after rebuilding the application  

### GUI

Reference: [MQTTX](./mqttx)

## Configuration options{#configs}

- Configuration file(volumed): */mosquito/config/mosquito.conf* 
- User authentication(√)

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### docker logs Error: Address not available？

Mosquitto 2.0 requires you to configure listeners and authentication before it will allow connections from anything other than the loopback interface. 