---
sidebar_position: 1.0
slug: /production-deploy
---

# Tutorial: Production deploy

Websoft9 is a enterprise-grade, production-level deployment platform for each hosted app.  

At this chapter, we introduce plan for production-level deployments by Websoft9.  

## Key points for production

In production deployment, merely running the application isn't enough. It involves deeper considerations to meet enterprise standards that includes:  

1. **Maximize infrastructure performance**: Ensure optimal use of hardware and network resources.

2. **Increase deployment efficiency**: Use automation and detailed process management to reduce errors and time.

3. **Continuous optimization**: Monitor performance, optimize based on feedback, and support seamless updates.

4. **Security and reliability**: Ensure secure access, prevent data breaches, and maintain high availability.

These measures ensure the application is not only online but also efficient, secure, and reliable for users and business needs.

## Step 1: Prepare infrastructure

Using Websoft9 to host modern enterprise cloud-native apps requires a robust infrastructure.  

- [Prepare domain](./domain-prepare)
- [Plan your infrastructure](./design-infrastructure)
- [Plan network brandwith and traffic](./brandwith-infra)
- [Extend and optimize storage](./storage)


## Step 2: Prepare software packages

Preparing installation packages is crucial and shouldn't be seen as a simple task. This involves careful consideration of format, retrieval, and automated compilation strategies.  

- [Prepare your artifacts package for installation](./plan-package)
- [Search templated application from Websoft9 App Store](./appstore)

## Step 3: Deploy application

Websoft9 enables users to use declarative infrastructure-as-code for deploying applications.  

- [Deploy from Websoft9 App Store](./deployment)
- [Use Git for automatic deployment](./plan-git)

## Step 4: Public application

Websoft9 have a security module ensuring application availability and access at Internet.

- [Set domain for application](./domain-set)
- [Set HTTPS for application](./domain-https)
- [Set CDN for access Acceleration](./gateway-cdn)

## Step 5: Continuous optimization

Websoft9 platform supports continuous deployment and optimization for running applications. 

- [Set your Docker](./docker-server)
- [Customized configs and update deployment](./app-compose)
- [Monitor the application](./monitor)

