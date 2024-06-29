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
| [Web Runtime](./runtime) |  Web runtime for your Java, Python, Node.js, PHP, Go, Ruby, and .NET applications  |
| [Subscription & Support](./business)   |  Paid use of Websoft9 products for enterprise-level business support services |
| [Troubleshooting](./faq)        |  Technical problems and failures   |

## About Websoft9

Websoft9 is a **Self-Hosting PaaS platform** that can deploy multiple applications in your own cloud infrastructure.It brings the extremely simple user experience of deploying an application with just a few clicks into a cloud provider of your choice, whether that is Azure, AWS, GCP, or AlibabaCloud. 

Websoft9 offers 200+ one-click deployment application templates and also supports customers in uploading their own Java, PHP, Ruby, and other artifacts to achieve custom application deployments.

Websoft9 comes with 200+ [one-click deployment templates](https://www.websoft9.com/apps) pre-built and supports users' customized deployment of programs such as Java, Python, Node.js, PHP, Go, Ruby and dotNET.

![](/img/websoft9-dashboard.png)

## Features

## Hosting Options

In the Websoft9 architecture, applications are managed by the **Websoft9 Console**, while logically remaining independent from the console.     

The servers are responsible for running the applications, and their usage strategy directly influences the choice of hosting mode.  

In light of this, Websoft9 offers users a range of flexible hosting options:  

**Deployment Location Options**    

- Application and Websoft9 Console deployed on the same server instance  
- Application and Websoft9 Console deployed on different server instances(coming soon)  

**Compute Resource Utilization Options**    

- Single server deployed with a single application
- Single server deployed with multiple applications
- Single application deployed in a k8s cluster across multiple servers(coming soon)

**Server Management Options**   

- User manages the server independently
- User delegates full server management to Websoft9

## Deployment Templates

The Websoft9 Console supports the following [application deployment templates](./apps) that can be installed with one click:

import Meta from './apps/_include/allapps.md';

<Meta name="meta" />

## Platform Comparison {#vs}

### Websoft9 vs cPanel vs BaoTa

Both cPanel and BaoTa are server panel tools designed to simplify PHP website deployment and server management.  

Compared to them, Websoft9 offers:

- **Application-Centric Approach**: Provides enterprise-level hosting services from deployment to operation, monitoring, and support for high availability, scalability, backup and recovery, and security compliance.  
- **Diverse Deployment Capabilities**: Over 200 one-click deployment templates, supporting various programming environments such as PHP, Java, Python, Ruby, .NET, Go, Docker, and HTML.  
- **Automation Capabilities**: GitOps-driven automated continuous deployment and rollback, enhancing operational and hosting efficiency while ensuring consistency and traceability of environments.  
- **Cloud-Native Architecture**: A cloud-native architecture centered on microservices and containers, with core modules adopting an assembly-style integration that is replaceable, iterative, and upgradable.  

### Websoft9 vs Heroku

Heroku is a PaaS platform that abstracts the underlying infrastructure, allowing developers to focus on code rather than servers. 

Compared to Heroku, Websoft9:

- Is a PaaS that gives users control over the infrastructure, meeting the convenience of hosting applications while offering control and cost management.
- Is built on a 100% open-source foundation, eliminating the possibility of vendor lock-in.

### Websoft9 vs OpenShit vs KubeSphere

OpenShift and KubeSphere are enterprise-grade container application platforms based on Kubernetes, providing complete DevOps toolchain support and automated operations capabilities. They support multi-tenancy and clusters, offering large enterprises the ability to isolate and manage different projects and teams while providing comprehensive security and compliance features. Their rich ecosystems help enterprises quickly achieve cloud-native application development, deployment, and management. 

Compared to them, Websoft9:

   - Is positioned as a platform centered on application deployment and maintenance, focusing on providing simplified application hosting solutions for innovative organizations and developers.  
   - Offers pre-configured software stacks and one-click deployment features, enabling users to quickly launch and run various applications.  
   - While it may not support the complete DevOps process or complex cluster deployments for large enterprises, it is an easy-to-manage GitOps platform.
