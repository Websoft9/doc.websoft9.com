---
sidebar_position: 1
slug: /install/linux
---


# For Linux  

## Automatic installation

If you do not have the Docker, Git, Ansible and other environments required above, it is recommended to use our **Automatic installation** below:  

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

## Manual installation

1. Install Websoft9 CLI: StackHub
   ```
   pip install stackhub
   ```
2. Use stackhub to install and manage application

## Offline installation

We provide a complete offline installation package service for no network environment
