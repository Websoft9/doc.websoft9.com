---
sidebar_position: 1
slug: /install-linux
title: "For Linux"
---


# Installation for Linux

The Linux package has different container services and tools required to run Websoft9. Most users can install it without laborious configuration.

## Automatic installation

To install Websoft9, you need root access; otherwise, use `sudo su` before running the script:

```
# Installation with default parameters
wget -O install.sh https://artifact.websoft9.com/release/websoft9/install.sh && bash install.sh

# Custom Parameter Installation
# -- channel release | dev
# --port
# --version
# --path

wget -O install.sh https://artifact.websoft9.com/release/websoft9/install.sh && bash install.sh --port 9000 --channel release --path "/data/websoft9/source" --version "latest"
```

> Upgrade Websoft9 by running the same script.  

## Offline installation

Computers in an offline environment are isolated from the public internet as a security measure.   

If you plan to deploy Websoft9 on a physically-isolated and offline network, please contact [Websoft9 Support Team](./helpdesk).


## Uninstall 

Websoft9 supports uninstallation and allows users to choose whether to keep data.  

```
curl https://websoft9.github.io/websoft9/install/uninstall.sh | bash
```

## Troubleshoot

For troubleshooting details, see [Troubleshooting Websoft9](./faq#websoft9-console) issues.