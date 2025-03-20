---
sidebar_position: 1.2
slug: /install-windows
title: "For Windows/macOS"
---


# Installation for Windows/macOS

Websoft9 can't install on Windows directly. So, use a Linux VM instead.  

The steps below:  

1. **Installing Virtual Machine Software on Windows/macOS**：

   - Download and install Virtual Machine Software, e.g [VirtualBox](https://www.virtualbox.org/) or [VMware Workstation Player](https://www.vmware.com/products/workstation-player.html)

2. **Create Linux VM by Virtual Machine Software**：

   - Select and download a Linux ISO file, like Ubuntu, CentOS Stream, or Debian.
   - Open VM software, create a new VM, and choose the Linux ISO file.
   - Configure VM resources (memory, disk space), then start and install Linux.
   - Ensure the Linux VM shares the external network with the Windows/macOS server.

4. **Install Websoft9 to Linux VM**：

   - Start Linux VM and connect by SSH terminal
   - [Install Websoft9](./install-linux) at Linux system

Complete these steps to access the [Websoft9 Console](./login-console) and start configuration.
