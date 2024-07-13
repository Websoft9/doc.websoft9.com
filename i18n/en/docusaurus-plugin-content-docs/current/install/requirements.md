---
sidebar_position: 1
slug: /install-requirements
---

# Requirements

This page includes information about the minimum requirements you need to install and use Websoft9.

## Hardware requirements{#server}

### CPU and Memory

CPU requirements are dependent on the number of users and expected workload. Your exact needs may be more, depending on your applications workload.  

Refer below for CPU recommendations depending on user count / load:  

- If not install application, **1 vCPU and 2 GB memory** can running
- Runing 1 WordPress, **2 vCPU and 4 GB memory** if need at leaset
- Runing 1 WordPress and 1 GitLab, **4 vCPU and 8 GB memory** if need at leaset

### Storage

The necessary hard drive space largely depends on the applications you want to hosting by Websoft9 but as a guideline you should have at least as much free space as all your repositories combined take up.

- The Linux package requires about **2.5 GB of storage space** for installation
- Websoft9 container requires about **1.5 GB of storage space**
- If you install 1 WordPress, you should prepare **10 GB of storage space** for it

### Network bandwidth

Websoft9 requires internet access with stable bandwidth not less than **100M/s** for installation.

## Operating system{#os}

Websoft9 supports major [Linux distributions](https://websoft9.github.io/websoft9/version.json) like Red Hat, CentOS Steam, RockyLinux, Oracle Linux, Debian, and Ubuntu.  

If you want to install Websoft9 at [Windows or macOS](./install-windows), you need to install VM software fist.  

## Domain{#domain}

A domain is not required for Websoft9 to run. However, without a domain, application access is limited. We recommend configuring a domain for your application.  

Websoft9 supports [wildcard domains](./domain-set#wildcard). Once set, all applications can use it.


## Software packages

Python 3.8+ is required for installing Websoft9.

## Supported web browsers

Websoft9 supports the following web browsers:

- Microsoft Edge
- Google Chrome
- Mozilla Firefox
- Apple Safari
- Chromium

## Related topics

- [Plan overall infrastructure](./design-infrastructure)
- [Plan bandwidth and traffic](./brandwith-infra)
- [Expand or optimize storage](./storage)



