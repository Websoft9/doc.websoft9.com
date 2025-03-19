---
sidebar_position: 1.0
slug: /design-infrastructure
---

# Plan overall infrastructure

Hosting modern, enterprise-grade, cloud-native applications with Websoft9 requires a complete, reliable and efficient infrastructure to support it.  

Here are the key components to consider when building such an infrastructure. 

## Cloud type

Websoft9 supports deployment on public, private, or hybrid clouds, but choosing the right cloud depends on an organization's business, compliance, and cost requirements:

- **Public Cloud**: Cloud resources provided by professional third-party service providers

  - **Cost Efficiency**: Typically uses a pay-as-you-go model, allowing cost optimization based on actual usage.
  - **Global Deployment**: Enables service deployment worldwide, reducing latency by being closer to users.
  - **Innovative Services**: Often offers the latest cloud services and technologies.

- **Private Cloud**: Self-built data centers or telecom-hosted solutions

  - **Control**: Complete control over your infrastructure, including hardware and software.
  - **Customization**: Metting specific needs, including performance optimization and enhanced security.
  - **Privacy Protection**: Data remains within the organization’s control, helping to meet specific privacy requirements.

- **Hybrid Cloud**: Combines the advantages of public and private clouds

  - **Flexibility**: Allocates workloads to the most suitable environment based on needs.
  - **Cost Optimization**: Selects the most cost-effective cloud environment for different workloads.
  - **Business Continuity**: Enhances disaster recovery capabilities across different cloud environments.

## Visual machine options

Visual machine servers are the foundation for hosting applications. Consider these factors: 

- **Performance specs:** Choose appropriate [CPU and memory](./install-requirements#server) based on performance needs.

- **Region selection:** Server regions should be close to customer locations.

- **Scalability:** Ensure servers can scale automatically or manually based on load.

- **Operating system:** Choose an OS that supports your application, like Linux.

- **Compatibility:** Ensure servers support containerization, like Docker and orchestration tools.

- **Availability:** Choose cloud services that support high availability to reduce downtime.

- **CPU architecture:** Ensure applications support common CPU architectures, like x86-64, ARM.

- **Private cloud virtualization:** Choose KVM, VMware, VirtualBox, OpenStack for private cloud.


## Snapshot for backup

Regular snapshots prevent data loss and allow quick recovery to a known good state.

- **Automated backups**: Set up automated backup policies for regular snapshots of systems and data.
- **Backup strategy**: Develop backup frequency and retention policies based on business needs.
- **Recovery testing**: Regularly perform recovery tests to ensure backups are effective.

## Network

Network is the core of cloud-native applications, ensuring security, reliability, and performance.

- **Networking:** Design a suitable network topology, including subnet division and isolation.
- **Security Groups:** Configure security groups to restrict unnecessary inbound and outbound traffic.
- **CDN:** Use a Content Delivery Network (CDN) to reduce distance between users and services.
- **Load Balancing:** Deploy load balancers to distribute traffic, ensuring high availability and scalability.
- **Bandwidth:** Choose sufficient [bandwidth](./brandwith-infra) to significantly improve hosting performance.

## Disk and storage

Choose suitable disk and storage solutions based on application [storage needs](./storage):

- **Persistent Storage:** For persistent data, choose storage services supporting persistent volumes.
- **Performance:** Select different storage types based on needs, like SSD for high IOPS.
- **Scaling Optimization:** Plan disk capacity and storage changes in advance.

## API

Automation boosts hosting efficiency, and it's based on API-managed infrastructure.

## Domain Name

Domains make it easier for users to access websites without needing to remember numerical IP addresses.

- [Prepare your domain](./domain-prepare)
- [Set global domain for Websoft9](./domain-set#wildcard)

## Security and compliance

Infrastructure security is crucial for application hosting:

- **Identity and Access Management (IAM)**: Ensure only authorized users access resources.
- **Encryption**: Implement encryption for data in transit and at rest.
- **Monitoring and Logging**: Track performance and security events; retain logs for audits.
- **Compliance**: Adhere to industry standards and regulations like GDPR, HIPAA, etc.

By carefully planning and implementing the above infrastructure services, you can build a solid foundation for your Websoft9 platform. This will ensure the smooth running of your application and also enhance the user experience and ultimately drive business success.  