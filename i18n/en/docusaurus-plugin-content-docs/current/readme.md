---
sidebar_position: 1
slug: /
---

# Introduction

This is the documentation for the next generation of Websoft9, which has been released and will replace the old version.  

It provides you with the best practices for self-hosting multiple applications.

| Section              | Description                                                     |
| ----------------- | -------------------------------------------------------- |
| [Installation](./install) | Install the Websoft9 Console on your Server |
| [Login to Websoft9](./login-console)   |  Log in to the Websoft9 console to interactively experience the hosting platform  |
| [Getting started](./starter)   |  Use Websoft9 to quickly deploy various types of applications, including one-click template deployment and customized deployment, etc.  |
| [User guide](./guide)   | Deploying, publishing, and managing applications using Websoft9  |
| [Administrator](./admin)   |  Operations and maintenance guides for administrator users for user management, upgrades, backups, data, storage, and security configurations  |
| [Applications](./apps) |  Websoft9 App Store 200+ One-Click Deployment Templates Quick Start and Configuration Guide  |
| [App Runtime](./runtime) |  App runtime for your Java, Python, Node.js, PHP, Go, Ruby, and .NET applications  |
| [Subscription](./busines)   |  Paid use of Websoft9 products for enterprise-level business support services |
| [Support](./helpdesk)   |  Get any support from Websoft9 Customer Success Team |
| [Troubleshooting](./faq)        |  Technical problems and failures   |

## About Websoft9

Websoft9 is a **Self-Hosting platform (Lite PaaS)** that can deploy multiple applications in your own cloud infrastructure.  

It brings the extremely simple user experience of deploying an application with just a few clicks into a cloud provider of your choice, whether that is Azure, AWS, GCP, or AlibabaCloud. 

Websoft9 comes with 200+ [one-click deployment templates](https://www.websoft9.com/apps) pre-built and supports users' customized deployment of programs such as Java, Python, Node.js, PHP, Go, Ruby and dotNET.

![](/img/websoft9-appstore.png)

## Features

- Open source and free for starter
- Web-based interface, easy to use
- Inner App Store have [200+ one-click deployment application templates](http://github.com/websoft9/docker-library)
- It is a tool implementing GitOps and Infrastructure as Code (IaC)principles, support continue deployment
- Supports customized deployment of programs such as Java, Python, Node.js, PHP, Go, Ruby and dotNET
- Hosting services from deployment to operation, monitoring, and support for high availability, scalability, backup and recovery, and security compliance.

## Use cases

Refer to: [Solution of Websoft9](https://www.websoft9.com/en-US/solutions)

## Hosting Options

Applications is running at server and managed by the **Websoft9 Console**.    

Websoft9 supports multiple hosting options: 

**Deployment architecture Options**    

- Application and Websoft9 Console deployed on the same server instance  
- Application and Websoft9 Console deployed on different server instances(coming soon)  
- Single server deployed with a single application
- Single server deployed with multiple applications
- Single application deployed in a k8s cluster across multiple servers(coming soon)

**Hosting Options**   

- Choose Websoft9 as **Managed Hosting provider** that Websoft9 handles server maintenance, security updates, backups, monitoring, and provides 24/7 support. Users focus on applications, not infrastructure.
- Choose Websoft9 as **Self-Hosting provider** that customers control deployment, configuration, and management. They handle maintenance, updates, security, and backups, offering flexibility and potential cost savings.

## Deployment Templates

The Websoft9 Console supports the following [application deployment templates](./apps) that can be installed with one click:

import Meta from './apps/_include/allapps.md';

<Meta name="meta" />

## Comparison {#vs}

### Websoft9 vs cPanel vs Plesk

Both cPanel and Plesk are server panel tools designed to simplify website hosting and server management.  

The main features of Websoft9 compared to them are:

- **Application-Centric**: Enterprise-grade managed services from deployment to operations and monitoring.

- **High Availability**: Supports scalability, backup, recovery, and security compliance.

- **Diverse Deployment**: 200+ one-click templates, supports PHP/Java/Python/Ruby/.NET/Go/Docker/HTML.

- **Automation**: GitOps-driven continuous deployment and rollback, ensuring consistency and traceability.

- **Cloud-Native**: Microservices and container-based, modular, replaceable, iterative, and upgradable core components. 

### Websoft9 vs Heroku

Heroku is a PaaS platform that abstracts away underlying infrastructure.

The main features of Websoft9 compared to them are:

- A lite PaaS giving users control over infrastructure, balancing application hosting convenience with control and cost.
- 100% open-source foundation, eliminating any possibility of vendor lock-in.

### Websoft9 vs OpenShit vs KubeSphere

OpenShift and KubeSphere both provide comprehensive Kubernetes management, support multi-cloud environments, offer DevOps tools, and ensure enterprise-grade security and scalability.  

The main features of Websoft9 compared to them are:


- Positioned as an application deployment and maintenance platform for innovative organizations and developers.
- Offers pre-configured software stacks and one-click deployment for quick application launches.
- May not support full DevOps or complex cluster deployments, but is an easy-to-manage GitOps platform.
