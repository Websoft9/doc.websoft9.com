---
title: Home Assistant
slug: /homeassistant
tags:
  - Internet of Things
  - IoT 
  - Home Assistant
---

import Meta from './_include/homeassistant.md';

<Meta name="meta" />

## Getting started{#guide}

### Connecting to MQTT

The Home Assistant application does not include the MQTT service by default:

1. Prepare the MQTT service or install the open source MQTT server [Eclipse Mosquitto](./mosquitto).    

2. Refer to: [MQTT Configuration](https://www.home-assistant.io/integrations/mqtt) to complete the connection and configuration.  

## Configuration options{#configs}

- [Configuration files](https://www.home-assistant.io/docs/configuration/) directory(mounted): /config
- [Home Assistant Add-ons](https://github.com/home-assistant/addons): only available for Linux native installations, not for containerized versions.

## Administer{#administrator}

## Troubleshooting{#troubleshooting}

#### Can't access Home Assistant through the domain name?

Currently it can be accessed only via IP and port. There is no solution for domain access at this time.
