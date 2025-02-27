---
title: Zammad
slug: /zammad
tags:
  - Customer Service System
  - Work Order System
  - zammad
---

import Meta from './\_include/zammad.md';

<Meta name="meta" />

## Getting Started {#guide}

1. After installing Zammad via the **Websoft9 Console**, view the application details through **My Applications** and retrieve the login information from the **Access** tab.

2. Zammad will initialize automatically. Due to the lengthy initialization process, please wait a few minutes before the initial page appears.

## Configuration Options {#configs}

- **Multilingual (✅)**: Zammad supports multiple languages. Switch languages via the user profile settings.

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### Can't connect after replacing the database?

Zammad database connection does not support hostnames containing an underscore ("\_"), Ensure that the replacement database hostname does not contain any underscores to meet the connection requirements.

#### Slow Initialization?

Zammad is taking longer than expected to initialize, Check your server resources and ensure sufficient CPU and memory are allocated to support Zammad’s initialization process.
