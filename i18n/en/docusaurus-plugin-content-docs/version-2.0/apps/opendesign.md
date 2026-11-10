---
title: OpenDesign
slug: /opendesign
tags:
  - OpenDesign
  - Design Collaboration
  - AI
---

import Meta from './_include/opendesign.md';

<Meta name="meta" />

## Getting Started {#guide}

### Initialize {#wizard}

After installing OpenDesign in the Websoft9 console, open **My Apps** > **OpenDesign** and get the access URL and credentials from the **Access** tab. Sign in to open the OpenDesign console.

### Start using OpenDesign {#usage}

After signing in, use the features available in the OpenDesign console. For details about the product's functionality and workflows, refer to the [OpenDesign website](https://open-design.ai) and project documentation.

### Change the password {#password}

1. Open the OpenDesign **Compose** tab in the Websoft9 console.
2. Update the password in `.env` and save.
3. Rebuild the app for the change to take effect.

## Best Practices

### Preserve application data {#data}

Application data is stored in the `opendesign_data` persistent volume mounted at `/app/.od`. Back up this volume before upgrading or recreating the app. To override configuration, mount a single file as read-only; do not replace the entire configuration directory.

## Configuration {#configs}

| Setting | Description | Default / location |
|---------|-------------|--------------------|
| Web Console and API | Web interface and API port | 7456 |
| Application data | OpenDesign persistent data directory | `opendesign_data` volume mounted at `/app/.od` |
| Password | Update in the app's `.env` | Rebuild the app after changing |
| Image version | Currently supported version | 0.24.1; `latest` is also available |
| Configuration files | Override with a read-only single-file mount | Files are included in the image |

Pin a specific image version for production.

## Administration {#administrator}

### Upgrade

Upgrade OpenDesign from the Websoft9 console. Back up the `opendesign_data` volume first. Recreate the app after upgrading or changing its configuration as prompted by the console.

### Backup and restore

Back up and restore the `opendesign_data` persistent volume. If you override configuration files, restore each read-only file mount separately; do not mount a directory over the image's entire configuration directory.

## Troubleshooting {#troubleshooting}

#### The app does not start

Check the app's Compose logs and confirm that the image and service started successfully.

#### The page is not reachable

Verify the access URL and check that port 7456 is allowed by the server firewall or cloud security group.

#### The new password does not work

Confirm that the password was saved in `.env` on the Compose tab and that the app was rebuilt before signing in again.

## References {#references}

- [OpenDesign website](https://open-design.ai)
- [OpenDesign project documentation](https://github.com/nexu-io/open-design)
- [OpenDesign releases](https://github.com/nexu-io/open-design/releases)
