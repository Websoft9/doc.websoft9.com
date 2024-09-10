---
title: Trivy
slug: /trivy
tags:
  - Antivirus
  - Security protection
  - trivy
---

import Meta from './\_include/trivy.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initial Setup {#wizard}

1. After completing the installation of Trivy via the **Websoft9 Console**, retrieve the application's **Overview** and **Access** information from the **My Apps** section.

2. To start a virus protection scan, access the Trivy container and run the following command:
   ```bash
   trivy fs /scandir
   ```

## Configuration Options {#configs}

- **CLI (√)**: `trivy`

## Administration {#administrator}

## Troubleshooting {#troubleshooting}

#### How to perform a quick scan?

Access the Trivy container and run the following commands:

```bash
apk add --no-cache python3 && ln -sf python3 /usr/bin/python
trivy fs --scanners vuln /tmp/usr/share
```
