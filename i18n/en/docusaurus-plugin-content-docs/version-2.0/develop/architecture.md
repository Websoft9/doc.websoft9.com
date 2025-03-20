---
sidebar_position: 1
slug: /developer/architecture
---

# Architecture

Websoft9 is an application-centric microservices architecture.  

## Architecture philosophy

**Everything is an application, everything can be assembled"** is the basic philosophy of Websoft9, based on this philosophy, we flexibly integrate excellent open source software into our product system.  

- Product Innovation through Assembly
- [The Twelve-Factor App](https://12factor.net/zh_cn/)
- Open source iteration, continuous development
- Focus on connectivity and reduce non-essential original components
- Leverage elements of technology that are already popular and avoid creating new specifications
- GitOps Cloud-native continuous delivery model
- Unix philosophy KISS principle: Keep It Simple, Stupid!
- [Infrastructure as Code (IaC)](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac)

## Architecture diagram

The technical elements used by Websoft9 include Linux, Docker, Gateway, service discovery, application orchestration, Git.  

The corresponding product architecture diagram is shown below:  

![](/img/websoft9-architecture.png)


- **Apphub**: Application management service, responsible for the entire life cycle of the application
- **Git**: Git acts as the single source of truth for system state at GitOps
- **Deployment**: Continuous deployment
- **Gateway**: Publishing and controlling access to the application.

## Open Souce

Websoft9 uses [Docker Compose](https://docs.docker.com/compose/) as a template for applications, and maintained an open source repository [docker-library](https://github.com/Websoft9/docker-) with 200+ templates.   

Applications running on Docker Compose can exist independently of Websoft9, which means maintenance and learning costs are extremely low.  