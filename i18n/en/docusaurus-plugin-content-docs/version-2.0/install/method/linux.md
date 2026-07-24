---
sidebar_position: 1
slug: /install-linux
title: "For Linux"
---


# Installation for Linux

Websoft9 currently only supports installation on Linux hosts.

## Install & Upgrade

The install script supports both **fresh install** and **upgrade**, and auto-detects the current environment. [Back up your data](../../admin/backup) before upgrading.

```
# Quick install
wget -O install.sh https://artifact.websoft9.com/websoft9/release/install.sh && sudo bash install.sh

# Custom options
sudo bash install.sh --console-port 9000 --path "/data/websoft9/source" --version "latest"
```

> Upgrade does not affect deployed applications.

## Offline Installation

For air-gapped environments without internet access, please contact [Websoft9 Support Team](./helpdesk).

## Uninstall

Websoft9 supports uninstallation. Data is **retained by default**. To fully purge, use `--purge` mode.

```
# Uninstall (keep data)
curl -fsSL https://artifact.websoft9.com/websoft9/release/uninstall.sh | sudo bash

# Full purge
sudo bash uninstall.sh --purge --yes
```